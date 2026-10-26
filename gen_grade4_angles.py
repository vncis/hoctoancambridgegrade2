# Adds picture-based Unit 8 (Angles) questions to grade4.js. Run: python3 gen_grade4_angles.py grade4.js
import json, math, random, sys
R=random.Random(88)
path=sys.argv[1] if len(sys.argv)>1 else 'grade4.js'
s=open(path).read(); D=json.loads(s.split('=',1)[1].rstrip().rstrip(';'))
D=[d for d in D if not d.get('svg')]          # re-runnable
UN="Angles"
SN={1:"8.1 Comparing angles",2:"8.2 Acute and obtuse",3:"8.3 Estimating angles"}
seen=set(); 
def add(w,a,an,q,acc,e,svg=None):
    k=(w,a,q,svg)
    if k in seen: return
    seen.add(k)
    d=dict(t=8,tn=UN,w=w,wn=SN[w],a=a,n=an,q=q,r=[str(x).lower() for x in acc],e=e,txt=1)
    if svg: d['svg']=svg
    D.append(d)
def ang(deg,label,rot=None,l1=None,l2=None,mark=True):
    rot=R.randint(0,359) if rot is None else rot
    l1=l1 or R.randint(38,58); l2=l2 or R.randint(38,58); cx=cy=62
    def pt(L,a): return cx+L*math.cos(math.radians(a)), cy-L*math.sin(math.radians(a))
    x1,y1=pt(l1,rot); x2,y2=pt(l2,rot+deg); r=16
    a1=pt(r,rot); a2=pt(r,rot+deg)
    g=f'<g><path d="M{x1:.1f} {y1:.1f} L{cx} {cy} L{x2:.1f} {y2:.1f}" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
    if mark: g+=f'<path d="M{a1[0]:.1f} {a1[1]:.1f} A{r} {r} 0 {1 if deg>180 else 0} 0 {a2[0]:.1f} {a2[1]:.1f}" fill="none" stroke="#e5484d" stroke-width="2"/>'
    g+=f'<text x="62" y="124" text-anchor="middle" font-size="16" font-weight="bold" fill="currentColor">{label}</text></g>'
    return g
def row(angles,labels=None,mark=True):
    labels=labels or "ABCDEFGH"[:len(angles)]; w=124*len(angles)
    out=f'<svg viewBox="0 0 {w} 132" width="{min(w,560)}" style="max-width:100%;height:auto;color:inherit" role="img">'
    for i,(d,l) in enumerate(zip(angles,labels)): out+=f'<g transform="translate({i*124},0)">{ang(d,l,mark=mark)}</g>'
    return out+'</svg>'
KEEP="Remember: the length of the arms does not matter. Only the opening (the turn) between the arms counts."
# ---- 8.1 Comparing angles
for k in range(12):
    a,b=R.sample(range(20,170,5),2)
    if abs(a-b)<12: continue
    big=k%2==0; ans="AB"[(a<b) if big else (a>b)]
    add(1,3,"Which angle is greater?",f"Look at angles A and B. Which angle is {'greater' if big else 'smaller'}? (write A or B)",[ans,ans.lower()],
        f"Compare how wide each angle opens. Angle {ans} opens {'more' if big else 'less'}, so it is the {'greater' if big else 'smaller'} angle. {KEEP}",row([a,b]))
for k in range(5):
    L=sorted(R.sample(range(20,170,10),5)); w=R.randint(1,3); L[w],L[w+1]=L[w+1],L[w]
    add(1,4,"Angle in the wrong place","These angles should go from smallest to greatest, but one is in the wrong place. Which letter is the angle in the wrong place? (A–E; if two are swapped, give the first one)",
        ["abcde"[w],"abcde"[w+1]],f"Check each angle opens a little more than the one before. Angles {'ABCDE'[w]} and {'ABCDE'[w+1]} are swapped.",row(L))
for k in range(10):
    L=R.sample(range(15,175,10),5); order=sorted(range(5),key=lambda i:L[i]); seq=[ "ABCDE"[i] for i in order]
    acc=["".join(seq),"".join(seq).lower(),", ".join(seq),", ".join(seq).lower(),"".join(x+" " for x in seq).strip().lower(),", ".join(seq).replace(", "," ").lower()]
    add(1,5,"Order the angles","Put these angles in order from smallest to greatest. (write the five letters, like BDACE)",acc,
        f"Compare the openings. Smallest to greatest: <b>{' '.join(seq)}</b>. {KEEP}",row(L))
for k in range(6):
    L=R.sample(range(15,175,10),5); big=k%2==0; i=max(range(5),key=lambda i:L[i]) if big else min(range(5),key=lambda i:L[i])
    add(1,6,"Greatest or smallest","Which is the "+("greatest" if big else "smallest")+" angle? (write the letter)",["ABCDE"[i],"abcde"[i]],
        f"Find the angle that opens {'most' if big else 'least'}. It is angle <b>{'ABCDE'[i]}</b>.",row(L))
# ---- 8.2 Acute and obtuse
for k in range(14):
    d=R.choice([20,35,45,55,70,80,100,110,125,140,155,170]); c="acute" if d<90 else "obtuse"
    add(2,3,"Acute or obtuse? (pictures)","Is angle A acute or obtuse?",[c],
        f"Compare with a right angle (90°). A smaller angle is acute; an angle between a right angle and a straight line is obtuse. This one is <b>{c}</b>.",row([d],["A"]))
