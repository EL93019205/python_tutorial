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
#print(id(X))
#print(id(Y))
print(Y)
print(X)
X=['a','b']
Y=X
#print(id(X))
#print(id(Y))
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

#print(fruits['apple'])

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
#print(kind)

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

print("""\
##################################
# 比較演算子と論理演算子を扱おう #
##################################\
""")
a=0
b=1
# aがbと等しい
print(a == b)
# aがbと異なる
print(a != b)
# aがbよりも小さい
print(a < b)
# aがbよりも大きい
print(a > b)
# aがb以下である
print(a <= b)
# aがb以上である
print(a >= b)
# aもbも真であれば真
print(a>0 and b>0)
# aまたはbが真であれば真
print(a>0 or b>0)

print("""\
###################
# InとNotを扱おう #
###################\
""")
y=[1,2,3]
x=1
if x in y:
	print('in')
if 100 not in y:
	print('not in')
a=1
b=2
# notは奨められていない
if not a == b:
	print('not equal')
# こっちが推奨
if a != b:
	print('not equal')
is_ok=True
if not is_ok:
	print('hello')

print("""\
################################
# 値が入っていない判定を行おう #
################################\
""")
is_ok=True
#False,0,0.0,'',[],(),{},set()
is_ok=[1,2,3,4]
if is_ok:
	print('OK')
else:
	print('NO!')
print("""\
####################
# Noneを判定しよう #
####################\
""")
is_empty=None
print(is_empty)
print(type(is_empty))
if is_empty is not None:
	print('None!!!')
print(1 == True)
#print(1 is True)
print(None is None)
print("""\
################################
# while,continue,breakを扱おう #
################################\
""")
count=0
while True:
	if count >= 5:
		break
	if count == 2:
		count+=1
		continue
	print(count)
	count+=1

print("""\
########################
# while else文を扱おう #
########################\
""")
count = 0
while count < 5:
	if count==1:
		break
	print(count)
	count+=1
else:
	print('done')
print("""\
#####################
# input関数を扱おう #
#####################\
""")
"""
while True:
	word=input('Enter:')
	if word=='ok':
		break
	print('next')
"""
print("""\
##############################
# for,break,continueを扱おう #
##############################\
""")
some_list=[1,2,3,4,5]
"""
i=0
while i < len(some_list):
	print(some_list[i])
	i+= 1
"""
for i in some_list:
	print(i)
for s in 'abcde':
	print(s)

for word in ['My', 'name', 'is', 'Mike']:
	if word == 'name':
		continue
	if word == 'Mike':
		break
	print(word)
print("""\
###################
# for elseを扱おう#
###################\
""")
for fruit in ['apple', 'banana', 'orange']:
	if fruit == 'banana':
		print('stop eating')
		break
	print(fruit)
else:
	print('I ate all!')

print("""\
#####################
# range関数を扱おう #
#####################\
""")

num_list=[0,1,2,3,4,5,6,7,8,9]
for i in num_list:
	print(i)

for i in range(2,10,3):
	print(i)
for i in range(10):
	print(i,'hello')
for _ in range(10):
	print('hello')
print("""\
#########################
# emumerate関数を扱おう #
#########################\
""")
i=0
for i, fruit in enumerate(['apple', 'banana','orange']):
	print(i,fruit)
#print(enumerate(['apple','banana','orange']))
print(type(enumerate(['apple','banana','orange'])))

print("""\
###################
# zip関数を扱おう #
###################\
""")
days = ['Mon','Tue','Wed']
fruits = ['apple', 'banana', 'orange']
drinks=['coffee','tea','beer']

for i in range(len(days)):
	print(days[i],fruits[i],drinks[i])
for day, fruit, drink in zip(days,fruits,drinks):
	print(day,fruit,drink)

print("""\
###########################
# 辞書をfor文で処理しよう #
###########################\
""")
d = {'x': 100, 'y':200}
print(d)
print(d.items())

for k, v in d.items():
	print(k, ':', v)

print("""\
####################
# 関数を定義しよう #
####################\
""")
def say_something():
	print('hi')
say_something()
say_something
print(type(say_something))
f=say_something
f()
def say_something():
	s='hi'
	return s
result=say_something()
print(result)

