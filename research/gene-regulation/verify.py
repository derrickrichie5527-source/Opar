"""Recalculate the simulated V2 case and check its published representation.

Run from any directory using Python 3; standard library only.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import math
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
data = json.loads((HERE / 'v2/data.json').read_text(encoding='utf-8'))
checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def near(actual, expected, tolerance=1e-9):
    check(math.isclose(actual, expected, rel_tol=tolerance, abs_tol=tolerance), f'{actual} != {expected}')

def sha(path):
    return hashlib.sha256(path.read_bytes().replace(b'\r\n', b'\n').rstrip(b'\n')+b'\n').hexdigest()

a, b, c, d = (data['panel_'+name] for name in 'abcd')
dcq = [t-r for t,r in zip(a['target_cq'], a['reference_cq'])]
ratio = a['amplification_factor'] ** -(dcq[1]-dcq[0])
mrna = ratio * a['reference_per_cell'][1] / a['reference_per_cell'][0]
near(ratio, 1); near(mrna, 2)
corrected = [v/r for v,r in zip(b['signal_au'], b['spike_recovery'])]
near(corrected[0], 125); near(corrected[1], 250); near(corrected[1]/corrected[0], 2)
ln2 = math.log(2)
loss = [-math.log(d[n][-1]/d[n][0])/d['times_h'][-1] for n in ['control', 'treatment']]
growth = [ln2/t for t in d['doubling_time_h']]
degradation = [k-g for k,g in zip(loss,growth)]
for k,g,kd,half,dh in zip(loss,growth,degradation,[4,6],[6,8]):
    near(ln2/k, half); near(ln2/kd, dh); near(k, g+kd); check(kd>=0, 'Negative degradation')
# Fit log signal with intercept to every rounded point; tolerate rounding only.
for name,k in zip(['control','treatment'],loss):
    x=d['times_h']; y=[math.log(v) for v in d[name]]
    xm=sum(x)/len(x); ym=sum(y)/len(y)
    fitted=-sum((t-xm)*(v-ym) for t,v in zip(x,y))/sum((t-xm)**2 for t in x)
    near(fitted,k,tolerance=.001)
    for t,v in zip(x,d[name]): near(round(math.exp(-k*t),3),v)
synthesis=[p*k for p,k in zip(c['protein_per_cell'],loss)]
sr=synthesis[1]/synthesis[0]; er=sr/mrna
near(sr,2); near(er,1)
deg_only=loss[0]/(degradation[1]+growth[0])
growth_only=loss[0]/(degradation[0]+growth[1])
combined=loss[0]/loss[1]
near(deg_only,1.2); near(growth_only,1.2); near(combined,1.5)
near(combined/deg_only,1.25); near(sr*combined,3)
for p,s,k in zip(c['protein_per_cell'],synthesis,loss): near(s-k*p,0)

class Page(HTMLParser):
    VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
    def __init__(self,text):
        super().__init__(convert_charrefs=True)
        self.stack=[]; self.ids=set(); self.links=[]; self.tables={}; self.current=None; self.row=None; self.cell=None
        self.headings=[]; self.captions=0; self.details=0; self.summaries=0
        self.feed(text); self.close()
        check(not self.stack, f'Unclosed HTML: {self.stack}')
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            check(a['id'] not in self.ids, 'Duplicate ID '+a['id']); self.ids.add(a['id'])
        if tag=='html': check(a.get('lang')=='en','Missing language')
        if tag=='a' and 'href' in a: self.links.append(a['href'])
        if tag=='img': check('alt' in a,'Missing image alt')
        if tag=='th': check(a.get('scope') in ['row','col'], 'Missing table header scope')
        if tag=='table': self.current=a['id']; self.tables[self.current]=[]
        if tag=='caption': self.captions+=1
        if tag=='tr': self.row=[]
        if tag in ['th','td']: self.cell=''
        if tag=='details': self.details+=1
        if tag=='summary': self.summaries+=1
        if tag not in self.VOID: self.stack.append(tag)
    def handle_data(self,text):
        if self.cell is not None: self.cell+=text
    def handle_endtag(self,tag):
        if tag in self.VOID: return
        check(bool(self.stack) and self.stack[-1]==tag, f'Misnested {tag}: {self.stack[-3:]}')
        self.stack.pop()
        if tag in ['th','td']: self.row.append(self.cell.strip()); self.cell=None
        if tag=='tr': self.tables[self.current].append(self.row); self.row=None
        if tag=='table': self.current=None

text=(ROOT/'gene-regulation.html').read_text(encoding='utf-8')
page=Page(text)
check('charset="utf-8"' in text and 'name="viewport"' in text,'Encoding/viewport')
check(page.captions==len(page.tables),'Every table needs a caption')
check(page.details==page.summaries,'Details without summaries')
check(all(f'q{i}' in page.ids for i in range(1,9)),'Eight questions')
check('Version 2 has not been evaluated' in text,'V2 disclosure')
check('All measurements are constructed' in text,'Simulation disclosure')
check('39/40 on the original rubric' in text,'Historical score labeling')
check('promoter-only' not in text and 'endogenous cis-regulatory element perturbation' in text,'Q7 scope')
check(not any(x in text for x in ['delta-Cq','delta-delta-Cq','k_loss','k_growth','k_degradation']),'Unformatted math')
for i,row in enumerate(page.tables['panel-d'][1:]):
    check([float(v) for v in row]==[d['times_h'][i],d['control'][i],d['treatment'][i]],'Panel D differs from data')
check([float(v) for v in page.tables['panel-b'][1][1:]]==b['signal_au'],'Panel B signals differ')
check([float(v.rstrip('%'))/100 for v in page.tables['panel-b'][2][1:]]==b['spike_recovery'],'Panel B recoveries differ')
expected_rates=[[ln2/k for k in loss],loss,growth,degradation,[ln2/k for k in degradation]]
for row,expected in zip(page.tables['answer-rates'][1:],expected_rates):
    for v,e in zip(row[1:],expected): near(float(v),e,tolerance=1e-6)
check(sum(int(row[1]) for row in page.tables['rubric-v2'][1:])==40,'Rubric total')
for link in page.links:
    parts=urlsplit(link)
    if parts.scheme or parts.netloc: continue
    dest=ROOT/unquote(parts.path) if parts.path else ROOT/'gene-regulation.html'
    check(dest.is_file(), 'Missing local file '+str(dest))
    if parts.fragment:
        dest_text=dest.read_text(encoding='utf-8')
        check(re.search(r'id=[\"\']'+re.escape(parts.fragment)+r'[\"\']',dest_text) is not None, 'Missing anchor '+link)
manifest=json.loads((HERE/'manifest.json').read_text(encoding='utf-8'))
check(sha(ROOT/'gene-regulation-v1.html')==manifest['archived_page_sha256'],'V1 archive changed')
for version in ['v1','v2']:
    for name,expected in manifest[version+'_files'].items(): check(sha(HERE/version/name)==expected, 'File changed: '+version+'/'+name)
template=json.loads((HERE/'v2/run-template.json').read_text(encoding='utf-8'))
check(template['status']=='not_run' and template['total_score'] is None,'Template must not claim a run')
print(json.dumps({'checks_passed':checks,'loss_rates_h-1':loss,'growth_rates_h-1':growth,'degradation_rates_h-1':degradation,'rna_corrected_au':corrected,'synthesis_ratio':sr,'effective_synthesis_per_mrna_ratio':er,'counterfactuals':{'degradation_only':deg_only,'growth_only':growth_only,'combined':combined}},indent=2))
