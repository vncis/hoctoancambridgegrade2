import re, json
hdr=open('/home/claude/g3/gen3.py').read().split('# ---------- Unit 1')[0]
exec(hdr)
UN={1:"Numbers and the number system",2:"Time and timetables",3:"Addition, subtraction and number sentences",4:"Likelihood",5:"Multiplication, multiples and factors",6:"2D shapes",7:"Fractions",8:"Angles",9:"Comparing, rounding and dividing",10:"Collecting and recording data",11:"Fractions and percentages",12:"Investigating 3D shapes and nets",13:"Addition and subtraction",14:"Area and perimeter",15:"Special numbers",16:"Data display and interpretation",17:"Multiplication and division",18:"Position, direction and movement"}
SN={(1,1):"1.1 Counting and sequences",(1,2):"1.2 More on negative numbers",(1,3):"1.3 Understanding place value",(2,1):"2.1 Time",(2,2):"2.2 Timetables and time intervals",(3,1):"3.1 Using a symbol to represent a missing number or operation",(3,2):"3.2 Addition and subtraction of whole numbers",(3,3):"3.3 Generalising with odd and even numbers",(4,1):"4.1 Likelihood",(5,1):"5.1 Tables, multiples and factors",(5,2):"5.2 Multiplication",(6,1):"6.1 2D shapes and tessellation",(6,2):"6.2 Symmetry",(7,1):"7.1 Understanding fractions",(7,2):"7.2 Fractions as operators",(8,1):"8.1 Comparing angles",(8,2):"8.2 Acute and obtuse",(8,3):"8.3 Estimating angles",(9,1):"9.1 Rounding, ordering and comparing whole numbers",(9,2):"9.2 Division of 2-digit numbers",(10,1):"10.1 How to collect and record data",(11,1):"11.1 Equivalence, comparing and ordering fractions",(11,2):"11.2 Percentages",(12,1):"12.1 The properties of 3D shapes",(12,2):"12.2 Nets of 3D shapes",(13,1):"13.1 Adding and subtracting efficiently",(13,2):"13.2 Adding and subtracting fractions with the same denominator",(14,1):"14.1 Estimating and measuring area and perimeter",(14,2):"14.2 Area and perimeter of rectangles",(15,1):"15.1 Ordering and comparing numbers",(15,2):"15.2 Working with special numbers",(15,3):"15.3 Tests of divisibility",(16,1):"16.1 Displaying and interpreting data",(17,1):"17.1 Developing written methods of multiplication",(17,2):"17.2 Developing written methods of division",(18,1):"18.1 Position and movement",(18,2):"18.2 Reflecting 2D shapes"}
def S(u,s,a,an): sec(u,UN[u],s,SN[(u,s)],a,an)
def negs(n): return [str(n),f"minus {abs(n)}",f"negative {abs(n)}"] if n<0 else nums(n)
YN=lambda b:["yes"] if b else ["no"]
# ---- printed sums
T=open('/tmp/g4.txt').read().split('\f'); cu,cs=1,1
eqre=re.compile(r'(?<![\d.,])(\d[\d,]*(?:\s*[+–−\-×x÷]\s*\d[\d,]*)+)\s*=\s*(?!\s*[\d?])')
OP={'+':'+','–':'-','−':'-','-':'-','×':'*','x':'*','÷':'/'}
for p in T[10:]:
    for l in p.split('\n'):
        m=re.match(r'^\s{20,}(\d+)\.(\d+) [A-Z]',l)
        if m and (int(m[1]),int(m[2])) in SN: cu,cs=int(m[1]),int(m[2])
    for m in eqre.finditer(p):
        ex=re.sub(r'[\s,]+','',m[1]); py=''.join(OP.get(c,c) for c in ex)
        try: v=eval(py)
        except Exception: continue
        if v!=int(v) or v<0: continue
        v=int(v); q=re.sub(r'([+–−\-×x÷])',r' \1 ',ex).replace('–','-').replace('−','-').replace('×','x')
        S(cu,cs,1,"Workbook questions")
        if '÷' in q: e=f"Think of sharing or the times table, then check by multiplying back. The answer is <b>{v}</b>."
        elif ' x ' in q: e=f"Use place value or partitioning. {q} = <b>{v}</b>."
        elif ' - ' in q: e=f"Count back or use a number line. {q} = <b>{v}</b>. Check by adding back."
        else: e=f"Add the hundreds, tens and ones. {q} = <b>{v}</b>."
        eq(q,v,e)
nbook=len(D)
# ---- Unit 1
S(1,1,2,"Number sequences")
for st,d in [(25,25),(100,100),(250,250),(1000,1000),(3,3),(4,4),(6,6),(7,7),(500,-50),(90,-9),(1000,-100),(5000,-1000)]:
    seq=[st+d*i for i in range(4)];tx(f"What comes next? {', '.join(map(str,seq))}, ?",nums(seq[-1]+d),f"The rule is {'add' if d>0 else 'subtract'} {abs(d)}. {seq[-1]} {'+' if d>0 else '-'} {abs(d)} = <b>{seq[-1]+d}</b>.")
for st,d in [(12,6),(45,5),(80,8),(200,25)]:
    seq=[st+d*i for i in range(5)];k=R.choice([1,2,3]);miss=seq[k];seq2=[('?' if i==k else str(x)) for i,x in enumerate(seq)]
    tx(f"Find the missing number: {', '.join(seq2)}",nums(miss),f"The rule is add {d}. The missing number is <b>{miss}</b>.")
