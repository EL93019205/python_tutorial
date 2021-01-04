# 変数を宣言しよう
num = 1
name = 'Mike'
is_ok = True

print("#############")
print("# 出力しよう#")
print("#############")
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))
print('Hi','Mike',sep=',',end='\n')

print("#################")
print("# 文字列を扱おう#")
print("#################")
print('hello')
print("hello")
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")
print('hello.\nHow are you?')
print(r'C:\name\name')
print("""\
line1
line2
line3\
""")
print('Hi.' * 3 + 'Mike.' )
print('Py''thon')
s = ('aaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbb')
print(s)

print("##########################################")
print("# 文字列のインデックスとスライスを扱おう #")
print("##########################################")
word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[0:2])
print(word[:2])
print(word[2:])
word='j'+word[1:]
print(word[:])
n = len(word)
print(n)

print("##############################")
print("# 文字列のメソッドを扱おう！ #")
print("##############################")
s = 'My name is Mike. Hi Mike.'
print(s)
is_start=s.startswith('My')
print(is_start)
is_start=s.startswith('X')
print(is_start)
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s[s.find('Mike')])
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike','Nancy'))

print("######################")
print("# 文字を代入しよう！ #")
print("######################")
print('a is {}'.format('a'))
print('a is {}'.format('test'))
print('a is {} {} {}'.format(1,2,3))
print('a is {0} {1} {2}'.format(1,2,3))
print('a is {2} {1} {0}'.format(1,2,3))
print('My name is {0} {1}'.format('Jun','Sakai'))
print('My name is {0} {1}. Watashi ha {1} {0}'.format('Jun','Sakai'))
print('My name is {name} {family}. Watashi ha {family} {name}'.format(name='Jun',family='Sakai'))
print(1)
print('1')
str(1)
x = str(1)
print(type(x))
print(str(3.14))
str(True)

print("############################")
print("# f-stringを使ってみよう！ #")
print("############################")
a = 'a'
print(f'a is {a}')

x,y,z=1,2,3
print(f'a is {x},{y},{z}')
print(f'a is {z},{y},{x}')

name = 'Jun'
family = 'Sakai'
print(f'My name is {name}{family}. Watashi ha {family} {name}')

print("############################")
print("# リスト型を使ってみよう！ #")
print("############################")
l=[1,20,4,50,2,1,2]
print(l[0])
print(l[1])
print(l[-1])
print(l[-2])
print(l[0:2])
print(l[:2])
print(l[2:])
print(l[2:5])
print(l[:])
print(len(l))
print(type(l))
print(list('abcdefg'))
#print(l[100])
n=[1,2,3,4,5,6,7,8,9,10]
print(n[1:8:2])
print(n[::-1])
a=['a','b','c']
n=[1,2,3]
x=[a,n]
print(x)
print(x[0])
print(x[1])
print(x[0][1])
print(x[1][2])

print("##########################")
print("# リストの操作をしよう！ #")
print("##########################")
s=['a','b','c','d','e','f','g']
print(s)
s[0]='x'
print(s)
s[2:5]=['C','D','E']
s[:]=[]
print(s)
n=[1,2,3,4,5,6,7,8,9,10]
n.append(100)
print(n)
n.insert(0,200)
print(n)
n.pop()
print(n)
n.pop(0)
print(n)
del n[0]
del n
n=[1,2,2,2,3]
n.remove(2)
print(n)
a=[1,2,3,4,5]
b=[6,7,8,9,10]
x=a+b
print(x)
a+=b
print(a)
x = [1,2,3,4,5]
y = [6,7,8,9,10]
x.extend(y)

print("##############################")
print("# リストのメソッドを扱おう！ #")
print("##############################")
r = [1,2,3,4,5,1,2,3]
print(r.index(3,3))
print(r.count(3))
if 100 in r:
    print('exist')
r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)
x= '###'.join(to_split)
print(x)
#print(help(list))

print("##########################")
print("# リストをコピーしよう！ #")
print("##########################")
i=[1,2,3,4,5]
j=i
j[0]=100
print('j=',j)
print('i=',i)
print(type(i))
print(type(j))
# pythonにも値渡しと参照渡しの概念があるので注意
x=[1,2,3,4,5]
y=x.copy()
y=x[:]
y[0]=100
print('x=',x)
print('y=',y)
X=20
Y=X
Y=5
print(id(X))
print(id(Y))
print(Y)
print(X)
X=['a','b']
Y=X
print(id(X))
print(id(Y))
Y[0]='p'
print(Y)
print(X)

