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