S(1,2,2,"Negative numbers")
for t,c in [(-4,6),(-2,5),(-7,3),(-3,8),(-10,4)]: tx(f"The temperature is {t}°C and it rises by {c}°C. What is the new temperature in °C?",negs(t+c),f"Count up {c} from {t} on a number line: <b>{t+c}</b>.")
for t,c in [(3,5),(2,6),(-1,4),(0,7),(5,9)]: tx(f"The temperature is {t}°C and it falls by {c}°C. What is the new temperature in °C?",negs(t-c),f"Count back {c} from {t} on a number line: <b>{t-c}</b>.")
for a,b in [(-3,-7),(-2,1),(-8,-5),(-1,-9)]:
    tx(f"Which is smaller: {a} or {b}?",negs(min(a,b)),f"On a number line, numbers further left are smaller. <b>{min(a,b)}</b> is smaller.")
for a,b in [(-6,-2),(-4,3),(-9,-3)]:
    tx(f"Which is greater: {a} or {b}?",negs(max(a,b)),f"Numbers further right are greater. <b>{max(a,b)}</b> is greater.")
for a,b in [(-5,3),(-8,4),(-2,9),(-6,6)]:
    tx(f"How many steps from {a} up to {b} on a number line?",nums(b-a),f"Count the jumps from {a} to 0 ({abs(a)}), then to {b} ({b}). {abs(a)} + {b} = <b>{b-a}</b>.")
S(1,3,2,"Place value")
for N in pick(1234,9876,8,lambda x:len(set(str(x)))==4 and '0' not in str(x)):
    p=R.randint(0,3);d=int(str(N)[p]);v=d*10**(3-p);pl=["thousands","hundreds","tens","ones"][p]
    tx(f"What is the value of the digit {d} in {N}?",nums(v),f"In {N}, {d} is in the {pl} place. {d} {pl} = <b>{v}</b>.")
for N in pick(2000,9999,6,lambda x:'0' not in str(x)):
    a,b,c,d=map(int,str(N));tx(f"{a} thousands + {b} hundreds + {c} tens + {d} ones = ?",nums(N),f"{a*1000} + {b*100} + {c*10} + {d} = <b>{N}</b>.")
for N in pick(12,999,6,lambda x:x%10!=0):
    for k in (10,100): 
        if R.random()<.5: eq(f"{N} x {k}",N*k,f"Each digit moves {1 if k==10 else 2} place{'s' if k==100 else ''} to the left. {N} x {k} = <b>{N*k}</b>.")
for N in pick(1,99,5):
    tx(f"{N*1000} ÷ 10 = ?",nums(N*100),f"Each digit moves 1 place to the right. <b>{N*100}</b>.")
for N in pick(1000,9999,4,lambda x:x%100):
    tx(f"Write {N} in words.",[W(N)],f"Say the thousands, hundreds, then the rest: <b>{W(N)}</b>.")
# ---- Unit 2
S(2,1,2,"12-hour and 24-hour time")
for h,m in [(15,30),(18,45),(20,10),(13,5),(22,15),(9,20),(12,40),(23,55)]:
    hh=h%12 or 12;ap='pm' if h>=12 else 'am';s=f"{hh}:{m:02d}"
    tx(f"Write {h:02d}:{m:02d} as a 12-hour time with am or pm (like 3:30 pm).",[f"{s} {ap}",f"{s}{ap}",f"{s} {ap[0]}.m.",f"{s} {ap[0]}.m"],f"{'After 12 noon, subtract 12 from the hours.' if h>12 else 'Morning hours stay the same.'} {h:02d}:{m:02d} is <b>{s} {ap}</b>.")
for h,m,ap in [(4,15,'pm'),(7,30,'pm'),(10,5,'pm'),(6,45,'am'),(11,20,'pm'),(2,50,'pm')]:
    H=h+12 if ap=='pm' else h;tx(f"Write {h}:{m:02d} {ap} in 24-hour time (like 15:30).",[f"{H:02d}:{m:02d}",f"{H}:{m:02d}"],f"{'Add 12 to the hours for pm.' if ap=='pm' else 'Morning times stay the same.'} <b>{H:02d}:{m:02d}</b>.")
for q,a,e in [("How many seconds are in 1 minute?",nums(60),"60 seconds."),("How many minutes are in 2 hours?",nums(120),"2 x 60 = 120."),("How many minutes are in 3 hours?",nums(180),"3 x 60 = 180."),("How many hours are in 2 days?",nums(48),"2 x 24 = 48."),("How many days are in 4 weeks?",nums(28),"4 x 7 = 28."),("How many months are in 3 years?",nums(36),"3 x 12 = 36."),("How many minutes are in 90 seconds? (use 'and a half' or decimals)",["1.5","1 and a half","1 1/2","one and a half"],"60 seconds = 1 minute, 30 seconds = half a minute. So 1.5 minutes.")]: tx(q,a,e)
S(2,2,2,"Time intervals")
for h1,m1,h2,m2 in [(8,45,11,20),(9,15,12,0),(13,10,15,40),(7,30,10,5),(14,20,16,55),(10,50,13,15),(6,40,9,10),(15,5,18,35)]:
    d=(h2*60+m2)-(h1*60+m1);H,M=divmod(d,60)
    tx(f"A journey starts at {h1:02d}:{m1:02d} and ends at {h2:02d}:{m2:02d}. How long is the journey? (hours and minutes)",[f"{H} hours {M} minutes",f"{H} hours {M} mins",f"{H} h {M} min",f"{H}h {M}min",f"{d} minutes",f"{H} hour {M} minutes",f"{H} hours {M} minute"] if M else [f"{H} hours",f"{H} hour",f"{H} h"],f"Count on to the next hour, then add the rest. From {h1:02d}:{m1:02d} to {h2:02d}:{m2:02d} is <b>{H} hours {M} minutes</b> ({d} minutes).")
for h,m,d in [(9,15,50),(13,40,35),(7,25,45),(16,10,80)]:
    t=h*60+m+d
    tx(f"A film starts at {h:02d}:{m:02d} and lasts {d} minutes. What time does it end? (24-hour, like 15:30)",[f"{t//60:02d}:{t%60:02d}",f"{t//60}:{t%60:02d}"],f"{h:02d}:{m:02d} + {d} minutes = <b>{t//60:02d}:{t%60:02d}</b>.")