print("################################")
print("# リストはどのような時に使うか #")
print("################################")
seat = []
min = 0
max = 5
print(min <= len(seat) < max)
seat.append('p')
seat.append('p')
seat.append('p')
seat.append('p')
seat.append('p')
print(min <= len(seat) < max)
seat.pop(0)
print(min <= len(seat) < max)

print("""\
##########################
# タプル型を扱ってみよう #
##########################\
""")
t = (1,2,3,4,1,2)
print(t)
print(type(t))
#t[0]=100
print(t[0])
print(t[2:5])
print(t.index(1))
print(t.index(1,1))
print(t.count(1))
print(t)
print(t)
print(t)
t=([1,2,3],[4,5,6])
t[0][0] = 100
print(t)
t = 1,2,3
print(type(t))
print(t)
t=1,
print(type(t))
t=()
print(type(t))
t=(1)
print(type(t))
t=('test')
print(type(t))
t=('test',)
print(type(t))
t=1,
#t+100
new_tuple = (1,2,3)+(4,5,6)
print(new_tuple)
#new_tuple =(1)+(4,5,6)
new_tuple=(1,)+(4,5,6)
print(new_tuple)

print("""\
########################################
# タプルのアンパッキングを扱ってみよう #
########################################\
""")
num_tuple = (10,20)
print(num_tuple)
x, y = num_tuple
print(x,y)

x, y = (10, 20)
print(x,y)

min, max = 0, 100
print(min, max)

a,b,c,d,e,f = 'Mike', 'l','l','l','e','f'
a='Mike'
b='1'

i=10
j=20
tmp=i
i=j
j=tmp
print(i,j)

a=100
b=200
print(a,b)
a,b=b,a
print(a,b)

print("""\
##################
# タプルの使い所 #
##################\
""")
choose_from_two = ('A','B','C')
answer=[]
answer.append('A')
answer.append('B')
print(choose_from_two)
print(answer)

print("""\
########################
# 辞書型を扱ってみよう #
########################\
""")
d = {'x':10, 'y': 20}
print(d)
print(type(d))
d['x']=100
print(d)
d['x']='XXXX'
print(d)
d['z']=200
print(d)
d[1]=10000
print(d)
print(dict(a=10,b=20))
d=dict([('a',10),('b',20)])
print(d)
d={'x':10,'y':20}
print(d.keys())
print(d.values())
d2={'x':1000,'j':500}
d.update(d2)
print(d)
print(d2)

print(d['x'])
print(d.get('x'))
#print(d['z'])
print(d.get('z'))
r=d.get('z')
print(r)
print(type(r))

print(d.get('x'))
print(d.pop('x'))
print(d)
del d['y']
print(d)
d={'a':100,'b':200}
d.clear()
print(d)
d={'a':100,'b':200}
print('a' in d)
print('j' in d)

x = {'a':1}
y = x
y['a']=1000
print(x)
print(y)
x = {'a':1}
y = x.copy()
y['a']=1000
print(x)
print(y)

fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,

}

print(fruits['apple'])

print("""\
########################
# 集合型を扱ってみよう #
########################\
""")
a = {1,2,2,3,4,4,4,5,6}
print(a)
print(type(a))
b={2,3,3,6,7}
print(b)
print(a-b)
print(b-a)
print(a & b)
print(a|b)
print(a^b)
s={1,2,3,4,5}
print(s)
#print(s[0])
s.add(6)
print(s)
s.add(6)
print(s)
s.remove(6)
print(s)
s.clear()
print(s)
a={}
print(type(a))
print(a)
my_friends = {'A', 'C', 'D'}
A_friends = {'B','D','E','F'}
print(my_friends & A_friends)
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)

print("""\
####################
# コメントを扱おう #
####################
\
""")
print('XXXXX')
# コメント
"""
ブロックコメント
"""
print('XXXXX')
# コメントは上に書くスタイル
some_value = 100 # Apple Value

print("""\
#########################
# 1行が長い場合を扱おう #
#########################
\
""")
s = ('aaaaaaaaaaa'
   + 'bbbbbbbbbbbbbb')
print(s)

# 1行は80文字で収めるべきというルールが一応ある

print("""\
######################
# if文を扱ってみよう #
######################
\
""")
x=10
if x < 0:
	print('negative')
elif x == 0:
	print('zero')
elif x == 10:
	print('100000')
elif x == 10:
	print('10')
else:
	print('positive')

a=5
b=10
if a > 0:
	print('a is positive')
	if b > 0:
		print('b is positive')