def what_is_this(color):
	if color == 'red':
		return 'tomato'
	elif color == 'green':
		return 'green pepper'
	else:
		return "I don't know"

result = what_is_this('red')
print(result)
result = what_is_this('green')
print(result)
result = what_is_this('yellow')
print(result)

print("""\
####################################
# 関数の引数と返り値の宣言について #
####################################\
""")
def add_num(a: int,b: int) -> int:
	return a+b
r=add_num('a','b')
print(r)

print("""\
####################################################
# 位置引数とキーワード引数とデフォルト引数を扱おう #
####################################################\
""")
def menu(entree='beef',drink='wine',desert='ice'):
	print('entree=',entree)
	print('drink=',drink)
	print('desert=',desert)

#menu('beef', desert='ice', drink='beer')
menu()
menu('chicken',drink='beer')

def test_func(x,l=None):
	if l is None:
		l = []
	l.append(x)
	return l

y=[1,2,3]
r=test_func(100,y)
print(r)


y=[1,2,3]
r=test_func(200,y)
print(r)


r=test_func(100)
print(r)

r=test_func(100)
print(r)
#デフォルト引数に辞書型やリスト型を指定すると不具合に繋がりやすい
#その場合はNoneを指定し、関数内で空のリストや辞書を入れる

print("""\
##############################
# 位置引数のタプル化を扱おう #
##############################\
""")
def say_something(word,*args):
	print('word='+word)
	for arg in args:
		print(arg)

t=('Mike','Nancy')
say_something('Hi!' , *t)

print("""\
################################
# キーワード引数を辞書化しよう #
################################\
""")
def menu(food, *args, **kwargs):
	print(food)
	print(args)
	print(kwargs)
menu('banana', 'apple', 'orange', entree='beef', drink='coffee')

print("""\
######################
# Docstringsを扱おう #
######################\
""")
def example_func(param1, param2):
	"""Example function with types documented in the docstring.
	
	Args:
		param1(int): The first parameter.
		param2(str): The second parameter.

	Returns:
		bool: The return value. True for success, False otherwise
	"""
	print(param1)
	print(param2)
	return True

print(example_func.__doc__)
help(example_func)

print("""\
############################
# 関数内関数を扱ってみよう #
############################\
""")
def outer(a,b):
	def plus(c,d):
		return c+d
	r1=plus(a,b)
	r2=plus(b,a)
	print(r1+r2)
outer(1,2)

print("""\
##############################
# クロージャーを扱ってみよう #
##############################\
""")
def outer(a,b):
	def inner():
		return a+b
	return inner


f=outer(1,2)
r=f()
print(r)

def circle_area_func(pi):
	def circle_area(radius):
		return pi * radius * radius

	return circle_area

ca1=circle_area_func(3.14)
ca2=circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

print("""\
##############################
# デコレーターを扱ってみよう #
##############################\
""")

def print_more(func):
	def wrapper(*args, **kwargs):
		print("***")
		print('func:' ,func.__name__)
		print('args:',args)
		print('kwargs:',kwargs)
		result=func(*args,**kwargs)
		print('result:',result)
		print("***")
		return result
	return wrapper


def print_info(func):
	def wrapper(*args,**kwargs):
		print('start')
		result=func(*args,**kwargs)
		print('end')
		return result
	return wrapper

@print_info
@print_more
def add_num(a,b):
	return a+b

@print_info
def sub_num(a,b):
	return a-b

r=add_num(10,20)
print(r)

r=sub_num(20,10)
print(r)

#f=print_into(add_num)
#r=f(10,20)
#print(r)

print("""\
########################
# ラムダを扱ってみよう #
########################\
""")
l=['Mon','tue','Wed','Thu','fri','sat','Sun']

def change_words(words,func):
	for word in words:
		print(func(word))
"""
def sample_func(word):
	return word.capitalize()
"""
change_words(l,lambda word: word.capitalize())
change_words(l,lambda word: word.lower())

print("""\
################################
# ジェネレーターを扱ってみよう #
################################\
""")
l = ['Good morning', 'Good afternoon', 'Good night']
for i in l:
	print(i)

def greeting():
	yield 'Good morning'
	yield 'Good afternoon'
	yield 'Good night'

for g in greeting():
	print(g)