# ---- Unit 3
S(3,1,2,"Missing numbers")
for _ in range(6):
    a=R.randint(15,70);b=R.randint(12,60);tx(f"? + {a} = {a+b}",nums(b),f"Use the inverse: {a+b} - {a} = <b>{b}</b>.")
for _ in range(5):
    a=R.randint(60,99);b=R.randint(12,50);tx(f"{a} - ? = {a-b}",nums(b),f"{a} - {a-b} = <b>{b}</b>.")
for _ in range(5):
    a=R.randint(3,9);b=R.randint(3,12);tx(f"? x {a} = {a*b}",nums(b),f"{a*b} ÷ {a} = <b>{b}</b>.")
for _ in range(4):
    a=R.randint(3,9);b=R.randint(3,12);tx(f"{a*b} ÷ ? = {b}",nums(a),f"{a*b} ÷ {b} = <b>{a}</b>.")
S(3,1,3,"Missing operations")
WD={'+':["add","plus","addition"],'-':["subtract","minus","subtraction","take away"],'x':["multiply","times","multiplication","x"],'÷':["divide","division","divided by"]}
for a,b,c,o in [(7,8,56,'x'),(9,6,54,'x'),(40,15,25,'-'),(23,19,42,'+'),(72,8,9,'÷'),(100,35,65,'-'),(36,4,9,'÷'),(14,6,84,'x')]:
    tx(f"Which operation goes in the box? {a} [ ] {b} = {c}  (write add, subtract, multiply or divide)",WD[o],f"Try each operation. {a} {o} {b} = {c}, so the operation is <b>{WD[o][0]}</b>.")
S(3,2,2,"Add and subtract whole numbers")
for _ in range(8):
    a,b=R.randint(120,780),R.randint(110,590);eq(f"{a} + {b}",a+b,f"Add hundreds, tens and ones. {a} + {b} = <b>{a+b}</b>.")
for _ in range(8):
    a=R.randint(450,990);b=R.randint(120,a-100);eq(f"{a} - {b}",a-b,f"Subtract in parts. {a} - {b} = <b>{a-b}</b>. Check: {a-b} + {b} = {a} ✔")
for _ in range(4):
    a,b=R.randint(1200,5600),R.randint(1100,3900);eq(f"{a} + {b}",a+b,f"Add thousands, hundreds, tens and ones. <b>{a+b}</b>.")
S(3,3,2,"Odd and even rules")
for q,a,e in [("Is the sum of two even numbers odd or even?",["even"],"Example: 4 + 6 = 10. Even + even = <b>even</b>."),("Is the sum of two odd numbers odd or even?",["even"],"Example: 3 + 5 = 8. Odd + odd = <b>even</b>."),("Is the sum of an odd and an even number odd or even?",["odd"],"Example: 3 + 4 = 7. Odd + even = <b>odd</b>."),("Is an even number multiplied by an odd number odd or even?",["even"],"Example: 4 x 3 = 12. Even x odd = <b>even</b>."),("Is an odd number multiplied by an odd number odd or even?",["odd"],"Example: 3 x 5 = 15. Odd x odd = <b>odd</b>.")]: tx(q,a,e)
for a,b in [(23,45),(18,36),(27,14),(51,49),(66,35),(12,38)]:
    tx(f"Is {a} + {b} odd or even? (Do not add. Use the rules.)",["even" if (a+b)%2==0 else "odd"],f"{a} is {'even' if a%2==0 else 'odd'} and {b} is {'even' if b%2==0 else 'odd'}. The sum is <b>{'even' if (a+b)%2==0 else 'odd'}</b>. Check: {a} + {b} = {a+b}.")
# ---- Unit 4
S(4,1,2,"Likelihood words")
for q,a in [("The sun will set tonight.","certain"),("You will roll a 7 on a normal dice.","impossible"),("It will rain at some point next month in a rainy country.","likely"),("You will win a lottery tomorrow.","unlikely"),("A fair coin lands on tails.","equal chance"),("A newborn baby will be older than 100 days tomorrow.","impossible"),("You will roll a number less than 7 on a normal dice.","certain"),("You will pick a red sweet from a bag with 9 red and 1 blue sweets.","likely"),("You will pick a blue sweet from a bag with 9 red and 1 blue sweets.","unlikely")]:
    tx(f"Is this certain, likely, equal chance, unlikely or impossible? \"{q}\"",[a] if a!="equal chance" else ["equal chance","even chance","equally likely","even"],f"Think about how many ways it can happen. This is <b>{a}</b>.")
S(4,1,3,"Counting chances")
for r,b in [(3,1),(2,5),(4,4),(1,6),(5,2)]:
    ans="red" if r>b else "blue" if b>r else "equal"
    tx(f"A bag holds {r} red and {b} blue counters. Which colour are you more likely to pick? (red, blue or equal)",[ans] if ans!="equal" else ["equal","equally likely","same"],f"Compare the numbers: {r} red and {b} blue. The answer is <b>{ans}</b>.")
for n in (6,8,10,4): tx(f"A spinner has {n} equal sections and 1 is blue. What fraction of the spinner is blue? (like 1/4)",[f"1/{n}"],f"1 out of {n} equal sections is <b>1/{n}</b>.")
# ---- Unit 5
S(5,1,2,"Tables up to 12 x 12")
for _ in range(14):
    a,b=R.randint(2,12),R.randint(3,12);eq(f"{a} x {b}",a*b,f"{a} groups of {b}. {a} x {b} = <b>{a*b}</b>.")
for _ in range(8):
    a,b=R.randint(2,12),R.randint(3,12);eq(f"{a*b} ÷ {a}",b,f"Think: {a} x ? = {a*b}. {a} x {b} = {a*b}, so <b>{b}</b>.")