for k in range(8):
    L=[R.choice([30,45,60,75,85,100,115,130,150,165]) for _ in range(6)]; n=sum(x<90 for x in L)
    add(2,4,"Count the acute angles","How many of these six angles are acute?",[n,["zero","one","two","three","four","five","six"][n]],
        f"Acute angles are smaller than a right angle. Acute: {', '.join('ABCDEF'[i] for i in range(6) if L[i]<90) or 'none'}. That is <b>{n}</b>.",row(L))
for k in range(6):
    L=[R.choice([40,55,70,80]) for _ in range(3)]; i=R.randrange(3); L[i]=R.choice([105,120,135])
    svg='<svg viewBox="0 0 372 132" width="560" style="max-width:100%;height:auto"><g>'
    # three triangles where one has an obtuse corner
    def tri(x0,obt,label):
        P=[(10,100),(100,100),(62,22)] if not obt else [(10,100),(100,100),(18,38)]
        return f'<g transform="translate({x0},0)"><polygon points="{" ".join(f"{a},{b}" for a,b in P)}" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linejoin="round"/><text x="55" y="124" text-anchor="middle" font-size="16" font-weight="bold" fill="currentColor">{label}</text></g>'
    svg+=tri(0,i==0,"A")+tri(124,i==1,"B")+tri(248,i==2,"C")+'</g></svg>'
    add(2,5,"Triangles","One of these triangles has an obtuse angle. Which one? (write A, B or C)",["abc"[i],"ABC"[i]],
        f"An obtuse angle opens wider than a right angle. Triangle <b>{'ABC'[i]}</b> has a corner that opens wider than a square corner.",svg)
nums=[45,60,10,50,80,100,130,120,165,175,70,20,150,35,160,110,40,65,145,135,105,170,155,125,30]
for k in range(6):
    L=R.sample(nums,6); n=sum(x>90 for x in L)
    add(2,6,"Obtuse numbers","How many of these degrees of turn are obtuse angles? "+", ".join(map(str,L)),[n,["zero","one","two","three","four","five","six"][n]],
        f"Obtuse angles are between 90° and 180°. Obtuse here: {', '.join(str(x) for x in L if x>90) or 'none'}. That is <b>{n}</b>.")
for q,a in [("An angle is between 90 and 180 degrees.","obtuse"),("An angle of 59 degrees is ___.","acute"),("An angle is smaller than a right angle.","acute"),("An angle of 100 degrees is ___.","obtuse"),("An angle is between 0 and 90 degrees.","acute"),("An angle of 91 degrees is ___.","obtuse"),("An angle of 89 degrees is ___.","acute"),("An angle that is greater than a right angle but less than a half turn is ___.","obtuse")]:
    add(2,7,"Complete the sentences",f"Write obtuse or acute: {q}",[a],f"Acute is less than 90°. Obtuse is between 90° and 180°. The answer is <b>{a}</b>.")
# ---- 8.3 Estimating angles
for k in range(14):
    d=R.choice([20,30,45,60,80,100,115,130,150,165]); alt=d+R.choice([-1,1])*R.choice([40,50,60]); alt=min(max(alt,15),175)
    if abs(alt-d)<30: continue
    o=[d,alt]; R.shuffle(o)
    add(3,3,"Best estimate (pictures)",f"Circle the best estimate for angle A: {o[0]}° or {o[1]}°? (write the number)",[d],
        f"Use 90° (right angle) and 45° (half a right angle) to compare. The best estimate is <b>{d}°</b>.",row([d],["A"]))
for k in range(16):
    d=R.choice([15,25,35,45,55,65,75,90,105,120,135,145,160,170]); tol=10
    add(3,4,"Estimate the angle","Estimate the size of angle A in degrees. (a number close to the answer is accepted)",[x for x in range(d-tol,d+tol+1)],
        f"Compare with 90° and 45°. This angle is about <b>{d}°</b>. Any estimate within 10° is a good estimate.",row([d],["A"],mark=False))
for q,a,e in [("How many right angles do you turn to make a full circle?",4,"4 x 90° = 360°."),("How many degrees are there in a full circle?",360,"4 right angles = 360°."),("How many right angles do you turn to make three-quarters of a circle?",3,"A quarter turn is 1 right angle, so 3 quarters is 3 right angles."),("How many degrees are there in three-quarters of a circle?",270,"3 x 90° = 270°."),("Sal turned on the spot 270 degrees. How many right angles is that?",3,"270 ÷ 90 = 3."),("Sal turned 270 degrees. How many more degrees does he need to turn to be back where he started?",90,"360 - 270 = 90."),("How many degrees are in 5 right angles?",450,"5 x 90 = 450."),("How many right angles make 180 degrees?",2,"180 ÷ 90 = 2.")]:
    add(3,5,"Turns and right angles",q,[a],e)
for d in (15,45,90,135,170):
    add(3,6,"Match the label",f"Angle A is about which size: 15°, 45°, 90°, 135° or 170°? (write the number)",[d],f"Compare with 90° (square corner), 45° (half a right angle) and 180° (straight line). This angle is about <b>{d}°</b>.",row([d],["A"],mark=False))
open(path,'w').write('const QUESTIONS4='+json.dumps(D,separators=(',',':'),ensure_ascii=False)+';\n')
print('total',len(D),'unit8',sum(d['t']==8 for d in D),'with pictures',sum(1 for d in D if d.get('svg')))