g = greeting()
print(next(g))
print("aaa")
print(next(g))
print("@@@")
print(next(g))
def counter(num=10):
	for _ in range(num):
		yield 'run'
	while True:
		yield 'stop'

c = counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print("""\
##########################
# リスト内包表記を扱おう #
##########################\
""")
t=(1,2,3,4,5)
t2=(5,6,7,8,9,10)
r=[]
for i in t:
	if i % 2 == 0:
		r.append(i)
print(r)

r=[i for i in t if i % 2 == 0]
print(r)

r=[]
for i in t:
	for j in t2:
		r.append(i*j)
print(r)

r=[i*j for i in t for j in t2]
print(r)

print("""\
########################
# 辞書包括表記を扱おう #
########################\
""")
w=['mon','tue','wed']
f=['coffee','milk','water']

d={}
for x,y in zip(w,f):
	d[x]=y

print(d)

d={x:y for x, y in zip(w,f)}
print(d)

print("""\
########################
# 集合内包表記を扱おう #
########################\
""")
s = set()

for i in range(10):
	if i % 2 == 0:
		s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

print("""\
##################################
# ジェネレーター内包表記を扱おう #
##################################\
""")
def g():
	for i in range(10):
		yield i
g=g()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

g=(i for i in range(10))

print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

g=(i for i in range(10) if i % 2 == 0)

print(type(g))
#print(g)

for x in g:
	print(x)
#ジェネレーターとタプルは表記が似ているので要注意！

print("""\
##############################
# 名前空間とスコープを扱おう #
##############################\
""")
animal = 'cat'

def f():
	"""Test func doc"""
	print(f.__name__)
	print(f.__doc__)
f()
#print('global:',globals())

print("""\
####################
# 例外処理を扱おう #
####################\
""")
l=[1,2,3]
i=5
try:
	l[0]
except IndexError as ex:
	print("Don't worry: {}".format(exi))
except NameError as ex:
	print(ex)
except Exception as ex:
	print('other:{}'.format(ex))
else:
	print('done')
finally:
	print('clean up')

print("""\
########################
# 独自例外を作成しよう #
########################\
""")
class UppercaseError(Exception):
	pass

def check():
	words = ['APPLE', 'orange', 'banana']
	for word in words:
		if word.isupper():
			raise UppercaseError(word)

try:
	check()
except UppercaseError as exc:
	print('This is my fault. Go next')

print("""\
##############################
# コマンドライン引数を扱おう #
##############################\
""")
import sys
print(sys.argv)
print('test')
for i in sys.argv:
	print(i)
print("""\
########################
# Import文とASを扱おう #
########################\
""")
#import lesson_package.utils
#from lesson_package import utils as u

#from lesson_package.utils import say_twice
#r=utils.say_twice('hello')
#print(r)

print("""\
######################################
# 絶対パスと相対パスのImportを扱おう #
######################################\
""")
from lesson_package.talk import human
print(human.sing())
print(human.cry())

print("""\
###############################################################
# アスタリスクのインポートと__init__.pyと__all_の意味を知ろう #
###############################################################\
""")
#from lesson_package.talk import animal
from lesson_package.talk import *
print(animal.sing())
print(animal.cry())
# import *は好まれていない

from lesson_package.tools import utils
print("""\
#######################
# ImportErrorを扱おう #
#######################\
""")
try:
	from lesson_package import utils
except ImportError:
	from lesson_package.tools import utils

print(utils.say_twice('word'))
print("""\
########################
# 組み込み関数を扱おう #
########################\
""")
#print(globals())
ranking={
	'A': 100,
	'B': 85,
	'C': 95
}

for key in ranking:
	print(key)
ranking.get('A')
print(sorted(ranking,key=ranking.get,reverse=True))
print("""\
##########################
# 標準ライブラリを扱おう #
##########################\
""")
s = "fjaskl;jfljslkjzmxnfkhjaiueorqp,mbnzvhhiuahfena"
d={}
for c in s:
	if c not in d:
		d[c]=0
	d[c]+=1
print(d)

d={}
for c in s:
	d.setdefault(c,0)
	d[c] += 1
print(d)

from collections import defaultdict
d=defaultdict(int)
for c in s:
	d[c] += 1
print(d)
print(d['f'])

