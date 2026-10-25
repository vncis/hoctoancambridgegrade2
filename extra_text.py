import json
from parse_text import words, MON
base=json.load(open('textq.json'))
X=[]
def add(w,topic,q,acc,e):
    acc=[a.lower() for a in acc]
    X.append(dict(t=5,w=w,a=1,n=topic,q=q,r=acc,e=e))
def num(n): return [str(n),words(n)]
DAYS="Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
# 1 Days and months
T="Days and months"
for i in (0,3,5): add(1,T,f"What day comes after {DAYS[i]}?",[DAYS[i+1]],f"Days in order: {', '.join(DAYS)}. After {DAYS[i]} comes <b>{DAYS[i+1]}</b>.")
for i in (2,4,6): add(1,T,f"What day comes before {DAYS[i]}?",[DAYS[i-1]],f"Days in order: {', '.join(DAYS)}. Before {DAYS[i]} comes <b>{DAYS[i-1]}</b>.")
add(1,T,"How many months are there in one year?",num(12)+["12 months","twelve months"],"January to December: 1 January, 2 February, 3 March, 4 April, 5 May, 6 June, 7 July, 8 August, 9 September, 10 October, 11 November, 12 December. That is <b>12</b> months.")
add(1,T,"Which month comes after March?",["april"],"Months in order: January, February, March, <b>April</b>.")
add(1,T,"Which month comes before June?",["may"],"Months in order: April, <b>May</b>, June.")
add(1,T,"What is the last month of the year?",["december"],"The year ends with <b>December</b> (month 12).")
add(1,T,"Which two days make the weekend?",["saturday and sunday","saturday sunday","sunday and saturday"],"The weekend is <b>Saturday and Sunday</b>. The other 5 days are school days.")
# 2 Number names (reverse) and words
T="Numbers in words"
for n in (11,15,30,45,60,72,88,90,99): add(2,T,f"Write the number name for {n}.",[words(n)],f"Say it slowly. <b>{n}</b> is written <b>{words(n)}</b>.")
for n in (13,27,54,66,81): add(2,T,f"Write the number for {words(n)}.",[str(n)],f"<b>{words(n)}</b> means <b>{n}</b>: {n//10} tens and {n%10} units.")
# 3 Ordinals
T="Ordinal numbers"
for k,w_ in ((1,"first"),(2,"second"),(3,"third"),(4,"fourth"),(5,"fifth")): add(3,T,f"Write the ordinal number for {w_} using digits and letters (for example 6th).",[f"{k}{'st' if k==1 else 'nd' if k==2 else 'rd' if k==3 else 'th'}"],f"{w_} is number {k}, so we write <b>{k}{'st' if k==1 else 'nd' if k==2 else 'rd' if k==3 else 'th'}</b>.")
add(3,T,"Which ordinal number comes after 4th?",["5th","fifth"],"1st, 2nd, 3rd, 4th, <b>5th</b>.")
add(3,T,"Which ordinal number comes before 10th?",["9th","ninth"],"8th, <b>9th</b>, 10th.")
add(3,T,"What is the 3rd letter of the alphabet?",["c"],"A is 1st, B is 2nd, <b>C</b> is 3rd.")
add(3,T,"What is the 5th letter of the alphabet?",["e"],"A, B, C, D, <b>E</b>: the 5th letter is E.")
# 4 Shapes
T="Shapes"
for q,a,e in (("How many sides does a square have?",4,"A square has <b>4</b> equal sides."),("How many sides does a rectangle have?",4,"A rectangle has <b>4</b> sides: 2 long and 2 short."),("How many sides does a pentagon have?",5,"Penta means five. A pentagon has <b>5</b> sides."),("How many sides does a hexagon have?",6,"Hexa means six. A hexagon has <b>6</b> sides."),("How many corners does a triangle have?",3,"A triangle has 3 sides and <b>3</b> corners.")):
    add(4,T,q,num(a)+[f"{a} sides" if 'sides' in q else f"{a} corners"],e)
