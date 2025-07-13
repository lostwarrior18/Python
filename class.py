a=20
b=30
c=(a+b)
print(c)

#Loop
i=1
while i<=5:
    print(i)
    i=i+1

for i in range(6):
    print(i)


#......
li=[10,20,30,40,2,3,4]
print(type(li))
li[0]=123
li.append(20)
print(li)

#....
tup=(20,30,40,50)
print(tup.count(20))
print(len(tup))
print(tup.index(30))
print(tup)

##.....
dict ={
    'name' : 'prashant',
    'age' : 20,
    'address' : 'kathmandu'
}
print(dict)
print(dict['name'])

#.set
set1= {1,2,3,4,'prashant','false'}
print(type(set1))
print(len(set1))
set1.pop()
print(set1)

#.
set1={1,2,3,4,5}
set2={3,7,5,8,9}
froset1=frozenset(set1)
froset2=frozenset(set2)
print(froset1)
print(froset2)
print(froset1.intersection(froset2))

#......
from collections import deque
dq= deque([1,2,3,4,5])
dq.append(6)
dq.appendleft(0)
dq.remove(2)
print(dq)

#.
from collections import defaultdict
d= defaultdict(int)
d['a']=1
print(d)

#..
from collections import defaultdict
name='sitaram'
dd=defaultdict(int)
for ch in name:
    dd[ch]+=1
print(dd)

#..
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)

#map
marks=[60,70,80,90]
def s_grade(marks):
    if marks>=90:
        return 'A'
    elif 90>marks>80:
        return 'B'
    elif 80>marks>70:
        return 'C'
    else:
        return 'D'
grade= map(s_grade, marks)
print("student marks", marks)
print("students grade", next(grade))

#filter
marks=[60,50,40,55]
def fail(marks):
    return marks<50
result = filter(fail,marks)
print('students marks', marks)
print('failing marks', list(result))


