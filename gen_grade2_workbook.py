import re, json, sys
hdr=open('/home/claude/g3/gen3.py').read().split('# ---------- Unit 1')[0]
exec(hdr)
UN={1:"Numbers to 100",2:"Geometry",3:"Measures",4:"Statistics",5:"Working with numbers to 100",6:"Money",7:"Time",8:"Numbers to 100 (2)",9:"Statistics (2)",10:"Calculating",11:"Geometry (2)",12:"Telling the time",13:"Measures (2)",14:"Pattern and probability",15:"Symmetry, position and movement"}
SN={(1,1):"1.1 Numbers to 100",(1,2):"1.2 Counting up to 100 objects",(1,3):"1.3 Comparing and ordering numbers",(2,1):"2.1 3D shapes",(2,2):"2.2 2D shapes and symmetry",(2,3):"2.3 Fractions of shapes",(3,1):"3.1 Length",(3,2):"3.2 Drawing and measuring lines",(4,1):"4.1 Carroll diagrams and tally charts",(5,1):"5.1 Addition",(5,2):"5.2 Subtraction",(5,3):"5.3 Multiplication",(5,4):"5.4 Division",(6,1):"6.1 Money",(7,1):"7.1 Units of time and the calendar",(8,1):"8.1 Numbers in words, rounding and regrouping",(8,2):"8.2 Fractions of numbers",(9,1):"9.1 Venn diagrams, lists and tables",(9,2):"9.2 Statistics",(10,1):"10.1 Adding and subtracting two 2-digit numbers",(10,2):"10.2 Connecting addition and subtraction",(10,3):"10.3 Multiplication",(10,4):"10.4 Division",(11,1):"11.1 Angles and turns",(11,2):"11.2 Circles",(12,1):"12.1 Telling the time",(13,1):"13.1 Mass and temperature",(13,2):"13.2 Capacity",(14,1):"14.1 Pattern and probability",(15,1):"15.1 Symmetry, position and movement"}
def S(u,s,a,an): sec(u,UN[u],s,SN[(u,s)],a,an)
# ---- 1. questions printed in the workbook (blank sums), answers computed
T=open('/tmp/g2b.txt').read().split('\f'); cu,cs=1,1
eqre=re.compile(r'(?<![\d.])(\d+(?:\s*[+–−\-×x÷]\s*\d+)+)\s*=\s*(?!\s*[\d?])')
OP={'+':'+','–':'-','−':'-','-':'-','×':'*','x':'*','÷':'/'}
for p in T[10:]:
    for l in p.split('\n'):
        m=re.match(r'^\s{20,}(\d+)\.(\d+) [A-Z]',l)
        if m and (int(m[1]),int(m[2])) in SN: cu,cs=int(m[1]),int(m[2])
    for m in eqre.finditer(p):
        ex=re.sub(r'\s+','',m[1]); py=''.join(OP.get(c,c) for c in ex)
        try: v=eval(py)
        except Exception: continue
        if v!=int(v) or v<0 or v>1000: continue
        v=int(v)
        if cu in (2,3): continue
        ccs=cs
        if cu in (5,10): ccs=3 if re.search('[×x]',ex) else 4 if '÷' in ex else (1 if '+' in ex else 2)
        S(cu,ccs,1,"Workbook questions")
        q=re.sub(r'([+–−\-×x÷])',r' \1 ',ex).replace('–','-').replace('−','-').replace('×','x')
        if q.count(' ')<2: continue
        if '÷' in q: e=f"Think of sharing or the times table: {q.replace(' ','')} gives <b>{v}</b>. Check by multiplying back."
        elif 'x' in q: e=f"Use equal groups or repeated addition. {q} = <b>{v}</b>."
        elif ' - ' in q: e=f"Count back or use tens and ones. {q} = <b>{v}</b>. Check by adding back."
        else: e=f"Add the tens and the ones. {q} = <b>{v}</b>."
        eq(q,v,e)