S(5,1,3,"Multiples")
for n,k in [(4,6),(6,5),(7,4),(8,3),(9,5),(5,8)]: tx(f"What is the {k}th multiple of {n}?",nums(n*k),f"Count in {n}s {k} times, or {n} x {k} = <b>{n*k}</b>.")
for n,m in [(24,8),(35,6),(42,7),(54,9),(30,4),(72,8),(45,5),(50,8)]: tx(f"Is {n} a multiple of {m}? (yes or no)",YN(n%m==0),f"{n} ÷ {m} {'= '+str(n//m)+' exactly' if n%m==0 else 'does not divide exactly'}. The answer is <b>{'yes' if n%m==0 else 'no'}</b>.")
S(5,1,4,"Factors")
for n in (12,18,20,24,30,36): 
    fs=[i for i in range(1,n+1) if n%i==0];tx(f"How many factors does {n} have?",nums(len(fs)),f"Factors of {n}: {', '.join(map(str,fs))}. That is <b>{len(fs)}</b> factors.")
for n,f in [(21,3),(28,5),(36,9),(40,6),(45,9),(32,8),(27,4),(48,12)]: tx(f"Is {f} a factor of {n}? (yes or no)",YN(n%f==0),f"{n} ÷ {f} {'= '+str(n//f) if n%f==0 else 'has a remainder'}. The answer is <b>{'yes' if n%f==0 else 'no'}</b>.")
S(5,2,2,"Multiplication methods")
for _ in range(8):
    a,b=R.randint(12,49),R.randint(2,9);eq(f"{a} x {b}",a*b,f"Partition: {a//10*10} x {b} = {a//10*10*b} and {a%10} x {b} = {a%10*b}. {a//10*10*b} + {a%10*b} = <b>{a*b}</b>.")
for a,b,c in [(2,5,7),(4,5,3),(2,5,9),(5,4,6),(3,2,10)]: eq(f"{a} x {b} x {c}",a*b*c,f"Multiply in a helpful order. {a} x {b} = {a*b}, then x {c} = <b>{a*b*c}</b>.")
# ---- Unit 6
S(6,1,2,"Polygons")
for n,nm in [(3,"triangle"),(4,"quadrilateral"),(5,"pentagon"),(6,"hexagon"),(7,"heptagon"),(8,"octagon"),(9,"nonagon"),(10,"decagon")]:
    tx(f"How many sides does a {nm} have?",nums(n),f"A {nm} has <b>{n}</b> sides."); 
for n,nm in [(5,"pentagon"),(6,"hexagon"),(8,"octagon"),(7,"heptagon"),(10,"decagon")]: tx(f"What is the name of a 2D shape with {n} straight sides?",[nm,"a "+nm],f"{n} sides is a <b>{nm}</b>.")
tx("What is a regular polygon? Which shape is regular: a square or a rectangle that is not a square?",["square","a square"],"A regular polygon has all sides equal and all angles equal. A <b>square</b> is regular.")
S(6,1,3,"Tessellation")
for q,a,e in [("Does a square tessellate? (yes or no)",["yes"],"Squares fit together with no gaps or overlaps."),("Does an equilateral triangle tessellate? (yes or no)",["yes"],"Equilateral triangles fit together with no gaps."),("Does a regular hexagon tessellate? (yes or no)",["yes"],"Hexagons fit together like a honeycomb."),("Does a circle tessellate? (yes or no)",["no"],"Circles leave gaps between them."),("Does a regular pentagon tessellate? (yes or no)",["no"],"Regular pentagons leave gaps."),("What do we call a pattern of shapes that fit together with no gaps or overlaps?",["tessellation","a tessellation"],"This is a tessellation.")]: tx(q,a,e)
S(6,2,2,"Lines of symmetry")
for s,n in [("square",4),("rectangle (not a square)",2),("equilateral triangle",3),("regular pentagon",5),("regular hexagon",6),("regular octagon",8),("isosceles triangle",1),("kite",1),("scalene triangle",0),("letter H",2),("letter M",1),("letter F",0)]:
    tx(f"How many lines of symmetry does a {s} have?",nums(n),f"A line of symmetry splits the shape into 2 matching halves. The answer is <b>{n}</b>.")
# ---- Unit 7
S(7,1,2,"Parts of fractions")
for n,d in [(3,8),(5,6),(2,9),(7,10),(4,5),(1,12)]:
    tx(f"In the fraction {n}/{d}, what is the numerator?",nums(n),f"The numerator is the top number: <b>{n}</b>.")
    tx(f"In the fraction {n}/{d}, what is the denominator?",nums(d),f"The denominator is the bottom number: <b>{d}</b>. It tells how many equal parts the whole is split into.")
S(7,1,3,"Mixed numbers")
for n,d in [(7,4),(5,2),(9,4),(11,3),(8,3),(13,5),(10,3),(7,2)]:
    w,r=divmod(n,d);tx(f"Write {n}/{d} as a mixed number (like 1 1/2).",[f"{w} {r}/{d}"],f"{n} ÷ {d} = {w} remainder {r}. So {n}/{d} = <b>{w} {r}/{d}</b>.")
for w,r,d in [(2,1,4),(1,3,5),(3,1,2),(2,2,3)]: tx(f"How many {'quarters' if d==4 else 'fifths' if d==5 else 'halves' if d==2 else 'thirds'} are in {w} {r}/{d}?",nums(w*d+r),f"{w} wholes = {w*d} parts, plus {r} more = <b>{w*d+r}</b>.")
S(7,2,2,"Fraction of an amount")
for n,d,N in [(1,3,24),(1,5,30),(1,6,36),(1,8,40),(3,4,20),(2,5,30),(3,10,50),(2,3,18),(3,8,24),(4,5,25),(5,6,30),(7,10,40)]:
    q=N//d;r=q*n;tx(f"What is {n}/{d} of {N}?",nums(r),f"{N} ÷ {d} = {q}."+(f" Then {q} x {n} = <b>{r}</b>." if n>1 else f" So <b>{r}</b>."))
