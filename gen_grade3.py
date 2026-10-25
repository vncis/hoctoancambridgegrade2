import random, json
R=random.Random(2026)
ones="zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
tens="_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
def W(n):
    if n<20: return ones[n]
    if n<100: return tens[n//10]+('-'+ones[n%10] if n%10 else '')
    if n>=1000: return ones[n//1000]+' thousand'+((' and '+W(n%1000)) if n%1000 else '')
    return ones[n//100]+' hundred'+(' and '+W(n%100) if n%100 else '')
def nums(n): return [str(n),W(n)]
def money(c):
    d,x=divmod(c,100)
    return (["%d"%d,"%d.00"%d,"$%d"%d,"$%d.00"%d] if x==0 else ["%d.%02d"%(d,x),"$%d.%02d"%(d,x)]+(["%d.%d"%(d,x//10)] if x%10==0 else []))
def ms(c):
    d,x=divmod(c,100); return "$%d.%02d"%(d,x)
D=[];ctx={}
def sec(u,un,w,wn,a,an): ctx.update(t=u,tn=un,w=w,wn=wn,a=a,n=an)
seen=set()
def tx(q,acc,e):
    k=(ctx['t'],ctx['w'],ctx['a'],q)
    if k in seen: return
    seen.add(k); D.append(dict(ctx,q=q,r=[str(x).lower() for x in acc],e=e,txt=1))
def eq(q,r,e):
    k=(ctx['t'],ctx['w'],ctx['a'],q)
    if k in seen: return
    seen.add(k); D.append(dict(ctx,q=q,r=r,e=e))
from math import gcd
def fr(n,d):
    g=gcd(n,d); return [f"{n}/{d}"]+([f"{n//g}/{d//g}"] if g>1 else [])
def pick(lo,hi,n,f=lambda x:True):
    s=set()
    while len(s)<n:
        x=R.randint(lo,hi)
        if f(x): s.add(x)
    return sorted(s,key=lambda _:R.random())
PL=["hundreds","tens","ones"]
U="Numbers to 1000"
# ---------- Unit 1
sec(1,U,1,"1.1 Hundreds, tens and ones",1,"Value of a digit")
for N in pick(123,987,8,lambda x:len(set(str(x)))==3 and '0' not in str(x)):
    p=R.randint(0,2);d=int(str(N)[p]);v=d*10**(2-p)
    tx(f"What is the value of the digit {d} in {N}?",nums(v),f"In {N} the digit {d} is in the {PL[p]} place. {d} {PL[p]} = <b>{v}</b>.")
sec(1,U,1,"1.1 Hundreds, tens and ones",2,"Make the number")
for N in pick(101,999,8,lambda x:'0' in str(x)[1:] or x%7==0):
    h,t,o=map(int,str(N))
    tx(f"{h} hundreds + {t} tens + {o} ones = ?",nums(N),f"{h} hundreds = {h*100}, {t} tens = {t*10}, {o} ones = {o}. {h*100} + {t*10} + {o} = <b>{N}</b>.")
sec(1,U,1,"1.1 Hundreds, tens and ones",3,"Number names")
for N in pick(101,999,6,lambda x:x%10!=0):
    tx(f"Write the number name for {N}.",[W(N)],f"Say the hundreds, then 'and', then the tens and ones. <b>{N}</b> is <b>{W(N)}</b>.")
for N in pick(120,980,4,lambda x:x%10!=0):
    tx(f"Write the number for {W(N)}.",[str(N)],f"{W(N)}: hundreds = {N//100}, then {N%100}. So the number is <b>{N}</b>.")
sec(1,U,2,"1.2 Comparing and ordering",1,"Bigger and smaller")
for a,b in [(R.randint(2,8)*100+R.randint(10,99),0) for _ in range(8)]:
    b=a+R.choice([-1,1])*R.choice([5,10,20,30,40,90]); b=max(b,101)
    if a==b: continue
    big=R.random()<.5; ans=max(a,b) if big else min(a,b)
    tx(f"Which number is {'bigger' if big else 'smaller'}: {a} or {b}?",[str(ans)],f"Compare the hundreds first, then the tens, then the ones. <b>{ans}</b> is {'bigger' if big else 'smaller'}.")
sec(1,U,2,"1.2 Comparing and ordering",2,"Ordering")
for _ in range(6):
    L=pick(100,999,3); big=R.random()<.5; ans=max(L) if big else min(L)
    tx(f"Which is the {'biggest' if big else 'smallest'} number: {L[0]}, {L[1]} or {L[2]}?",[str(ans)],f"Look at the hundreds digits first. In order: {', '.join(map(str,sorted(L)))}. The {'biggest' if big else 'smallest'} is <b>{ans}</b>.")
sec(1,U,2,"1.2 Comparing and ordering",3,"10 and 100 more or less")
for _ in range(8):
    N=R.randint(120,880); k=R.choice([10,100]); s=R.choice([1,-1]); r=N+s*k
    eq(f"{N} {'+' if s>0 else '-'} {k}",r,f"{k} {'more' if s>0 else 'less'}: change the {'tens' if k==10 else 'hundreds'} digit by 1. {N} {'+' if s>0 else '-'} {k} = <b>{r}</b>.")
sec(1,U,3,"1.3 Estimating and rounding",1,"Round to the nearest 10")
for N in pick(11,989,8,lambda x:x%10!=0):
    r=round(N/10+0.0001)*10 if N%10!=5 else (N//10+1)*10
    tx(f"Round {N} to the nearest 10.",nums(r),f"Look at the ones digit {N%10}. {'5 or more: round up' if N%10>=5 else 'less than 5: round down'}. {N} rounds to <b>{r}</b>.")
sec(1,U,3,"1.3 Estimating and rounding",2,"Round to the nearest 100")
for N in pick(110,990,8,lambda x:x%100!=0 and x%100!=50):
    r=(N//100+(1 if N%100>=50 else 0))*100
    tx(f"Round {N} to the nearest 100.",nums(r),f"Look at the tens digit {N//10%10}. {'5 or more: round up' if N%100>=50 else 'less than 5: round down'}. {N} rounds to <b>{r}</b>.")
# ---------- Unit 2
U="Statistics: tally charts and frequency tables"
sec(2,U,1,"2.1 Tally charts and frequency tables",1,"Counting tally marks")
for g,x in [(2,3),(3,1),(4,4),(1,2),(5,0),(3,4),(2,2),(4,1)]:
    n=g*5+x
    tx(f"A tally chart shows {g} groups of five (each group has a line through it) and {x} more single marks. What number is shown?",nums(n),f"Each group of five is 5. {g} x 5 = {g*5}. Then add the {x} single marks: {g*5} + {x} = <b>{n}</b>.")
sec(2,U,1,"2.1 Tally charts and frequency tables",2,"Reading frequency tables")
for items in [("red","blue","green"),("cats","dogs","fish"),("apples","bananas","oranges"),("football","tennis","swimming"),("rice","pasta","bread"),("rain","sun","cloud")]:
    v=pick(3,15,3);d=dict(zip(items,v))
    s=", ".join(f"{k} {x}" for k,x in d.items());top=max(d,key=d.get);low=min(d,key=d.get)
    tx(f"A frequency table shows: {s}. Which is the most popular?",[top],f"The biggest number is {d[top]}, so <b>{top}</b> is the most popular.")
    tx(f"A frequency table shows: {s}. How many are there in total?",nums(sum(v)),f"Add them: {' + '.join(map(str,v))} = <b>{sum(v)}</b>.")
    tx(f"A frequency table shows: {s}. How many more {top} than {low}?",nums(d[top]-d[low]),f"Subtract: {d[top]} - {d[low]} = <b>{d[top]-d[low]}</b>.")
# ---------- Unit 3
U="Addition, subtraction and money"
sec(3,U,1,"3.1 Addition",1,"Add 2-digit numbers")
for _ in range(10):
    a,b=R.randint(12,48),R.randint(11,49)
    eq(f"{a} + {b}",a+b,f"Add the tens: {a//10*10} + {b//10*10} = {a//10*10+b//10*10}. Add the ones: {a%10} + {b%10} = {a%10+b%10}. Together: <b>{a+b}</b>.")
sec(3,U,1,"3.1 Addition",2,"Add 3-digit numbers")
for _ in range(10):
    a,b=R.randint(110,690),R.choice([R.randint(10,90),R.randint(100,290)])
    eq(f"{a} + {b}",a+b,f"Add the hundreds, tens and ones in parts. {a} + {b} = <b>{a+b}</b>. Check by counting on from {a}.")
sec(3,U,1,"3.1 Addition",3,"Estimate sums")
for _ in range(6):
    a,b=R.randint(21,79),R.randint(21,79);ra,rb=round(a/10+.01)*10,round(b/10+.01)*10
    tx(f"Estimate {a} + {b} by rounding each number to the nearest 10.",nums(ra+rb),f"{a} rounds to {ra} and {b} rounds to {rb}. {ra} + {rb} = <b>{ra+rb}</b>.")
sec(3,U,2,"3.2 Subtraction",1,"Subtract 2-digit numbers")
for _ in range(10):
    a=R.randint(40,99);b=R.randint(11,a-10)
    eq(f"{a} - {b}",a-b,f"Count back or use tens and ones. {a} - {b} = <b>{a-b}</b>. Check: {a-b} + {b} = {a} ✔")
sec(3,U,2,"3.2 Subtraction",2,"Subtract 3-digit numbers")
for _ in range(10):
    a=R.randint(250,950);b=R.choice([R.randint(11,99),R.randint(100,240)])
    eq(f"{a} - {b}",a-b,f"Take away in parts. {a} - {b} = <b>{a-b}</b>. Check: {a-b} + {b} = {a} ✔")
sec(3,U,3,"3.3 Money",1,"Adding money")
for _ in range(8):
    a=R.randint(1,9)*100+R.choice([0,50]);b=R.randint(1,8)*100+R.choice([0,50])
    tx(f"A book costs {ms(a)} and a pen costs {ms(b)}. How much do they cost together?",money(a+b),f"Add dollars and cents: {ms(a)} + {ms(b)} = <b>{ms(a+b)}</b>.")
sec(3,U,3,"3.3 Money",2,"Change")
for _ in range(8):
    p=R.randint(1,9)*100+R.choice([0,50]);pay=R.choice([1000,2000]);pay=pay if pay>p else 2000
    tx(f"You pay {ms(pay)} for something that costs {ms(p)}. How much change do you get?",money(pay-p),f"Change = money paid - price. {ms(pay)} - {ms(p)} = <b>{ms(pay-p)}</b>.")
sec(3,U,3,"3.3 Money",3,"Dollars and cents")
for d in (2,3,5,7,10):
    tx(f"How many cents are there in ${d}?",nums(d*100),f"$1 = 100 cents. {d} x 100 = <b>{d*100}</b> cents.")
for d,c in ((3,50),(4,25),(6,75),(2,20)):
    tx(f"How many cents is ${d}.{c:02d}?",nums(d*100+c),f"{d} dollars = {d*100} cents. Add {c} cents: <b>{d*100+c}</b> cents.")
# ---------- Unit 4
U="3D shapes"
sec(4,U,1,"4.1 3D shapes",1,"Faces, edges and vertices")
S={"cube":(6,12,8),"cuboid":(6,12,8),"triangular prism":(5,9,6),"square-based pyramid":(5,8,5),"triangle-based pyramid":(4,6,4)}
for s,(f,e,v) in S.items():
    for i,(nm,val) in enumerate((("faces",f),("edges",e),("vertices",v))):
        if s in("cuboid",) and i>0: continue
        tx(f"How many {nm} does a {s} have?",nums(val),f"A {s} has <b>{f}</b> faces, <b>{e}</b> edges and <b>{v}</b> vertices (corners). So the answer is <b>{val}</b>.")
tx("How many flat faces does a cylinder have?",nums(2),"A cylinder has 2 flat circular faces and 1 curved surface.")
tx("How many flat faces does a cone have?",nums(1),"A cone has 1 flat circular face (the base), 1 curved surface and 1 vertex.")
tx("How many flat faces does a sphere have?",nums(0),"A sphere is completely curved. It has no flat faces, no edges and no vertices.")
sec(4,U,1,"4.1 3D shapes",2,"Name the 3D shape")
for q,a,e in [("I have 6 square faces that are all the same. What am I?",["cube","a cube"],"Only a cube has 6 equal square faces."),
 ("I have 2 flat circular faces and 1 curved surface. What am I?",["cylinder","a cylinder"],"This describes a cylinder, like a tin can."),
 ("I am round all over, with no flat faces. What am I?",["sphere","a sphere"],"A ball is a sphere."),
 ("I have 1 flat circular face, 1 curved surface and 1 vertex. What am I?",["cone","a cone"],"This is a cone, like an ice-cream cone."),
 ("I have 5 faces: 1 square and 4 triangles. What am I?",["square based pyramid","square-based pyramid","a square based pyramid","a square-based pyramid","pyramid"],"A square base and 4 triangle sides make a square-based pyramid."),
 ("I have 2 triangle faces and 3 rectangle faces. What am I?",["triangular prism","a triangular prism"],"2 triangles + 3 rectangles = a triangular prism."),
 ("A shoebox has 6 rectangle faces. What 3D shape is it?",["cuboid","a cuboid","rectangular prism","a rectangular prism"],"A box with rectangle faces is a cuboid (rectangular prism)."),
 ("Which 3D shape is a dice?",["cube","a cube"],"A dice has 6 equal square faces, so it is a cube.")]:
    tx(q,a,e)
# ---------- Unit 5
U="Multiplication and division"
sec(5,U,1,"5.1 Exploring multiplication and division",1,"Equal groups")
for g,n in [(3,5),(4,6),(5,4),(6,3),(2,9),(7,2),(4,10),(3,8)]:
    eq(f"{g} x {n}",g*n,f"{g} groups of {n}: {' + '.join([str(n)]*g)} = <b>{g*n}</b>.")
sec(5,U,1,"5.1 Exploring multiplication and division",2,"Sharing equally")
for t,g in [(20,4),(18,3),(15,5),(24,6),(30,5),(16,2),(27,3),(40,10)]:
    eq(f"{t} ÷ {g}",t//g,f"Share {t} into {g} equal groups. Each group gets <b>{t//g}</b>. Check: {t//g} x {g} = {t} ✔")
for k,(t,g,thing) in enumerate([(12,3,"children"),(20,5,"boxes"),(18,2,"friends")]):
    pass
sec(5,U,2,"5.2 Connecting 2x, 4x and 8x",1,"The 2x, 4x and 8x tables")
for m in (2,4,8):
    for n in pick(2,10,5):
        e={2:"Double the number.",4:"Double the 2x answer: 4 x n = double (2 x n).",8:"Double the 4x answer: 8 x n = double (4 x n)."}[m]
        eq(f"{m} x {n}",m*n,f"{e} {m} x {n} = <b>{m*n}</b>.")
sec(5,U,2,"5.2 Connecting 2x, 4x and 8x",2,"Division facts for 2, 4 and 8")
for m in (2,4,8):
    for n in pick(2,10,4):
        eq(f"{m*n} ÷ {m}",n,f"Think: {m} x ? = {m*n}. {m} x {n} = {m*n}, so {m*n} ÷ {m} = <b>{n}</b>.")
sec(5,U,3,"5.3 Connecting 3x, 6x and 9x",1,"The 3x, 6x and 9x tables")
for m in (3,6,9):
    for n in pick(2,10,5):
        e={3:"Count in 3s.",6:"Double the 3x answer: 6 x n = double (3 x n).",9:"Use 10 x n then subtract n: 9 x n = 10 x n - n."}[m]
        eq(f"{m} x {n}",m*n,f"{e} {m} x {n} = <b>{m*n}</b>.")
sec(5,U,3,"5.3 Connecting 3x, 6x and 9x",2,"Division facts for 3, 6 and 9")
for m in (3,6,9):
    for n in pick(2,10,4):
        eq(f"{m*n} ÷ {m}",n,f"Think: {m} x ? = {m*n}. {m} x {n} = {m*n}, so {m*n} ÷ {m} = <b>{n}</b>.")
# ---------- Unit 6
U="Measurement, area and perimeter"
sec(6,U,1,"6.1 Measurement",1,"Length units")
for q,a,e in [("How many centimetres are in 1 metre?",nums(100),"1 m = 100 cm."),("How many millimetres are in 1 centimetre?",nums(10),"1 cm = 10 mm."),("How many metres are in 1 kilometre?",nums(1000),"1 km = 1000 m.")]: tx(q,a,e)
for m in (2,3,5,7,9): tx(f"{m} m = ? cm",nums(m*100),f"1 m = 100 cm. {m} x 100 = <b>{m*100}</b> cm.")
for c in (2,4,6,9): tx(f"{c} cm = ? mm",nums(c*10),f"1 cm = 10 mm. {c} x 10 = <b>{c*10}</b> mm.")
for q,a in [("Which unit would you use to measure the length of a classroom: mm, m or km?","m"),("Which unit would you use to measure the distance between two towns: cm, m or km?","km"),("Which unit would you use to measure the length of an ant: mm, m or km?","mm")]:
    tx(q,[a],f"Choose a sensible unit: <b>{a}</b> fits best here.")
sec(6,U,2,"6.2 2D shapes and perimeter",1,"Perimeter of rectangles")
for _ in range(8):
    l,w=R.randint(4,12),R.randint(2,8)
    if l==w: continue
    tx(f"A rectangle is {l} cm long and {w} cm wide. What is its perimeter in cm?",nums(2*(l+w)),f"Perimeter = distance all the way round. {l} + {w} + {l} + {w} = <b>{2*(l+w)}</b> cm.")
sec(6,U,2,"6.2 2D shapes and perimeter",2,"Perimeter of squares and triangles")
for s in (3,5,6,8,10): tx(f"A square has sides of {s} cm. What is its perimeter in cm?",nums(4*s),f"A square has 4 equal sides. {s} + {s} + {s} + {s} = <b>{4*s}</b> cm.")
for a,b,c in [(3,4,5),(6,6,6),(5,5,8),(7,9,10)]: tx(f"A triangle has sides {a} cm, {b} cm and {c} cm. What is its perimeter in cm?",nums(a+b+c),f"Add all the sides: {a} + {b} + {c} = <b>{a+b+c}</b> cm.")
sec(6,U,3,"6.3 Introducing area",1,"Area by counting squares")
for l,w in [(4,3),(5,2),(6,3),(5,5),(7,2),(4,4),(8,3),(6,5)]:
    tx(f"A rectangle is {l} squares long and {w} squares wide. How many squares cover it (its area)?",nums(l*w),f"There are {w} rows of {l} squares. {w} x {l} = <b>{l*w}</b> squares.")
# ---------- Unit 7
U="Fractions of shapes"
sec(7,U,1,"7.1 Fractions and equivalence of shapes",1,"Naming fractions")
FR={(1,2):["1/2","half","one half","a half"],(1,3):["1/3","third","one third","a third"],(1,4):["1/4","quarter","one quarter","a quarter","one fourth"],(2,4):["2/4","two quarters"],(3,4):["3/4","three quarters"],(2,3):["2/3","two thirds"]}
for (n,d),acc in FR.items():
    tx(f"A shape is split into {d} equal parts and {n} part{'s are' if n>1 else ' is'} shaded. What fraction is shaded?",acc,f"{n} out of {d} equal parts: write <b>{n}/{d}</b>.")
for q,a,e in [("How many quarters make one whole?",nums(4),"4 quarters = 1 whole."),("How many halves make one whole?",nums(2),"2 halves = 1 whole."),("How many thirds make one whole?",nums(3),"3 thirds = 1 whole."),("How many halves are there in 3 wholes?",nums(6),"Each whole has 2 halves. 3 x 2 = 6."),("How many quarters are there in 2 wholes?",nums(8),"Each whole has 4 quarters. 2 x 4 = 8.")]: tx(q,a,e)
sec(7,U,1,"7.1 Fractions and equivalence of shapes",2,"Equivalent fractions")
for q,a,e in [("1/2 = ?/4",nums(2),"Cut each half into 2 quarters: 1/2 = <b>2</b>/4."),("1/2 = ?/8",nums(4),"1/2 = 2/4 = <b>4</b>/8."),("2/4 = 1/?",nums(2),"2 quarters is the same as 1 half: 2/4 = 1/<b>2</b>."),("1/4 = ?/8",nums(2),"Cut each quarter in half: 1/4 = <b>2</b>/8."),("4/8 = 1/?",nums(2),"4 eighths make half: 4/8 = 1/<b>2</b>."),("3/6 = 1/?",nums(2),"3 sixths make half: 3/6 = 1/<b>2</b>.")]: tx("Complete: "+q,a,e)
for q,a,e in [("Which is bigger: 1/2 or 1/4?",["1/2","half","one half"],"The fewer the parts, the bigger each part. 1/2 is bigger than 1/4."),("Which is smaller: 1/3 or 1/2?",["1/3","third","one third"],"1/3 is smaller than 1/2."),("Which is bigger: 1/4 or 1/8?",["1/4","quarter","one quarter"],"1/4 is bigger than 1/8.")]: tx(q,a,e)
# ---------- Unit 8
U="Time"
sec(8,U,1,"8.1 Time",1,"Telling the time")
for q,a in [("half past 7","7:30"),("quarter past 4","4:15"),("quarter to 9","8:45"),("half past 12","12:30"),("20 minutes past 6","6:20"),("10 minutes to 3","2:50"),("5 minutes past 10","10:05"),("quarter to 1","12:45")]:
    tx(f"Write '{q}' in digital time (for example 3:30).",[a],f"Past means after the hour, to means before the next hour. '{q}' is <b>{a}</b>.")
sec(8,U,1,"8.1 Time",2,"Units of time")
for q,a,e in [("How many minutes are there in 1 hour?",nums(60),"1 hour = 60 minutes."),("How many seconds are there in 1 minute?",nums(60),"1 minute = 60 seconds."),("How many hours are there in 1 day?",nums(24),"1 day = 24 hours."),("How many days are there in 1 week?",nums(7),"1 week = 7 days."),("How many months are there in 1 year?",nums(12),"1 year = 12 months."),("How many minutes are there in half an hour?",nums(30),"Half of 60 is 30."),("How many minutes are there in a quarter of an hour?",nums(15),"A quarter of 60 is 15."),("How many days are there in a normal year?",nums(365),"A normal year has 365 days; a leap year has 366."),("How many days are there in a leap year?",nums(366),"A leap year has one extra day (29 February): 366 days.")]: tx(q,a,e)
sec(8,U,1,"8.1 Time",3,"How long does it take?")
for h1,m1,h2,m2 in [(2,0,5,0),(8,30,3+12,30),(9,15,9,45),(1,0,1,50),(7,0,7,25),(10,30,12,30),(3,10,3,55),(11,0,11,35)]:
    d=(h2*60+m2)-(h1*60+m1)
    f=lambda h,m:f"{h%12 or 12}:{m:02d}"
    tx(f"From {f(h1,m1)} to {f(h2,m2)}, how many {'hours' if d%60==0 else 'minutes'} pass?",nums(d//60 if d%60==0 else d),f"Count on from {f(h1,m1)} to {f(h2,m2)}: <b>{d//60 if d%60==0 else d}</b> {'hours' if d%60==0 else 'minutes'}.")
# ---------- Unit 9
U="More addition and subtraction"
sec(9,U,1,"9.1 Addition: regrouping tens and reordering",1,"Add with regrouping")
for _ in range(10):
    a=R.randint(35,89);b=R.randint(36,89)
    while (a%10)+(b%10)<10: b=R.randint(36,89)
    eq(f"{a} + {b}",a+b,f"Ones: {a%10} + {b%10} = {a%10+b%10}, regroup 10 ones as 1 ten. Tens: {a//10} + {b//10} + 1 = {a//10+b//10+1}. Answer <b>{a+b}</b>.")
sec(9,U,1,"9.1 Addition: regrouping tens and reordering",2,"Add 3-digit numbers")
for _ in range(10):
    a=R.randint(150,480);b=R.randint(150,490)
    eq(f"{a} + {b}",a+b,f"Add the hundreds, tens and ones, regrouping when a column makes 10 or more. {a} + {b} = <b>{a+b}</b>.")
sec(9,U,2,"9.2 Subtraction: regrouping tens",1,"Subtract with regrouping")
for _ in range(10):
    a=R.randint(52,95);b=R.randint(13,a-8)
    while b%10<=a%10 or b>=a: b=R.randint(13,a-8)
    eq(f"{a} - {b}",a-b,f"You cannot take {b%10} from {a%10}, so regroup 1 ten as 10 ones: {10+a%10} - {b%10} = {10+a%10-b%10}. Tens: {a//10-1} - {b//10} = {a//10-1-b//10}. Answer <b>{a-b}</b>.")
sec(9,U,2,"9.2 Subtraction: regrouping tens",2,"Subtract 3-digit numbers")
for _ in range(10):
    a=R.randint(420,950);b=R.randint(120,a-150)
    eq(f"{a} - {b}",a-b,f"Subtract hundreds, tens and ones, regrouping when needed. Check: {a-b} + {b} = {a} ✔. Answer <b>{a-b}</b>.")
sec(9,U,3,"9.3 Complements",1,"Complements to 100")
for n in (35,60,45,72,18,90,64,27):
    tx(f"Complete: {n} + ? = 100",nums(100-n),f"{100-n} + {n} = 100. Think: make the next ten ({n}+{(10-n%10)%10}={n+(10-n%10)%10}), then add up to 100. Answer <b>{100-n}</b>.")
sec(9,U,3,"9.3 Complements",2,"Complements to 1000")
for n in (300,750,450,600,250,820,125,675):
    tx(f"Complete: {n} + ? = 1000",nums(1000-n),f"{n} + {1000-n} = 1000. Answer <b>{1000-n}</b>.")
# ---------- Unit 10
U="Graphs"
sec(10,U,1,"10.1 Pictograms and bar charts",1,"Pictograms")
for k,n in [(2,6),(5,4),(2,9),(10,3),(5,7),(2,5)]:
    tx(f"In a pictogram, each picture stands for {k} children. There are {n} pictures. How many children is that?",nums(k*n),f"{n} pictures x {k} = <b>{k*n}</b> children.")
for k,c in [(2,14),(5,35),(10,50),(2,8)]:
    tx(f"In a pictogram, each picture stands for {k} children. How many pictures show {c} children?",nums(c//k),f"{c} ÷ {k} = <b>{c//k}</b> pictures.")
sec(10,U,1,"10.1 Pictograms and bar charts",2,"Bar charts")
for items in [("Cats","Dogs","Fish"),("Red","Blue","Green"),("Mon","Tue","Wed"),("Football","Tennis","Swimming")]:
    v=pick(4,20,3);d=dict(zip(items,v));s=", ".join(f"{k} {x}" for k,x in d.items());top=max(d,key=d.get);low=min(d,key=d.get)
    tx(f"A bar chart shows: {s}. Which bar is the longest?",[top.lower()],f"The longest bar shows the biggest number. {top} has {d[top]}, so the answer is <b>{top}</b>.")
    tx(f"A bar chart shows: {s}. Which bar is the shortest?",[low.lower()],f"The shortest bar shows the smallest number. {low} has {d[low]}, so the answer is <b>{low}</b>.")
    tx(f"A bar chart shows: {s}. What is the difference between the longest and the shortest bar?",nums(d[top]-d[low]),f"{d[top]} - {d[low]} = <b>{d[top]-d[low]}</b>.")
sec(10,U,2,"10.2 Venn and Carroll diagrams",1,"Venn diagrams")
for lim,name in [(10,"bigger than 5"),(12,"bigger than 6")]:
    k=int(name.split()[-1]);both=[n for n in range(1,lim+1) if n%2==0 and n>k]
    tx(f"Numbers 1 to {lim} are sorted into two circles: 'even numbers' and '{name}'. Which numbers go in both circles? (write them with spaces)",[" ".join(map(str,both))],f"Even numbers that are also {name}: <b>{', '.join(map(str,both))}</b>.")
    tx(f"Numbers 1 to {lim} are sorted into two circles: 'even numbers' and '{name}'. How many numbers go in both circles?",nums(len(both)),f"The numbers in both circles are {', '.join(map(str,both))}. That is <b>{len(both)}</b> numbers.")
for q,a,e in [("In a Venn diagram, which numbers from 1 to 10 are in neither 'even' nor 'bigger than 5'? (write them with spaces)",["1 3 5"],"Odd numbers that are 5 or less: <b>1, 3, 5</b>."),
 ("In a Carroll diagram, a number is sorted by 'odd or even' and 'bigger than 10 or not'. Where does 14 go?",["even and bigger than 10","even bigger than 10"],"14 is even and 14 is bigger than 10.")]: tx(q,a,e)
# ---------- Unit 11
U="More multiplication and division"
sec(11,U,1,"11.1 Revisiting multiplication and division",1,"Times tables mix")
for _ in range(10):
    a,b=R.randint(2,10),R.randint(2,10); eq(f"{a} x {b}",a*b,f"{a} groups of {b}. {a} x {b} = <b>{a*b}</b>.")
for _ in range(6):
    a,b=R.randint(2,10),R.randint(2,10); eq(f"{a*b} ÷ {a}",b,f"Think: {a} x ? = {a*b}. {a} x {b} = {a*b}, so the answer is <b>{b}</b>.")
sec(11,U,2,"11.2 Playing with multiplication and division",1,"Multiply three numbers")
for a,b,c in [(2,3,5),(4,5,2),(5,5,4),(3,2,6),(9,3,2),(2,2,8),(5,3,4),(10,2,3)]:
    eq(f"{a} x {b} x {c}",a*b*c,f"Multiply two numbers first: {a} x {b} = {a*b}. Then {a*b} x {c} = <b>{a*b*c}</b>.")
sec(11,U,3,"11.3 Extending multiplication and division",1,"2-digit x 1-digit")
for a,b in [(11,5),(12,4),(13,3),(14,2),(15,4),(19,2),(21,3),(16,3),(12,5),(18,3)]:
    eq(f"{a} x {b}",a*b,f"Partition {a} = {a//10*10} + {a%10}. {a//10*10} x {b} = {a//10*10*b} and {a%10} x {b} = {a%10*b}. {a//10*10*b} + {a%10*b} = <b>{a*b}</b>.")
sec(11,U,3,"11.3 Extending multiplication and division",2,"2-digit ÷ 1-digit")
for a,b in [(48,4),(36,3),(52,2),(75,5),(84,4),(66,3),(90,5),(96,2)]:
    eq(f"{a} ÷ {b}",a//b,f"Share {a} into {b} equal groups. Check: {a//b} x {b} = {a} ✔. Answer <b>{a//b}</b>.")
# ---------- Unit 12
U="More fractions"
sec(12,U,1,"12.1 Fractions of numbers",1,"Fraction of a number")
for n,d,N in [(1,2,18),(1,2,30),(1,4,20),(1,4,12),(1,3,12),(1,3,21),(1,5,25),(1,10,50),(3,4,8),(2,3,9)]:
    r=N//d*n
    tx(f"What is {n}/{d} of {N}?",nums(r),f"Divide {N} by {d}: {N} ÷ {d} = {N//d}." + (f" Then multiply by {n}: {N//d} x {n} = <b>{r}</b>." if n>1 else f" So 1/{d} of {N} is <b>{r}</b>."))
sec(12,U,2,"12.2 Ordering and comparing fractions",1,"Biggest fraction")
for L in [("1/2","1/4","1/8"),("1/3","1/6","1/2"),("1/5","1/10","1/2"),("1/4","1/3","1/2")]:
    v=sorted(L,key=lambda s:-1/int(s[2:]))
    tx(f"Which is the biggest fraction: {', '.join(L)}?",[v[0]],f"For unit fractions, the smaller the bottom number, the bigger the fraction. Order: {' > '.join(v)}. The biggest is <b>{v[0]}</b>.")
    tx(f"Which is the smallest fraction: {', '.join(L)}?",[v[-1]],f"Order: {' > '.join(v)}. The smallest is <b>{v[-1]}</b>.")
sec(12,U,3,"12.3 Calculating with fractions",1,"Add and subtract fractions")
for a,b,d in [(1,1,4),(1,2,4),(2,3,8),(1,1,3),(3,2,10),(2,2,6)]:
    tx(f"1 fraction sum: {a}/{d} + {b}/{d} = ? (write like 3/4)".replace("1 fraction sum: ","Add: "),fr(a+b,d),f"The bottom number stays {d}. Add the tops: {a} + {b} = {a+b}. Answer <b>{a+b}/{d}</b>.")
for a,b,d in [(3,1,4),(5,2,8),(2,1,3),(4,3,6)]:
    tx(f"Subtract: {a}/{d} - {b}/{d} = ? (write like 1/4)",fr(a-b,d),f"The bottom number stays {d}. Subtract the tops: {a} - {b} = {a-b}. Answer <b>{a-b}/{d}</b>.")
# ---------- Unit 13
U="Measures"
sec(13,U,1,"13.1 Mass",1,"Kilograms and grams")
tx("How many grams are there in 1 kilogram?",nums(1000),"1 kg = 1000 g.")
for k in (2,3,5,6): tx(f"{k} kg = ? g",nums(k*1000),f"1 kg = 1000 g. {k} x 1000 = <b>{k*1000}</b> g.")
for g in (2000,4000,7000): tx(f"{g} g = ? kg",nums(g//1000),f"1000 g = 1 kg. {g} ÷ 1000 = <b>{g//1000}</b> kg.")
tx("Half a kilogram is how many grams?",nums(500),"Half of 1000 g is 500 g.")
tx("Which is heavier: 1 kg or 900 g?",["1 kg","1kg","1 kilogram"],"1 kg = 1000 g, and 1000 g is more than 900 g.")
sec(13,U,2,"13.2 Capacity",1,"Litres and millilitres")
tx("How many millilitres are there in 1 litre?",nums(1000),"1 litre = 1000 ml.")
for l in (2,3,4,5): tx(f"{l} litres = ? ml",nums(l*1000),f"1 litre = 1000 ml. {l} x 1000 = <b>{l*1000}</b> ml.")
for m in (3000,6000): tx(f"{m} ml = ? litres",nums(m//1000),f"1000 ml = 1 litre. {m} ÷ 1000 = <b>{m//1000}</b> litres.")
tx("Half a litre is how many millilitres?",nums(500),"Half of 1000 ml is 500 ml.")
tx("A jug holds 250 ml. How many jugs fill 1 litre?",nums(4),"4 x 250 ml = 1000 ml = 1 litre.")
sec(13,U,3,"13.3 Temperature",1,"Reading temperature")
for q,a,e in [("At what temperature in °C does water freeze?",nums(0),"Water freezes at 0 °C."),("At what temperature in °C does water boil?",nums(100),"Water boils at 100 °C."),("What do we use to measure temperature?",["thermometer","a thermometer"],"A thermometer measures temperature.")]: tx(q,a,e)
for t,c in [(12,7),(20,5),(8,9),(25,10)]: tx(f"The temperature is {t} °C and it rises by {c} °C. What is the new temperature in °C?",nums(t+c),f"Rises means add: {t} + {c} = <b>{t+c}</b> °C.")
for t,c in [(18,6),(30,12),(15,9)]: tx(f"The temperature is {t} °C and it falls by {c} °C. What is the new temperature in °C?",nums(t-c),f"Falls means subtract: {t} - {c} = <b>{t-c}</b> °C.")
# ---------- Unit 14
U="Time (2)"
sec(14,U,1,"14.1 Time",1,"a.m. and p.m.")
for q,a,e in [("Is 7 o'clock in the morning a.m. or p.m.?",["am","a.m."],"Morning times are a.m."),("Is 3 o'clock in the afternoon a.m. or p.m.?",["pm","p.m."],"Afternoon and evening times are p.m."),("Is 9 o'clock at night a.m. or p.m.?",["pm","p.m."],"Night before midnight is p.m."),("What time is midday: 12 noon or 12 midnight?",["12 noon","noon"],"Midday is 12 noon.")]: tx(q,a,e)
sec(14,U,1,"14.1 Time",2,"Days and months")
for m,d in [("January",31),("February (normal year)",28),("April",30),("June",30),("September",30),("November",30),("July",31),("December",31)]:
    tx(f"How many days are in {m}?",nums(d),f"{m.split(' (')[0]} has <b>{d}</b> days. Remember: 30 days have September, April, June and November.")
sec(14,U,2,"14.2 Timetables",1,"Reading timetables")
for h,m,d in [(9,20,45),(8,10,50),(10,5,40),(1,15,35),(3,0,25),(11,30,55)]:
    t1=h*60+m;t2=t1+d;f=lambda x:f"{(x//60)%12 or 12}:{x%60:02d}"
    tx(f"A bus leaves at {f(t1)} and arrives at {f(t2)}. How many minutes is the journey?",nums(d),f"Count on from {f(t1)} to {f(t2)}: <b>{d}</b> minutes.")
for h,m,d in [(9,0,30),(2,15,45),(6,40,20)]:
    t1=h*60+m;t2=t1+d;f=lambda x:f"{(x//60)%12 or 12}:{x%60:02d}"
    tx(f"A film starts at {f(t1)} and lasts {d} minutes. What time does it finish? (write like 3:30)",[f(t2)],f"{f(t1)} + {d} minutes = <b>{f(t2)}</b>.")
# ---------- Unit 15
U="Angles and movement"
sec(15,U,1,"15.1 Angles, direction, position and movement",1,"Angles")
for q,a,e in [("How many degrees are there in a right angle?",nums(90),"A right angle is 90°."),("How many right angles make a full turn?",nums(4),"4 right angles make a full turn (360°)."),("How many right angles make a half turn?",nums(2),"2 right angles make a half turn (180°)."),("How many right angles make a quarter turn?",nums(1),"A quarter turn is 1 right angle."),("How many right angles does a square have?",nums(4),"A square has 4 right-angled corners."),("How many right angles does a rectangle have?",nums(4),"A rectangle has 4 right-angled corners."),("Is an angle smaller than a right angle called acute or obtuse?",["acute"],"Smaller than 90° is acute; bigger than 90° is obtuse.")]: tx(q,a,e)
sec(15,U,1,"15.1 Angles, direction, position and movement",2,"Direction")
for q,a,e in [("Which direction is opposite to north?",["south"],"North and south are opposite."),("Which direction is opposite to east?",["west"],"East and west are opposite."),("You face north and turn a quarter turn clockwise. Which way do you face?",["east"],"Clockwise from north: east."),("You face east and turn a quarter turn clockwise. Which way do you face?",["south"],"Clockwise: north, east, south, west."),("You face north and turn a half turn. Which way do you face?",["south"],"A half turn faces the opposite way."),("You face north and turn a quarter turn anticlockwise. Which way do you face?",["west"],"Anticlockwise from north: west.")]: tx(q,a,e)
# ---------- Unit 16
U="Chance"
sec(16,U,1,"16.1 Chance",1,"Certain, likely, unlikely or impossible")
for q,a in [("The sun will rise tomorrow.","certain"),("A cat will learn to fly like a bird.","impossible"),("It will be hot in the desert in summer.","likely"),("It will snow in a hot desert tomorrow.","unlikely"),("You will get a number from 1 to 6 when you roll a normal dice.","certain"),("You will roll a 7 on a normal dice.","impossible"),("A fair coin lands on heads.","even chance"),("A baby will be born today somewhere in the world.","certain"),("You will meet a real dinosaur at school today.","impossible"),("You will see a car on a busy road today.","likely")]:
    tx(f"Is this certain, likely, unlikely, impossible or an even chance? \"{q}\"",[a] if a!="even chance" else ["even chance","even","equal chance"],f"Think how often it would happen. This is <b>{a}</b>.")
# ---------- Unit 17
U="Pattern and symmetry"
sec(17,U,1,"17.1 Shape and symmetry",1,"Lines of symmetry")
for s,n in [("square",4),("rectangle",2),("equilateral triangle",3),("circle","lots"),("letter A",1),("letter H",2),("letter T",1)]:
    if n=="lots": tx("Does a circle have lots of lines of symmetry or none?",["lots","lots of lines","lots of lines of symmetry","many"],"You can fold a circle in half in many ways, so it has lots of lines of symmetry."); continue
    tx(f"How many lines of symmetry does a {s} have?",nums(n),f"A line of symmetry splits a shape into two matching halves. A {s} has <b>{n}</b>.")
sec(17,U,2,"17.2 Pattern and symmetry",1,"Number patterns")
for st,d,n in [(2,2,5),(5,5,5),(10,10,5),(3,3,5),(4,4,5),(1,3,5),(100,10,5),(50,-5,5),(30,-3,5),(7,7,5)]:
    seq=[st+d*i for i in range(n)]
    tx(f"What number comes next? {', '.join(map(str,seq))}, ?",nums(seq[-1]+d),f"The pattern {'adds' if d>0 else 'subtracts'} {abs(d)} each time. {seq[-1]} {'+' if d>0 else '-'} {abs(d)} = <b>{seq[-1]+d}</b>.")
for st,d in [(5,5),(3,3),(10,2),(100,-10)]:
    seq=[st+d*i for i in range(4)]
    tx(f"What is the rule for this pattern? {', '.join(map(str,seq))}  (write like 'add 5' or 'subtract 5')",[f"{'add' if d>0 else 'subtract'} {abs(d)}",f"{'+' if d>0 else '-'}{abs(d)}",f"{'plus' if d>0 else 'minus'} {abs(d)}"],f"Each number is {abs(d)} {'more' if d>0 else 'less'}, so the rule is <b>{'add' if d>0 else 'subtract'} {abs(d)}</b>.")
for q,a in [("ABABAB ... What letter comes next? (A B A B A B ?)","A"),("AABAAB ... What letter comes next? (A A B A A B A A ?)","B")]:
    tx(q,[a.lower()],f"Follow the repeating pattern. The next letter is <b>{a}</b>.")
open('grade3.js','w').write('const QUESTIONS3='+json.dumps(D,separators=(',',':'),ensure_ascii=False)+';\n')
import collections
print(len(D)); c=collections.Counter(d['t'] for d in D); print(sorted(c.items()))
bad=[d for d in D if not d['r'] or not d['e'] or not d['q']]; print('bad',len(bad))