nbook=len(D)
# ---- 2. extra practice, following the same units
S(1,1,2,"Tens and ones")
for n in pick(11,99,6,lambda x:x%10):
    tx(f"How many tens are in {n}?",nums(n//10),f"In {n}, the first digit shows tens: <b>{n//10}</b> tens.")
    tx(f"{n//10} tens and {n%10} ones make which number?",nums(n),f"{n//10*10} + {n%10} = <b>{n}</b>.")
S(1,1,3,"Before, after and between")
for n in pick(12,98,6):
    tx(f"What number comes after {n}?",nums(n+1),f"Count on 1: {n}, <b>{n+1}</b>.")
    tx(f"What number comes before {n}?",nums(n-1),f"Count back 1: <b>{n-1}</b>, {n}.")
S(1,2,2,"Counting in steps")
for st,sz in [(2,2),(10,10),(5,5),(20,10),(30,5),(12,2),(40,10),(15,5)]:
    seq=[st+sz*i for i in range(4)]
    tx(f"Count on in {sz}s. What comes next? {', '.join(map(str,seq))}, ?",nums(seq[-1]+sz),f"Add {sz} each time. {seq[-1]} + {sz} = <b>{seq[-1]+sz}</b>.")
for g,sz in [(3,10),(5,10),(4,5),(6,2),(7,10),(8,5)]:
    eq(f"{g} x {sz}",g*sz,f"{g} groups of {sz}: count in {sz}s. {g} x {sz} = <b>{g*sz}</b>.")
S(1,3,2,"Compare and order")
for a,b in [(R.randint(11,89),0) for _ in range(8)]:
    b=a+R.choice([-1,1])*R.choice([1,3,9,10,11,20]); 
    if not 10<b<100 or a==b: continue
    big=R.random()<.5
    tx(f"Which number is {'bigger' if big else 'smaller'}: {a} or {b}?",[str(max(a,b) if big else min(a,b))],f"Compare the tens first, then the ones. The {'bigger' if big else 'smaller'} number is <b>{max(a,b) if big else min(a,b)}</b>.")
for _ in range(5):
    L=pick(10,99,3);big=R.random()<.5
    tx(f"Which is the {'biggest' if big else 'smallest'}: {L[0]}, {L[1]} or {L[2]}?",[str(max(L) if big else min(L))],f"In order: {', '.join(map(str,sorted(L)))}. The {'biggest' if big else 'smallest'} is <b>{max(L) if big else min(L)}</b>.")
for _ in range(6):
    n=R.randint(15,85);k=R.choice([1,10]);s=R.choice([1,-1])
    tx(f"What is {k} {'more' if s>0 else 'less'} than {n}?",nums(n+s*k),f"{n} {'+' if s>0 else '-'} {k} = <b>{n+s*k}</b>.")
S(2,1,2,"3D shapes")
for q,a,e in [("Which 3D shape is like a ball?",["sphere","a sphere"],"A ball is a sphere."),("Which 3D shape is like a tin of beans?",["cylinder","a cylinder"],"A tin is a cylinder."),("Which 3D shape is like a dice?",["cube","a cube"],"A dice is a cube."),("Which 3D shape is like an ice-cream cone?",["cone","a cone"],"It is a cone."),("Which 3D shape is like a cereal box?",["cuboid","a cuboid","rectangular prism"],"A box with rectangle faces is a cuboid."),("How many faces does a cube have?",nums(6),"A cube has 6 square faces."),("How many faces does a cuboid have?",nums(6),"A cuboid has 6 rectangle faces."),("Does a sphere roll or slide?",["roll","it rolls","rolls"],"A sphere is curved all over, so it rolls."),("Does a cube roll or slide?",["slide","it slides","slides"],"A cube has flat faces, so it slides."),("Does a cylinder roll, slide or both?",["both","roll and slide"],"A cylinder rolls on its curved side and slides on its flat faces."),("How many flat faces does a cylinder have?",nums(2),"A cylinder has 2 flat circular faces.")]: tx(q,a,e)
S(2,2,2,"2D shapes")
for q,a,e in [("How many sides does a triangle have?",nums(3),"Tri means three: 3 sides."),("How many sides does a square have?",nums(4),"A square has 4 equal sides."),("How many sides does a rectangle have?",nums(4),"A rectangle has 4 sides."),("How many sides does a pentagon have?",nums(5),"Penta means five."),("How many sides does a hexagon have?",nums(6),"Hexa means six."),("How many corners does a triangle have?",nums(3),"A triangle has 3 corners."),("How many corners does a circle have?",nums(0),"A circle is round. It has no corners."),("Which shape has 4 equal sides?",["square","a square"],"A square has 4 equal sides."),("Which shape has 3 sides?",["triangle","a triangle"],"A triangle has 3 sides."),("Which shape is round with no corners?",["circle","a circle"],"A circle is round.")]: tx(q,a,e)
S(2,3,2,"Fractions of shapes")
FR2={(1,2):["1/2","half","one half","a half"],(1,4):["1/4","quarter","one quarter","a quarter"],(3,4):["3/4","three quarters"],(2,4):["2/4","two quarters","1/2","half"]}
for (n,d),acc in FR2.items(): tx(f"A shape is cut into {d} equal parts. {n} part{'s are' if n>1 else ' is'} shaded. What fraction is shaded?",acc,f"{n} out of {d} equal parts is <b>{n}/{d}</b>.")
for q,a,e in [("How many halves make one whole?",nums(2),"2 halves = 1 whole."),("How many quarters make one whole?",nums(4),"4 quarters = 1 whole."),("Which is bigger: a half or a quarter?",["half","a half","1/2"],"A half is bigger than a quarter.")]: tx(q,a,e)
S(3,1,2,"Length")
for q,a,e in [("How many centimetres are in 1 metre?",nums(100),"1 m = 100 cm."),("Which is longer: 1 metre or 1 centimetre?",["1 metre","metre","1 m","1m"],"A metre is much longer than a centimetre."),("Which unit would you use to measure a pencil: cm or km?",["cm"],"A pencil is small. Use cm."),("Which unit would you use to measure a road: cm or km?",["km"],"A road is long. Use km.")]: tx(q,a,e)
for a,b in [(5,8),(3,9),(7,12),(4,10)]: tx(f"A pencil is {a} cm long and a ruler is {b} cm long. How much longer is the ruler (in cm)?",nums(b-a),f"{b} - {a} = <b>{b-a}</b> cm.")
S(3,2,2,"Measuring lines")
for a,b in [(3,4),(5,2),(6,3),(7,5)]: tx(f"Draw a line {a} cm long, then {b} cm more in a straight line. How long is the line altogether (in cm)?",nums(a+b),f"{a} + {b} = <b>{a+b}</b> cm.")
S(4,1,2,"Tally charts")
for g,x in [(1,2),(2,3),(3,1),(2,0),(4,2),(3,3)]: tx(f"A tally chart shows {g} group{'s' if g>1 else ''} of five and {x} more marks. What number is that?",nums(g*5+x),f"{g} x 5 = {g*5}. {g*5} + {x} = <b>{g*5+x}</b>.")
S(4,1,3,"Carroll diagrams")
for n in (7,12,18,25,30):
    tx(f"A Carroll diagram sorts numbers into 'odd' and 'even'. Which box does {n} go in?",["even" if n%2==0 else "odd"],f"{n} ends in {n%10}, so it is <b>{'even' if n%2==0 else 'odd'}</b>.")
S(5,1,2,"Add to 2-digit numbers")
for _ in range(8):
    a,b=R.randint(21,85),R.randint(2,9);eq(f"{a} + {b}",a+b,f"Add the ones: {a%10} + {b} = {a%10+b}. Keep the tens. {a} + {b} = <b>{a+b}</b>.")
for _ in range(6):
    a,b=R.randint(12,70),R.choice([10,20,30]);eq(f"{a} + {b}",a+b,f"Adding {b} adds {b//10} to the tens digit. {a} + {b} = <b>{a+b}</b>.")
S(5,1,3,"Add three numbers")
for a,b,c in [(5,5,5),(6,4,7),(8,2,9),(3,7,4),(10,20,30),(5,5,10),(4,6,8),(2,8,5)]: eq(f"{a} + {b} + {c}",a+b+c,f"Look for numbers that make 10 first. {a} + {b} + {c} = <b>{a+b+c}</b>.")
S(5,2,2,"Subtract from 2-digit numbers")
for _ in range(8):
    a,b=R.randint(31,98),R.randint(2,9);eq(f"{a} - {b}",a-b,f"Count back {b} from {a}. {a} - {b} = <b>{a-b}</b>. Check: {a-b} + {b} = {a} ✔")
for _ in range(6):
    a,b=R.randint(35,99),R.choice([10,20,30]);eq(f"{a} - {b}",a-b,f"Subtracting {b} takes {b//10} from the tens digit. {a} - {b} = <b>{a-b}</b>.")
S(5,3,2,"Times tables 2, 5 and 10")
for m in (2,5,10):
    for n in pick(1,10,5): eq(f"{m} x {n}",m*n,f"{m} groups of {n}, or count in {m}s {n} times. {m} x {n} = <b>{m*n}</b>.")
S(5,4,2,"Sharing")
for m in (2,5,10):
    for n in pick(2,10,4): eq(f"{m*n} ÷ {m}",n,f"Share {m*n} into {m} equal groups, or think {m} x ? = {m*n}. The answer is <b>{n}</b>.")
for t,g,th in [(12,2,"sweets"),(20,5,"stickers"),(30,10,"marbles"),(16,2,"cards")]: tx(f"{t} {th} are shared equally between {g} children. How many does each child get?",nums(t//g),f"{t} ÷ {g} = <b>{t//g}</b>.")
S(6,1,2,"Coins and totals")
for q,a,e in [("How many 5c coins make 20c?",nums(4),"5 + 5 + 5 + 5 = 20."),("How many 10c coins make 50c?",nums(5),"10 x 5 = 50."),("How many 2c coins make 10c?",nums(5),"2 x 5 = 10."),("How many 10c coins make US$1?",nums(10),"10 x 10c = 100c = US$1."),("How many cents are there in US$1?",nums(100),"US$1 = 100c.")]: tx(q,a,e)
for p,pay in [(25,50),(30,50),(15,20),(40,100),(35,50),(60,100)]: tx(f"A sweet costs {p}c. You pay {pay}c. How much change do you get (in c)?",[str(pay-p),f"{pay-p}c"],f"{pay} - {p} = <b>{pay-p}</b>c.")
for a,b in [(10,5),(20,10),(15,5),(50,20)]: tx(f"A toy costs US${a} and a book costs US${b}. How much is that in total (US$)?",[str(a+b),f"${a+b}",f"us${a+b}"],f"{a} + {b} = <b>{a+b}</b>.")
S(7,1,2,"Days and months")
DAYS="Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
for i in range(6): tx(f"What day comes after {DAYS[i]}?",[DAYS[i+1]],f"After {DAYS[i]} comes <b>{DAYS[i+1]}</b>.")
for i in (1,3,6): tx(f"What day comes before {DAYS[i]}?",[DAYS[i-1]],f"Before {DAYS[i]} comes <b>{DAYS[i-1]}</b>.")
for q,a,e in [("How many days are there in a week?",nums(7),"7 days."),("How many months are there in a year?",nums(12),"12 months."),("How many days are in 2 weeks?",nums(14),"7 + 7 = 14."),("What is the first month of the year?",["january"],"January."),("What is the last month of the year?",["december"],"December."),("Which month comes after May?",["june"],"May, June."),("Which month comes before October?",["september"],"September, October."),("Which season comes after winter?",["spring"],"The seasons: winter, spring, summer, autumn.")]: tx(q,a,e)
S(8,1,2,"Numbers in words")
for n in pick(11,99,8,lambda x:x%10): tx(f"Write the number name for {n}.",[W(n)],f"<b>{n}</b> is written <b>{W(n)}</b>.")
for n in pick(21,99,4,lambda x:x%10): tx(f"Write the number for {W(n)}.",[str(n)],f"{W(n)} = <b>{n}</b>.")
S(8,1,3,"Rounding and regrouping")
for n in pick(11,98,8,lambda x:x%10):
    r=(n//10+(1 if n%10>=5 else 0))*10
    tx(f"Round {n} to the nearest 10.",nums(r),f"Look at the ones digit {n%10}. {'5 or more: round up.' if n%10>=5 else 'Less than 5: round down.'} <b>{r}</b>.")
for n in pick(31,95,5,lambda x:x%10<8):
    tx(f"{n} = {n//10-1} tens and ? ones",nums(n%10+10),f"Take 1 ten and make it 10 ones: {n%10} + 10 = <b>{n%10+10}</b> ones.")
S(8,2,2,"Fractions of numbers")
for n,d in [(10,2),(12,2),(20,2),(16,2),(20,4),(12,4),(8,4),(40,4),(18,2),(24,4)]:
    nm="half" if d==2 else "quarter"
    tx(f"What is a {nm} of {n}?",nums(n//d),f"Share {n} into {d} equal parts: {n} ÷ {d} = <b>{n//d}</b>.")
S(9,1,2,"Venn diagrams and lists")
for q,a,e in [("Numbers 1 to 10 go in a Venn diagram: 'even' and 'bigger than 5'. Which numbers are in both circles? (use spaces)",["6 8 10"],"Even and bigger than 5: <b>6, 8, 10</b>."),("In the same diagram, which numbers are in neither circle? (use spaces)",["1 3 5"],"Odd and 5 or less: <b>1, 3, 5</b>."),("How many even numbers are there from 1 to 10?",nums(5),"2, 4, 6, 8, 10 = 5 numbers.")]: tx(q,a,e)
S(9,2,2,"Reading data")
for items in [("cats","dogs","fish"),("red","blue","green"),("apples","pears","plums")]:
    v=pick(2,12,3);d=dict(zip(items,v));s=", ".join(f"{k} {x}" for k,x in d.items());top=max(d,key=d.get);low=min(d,key=d.get)
    tx(f"A table shows: {s}. Which has the most?",[top],f"{top} has the biggest number, {d[top]}.")
    tx(f"A table shows: {s}. How many are there in total?",nums(sum(v)),f"{' + '.join(map(str,v))} = <b>{sum(v)}</b>.")
    tx(f"A table shows: {s}. How many more {top} than {low}?",nums(d[top]-d[low]),f"{d[top]} - {d[low]} = <b>{d[top]-d[low]}</b>.")
S(10,1,2,"Add 2-digit numbers")
for _ in range(10):
    a,b=R.randint(12,48),R.randint(11,49);eq(f"{a} + {b}",a+b,f"Add the tens: {a//10*10} + {b//10*10} = {a//10*10+b//10*10}. Add the ones: {a%10} + {b%10} = {a%10+b%10}. Total <b>{a+b}</b>.")
S(10,1,3,"Subtract 2-digit numbers")
for _ in range(10):
    a=R.randint(40,99);b=R.randint(11,a-10);eq(f"{a} - {b}",a-b,f"Take away the tens, then the ones. {a} - {b} = <b>{a-b}</b>. Check: {a-b} + {b} = {a} ✔")
S(10,2,2,"Add and subtract families")
for a,b in [(35,20),(48,10),(27,30),(54,40),(63,5),(72,6)]:
    tx(f"{a} + {b} = {a+b}. So {a+b} - {b} = ?",nums(a),f"Subtraction undoes addition. {a+b} - {b} = <b>{a}</b>.")
for a,b in [(14,6),(25,5),(37,3)]: tx(f"Complete: {a} + ? = {a+b}",nums(b),f"{a+b} - {a} = <b>{b}</b>.")
S(10,3,2,"Multiplication facts")
for m in (2,5,10,3,4):
    for n in pick(2,10,3): eq(f"{n} x {m}",n*m,f"{n} groups of {m}. {n} x {m} = <b>{n*m}</b>. (Order does not matter: {m} x {n} is the same.)")
S(10,4,2,"Division facts")
for m in (2,5,10,3,4):
    for n in pick(2,10,3): eq(f"{m*n} ÷ {m}",n,f"Think: {m} x ? = {m*n}. {m} x {n} = {m*n}, so the answer is <b>{n}</b>.")
S(11,1,2,"Angles and turns")
for q,a,e in [("How many right angles make a full turn?",nums(4),"4 quarter turns make a full turn."),("How many right angles make a half turn?",nums(2),"2 quarter turns make a half turn."),("How many right angles does a square have?",nums(4),"A square has 4 square corners."),("You face the door and turn a half turn. Which way do you face now?",["away from the door","opposite","the other way"],"A half turn faces you the opposite way."),("Which way do clock hands turn: clockwise or anticlockwise?",["clockwise"],"Clock hands turn clockwise.")]: tx(q,a,e)
S(11,2,2,"Circles")
for q,a,e in [("How many corners does a circle have?",nums(0),"A circle is round. It has no corners."),("How many straight sides does a circle have?",nums(0),"A circle has one curved edge and no straight sides."),("Which of these is a circle: a wheel or a window?",["wheel","a wheel"],"A wheel is round.")]: tx(q,a,e)
S(12,1,2,"Clock times")
for q,a in [("half past 3","3:30"),("quarter past 6","6:15"),("quarter to 5","4:45"),("7 o'clock","7:00"),("half past 10","10:30"),("quarter past 12","12:15"),("quarter to 2","1:45"),("9 o'clock","9:00")]: tx(f"Write '{q}' in digital time (like 3:30).",[a],f"'{q}' is <b>{a}</b>.")
for q,a,e in [("How many minutes are in 1 hour?",nums(60),"60 minutes."),("How many minutes are in half an hour?",nums(30),"30 minutes."),("How many minutes are in a quarter of an hour?",nums(15),"15 minutes."),("How many hours are in a day?",nums(24),"24 hours.")]: tx(q,a,e)
S(13,1,2,"Mass and temperature")
for q,a,e in [("How many grams are in 1 kilogram?",nums(1000),"1 kg = 1000 g."),("Which is heavier: 1 kg or 1 g?",["1 kg","1kg","kilogram","1 kilogram"],"1 kg is 1000 times heavier."),("Which unit would you use to weigh an apple: g or kg?",["g"],"An apple is light, so use g."),("What do we use to measure temperature?",["thermometer","a thermometer"],"A thermometer."),("At what temperature does water freeze (in °C)?",nums(0),"0 °C."),("Is ice hot or cold?",["cold"],"Ice is cold.")]: tx(q,a,e)
S(13,2,2,"Capacity")
for q,a,e in [("How many millilitres are in 1 litre?",nums(1000),"1 litre = 1000 ml."),("Which holds more: a bucket or a cup?",["bucket","a bucket"],"A bucket is bigger."),("Which unit would you use for a bottle of water: ml or litres?",["litres","litre","l"],"A big bottle is measured in litres."),("A jug holds 2 litres. How many litres do 3 jugs hold?",nums(6),"2 + 2 + 2 = 6.")]: tx(q,a,e)
S(14,1,2,"Number patterns")
for st,d in [(2,2),(5,5),(10,10),(1,2),(3,3),(4,2),(50,10),(20,-2),(30,-5)]:
    seq=[st+d*i for i in range(4)];tx(f"What comes next? {', '.join(map(str,seq))}, ?",nums(seq[-1]+d),f"The pattern {'adds' if d>0 else 'subtracts'} {abs(d)}. {seq[-1]} {'+' if d>0 else '-'} {abs(d)} = <b>{seq[-1]+d}</b>.")
S(14,1,3,"Probability words")
for q,a in [("The sun will rise tomorrow.","certain"),("A dog will talk to you today.","impossible"),("You will eat something today.","likely"),("It will snow in a hot desert.","unlikely"),("Day comes after night.","certain"),("A pig will fly.","impossible")]:
    tx(f"Is this certain, likely, unlikely or impossible? \"{q}\"",[a],f"Think how often it happens. This is <b>{a}</b>.")
S(15,1,2,"Symmetry")
for s,n in [("square",4),("rectangle",2),("circle","lots"),("letter A",1),("letter H",2),("heart",1)]:
    if n=="lots": tx("Does a circle have lots of lines of symmetry or none?",["lots","lots of lines of symmetry","lots of lines"],"You can fold a circle in half many ways."); continue
    tx(f"How many lines of symmetry does a {s} have?",nums(n),f"A line of symmetry splits a shape into 2 matching halves. A {s} has <b>{n}</b>.")
S(15,1,3,"Left, right and position")
for q,a,e in [("If you face north, which side is east: left or right?",["right"],"East is on your right when facing north."),("If you face north, which side is west: left or right?",["left"],"West is on your left when facing north."),("Which direction is opposite to north?",["south"],"North and south are opposite."),("Which direction is opposite to east?",["west"],"East and west are opposite."),("You face north and turn a quarter turn clockwise. Which way do you face?",["east"],"Clockwise from north is east.")]: tx(q,a,e)
open('grade2wb.js','w').write('const QUESTIONS2W='+json.dumps(D,separators=(',',':'),ensure_ascii=False)+';\n')
import collections
print('total',len(D),'from book blanks',nbook);print(sorted(collections.Counter(d['t'] for d in D).items()))