# ---- Unit 8
S(8,1,2,"Comparing angles")
for q,a,e in [("How many degrees are in a right angle?",nums(90),"A right angle is 90°."),("How many degrees are in a straight line?",nums(180),"A straight angle is 180°."),("How many degrees are in a full turn?",nums(360),"A full turn is 360°."),("How many right angles make a straight line?",nums(2),"2 x 90° = 180°."),("How many right angles make a full turn?",nums(4),"4 x 90° = 360°."),("How many degrees are in a half turn?",nums(180),"A half turn is 180°."),("How many degrees are in a quarter turn?",nums(90),"A quarter turn is 90°."),("What do we use to measure angles?",["protractor","a protractor"],"A protractor measures angles in degrees.")]: tx(q,a,e)
S(8,2,2,"Acute, right, obtuse")
for d in (30,45,60,80,89,90,100,120,135,150,175):
    c="acute" if d<90 else "right" if d==90 else "obtuse"
    tx(f"Is an angle of {d}° acute, right or obtuse?",[c,c+" angle"],f"Acute is less than 90°, right is exactly 90°, obtuse is between 90° and 180°. {d}° is <b>{c}</b>.")
for a in (30,50,70,110): tx(f"Two angles make a straight line. One is {a}°. What is the other angle in degrees?",nums(180-a),f"A straight line is 180°. 180 - {a} = <b>{180-a}</b>.")
S(8,3,2,"Estimating angles")
for q,o,a in [("a little more than a right angle",(20,100,200),100),("half of a right angle",(45,90,180),45),("a half turn",(90,180,360),180),("about a quarter of a right angle",(20,60,120),20),("nearly a full turn",(90,180,350),350)]:
    tx(f"Which is the best estimate for {q}: {o[0]}°, {o[1]}° or {o[2]}°?",nums(a),f"Compare with 90° (right angle), 180° (half turn) and 360° (full turn). The best estimate is <b>{a}°</b>.")
