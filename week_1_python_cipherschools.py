a=255
print(id(a))
1650840267120

[4]
b=276
print(id(b))
1650919841552

[5]
c=278
print(id(c))
1650919839056

[6]
a='aaaaa'
print(type(a))
<class 'str'>

[7]
print('Nikhil kumar')
Nikhil Kumar

[8]
print(1,2,3,'Nikhil',3.3,1_5j, sep=",")
1,2,3,Nikhil,3.3,15j

[11]
print('Hello', end=';')
print('World :')
Hello;World :

[12]
print('a')
print('b')
print('c')
a
b
c

[13]
a=15
bin(a)
'0b1111'
[14]
a=15
str(a)
'15'
[15]
int('1234')
1234
[16]
float('1.5')
1.5
[18]
isinstance(a,object)
True
[19]
a='A'
isinstance(a,object)
True
[20]
5+5
10
[24]
10-5
5
[26]
isinstance(10.0,int)
False
[22]
10/3
3.3333333333333335
[23]
10//3
3
[27]
10%3
1
[28]
2**3
8
[29]
2*3
6
[30]
'nikhil'+'kumar'
'nikhilkumar'
[34]
"abc" *6
'abcabcabcabcabcabc'
[36]
'nikhil'' ' 'kumar'
'nikhilkumar'
[37]
1==2
False
[38]
1!=2
True
[39]
2>3
False
[40]
'ab'<'z'
True
[41]
'a'<'A'
False
[42]
True and False
False
[43]
True or False
True
[44]
True and 1
1
[45]
1 and 0
0
[46]
1 and 5
5
[47]
isinstance(True, int)
True
[48]
type(True)
bool
[49]
'' and 6
''
[51]
1.6 or ''
1.6
[52]
bool('')
False
[53]
bool([1,2,3])
True
[54]
'' and 0
''
[55]
112 and 0
0
[58]
a=True
if a:
    print('the value is true')
print('end')
    
the value is true
end

[59]
a=True
if a:
    print('this value is true')
else:
    print('this value is false')
this value is true

[60]
a=5
if a==3:
    print("this value is 3")
elif a==5:
    print("this value is 5")
else:
    print("this value is not 3 or 5")
this value is 5

[61]
a=1
while a<10:
    print(a)
    a+=1
1
2
3
4
5
6
7
8
9

[65]
name='Nikhil'
a.iter
<method-wrapper 'iter' of str object at 0x000001806282B3F0>
[67]
print(type(name))
for c in name:
    print(c)
    print(type(c))
<class 'str'>
A
<class 'str'>
b
<class 'str'>
h
<class 'str'>
i
<class 'str'>
s
<class 'str'>
h
<class 'str'>
e
<class 'str'>
k
<class 'str'>

[69]
for i in range(5):
    print(i)
0
1
2
3
4

a=range(5)
[70]
a.iter
<method-wrapper 'iter' of str object at 0x000001806282B3F0>
[72]
'aaaaaa'*4
'aaaaaaaaaaaaaaaaaaaaaaaa'
[79]
for i in range(5):
    print(i)
    if i == 3:
        break
        
0
1
2
3

[81]
for i in range(5):
    print(i)
    i=100
0
1
2
3
4

[82]
if True:
    'jhdgkygbiuy'
    print('rest of the code')
rest of the code

[83]
for i in range(5):
    print(i)
else:
    print('something')
0
1
2
3
4
something

[89]
n=5
for i in range(n):
    for j in range(n):
        print(i, end=' ')
    print()
0 0 0 0 0 
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 

[90]
n=5
[91]
for i in range(n):
    for j in range(n):
        print(i, end=' ')
    print('\n')
0 0 0 0 0 

1 1 1 1 1 

2 2 2 2 2 

3 3 3 3 3 

4 4 4 4 4 


[92]
n=5
[93]
for i in range(n):
    for j in range(n):
        print(n-j, end=' ')
    print('\n')
5 4 3 2 1 

5 4 3 2 1 

5 4 3 2 1 

5 4 3 2 1 

5 4 3 2 1 


[94]
max(1,2,3,4,5,7)
7
[98]
n=9
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,n-j), end=' ')
    print()
9 9 9 9 9 9 9 9 9 
9 8 8 8 8 8 8 8 9 
9 8 7 7 7 7 7 8 9 
9 8 7 6 6 6 7 8 9 
9 8 7 6 5 6 7 8 9 
9 8 7 6 6 6 7 8 9 
9 8 7 7 7 7 7 8 9 
9 8 8 8 8 8 8 8 9 
9 9 9 9 9 9 9 9 9 

[101]
n=5
for i in range(n):
    for j in range(n):
        i,j
        print((i,j), end=' ')
    print()
(0, 0) (0, 1) (0, 2) (0, 3) (0, 4) 
(1, 0) (1, 1) (1, 2) (1, 3) (1, 4) 
(2, 0) (2, 1) (2, 2) (2, 3) (2, 4) 
(3, 0) (3, 1) (3, 2) (3, 3) (3, 4) 
(4, 0) (4, 1) (4, 2) (4, 3) (4, 4) 

[103]
for i in range(n):
    for j in range(n):
        print(max(i,j), end=' ')
    print()
0 1 2 3 4 
1 1 2 3 4 
2 2 2 3 4 
3 3 3 3 4 
4 4 4 4 4 

[104]
for i in range(n):
    for j in range(n):
        print(j, end=' ')
    print()
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4 

[107]
for i in range(n):
    for j in range(n):
        print(n-i-1, end=' ')
    print()
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1 
0 0 0 0 0 

[108]
for i in range(n):
    for j in range(n):
        print(n-j-1, end=' ')
    print()
4 3 2 1 0 
4 3 2 1 0 
4 3 2 1 0 
4 3 2 1 0 
4 3 2 1 0 

[109]
max(1,2,3,4,5,6,7,8,9)
9
[110]
sum([1,2,3,4,5,6,7,8,9])
45