print("""\
########################################
# サードパーティーのライブラリを扱おう #
########################################\
""")
from termcolor import colored
print(colored('test','red'))
print(colored('test','green'))
#print(help(colored))

print("""\
##################################
# imoprtする際の記述に注意しよう #
##################################\
""")
# 標準ライブラリ
import collections
import os
import sys

# サードパーティーライブラリ
import termcolor

# 他チームのライブラリ
import lesson_package

# 自分のライブラリ
#import config

#print(collections.__file__)
#print(termcolor.__file__)
#print(lesson_package.__file__)
#print(config.__file__)

#print(sys.path)
print("""\
#######################################
# __name__と__main__の扱いに注意しよう#
#######################################\
""")
import config
import lesson_package.talk.animal
def main():
	lesson_package.talk.animal.sing()

print('main:',__name__)
if __name__ == '__main__':
	main()

print("""\
######################
# クラスを定義しよう #
######################\
""")
s='asdkfjakfd'
print(s.capitalize())
class Person(object):
	def say_something(self):
		print('hello')

person=Person()
person.say_something()

def person(name):
	if name == 'A':
		print('hello')

print("""\
######################################
# クラスを初期化しクラス変数を扱おう #
######################################\
""")
class Person(object):
	def __init__(self,name):
		self.name=name

	def say_something(self):
		print('I am {}. hello'.format(self.name))
		self.run(10)

	def run(self, num):
		print('run'*num)

person=Person('Mike')
person.say_something()

print("""\
########################################
# コンストラクタとデストラクタを扱おう #
########################################\
""")
class Person(object):
	def __init__(self,name):
		self.name=name

	def say_something(self):
		print('I am {}. hello'.format(self.name))
		self.run(10)

	def run(self, num):
		print('run'*num)
	def __del__(self):
		print('goodbye')

person=Person('Mike')
person.say_something()

del person

print('#########')

print("""\
######################
# クラスを継承しよう #
######################
""")
class Car(object):
	def run(self):
		print('run')

class ToyotaCar(Car):
	pass

class TeslaCar(Car):
	def auto_run(self):
		print('auto run')

car = Car()
car.run()

print('#########')
toyota_car = ToyotaCar()
toyota_car.run()
#toyota_car.auto_run()
print('#########')
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()

print("""\
###############################################################
# メソッドのオーバーライドとsuperによる親メソッドを呼び出そう #
###############################################################\
""")
class Car(object):
	def __init__(self, model=None):
		self.model=model
		# print(model+'aasdffafsgg')
	def run(self):
		print('run')

class ToyotaCar(Car):
	def run(self):
		print('fast')

class TeslaCar(Car):
	def __init__(self, model='Model S', enable_auto_run=False):
		# self.model=model
		super().__init__(model)
		self.enable_auto_run=enable_auto_run
	def run(self):
		print('super fast')
	def auto_run(self):
		print('auto run')

car = Car()
car.run()

print('#########')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('#########')
tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()
print("""\
##########################################
# プロパティーを使った属性の設定をしよう #
##########################################\
""")
class Car(object):
	def __init__(self, model=None):
		self.model=model
		# print(model+'aasdffafsgg')
	def run(self):
		print('run')

class ToyotaCar(Car):
	def run(self):
		print('fast')

class TeslaCar(Car):
	def __init__(self, model='Model S', 
				enable_auto_run=False,
				passwd='123'):
		# self.model=model
		super().__init__(model)
		self.__enable_auto_run=enable_auto_run
		self.passwd = passwd
	
	@property
	def enable_auto_run(self):
		return self.__enable_auto_run
	
	@enable_auto_run.setter
	def enable_auto_run(self, is_enable):
		if self.passwd == '456':
			self.__enable_auto_run=is_enable
		else:
			raise ValueError

	def run(self):
		print(self.__enable_auto_run)
		print('super fast')
	def auto_run(self):
		print('auto run')
tesla_car = TeslaCar('Model S',passwd="111")
tesla_car.__enable_auto_run='XXXXXXXXXXXXXX'
tesla_car.run()
print(tesla_car.__enable_auto_run)

print("""\
##############################################
# クラスを構造体として扱う時の注意点を知ろう #
##############################################\
""")
class T(object):
	pass

t=T()
t.name='Mike'
t.age=20
print(t.name,t.age)