# ---- Unit 9
S(9,1,2,"Rounding")
for N in pick(1011,9989,6,lambda x:x%10!=0):
    r=(N//10+(1 if N%10>=5 else 0))*10;tx(f"Round {N} to the nearest 10.",nums(r),f"Look at the ones digit {N%10}: {'5 or more, round up' if N%10>=5 else 'less than 5, round down'}. <b>{r}</b>.")
for N in pick(1110,9890,6,lambda x:x%100!=0):
    r=(N//100+(1 if N%100>=50 else 0))*100;tx(f"Round {N} to the nearest 100.",nums(r),f"Look at the tens digit {N//10%10}: {'5 or more, round up' if N%100>=50 else 'less than 5, round down'}. <b>{r}</b>.")
for N in pick(1100,9900,6,lambda x:x%1000!=0 and x%1000!=500):
    r=(N//1000+(1 if N%1000>=500 else 0))*1000;tx(f"Round {N} to the nearest 1000.",nums(r),f"Look at the hundreds digit {N//100%10}: {'5 or more, round up' if N%1000>=500 else 'less than 5, round down'}. <b>{r}</b>.")
S(9,1,3,"Comparing and ordering")
for _ in range(6):
    L=pick(1000,9999,3);big=R.random()<.5;tx(f"Which is the {'greatest' if big else 'smallest'}: {L[0]}, {L[1]} or {L[2]}?",[str(max(L) if big else min(L))],f"Compare thousands first, then hundreds, tens, ones. In order: {', '.join(map(str,sorted(L)))}. <b>{max(L) if big else min(L)}</b>.")
S(9,2,2,"Divide 2-digit numbers")
for _ in range(8):
    b=R.randint(2,9);q=R.randint(11,30);eq(f"{b*q} ÷ {b}",q,f"Partition: split {b*q} into tens and ones that divide by {b}. Check: {q} x {b} = {b*q} ✔. Answer <b>{q}</b>.")
for _ in range(8):
    b=R.randint(3,9);n=R.randint(30,99)
    if n%b==0: continue
    q,r=divmod(n,b);tx(f"{n} ÷ {b} = ? (write like 12 r 3)",[f"{q} r {r}",f"{q} remainder {r}",f"{q} r{r}"],f"{b} x {q} = {b*q}. {n} - {b*q} = {r} left over. Answer <b>{q} remainder {r}</b>.")
# ---- Unit 10
S(10,1,2,"Frequency tables")
for items in [("walk","bus","car"),("pizza","pasta","salad"),("football","chess","art"),("spring","summer","autumn")]:
    v=pick(5,40,3);d=dict(zip(items,v));s=", ".join(f"{k} {x}" for k,x in d.items());top=max(d,key=d.get);low=min(d,key=d.get)
    tx(f"A survey shows: {s}. Which is the most popular?",[top],f"The biggest number is {d[top]}: <b>{top}</b>.")
    tx(f"A survey shows: {s}. How many people answered in total?",nums(sum(v)),f"{' + '.join(map(str,v))} = <b>{sum(v)}</b>.")
    tx(f"A survey shows: {s}. How many more chose {top} than {low}?",nums(d[top]-d[low]),f"{d[top]} - {d[low]} = <b>{d[top]-d[low]}</b>.")
S(10,1,3,"Types of data")
for q,a,e in [("Is 'favourite colour' data categorical or numerical?",["categorical"],"Colours are names, so they are categorical."),("Is 'number of pets' data categorical or numerical?",["numerical"],"A number of pets is a count, so it is numerical."),("Is 'height of children in cm' data categorical or numerical?",["numerical"],"Heights are measured numbers."),("Is 'type of fruit' data categorical or numerical?",["categorical"],"Types are names.")]: tx(q,a,e)
tx("A tally chart has 3 groups of five and 4 single marks. What number is shown?",nums(19),"3 x 5 = 15, then 15 + 4 = <b>19</b>.")
# ---- Unit 11
S(11,1,2,"Equivalent fractions")
for n,d,k in [(1,2,5),(1,2,4),(2,3,2),(3,4,2),(1,3,3),(2,5,3),(1,4,3),(3,5,2)]:
    tx(f"{n}/{d} = ?/{d*k}",nums(n*k),f"Multiply top and bottom by {k}: {n} x {k} = <b>{n*k}</b>, {d} x {k} = {d*k}.")
for n,d in [(4,8),(6,9),(10,15),(6,8),(5,10),(12,16),(8,12)]:
    g=gcd(n,d);tx(f"Write {n}/{d} in its simplest form (like 1/2).",[f"{n//g}/{d//g}"],f"Divide top and bottom by {g}: <b>{n//g}/{d//g}</b>.")
S(11,1,3,"Comparing fractions")
for a,b in [((3,4),(2,3)),((1,2),(3,5)),((2,5),(3,10)),((5,6),(3,4)),((1,3),(2,5)),((7,10),(3,4))]:
    va,vb=a[0]/a[1],b[0]/b[1];big=a if va>vb else b
    tx(f"Which is bigger: {a[0]}/{a[1]} or {b[0]}/{b[1]}?",[f"{big[0]}/{big[1]}"],f"Change to the same denominator, or compare as decimals: {a[0]}/{a[1]} = {va:.2f} and {b[0]}/{b[1]} = {vb:.2f}. <b>{big[0]}/{big[1]}</b> is bigger.")
S(11,2,2,"Percentages")
for p,fr_ in [(50,"1/2"),(25,"1/4"),(75,"3/4"),(10,"1/10"),(20,"1/5"),(100,"1")]:
    tx(f"What is {p}% as a fraction in its simplest form?",[fr_] if p!=50 else [fr_,"half","one half"],f"{p}% means {p} out of 100. Simplify {p}/100 = <b>{fr_}</b>.")
for p,N in [(50,60),(25,80),(10,70),(10,250),(50,90),(25,48),(75,40),(20,50),(100,35),(1,200)]:
    r=N*p//100;tx(f"What is {p}% of {N}?",nums(r),f"{p}% of {N}: {N} x {p} ÷ 100 = <b>{r}</b>.")
for fr_,p in [("1/2",50),("1/4",25),("3/4",75),("1/10",10),("1/5",20)]: tx(f"Write {fr_} as a percentage.",[str(p),f"{p}%"],f"{fr_} = {p} out of 100 = <b>{p}%</b>.")
# ---- Unit 12
S(12,1,2,"Faces, edges, vertices")
PR={"triangular prism":3,"rectangular prism":4,"pentagonal prism":5,"hexagonal prism":6}
for nm,n in PR.items():
    for w,v in (("faces",n+2),("edges",3*n),("vertices",2*n)): tx(f"How many {w} does a {nm} have?",nums(v),f"A prism with a {n}-sided base has {n+2} faces, {3*n} edges and {2*n} vertices. Answer <b>{v}</b>.")
PY={"triangle-based pyramid":3,"square-based pyramid":4,"pentagon-based pyramid":5,"hexagon-based pyramid":6}
for nm,n in PY.items():
    for w,v in (("faces",n+1),("edges",2*n),("vertices",n+1)): tx(f"How many {w} does a {nm} have?",nums(v),f"A pyramid with a {n}-sided base has {n+1} faces, {2*n} edges and {n+1} vertices. Answer <b>{v}</b>.")
S(12,2,2,"Nets")
for q,a,e in [("How many squares are in the net of a cube?",nums(6),"A cube has 6 square faces."),("A net of a triangular prism has 2 triangles and how many rectangles?",nums(3),"A triangular prism has 3 rectangle faces."),("A net of a square-based pyramid has 1 square and how many triangles?",nums(4),"4 triangle sides meet at the top."),("How many faces are in the net of a cuboid?",nums(6),"A cuboid has 6 faces."),("How many faces are in the net of a pentagonal prism?",nums(7),"2 pentagons + 5 rectangles = 7."),("Which 3D shape has a net of 4 triangles?",["triangle-based pyramid","tetrahedron","triangular pyramid"],"A triangle-based pyramid has 4 triangle faces.")]: tx(q,a,e)
# ---- Unit 13
S(13,1,2,"Efficient addition")
for a,b in [(99,47),(198,35),(49,76),(299,58),(398,125),(197,246),(59,83),(999,44)]:
    t=round(a/10+.001)*10 if a%100!=99 and a%100!=98 and a%100!=97 else (a//100+1)*100
    t=(a+ (100-a%100)) if a%100>=90 else a+(10-a%10)
    d=t-a;eq(f"{a} + {b}",a+b,f"Round {a} up to {t} (add {d}). {t} + {b} = {t+b}. Then subtract {d}: {t+b} - {d} = <b>{a+b}</b>.")
for a,b in [(120,59),(230,98),(345,199),(502,297),(610,399),(784,298)]:
    t=b+(100-b%100) if b%100 else b;d=t-b;eq(f"{a} - {b}",a-b,f"Round {b} up to {t}. {a} - {t} = {a-t}. Then add back {d}: {a-t} + {d} = <b>{a-b}</b>.")
S(13,2,2,"Fractions with the same denominator")
for a,b,d in [(1,2,5),(2,3,7),(3,2,8),(4,3,9),(1,1,6),(3,4,10),(2,2,9),(5,3,12)]: tx(f"{a}/{d} + {b}/{d} = ? (write like 3/5)",fr(a+b,d),f"Same denominator: add the tops. {a} + {b} = {a+b}. Answer <b>{a+b}/{d}</b>.")
for a,b,d in [(5,2,7),(7,3,8),(6,1,9),(9,4,10),(8,5,12),(4,3,5)]: tx(f"{a}/{d} - {b}/{d} = ? (write like 2/5)",fr(a-b,d),f"Same denominator: subtract the tops. {a} - {b} = {a-b}. Answer <b>{a-b}/{d}</b>.")
for a,b,d in [(3,4,5),(4,5,6),(5,6,8)]:
    s=a+b;w,r=divmod(s,d);tx(f"{a}/{d} + {b}/{d} = ? (write as a mixed number like 1 2/5)",[f"{w} {r}/{d}"],f"{a} + {b} = {s}, so {s}/{d} = <b>{w} {r}/{d}</b>.")
# ---- Unit 14
S(14,1,2,"Area by counting squares")
for l,w in [(4,3),(6,2),(5,5),(7,3),(8,4),(9,2)]: tx(f"A rectangle covers {l} squares across and {w} squares down. What is its area in squares?",nums(l*w),f"{l} x {w} = <b>{l*w}</b> squares.")
S(14,1,3,"Perimeter")
for l,w in [(5,3),(8,2),(10,4),(6,6),(9,5),(12,7)]: tx(f"A rectangle is {l} cm long and {w} cm wide. What is its perimeter in cm?",nums(2*(l+w)),f"2 x ({l} + {w}) = 2 x {l+w} = <b>{2*(l+w)}</b> cm.")
S(14,2,2,"Area and perimeter of rectangles")
for l,w in [(6,4),(9,3),(12,5),(8,8),(15,4),(11,6)]: tx(f"A rectangle is {l} cm long and {w} cm wide. What is its area in cm²? (just the number)",nums(l*w),f"Area = length x width = {l} x {w} = <b>{l*w}</b> cm².")
for l,w in [(6,4),(9,3),(12,5),(8,7)]: tx(f"A rectangle has an area of {l*w} cm² and a length of {l} cm. What is its width in cm?",nums(w),f"Width = area ÷ length = {l*w} ÷ {l} = <b>{w}</b> cm.")
for l,w in [(10,3),(12,4),(9,6)]: tx(f"A rectangle has a perimeter of {2*(l+w)} cm and a length of {l} cm. What is its width in cm?",nums(w),f"Half the perimeter is {l+w}. Width = {l+w} - {l} = <b>{w}</b> cm.")
# ---- Unit 15
S(15,1,2,"Ordering bigger numbers")
for _ in range(6):
    L=pick(10000,99999,3);big=R.random()<.5;tx(f"Which is the {'greatest' if big else 'smallest'}: {L[0]}, {L[1]} or {L[2]}?",[str(max(L) if big else min(L))],f"Compare the digits from the left. In order: {', '.join(map(str,sorted(L)))}. <b>{max(L) if big else min(L)}</b>.")
for N in pick(1000,9999,4,lambda x:x%10):
    tx(f"Put in order, smallest first: {N}, {N+100}, {N-100}. Which number is in the middle?",nums(N),f"Order: {N-100}, {N}, {N+100}. The middle number is <b>{N}</b>.")
S(15,2,2,"Square, prime and triangular numbers")
for n in (3,4,5,6,7,8,9,10,11,12): eq(f"{n} x {n}",n*n,f"{n} squared means {n} x {n} = <b>{n*n}</b>.")
for n in (25,49,64,81,100,121): tx(f"Which number multiplied by itself gives {n}?",nums(int(n**.5)),f"{int(n**.5)} x {int(n**.5)} = {n}, so the answer is <b>{int(n**.5)}</b>.")
PRM=[2,3,5,7,11,13,17,19,23,29,31]
for n in (7,9,13,15,17,21,23,27,29,33): tx(f"Is {n} a prime number? (yes or no)",YN(n in PRM),f"A prime number has exactly 2 factors: 1 and itself. {n} {'has only 1 and '+str(n) if n in PRM else 'also divides by '+str(next(i for i in range(2,n) if n%i==0))}. Answer <b>{'yes' if n in PRM else 'no'}</b>.")
for seq in ([1,3,6,10,15],[3,6,10,15,21],[6,10,15,21,28]): tx(f"These are triangular numbers: {', '.join(map(str,seq))}, ?  What comes next?",nums(seq[-1]+len(seq)+1),f"The gaps grow by 1 each time: +{len(seq)+1}. {seq[-1]} + {len(seq)+1} = <b>{seq[-1]+len(seq)+1}</b>.")
S(15,3,2,"Divisibility tests")
for n,d in [(135,5),(240,10),(138,2),(147,3),(123,3),(256,3),(729,9),(504,9),(318,6),(1000,4),(365,5),(472,2)]:
    ok=n%d==0;tx(f"Is {n} divisible by {d}? (yes or no)",YN(ok),f"{ {2:'Even numbers end in 0, 2, 4, 6 or 8.',3:'Add the digits. If the total is in the 3 times table, it divides by 3.',5:'Numbers ending in 0 or 5 divide by 5.',9:'Add the digits. If the total is in the 9 times table, it divides by 9.',10:'Numbers ending in 0 divide by 10.',6:'It must divide by 2 and by 3.',4:'Check if the last two digits divide by 4.'}[d]} {n} ÷ {d} {'= '+str(n//d) if ok else 'has a remainder'}. Answer <b>{'yes' if ok else 'no'}</b>.")
# ---- Unit 16
S(16,1,2,"Pictograms and bar charts")
for k,n in [(5,7),(10,4),(2,9),(20,3),(4,6)]: tx(f"In a pictogram, each symbol stands for {k} people. There are {n} symbols. How many people is that?",nums(k*n),f"{n} x {k} = <b>{k*n}</b>.")
for k,n in [(5,35),(10,60),(4,28)]: tx(f"In a pictogram, each symbol stands for {k} people. How many symbols show {n} people?",nums(n//k),f"{n} ÷ {k} = <b>{n//k}</b>.")
for s,n in [(5,8),(10,6),(2,13),(20,3)]: tx(f"On a bar chart, each square of the scale is {s}. A bar is {n} squares high. What value does it show?",nums(s*n),f"{n} x {s} = <b>{s*n}</b>.")
S(16,1,3,"Line graphs and tables")
for (t1,v1),(t2,v2) in [(("9 am",12),("12 noon",18)),(("8 am",5),("11 am",14)),(("1 pm",20),("4 pm",11))]:
    d=abs(v2-v1);tx(f"A line graph shows the temperature was {v1}°C at {t1} and {v2}°C at {t2}. How many degrees {'warmer' if v2>v1 else 'cooler'} is it at {t2}?",nums(d),f"{max(v1,v2)} - {min(v1,v2)} = <b>{d}</b>.")
for a,b,c in [(12,18,9),(25,30,14),(7,15,22)]: tx(f"A table shows 3 days of sales: {a}, {b} and {c}. What is the total?",nums(a+b+c),f"{a} + {b} + {c} = <b>{a+b+c}</b>.")
# ---- Unit 17
S(17,1,2,"Written multiplication")
for _ in range(8):
    a,b=R.randint(112,498),R.randint(2,9);eq(f"{a} x {b}",a*b,f"Partition {a} = {a//100*100} + {a//10%10*10} + {a%10}. {a//100*100*b} + {a//10%10*10*b} + {a%10*b} = <b>{a*b}</b>.")
for _ in range(6):
    a,b=R.randint(13,48),R.choice([10,20,30,40]);eq(f"{a} x {b}",a*b,f"Do {a} x {b//10} = {a*(b//10)}, then x 10 = <b>{a*b}</b>.")
for _ in range(5):
    a,b=R.randint(12,35),R.randint(11,25);eq(f"{a} x {b}",a*b,f"{a} x {b//10*10} = {a*(b//10*10)} and {a} x {b%10} = {a*(b%10)}. Add: <b>{a*b}</b>.")
S(17,2,2,"Written division")
for _ in range(8):
    b=R.randint(3,9);q=R.randint(105,199);eq(f"{b*q} ÷ {b}",q,f"Divide hundreds, tens and ones in turn. Check: {q} x {b} = {b*q} ✔. Answer <b>{q}</b>.")
for _ in range(6):
    b=R.randint(3,9);n=R.randint(110,500)
    if n%b==0: continue
    q,r=divmod(n,b);tx(f"{n} ÷ {b} = ? (write like 45 r 2)",[f"{q} r {r}",f"{q} remainder {r}",f"{q} r{r}"],f"{b} x {q} = {b*q}. {n} - {b*q} = {r}. Answer <b>{q} remainder {r}</b>.")
for n,g in [(75,4),(100,8),(50,6),(90,7)]: tx(f"{n} sweets are shared equally between {g} children. How many sweets are left over?",nums(n%g),f"{n} ÷ {g} = {n//g} remainder <b>{n%g}</b>.")
# ---- Unit 18
S(18,1,2,"Coordinates")
for x,y in [(3,5),(6,2),(4,7),(1,8),(7,4)]:
    tx(f"In the point ({x}, {y}), which number is the x-coordinate (across)?",nums(x),f"The first number is across: <b>{x}</b>.")
    tx(f"In the point ({x}, {y}), which number is the y-coordinate (up)?",nums(y),f"The second number is up: <b>{y}</b>.")
for x,y,dx,dy,dn,dd in [(2,3,4,1,"right","up"),(5,2,2,3,"right","up"),(6,6,3,2,"left","down"),(4,1,1,5,"left","up"),(1,7,5,4,"right","down")]:
    nx=x+dx if dn=="right" else x-dx;ny=y+dy if dd=="up" else y-dy
    tx(f"Move the point ({x}, {y}) {dx} {dn} and {dy} {dd}. What is the new point? (write like 3, 4)",[f"{nx}, {ny}",f"({nx}, {ny})",f"{nx},{ny}"],f"Across: {x} {'+' if dn=='right' else '-'} {dx} = {nx}. Up/down: {y} {'+' if dd=='up' else '-'} {dy} = {ny}. New point <b>({nx}, {ny})</b>.")
S(18,2,2,"Reflection")
for x,y,m in [(2,3,5),(1,4,4),(3,6,6),(4,2,7),(2,5,3),(1,1,3)]:
    nx=2*m-x;tx(f"Reflect the point ({x}, {y}) in the vertical mirror line x = {m}. What is the new point? (write like 3, 4)",[f"{nx}, {y}",f"({nx}, {y})",f"{nx},{y}"],f"The point is {abs(m-x)} from the mirror, so the image is {abs(m-x)} on the other side: x = {m} + {m-x} = {nx}. The y-coordinate stays {y}. Answer <b>({nx}, {y})</b>.")
for x,y,m in [(3,2,5),(4,1,3),(2,6,8),(5,3,4)]:
    ny=2*m-y;tx(f"Reflect the point ({x}, {y}) in the horizontal mirror line y = {m}. What is the new point? (write like 3, 4)",[f"{x}, {ny}",f"({x}, {ny})",f"{x},{ny}"],f"The point is {abs(m-y)} from the mirror, so the image is {abs(m-y)} on the other side: y = {m} + {m-y} = {ny}. The x-coordinate stays {x}. Answer <b>({x}, {ny})</b>.")
open('grade4.js','w').write('const QUESTIONS4='+json.dumps(D,separators=(',',':'),ensure_ascii=False)+';\n')
import collections
print('total',len(D),'from book',nbook);print(sorted(collections.Counter(d['t'] for d in D).items()))
