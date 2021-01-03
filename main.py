# 変数を宣言しよう
num = 1
name = 'Mike'
is_ok = True

# 出力しよう
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))
print('Hi','Mike',sep=',',end='\n')

# 文字列を扱おう
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

# 文字列のインデックスとスライスを扱おう
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

#文字列のメソッドを扱おう！
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


# 文字を代入しよう！
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

# f-stringを使ってみよう！
a = 'a'
print(f'a is {a}')

x,y,z=1,2,3
print(f'a is {x},{y},{z}')
print(f'a is {z},{y},{x}')

name = 'Jun'
family = 'Sakai'
print(f'My name is {name}{family}. Watashi ha {family} {name}')







