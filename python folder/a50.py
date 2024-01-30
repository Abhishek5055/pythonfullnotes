#50 lecture
#readlines() method #it is used to read the sentence line by line
f=open('ab.txt','r')
while True:
    line =f.readline()
    if not line:
        break
    print(line)
    
#Example 2
f=open('ex.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"marks of student {i} in Maths is:{m1}")
    print(f"marks of student {i} in English is:{m2}")
    print(f"marks of student {i} in SST is:{m3}")
    print(line)
    
#Example 3
#writelines()
f=open('xt.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()


#51 lecture
with open('re.txt','r') as f:
    f.seek(10)          #it will start first 10 letters
    print(f.tell())
    # data=f.read()
    # print(data)
    data=f.read(5)      #it will read only 5 letters
    print(data)
    
#example 3
#truncate() function
with open('sample.txt','w') as f:
    f.write("Good World!")
    f.truncate(5)       #it will read 5 characters starting 5
with open('sample.txt','r') as f:
    print(f.read())
    
#52 lecture
#lambda functions
#Example 1
double =lambda x:x*x        #lambda function
print(double(5))

#Example 2
def apply(fx,value):
    return 6+fx(value)
double =lambda x:x*2
cube =lambda x:x*x*x
avg =lambda x,y,z:(x+y+z)/3

print(double(5))
print(cube(5))
print(avg(3,5,10))

print(apply(lambda x:x*x,5))

#53 lecture
#map
def cube(x):
    return x*x*x
print(cube(5))

l=[11,12,13,14,15]
new=list(map(cube,l))
print(new)

#filter
def filter_function(a):
    return a>12
newnewl=list(filter(filter_function,l))
print(newnewl)

#reduce
from functools import reduce
numbers=[1,2,3,4,5]

sum=reduce(lambda x,y:x+y,numbers)
print(sum)