print("""\
##############################
# ダック・タイピングを扱おう #
##############################\
""")
class Person(object):
	def __init__(self, age=1):
		self.age=age
	def drive(self):
		if self.age >= 18:
			print('ok')
		else:
			raise Exception('No drive')

class Baby(Person):
	def __init__(self, age=1):
		if age < 18:
			super().__init__(age)
		else:
			raise ValueError

class Adult(Person):
	def __init__(self, age=18):
		if age >= 18:
			super().__init__(age)
		else:
			raise ValueError
baby=Baby()
adult=Adult()
class Car(object):
	def __init__(self, model=None):
		self.model=model
		# print(model+'aasdffafsgg')
	def run(self):
		print('run')
	def ride(self, person):
		person.drive()

car=Car()
car.ride(adult)

print("""\
######################
# 抽象クラスを扱おう #
######################\
""")
import abc
class Person(metaclass=abc.ABCMeta):
	def __init__(self, age=1):
		self.age=age
	@abc.abstractmethod
	def drive(self):
		pass
	


class Baby(Person):
	def __init__(self, age=1):
		if age < 18:
			super().__init__(age)
		else:
			raise ValueError
	def drive(self):
		raise Exception('No drive')

class Adult(Person):
	def __init__(self, age=18):
		if age >= 18:
			super().__init__(age)
		else:
			raise ValueError
	def drive(self):
		print('ok')

baby=Baby()
#baby.drive()
adult=Adult()
#adult.drive()
class Car(object):
	def __init__(self, model=None):
		self.model=model
		# print(model+'aasdffafsgg')
	def run(self):
		print('run')
	def ride(self, person):
		person.drive()

car=Car()
car.ride(adult)

print("""\
####################
# 多重継承を扱おう #
####################\
""")
class Person(object):
	def talk(self):
		print('talk')
	def run(self):
		print('person run')

class Car(object):
	def run(self):
		print('car run')

class PersonCarRobot(Car,Person):
	def fly(self):
		print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()

print("""\
######################
# クラス変数を扱おう #
######################\
""")
class Person(object):
	kind='human'
	def __init__(self,name):
		self.kind = 'human'
		self.name = name
	def who_are_you(self):
		print(self.name, self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

class T(object):
	def __init__(self):
		self.words=[]
	def add_word(self, word):
		self.words.append(word)

c=T()
c.add_word('add 1')
c.add_word('add 2')
print(c.words)

d=T()
d.add_word('add 3')
d.add_word('add 4')
print(d.words)

print("""\
################################################
# クラスメソッドとスタティックメソッドを扱おう #
################################################\
""")
def about(year):
	print('about human {}'.format(year))

class Person(object):
	kind='human'

	def __init__(self):
		self.x=100

	@classmethod
	def what_is_your_kind(cls):
		return cls.kind
	
	@staticmethod
	def about(year):
		print('about human {}'.format(year))

a=Person()
print(a.what_is_your_kind())
b=Person
print(b.what_is_your_kind())
print(Person.kind)
print(Person.what_is_your_kind())
Person.about(1999)

print("""\
########################
# 特殊メソッドを扱おう #
########################\
""")
class Word(object):
	def __init__(self, text):
		self.text = text

	def __str__(self):
		return 'Word!!!!!'
	
	def __len__(self):
		return len(self.text)

	def __add__(self, word):
		return self.text.lower() + word.text.lower()
	
	def __eq__(self,word):
		return self.text.lower() == word.text.lower()

w = Word('test')
w2 = Word('test')
print(w)
print(len(w))
print(w+w2)
print(w==w2)

print("""\
########################
# ファイルを作成しよう #
########################\
""")
print("""\
################################################
# withステートメントでファイルをオープンしよう #
################################################\
""")
print("""\
########################
# ファイルを読み込もう #
########################\
""")
print("""\
##########################
# seekを使って移動しよう #
##########################\
""")
s="""\
AAA
BBB
CCC
DDD
"""
with open('test.txt', 'r') as f:
	print(f.tell())
	print(f.read(1))
	f.seek(5)
	print(f.read(1))
	f.seek(14)
	print(f.read(1))
	f.seek(15)
	print(f.read(1))
	f.seek(5)
	print(f.read(1))
















