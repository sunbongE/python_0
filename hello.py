print("hello")
print("hello", "world")
print("hello " + "world")
print("hello"+ ' ' +"world")

a=1+2
print(a)
a=2+3
print(a)


dic={'name':'e','age':10}
print(dic['age'])

a=1+2
a
a=2+3
a

print('hi') #이 주석은 hi를 출력합니다
print('hi')#print('hi')

a=2+3
print(a)
print('a의값은',a)
'''
a의 값을 구한다. (2+3=5)
a의 값을 출력한다. (5)
a의 값은 5를 출력한다.
'''

x=100
type(x)

x=[1:62]
x(7)


from random import* #로또 번호 생성기
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)

x= complex(2,3)
x
#사칙연산
a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a=10
b=3
print(a//b)# // 은 나눗셈의 몫을 구한다. 
print(a%b)# % 는 나머지를 구함
divmod(a, b) # divmod 는 나머지와 몫을 한번에 구한다.

a= -10
print(a) #음수
print(-a) #양수
print(abs(a)) #절대값

a= 3.14 #실수
b= 10 #정수
print(int(a)) # 실수를 정수로 바꿈
print(float(b)) # 정수를 실수로

a=2
b=3
pow(2,3) #2의 3제곱을 구한다. pow(수,n제곱)

a=2
b=3
a**b # 같은 2의 3제곱을 구함 

"Hello my name is DetegiCE. \
Welcome to my blog. \
I teach Python programming \
to a lot of people who visit my blog."#백슬레쉬로 이어붙이기

a="hi im taeho.\n90\
i study python.\n\  # \n\은 엔터와 같이 다음 줄로 넘기는 기능
it is little hard.\  # \는 아래쓴 문자와 합하여 나타남
thanks."
print(a) #print가 있어야 하는게 함정

a="first name\tTAEHO\nlast name\tPARK" 
print(a) # 여기서 \t 는 텝 키와 같이 일정 간격 띄어줌. \n ~은 아래 줄 이동과 시작하는 문구

a="""Hi my first name is TAEHO
last name is PARK"""
print(a)  # 큰 따옴표를 3개를 시작과 끝에 붙이면 내가 쓴데로 줄 이동 등이 자유로움

a="""1   one
2   two
3   three"""
print(a)

'It\'s me' #따옴표 출력은 보기와 같이 ' 전에 \를 해서 \'로 해야 오류가없음

'hi'*2 # 반복 출력은 *반복횟수로 한다.

a="ikssan park taeho"  
a[1]  #여기서는 0번째 부터 있어서 1이면 k임
a="ikssan park taeho"
a[-1] # -는 뒤에서 부터 선택 -1부터 시작

a="ikssan park taeho"
a[3:6] #3번째 문자부터 5번째 문자까지 출력함 

a="ikssan park taeho"
print(a[:6])  #앞에 6글자 출력. 몇번째와는 다른 개념
print(a[-5:]) #뒤에 5글자 출력

--- formatting 포메팅---
'I\'m %d years old' %26 # %d를 이용한 숫자 삽입

'%d=0o%o=0x%x' %(17,17,17)  #10진수는 %앞에 0d없이 한다. 
# 0d는 10진법을 0o는 8진수 0x는 16진수임을 알리고 %d,o,x는 나타낼 숫자 입력.

'%d=0o%o=0x%x' %(26,26,26)#연습
'%x' %(17), '%o' %(17) #이건 뭐지

'pi is %f not %d' %(3.14,3.14) #실수와 정수를 나타낼수도 있다.

'%c is name\'s %s character' %('p','first')
# %c는 한글자만 넣을 수 있고 %s는 문자열을 넣을 수 있다.
#깨달음 문자는 따옴표 안에 있어야한다.

age=26
f'I\'m {age} years old'
# f와 {}으로 삽입하는 방식. f를 띄어쓰면 안됨.

x='I\'m {0} years old'#여기서 {0}은 함수안에 0번째 매개변수이므로 26을 뜻함
x.format(26)

x='I\'m {0}{1} years old'
x.format(2,6) #이런 느낌

x='I\'m {0} {1} old'
x.format(26,'years') # 이런 느낌

a='abcde'
print(a) #a를 출력한다.
print(len(a)) #a의 문열의 길이 즉, 글자 수를 알려준다.

a='Hello python'
a.count('l') # a문자열에서 ()안의 문자의 갯수를 알려줌
a.count('ll') # ll은 한개임 

a='Hello pyton'
a.find('l')
a.find('py') #띄어쓰기 포함해서 순서를 셈

a='안녕'
a.find('안') #한글도 됨

a='hello python'
a.find('car')  # 해당 단어가 없으면 -1을 리턴한다.
a.index('car') # 해당 단어가 없으면 error를 리턴한다. index:찾아보기
---------문자열 변형----------
upper 대문자  lower 소문자
a='python'
print(a.upper())
print(a.lower())

특정 문자열을 다른 문자열로 대체하는 replace:대체하다 함수도있음
a='He is tired'
a=a.replace('He','she') # He를 she로 대체시켜준다.
print(a)

문자와 문자사이에 끼워 넣기 join 함수
a='kg'
b='1230' # 1230사이에 kg을 삽입해서 0뒤에는 붙지 않아
a.join(b) #a를 b에 끼워넣다

공백을 없애주는 함수 strip 앞은 lstrip 뒤는 rstrip 사용 strip은 전부
a='     in&out      '
a.strip() #공백 없게
a.lstrip() #앞에만 없게
a.rstrip() #뒤에만 없게

분할 split
a='Hi i\'m park'
print(a.split())

a="pork hun"  # '', "" 둘다 무관하군
print(a.split())
type(a)
----------논리형-----------
참으 true 거짓은 false type은 bool이다
a=True
type(a)

a=1>2
print(a)  # true or false 판단 출력
type(a) # type 출력

----------리스트------------
list1=[1,2,3,4,5] #리스트안에는 숫자형 문자열 논리형 리스트도 들어갈수있다.
list2=[1,'two',3]
list3=[1,[2,3],4,[False,'six']]

x=[1,[2,3,4],5,[6,[7,8]]]
print(x[0]) #0번째 수 출력
print(x[1][1]) #1번째 리스트의 1번째 수 출력
print(x[3][1][1]) #3번째 리스트안에 1번째 리스트의 1번째 수 출력

x=[1,2,3,4,5]
x[-2] # -이용으로 뒤숫자 출력

x=['a','b','c','d','e']
x[0:4]  #[몇번째부터 : 몇개뽑을지]

x=[1,2,3,4,5]
x[2]=10 #2번째 수를 10으로 바꿈
x
---리스트에서 값 바꾸기---
x=[1,2,3,4,5]
x[0:3]=(11,11,11,11,11) #?!?!?!뭐지 이러면..안될듯
x

x=[1,2,3,4,5]
x[1:3]=(13,13) #이게 정상임 1번째와2번째 수를 13으로 대체
x 
---값 추가하기---
a=[1,2,3]
a.append(0) #0 추가  append는 값 1개 추가 가능
a # 뒤에 추가됨

a=[1,2,3]
a.extend([4,0]) #여러값을 추가할때 extend 확장 이라는 함수 사용 ([])이안에써야함
a
-----삽입 insert-----
a=[1,2,4,5]
a.insert(2,3) #2번째 위치에 3을 삽입한다.
a

a=[1,2,3]
a=a+[4,5]
a
-------요서 삭제--------
a=[1,2,2,3,4]
a.pop(1)
a
print함수를 사용하지 않아도 뺀 값과 a 출력됨
a=[1,2,2,3,4]
print(a.pop(1)) #여기서 4를 지우고싶으면 pop() 괄호안을 비우면 가장 뒷자리 삭제
print(a)

a=['a','b','c','d']
del a[1] #삭제할 요소 위치 기입
print(a)


a=['a','b','c','d']
del x #전부 삭제
print(x)

a=['car','home','phone']
a.remove('phone') #입력한 값을 제거
print(a)
---복사---
x=[1,2,3,4,5]
x2=x
print(x2)
x3=x.copy()
print(x3)

x=[1,2,3,4,5]
x2=x
print(x2) #x2는x다
x3=x.copy()
print(x3) #x3는x를 copy했다
x.remove(2) #x에서 2를 제거 
print(x2) # 2를 뺀 값이 나온다
print(x3) # 초기 x값이 나옴
---요소 위치 변형(정렬,뒤집기)
x=[5,1,3,2,9]
x.sort()  #오름차순 정렬
print(x)       

x=[5,1,3,2,9]
x.sort(reverse=True) #내림차순 정렬 sort(reverse=True) 이거 해야함
print(x)

x=[5,1,3,2,9]
print(x)
x.reverse() #리스트 원소들을 그대로 뒤집는다.
print(x)

---튜플()---
a=(1,2,3)
b=1,2,3
c=1,  # 요소가 하나인 경우 반드시 뒤에 쉼표를 붙인다.
print(a)
print(b)
print(c)
---대입---
a,b,c=1,2,3
print(a)
print(b)
print(c)

x=100
y=200
print(x,y) 
x,y=y,x
print(x,y) 
---튜플 인덱싱활용---
t=(1,2,3,4,5)
t2=t[:2]+(0,)+t[3:]
print(t2)
---리스트와 튜플---
l=[1,2,3]
t=tuple(l) #리스트와 튜플은 서로 형태변화가능
print(l)
print(t)

t=(1,2,3)
l=list(t)
print(t)
print(l)
---딕셔너리--- key와value로 사용
dic={'apple':'사과','banana':'바나나'}
print(dic)
print('apple은 한국어로',dic['apple'])

dic={'a':'taeho','b':'seo'}
print('my name is',dic['a'])

dic={'c':'car','v':'vehicle'}
print('차는 영어로',dic['c'])

dic={'dog':'개','cat':'고양이'}
dic['rabbit']='토끼' #토끼 추가
print(dic)
del dic['rabbit'] #토끼 삭제
print(dic)
dic['dog']='개새' # 수정
print(dic) 

dic={'apple':'사과','grape':'포도','strawberry':'딸기'}
print(dic.keys()) #key검색
print(dic.values()) #value 검색
print(dic.items()) #모두 검색
print('apple' in dic) #dic에 있는지 확인
print('banana' in dic) # 없으면 false

dic={'name':'park','name':'seo','name':'choi','name':'joseb'}
print(dic)#key가 중복이면 value를 하나만 출력
-----셋set([])-----
s1=set([11,2,3,4,4,4,1]) #중복은 삭제
s2=set('hello') #문자로 나옴
s3=set([1,2,3])
print(s1)
print(s2)
print(s3)

l=[11,22,33,33,44]
s=set(l)
print(s)
l2=list(s)
print(l2)# set은 리스트의 중복을 지우기로 사용됨
---set에서 추가,삭제---
s=set([1,2,3,4,5,5])
s.add(6) #6을 추가함
print(s)

s=set([1,2,3,3])
s.update([4,5,6]) #여러 수를 추가할 때
print(s)

s=set([1,2,2,3,4])
s.remove(4)
print(s)
---집합연산---
s1=set([1,2,3,4])
s2=set(3,4,9)
s3=set()
print(s1)
print(s2)
print(s3) #s3가 비어있어서 공집합

s1=set([1,2,3,4,5])
s2=set([3,4,5,6,8])
s3=set()
print(s1&s2) #교집합
print(s1.intersection(s2))
print(s1|s2)  #합집합
print(s1.union(s2))
print(s1-s2) #차집합 s1의 나머지를 보여줌
print(s1.difference(s2))
print(s2-s1)
print(s2.difference(s1))
print(s1^s2) #s1,s2를 차집합하고 양쪽 나머지를 보여줌
---조건문(if,elif,else)---
x=20
y=20
if x>y:
    print('x > y')
elif x<y:
    print('x < y')
else:
    print('x = y')

score=9 #이 값을 기준으로 판단 출력
if score >= 60:
     "success"
else:
    "fail"


score=80
message='success' if score>=60 else "fail"
print(message)
---조건문2 or,and,not,in,pass---
a=0
if a > 10 or a == 0: #둘중 하나가 사실이면 true
    print('true')

a=0
if a>-1 and a<10: #두 조건을 만족하면 true
    print('True')

a=0
if not a:  #a가 0이 아니면 true 
    print('true')

x=[1,2,3] #리스트에서 사용가능
if 2 in x:
    print('in')
if 4 not in x:
    print('not in')

x=(1,2,3) #튜플도 사용가능
if 2 in x:
    print('in')
if 4 not in x:
    print('not in') #문자열에서도 같은 방법 사용 가능

wallet=[1000,5000,10000]
if 10000 in wallet: pass # 만원이 있으면 종료
else: print('do card') #만원 없으면 do card실행
print('complete')#pass는 조건문이 참이나 거짓이면 종료됨 

-----반복문 while-----
while은 조건문이 거짓이 될 때 까지 반복한다.
a=0
while a<5: 
    print(a)#0을 출력한다.
    a=a+1#출력한 0에 +1

number=0  #실행은 되는데 1~4가 안나옴
while number !=4:
    print(number)
    number=int(input())
    

a=1
while a:
    print(a)
    a += 1
    if a >= 5:
        break

a=0
while a !=4:
    print(a)
    a=int(input())

---자판기 프로그램 만들어보기---
coffee=10 #처음부터 10개의 커피가 있다.
while True:
    money= int(input("동전을 넣어주세요:"))
    if money == 300:
        print("커피가 나옵니다.")
        coffee -= 1
    elif money >300:
        print("거스름 돈이 %d원과 커피가 나옵니다." %(money -300))
        coffee -=1
    else:
        print("돈을 다시 돌려주고 커피는 주지 않는다.")
    if coffee == 0:
        print("커피가 매진되었습니다.")
        break

a=0
while a < 10: #10보다 작은 수
    a = a + 1
    if a % 2 ==0:#짝수는 출력안함
        continue #while문을 빠져나가지않고 돌아가고싶을 때 사용
    print(a)

---반복문 for---
for의 형태는 
for 변수 in 리스트[]/튜플()/'문자열'/dic{}딕셔너리:
    문장

for x in [1,2,3]:
    print(x)

for x in (1,2,3):
    print(x)

for x in "a,s,d":
    print(x)

dic = {'a':1,'b':2}
for x in dic:
    print(x)
    print(dic[x])

for x in [1,2,3,4,5,6]:
    if x %2 ==0:
        print(x,'는 짝수이다.')

sore=[90,80,30,59]
for a in sore:
    if a >=60:
        print(a,'점 통과')

a= range(1,11)#자동으로 숫자 리스트를 만들어준다.
print(a)

b= range(9)
print(b)
--활용--
sum=0
for a in range(1,11): #1부터10까지의 합을 구한다.
    sum=sum + a
print(sum)          

for x in range(5):
    print(x)
    if x == 3:
        break #x가 3이면 반복문 탈출

for x in range(6):
    if x %2 == 1:
        continue
    print(x)#홀수는 수행하지 않음

for x in range(2, 10):
    for y in range(1, 10):
        print(x*y, end = ' ')#' '띄어쓰기 해야함
    print('')#x가2일때x가3일때~y를 다 곱해주는거임 구구단느낌

a=[1,2,3,4]
result = []

for num in a:
    result.append(num*3)#a 각 3배

print(result)

a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

a = [1,2,3,4]
result= [num*3 for num in a if num % 2 == 0]
print(result)#짝수에만 3배하여출력

구구단 = [x*y for x in range(2,10) #2에서9까지
            for y in range(1,10)]
print(구구단)
--파이썬에서의 함수 형태--
def sum(a, b): #입력값이 있고 
    answer = a+b
    return answer#결과값이 있다.

print(sum(2,4))

def sayhi():#입력값이 없음
    return 'hi'

a = sayhi()
print(a)

def saytwo(first, second):
    print(first, second)

saytwo('hi','taeho')

def add(a, b):
    print('%d + %d = %d' %(a, b, a+b) )

add(5, 2)

def say(): #입력과 결과값이 모두 없는 경우
    print('hi')

say()

def adds(*nums): # 입력값의 개수를 알수없을때 * 을 사용
    result = 0
    for i in nums:
        result = result + i
    return result
print(adds(1,2,3,4,5)) #1~5까지 합한수가 나옴

def say(one, two, *three):
    print(one, two)
    for i in three:
        print(i)
say('hi', 'i\'m', 'tae, ho')

--응용 계산기만들기--
def easy_calc(sign, *nums):#sign에들어갈 명령에 맞춰 계산
    result = 0
    if sign == '+':#합
        for i in nums:
            result = result + i
    elif sign == '*':#곱
        result = 1
        for i in nums:
            result = result * i
    else:
        result = -1
    return result

print(easy_calc('+', 1, 2, 6, 8))
print(easy_calc('*', 5, 1, 3, 2))
--딕셔너리 자료형--
def myfunc(**kwargs):
    print(kwargs)

myfunc(foo=1, bar=2)
myfunc(name='taeho', age=26)

def introduce(name, age, school='Inha university'):
    print('My name is', name)
    print('I am', age, 'years old')
    print('I attend to', school)

introduce('park', 26)#학교를 안쓰면 설정값으로
introduce('kim', 26, 'outha university')#쓰면 바뀜

#여러 반환값을 얻고 싶은 경우 리스트나 튜플로 묶어서 반환
def add_mul(a,b):
    return a+b, a*b
res1, res2 = add_mul(2, 3)
print(res1, res2)

def pass_fail(a):
    if a >= 70:
        print('PASS')
        return #여기에 리턴이 없으면 FAIL도 함께 출력됨
    print('FAIL')

pass_fail(80)
pass_fail(40)