add(4,T,"Which flat shape has 3 sides?",["triangle","a triangle"],"<b>Tri</b> means three. A <b>triangle</b> has 3 sides.")
add(4,T,"Which flat shape has 4 equal sides?",["square","a square"],"A <b>square</b> has 4 sides that are all the same length.")
add(4,T,"What 3-D object is shaped like a ball?",["sphere","a sphere"],"A ball is a <b>sphere</b>. It can roll in every direction.")
add(4,T,"What 3-D object is shaped like a tin of beans?",["cylinder","a cylinder"],"A tin has two round flat faces and a curved side. It is a <b>cylinder</b>.")
add(4,T,"What 3-D object is shaped like a dice?",["cube","a cube","dice","a dice"],"All the faces of a dice are equal squares. It is a <b>cube</b>.")
# 5 Money
T="Money"
add(5,T,"How many cents are there in R1?",num(100)+["100c","100 cents"],"R1 = <b>100</b> cents.")
add(5,T,"How many 10c coins make R1?",num(10)+["10 coins","ten coins"],"10c × 10 = 100c = R1, so you need <b>10</b> coins.")
add(5,T,"How many 5c coins make 20c?",num(4)+["4 coins","four coins"],"5 + 5 + 5 + 5 = 20, so you need <b>4</b> coins.")
add(5,T,"How many 2c coins make 10c?",num(5)+["5 coins","five coins"],"2 + 2 + 2 + 2 + 2 = 10, so you need <b>5</b> coins.")
add(5,T,"You buy a sweet for R3 and pay with R5. How much change do you get?",["r2","2","two","r2 change"],"Change = money you gave − price. R5 − R3 = <b>R2</b>.")
# 6 Time and measure
T="Time and measurement"
add(6,T,"How many hours are there in one day?",num(24)+["24 hours","twenty four hours"],"One whole day and night is <b>24</b> hours.")
add(6,T,"How many minutes are there in one hour?",num(60)+["60 minutes","sixty minutes"],"1 hour = <b>60</b> minutes.")
add(6,T,"How many minutes are there in half an hour?",num(30)+["30 minutes","thirty minutes"],"Half of 60 is <b>30</b>.")
add(6,T,"How many centimetres are there in 1 metre?",num(100)+["100 cm","100 centimetres"],"1 m = <b>100</b> cm.")
add(6,T,"Which is longer: a metre or a centimetre?",["metre","a metre","the metre"],"1 metre is 100 centimetres, so the <b>metre</b> is longer.")
add(6,T,"Which is heavier: a kilogram or a gram?",["kilogram","a kilogram","the kilogram"],"1 kilogram = 1000 grams, so the <b>kilogram</b> is heavier.")
add(6,T,"How many days are there in February in a normal year?",num(28)+["28 days"],"February is the shortest month. It has <b>28</b> days (29 in a leap year).")
# 7 Number sense
T="Number sense"
for n in (8,15,22,37,40): add(7,T,f"Is {n} odd or even?",["even" if n%2==0 else "odd"],f"Even numbers end in 0, 2, 4, 6 or 8. {n} ends in {n%10}, so it is <b>{'even' if n%2==0 else 'odd'}</b>.")
for a,b in ((45,54),(19,91),(68,86)):
    add(7,T,f"Which number is bigger: {a} or {b}?",[str(max(a,b))],f"Compare the tens first: {a//10} tens and {b//10} tens. <b>{max(a,b)}</b> is bigger.")
    add(7,T,f"Which number is smaller: {a} or {b}?",[str(min(a,b))],f"Compare the tens first: {a//10} tens and {b//10} tens. <b>{min(a,b)}</b> is smaller.")
add(7,T,"What is 1 more than 99?",num(100),"99 + 1 = <b>100</b>.")
add(7,T,"What is 1 less than 50?",num(49),"50 − 1 = <b>49</b>.")
add(7,T,"What is double 6?",num(12),"Double means two groups of the same number: 6 + 6 = <b>12</b>.")
add(7,T,"What is half of 10?",num(5),"Half means share into 2 equal groups: 10 ÷ 2 = <b>5</b>.")
# 8 Place value
T="Place value"
for n in (47,63,85):
    add(8,T,f"How many tens are in {n}?",num(n//10),f"In {n}, the first digit shows tens: <b>{n//10}</b> tens.")
    add(8,T,f"How many units are in {n}?",num(n%10),f"In {n}, the last digit shows units: <b>{n%10}</b> units.")
for n in (53,76): add(8,T,f"What is the value of the {n//10} in {n}?",num(n//10*10),f"{n//10} is in the tens place. {n//10} tens = <b>{n//10*10}</b>.")
for n in (36,59): add(8,T,f"{n//10} tens + {n%10} units = ?",[str(n),words(n)],f"{n//10} tens = {n//10*10}. {n//10*10} + {n%10} = <b>{n}</b>.")
allq=base+X
open('textquestions.js','w').write('const TEXTQ='+json.dumps(allq,separators=(',',':'))+';\n')
print(len(base),len(X),len(allq))
