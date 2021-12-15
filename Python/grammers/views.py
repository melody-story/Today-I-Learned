import json
from typing import Counter
from django import views
import django
# import requests

from django.views         import View
from django.http.response import JsonResponse



class GrammerView(View):
    def get(self, request):
        '''
        [ 값 교환 ]
        =======================
        a, b = 10, 20
        a, b = b, a
        print(a, b)
        => 결과 : 20, 10
        
        [ 출력 ] 
        =======================
        print("number : ", a, b, c)
        => number : 1, 2, 3
        
        print(i, sep=', ')
        => 1, 2, 3
        
        print(i, sep='')
        => 123
        
        print(i, sep='\n')
        =>
        1
        2
        3
        
        print(i, end=' ')
        => 결과 : 1 2 3 6 7 14 21 42
        
        =======================
            
        [ 반복문 ]
        
        @ For
        =======================
        1) i 증가
            for i in range(10):
                print(i)
            
            => 결과 : 0~9
            
        2) i 감소
            for i in range(10, 0, -2):
                print(i)
            => 결과 : 10, 8, 6, 4, 2
    
        2) 특정 조건에 해당하면 다시 반복문 처음으로 돌아가게하기
            for i in range(10):
                if i%2 == 0:
                    continue
                print(i) # 홀수만 출력됨
                i=i+1
                
                
            3) 특정 상황에서 반복문 멈추게 하기
            ** for ~, else~ 구문 : for 문에서 break가 걸리면, 실행되지 않는다. break가 걸리지 않을 때만 실행된다. 
            
                for i in range(1,11):
                    print(i)
                    if i>15:
                        break
                else:
                    print(11)

                    
                    
        @ While : 조건이 들어간다. i<=10이 참일 때, 반복문 중지
        =======================
        1) i 증가
            i=1
            while i<=10:
                print(i)
                i=i+1
            
        2) i 감소     
            i=10
            while i>=1:
                print(i)
                i=i-1
            
        3) 무한반복을 멈추게 하거나, 특정 상황에서 반복문 멈추게 하기
            i=1
            while True:
                print(i)
                if i == 4:
                    break
                i=i+1         
            
        4) 특정 조건에 해당하면 다시 반복문 처음으로 돌아가게하기
            ** 주의 while문에서 적용할 때는 i의 증감 연산자가 continue보다 먼저 오지 않으면, 반복문이 계속 돌게된다. 
            i = 1
            while i<10:
                i=i+1
                if i % 2 == 0:
                    continue
                print(i)
            
            => 결과 : 3, 5, 7, 9
            
            
        
        [ 반복문을 이용한 문제풀이 ]
        ==========================
        1) 1부터 N까지 홀수 출력하기
            input() :  값을 입력 받는다. ** 타입은 문자가 되므로 연산을 하고싶다면, int형으로 바꿔주어야함.
            
            n=int(input()) 
            for i in range(1, n+1):
                if i%2==1:
                    print(i)
                
        2) 1부터 N까지의 합 구하기
        
            sum=0
            n=int(input()) 
            for i in range(1, n+1):
                sum=sum+i
            print(sum)
        
        3) N의 약수 출력하기// 약수 : 1 부터 나 자신의 수까지, 나 자신과 나눠서 0이 되는 어떤 수 .
        
        n=int(input()) 
        for i in range(1,n+1):
            if n%i==0:
                print(i, end=' ')
        => 1 2 3 6 7 14 21 42
        
       
        
        [ 중첩 반복묵(2중 for 문) ]
        ============================
        for i in range(5):
            for j in range(5):
                print('*', end=' ')
            print()                                                                                
        
        * * * * *
        * * * * *
        * * * * *
        * * * * *
        * * * * *
        
        for i in range(5):
            for j in range(i+1):
                print('*', end=' ')
            print()    
                        
        *
        * *
        * * *
        * * * *
        * * * * *
        
        for i in range(5):
            for j in range(5-i):
                print('*', end=' ')
            print()        
            
        * * * * *
        * * * *
        * * *
        * *
        *      
        
        
        [ 문자열과 내장함수 ]
        ================================
           
        1) upper()  : 문자열 모두 대문자 전환 
            msg = "It is Time"
            print(msg.upper())      
            => IT IS TIME   
        2) lower()  :  문자열 모두 소문자 전환
            msg = "It is Time"
            print(msg.lower())   
            => it is time   
        3) find('T') : 처음 발견되는 T의 인덱스 번호
            msg = "It is Time"
            print(msg.find('T'))  
            => 6 
        4) count('T') : T의 갯수
            msg = "It is Time"
            print(msg.count('T'))  
            => 1
        5) [:2] : 0~1인덱스까지의 문자열 추출
            msg = "It is Time"
            print(msg[:2])  
            => It
        6) [3:5] : 3~4덱스까지의 문자열 추출
            msg = "It is Time"
            print(msg[3:5])  
            => is
        7) len(msg) : 문자열의 길이(공백 포함)    
            msg = "It is Time"
            for i in range(len(msg)):
                print(i, end=' ')
            => 0 1 2 3 4 5 6 7 8 9
        9) 문자열 리스트의 문자 하나하나 반환
        
        (방법1)
            msg = "It is Time"
            for i in range(len(msg)):
                print(msg[i], end=' ')
            print()
            =>I t   i s   T i m e
        
        (방법2)
            msg = "It is Time"
            for x in msg:
                print(x, end=' ')
            print()
            =>I t   i s   T i m e
        
        10) isupper() : 대문자면 true // 대문자만 출력
            msg = "It is Time"
            for x in msg:
                if x.isupper():
                    print(x, end=' ')    
            =>I T
        
        11) islower() : 소문자면 true // 소문자만 출력
            msg = "It is Time"
            for x in msg:
                if x.islower():
                    print(x, end=' ')    
            =>t i s i m e
            
        11) isalpha() : 공백은 X, 오직 알파벳일 때만
        msg = "It is Time"
        for x in msg:
            if x.isalpha():
                print(x, end='')    
        =>ItisTime
        
        12)  ord() : 아스키 넘버 출력(A ~ Z : 65 ~ 90, a ~ z : 97~122)
        
        tmp='AZ'
        for x in tmp:
            print(ord(x))
            
        tmp='az'
        for x in tmp:
            print(ord(x))
            
        
        13)  chr() : 아스키 넘버에 대응되는 문자 출력(A ~ Z : 65 ~ 90, a ~ z : 97~122)
        tmp=65
        print(chr(tmp))
        
        
        [리스트와 내장함수]
        ======================
        - 리스트 : 변수 하나하나를 나열하여 인덱스를 붙인 것. a1,a2,a3.. =>a[0], a[1], a[2]
        1) 빈리스트 만들기
                a = []
                print(a)
                b=list()
                print(b)       
                =>[], [] 
        
        
        2) 값이 있는 리스트 만들기 
            (1) a = [1,2,3,4,5]
            
            (2) b = list(range(1,11))
            
            (3) c=a+b
        
        
        3) a.append(6) # 리스트 멘 마지막에 값 6을 추가
            print(a)
        
        4) a.insert(3,7)# 3번 인덱스에 7을 추가, 나머지는 뒤로 밀림
            print(a)
        
        5) a.pop() # 리스트에서 마지막 값을 제거
            print(a)
        
        6) a.pop(3) # 3번 인덱스의 값을 제거
            print(a)
        
        7) a.remove(4) # 리스트에서 값 4 를 제거, 앞으로 당겨짐
            print(a)
        
        8) a.index(5) # 5라는 값이 몇번 인덱스에 있는지
            print(a.index(5))
            
            a=list(range(1,11))
        
        9) print(sum(a)) # 1~10의 모든 수의 합
        
        10) print(max(a)) # 최대값
        
        11) print(min(a)) # 최소값 
            print(min(7,5)) # 인자들 중 최소값       
            print(min(7,3,5)) # 인자들 중 최소값       
            print(max(7,5)) # 인자들 중 최대값    
        
        12) 무작위로 섞기
        
            import random as r
            
            r.shuffle(a) # 무작위로 섞기
            print(a)   
        
        13) a.sort() #오름차순
            print(a)   
        
        14) a.sort(reverse=True) # 내림차순
            print(a)   

        15) a.clear() # 빈리스트로 만들기
            print(a)   
            
        
        리스트와 내장함수(2)
        ========================
        a=[23, 12, 36, 53, 19]
        print(a[:3])
        print(a[1:4])
        
        1.  리스트 값 출력
        =====================
        방법 1)
            for i in range(len(a)):
                print(a[i], end=' ')
            print()
            =>23 12 36 53 19
        
            for x in a:
                print(x, end=' ')
            print()
            =>23 12 36 53 19
        
        방법 2)
            for x in a:
                if x%2==1:
                    print(x, end=' ')
            print()
        
        방법 3) enumerate()
            for x in enumerate(a):#(인덱스, value)의 형태로 튜플 반환
                print(x)
            =>  (0, 23)
                (1, 12)
                (2, 36)
                (3, 53)
                (4, 19)
        
            ** 튜플의 구조는 리스트와 같으나, 값을 변경할 수 없다.
                a = [23, 12, 36, 53, 19]
                a[0] = 43
                print(a)
                =>[43, 12, 36, 53, 19]
                
                a = (23, 12, 36, 53, 19)
                a[0] = 43
                =>TypeError: 'tuple' object does not support item assignment
            
        방법 4) x[0], x[1]
            for x in enumerate(a):
                print(x[0], x[1]) # x=(인덱스, value)이므로 x[0]은 인덱스 , x[1]은 값 
            =>
            0 23
            1 12
            2 36
            3 53
            4 19
        
        방법 5) 가장 많이 쓰는 enumerate 사용
            for index, value in enumerate(a):
                print(index, value)
            print()
            =>
            0 23
            1 12
            2 36
            3 53
            4 19
        
        방법 6) 가장 많이 쓰는 enumerate 사용
            if all(60>x for x in a): # 모두 충족하면 참
                print("YES")
            else:
                print("NO")

            if any(15>x for x in a): # 한가지라도 충족하면 참
                print("YES")
            else:                    # 모두가 충족안할때, 거짓
                print("NO")
            
        
        
        [2차원 리스트 생성과 접근]
        =========================
        a = [0] * 10 # 인덱스 번호가 0~9까지인 크기가 10인 일차원 리스트    
        a = [0] * 3 # 인덱스 번호가 0~2까지인 크기가 3인 일차원 리스트
        
        1)  for _ in range(3) // _를 하면 변수없이 반복문이 3번 돈다.
            a=[[0]*3 for _ in range(3)] # [0]*3 가 3번 반복됨.    
            print(a)
            =>[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            열       
            행    0  1  2
            0 [0, 0, 0]
            1 [0, 0, 0]
            2 [0, 0, 0]
            
            열       
            행    0  1  2
            0 [0, 1, 0]
            1 [0, 2, 0]
            2 [0, 0, 0]
            
            a=[[0]*3 for _ in range(3)] # [0]*3 가 3번 반복됨.    
            a[0][1]=1
            a[1][1]=2
            print(a)
            =>[[0, 1, 0], [0, 2, 0], [0, 0, 0]]
            
        
        2) 2차원 리스트 표로 출력하기
            for x in a:
                print(x)
            =>
            [0, 1, 0]
            [0, 2, 0]
            [0, 0, 0]
            
        
        3) 대괄호없이 2차원 리스트 출력하기
            a=[[0]*3 for _ in range(3)] # [0]*3 가 3번 반복됨.    
            for x in a:
                for y in x:
                    print(y, end=' ')
                print()
            =>
            0 0 0   
            0 0 0
            0 0 0    
            
        
        
        [함수 만들기]
        =================
        # 함수는 값을 return 하며, 함수를 종료 한다.
            def add(a,b):
                c=a+b
                return c
            print(add(3,2))
            =>5
        # 파이썬에서는 2개이상의 값을 튜플로 반환할 수 있다.
            def add(a,b):
                c=a+b
                d=a-b
                return c, d
            print(add(3,2))
            =>(5, 1)
        
        # 소수(나누어 떨어지지 않는 수 )만 출력하는 함수 만들기(1~자기자신까지의 수중 1,과 자기자신을 제외하고 나누어서 떨어지지 않는 수)
            def isPrime(x):
                for i in range(2,x):
                    if x%i==0:
                        return False # 여기서 함수가 종료됨.
                return True


        a=[12, 13, 7, 9, 19]
        for y in a:
            if isPrime(y):
                print(y, end=' ')
        
        
            
        [람다함수]
        ====================
        - 람다함수 : 익명의 함수 또는 표현식
        
        def plus_one(x):
            return x+1
        print(plus_one(1))
        =>2
        
        # 람다함수(익명의 함수)로 표현하기(변수에 담아서 호출해주어야함)
        plus_two=lambda x: x+2
        print(plus_two(1))
        =>3
        
        
        * map(함수, 함수를 적용할 자료)
            a=[1,2,3]
            print(list(map(plus_one, a)))
            =>[2, 3, 4]
        
        * 함수 이름이 필요없이 익명의 함수를 사용하여 바로 사용할수있음.
            print(list(map(lambda x: x+1, a))) 
            =>[2, 3, 4]
        
            
        [선형 탐색, x의 위치 찾기]
        ====================
            L = [3,8,2,7,6,10,9]
            x = 6
            def linear_search(S, x):
                i=0
                while i<len(L) and L[i] != x:
                    i+=1
                if i < len(L):
                    return i
                else:
                    return -1    
                
            def linear_search(S, x):
                return S.index(x)
        
        
        [재귀 알고리즘]
        =============== 
        1) 잘못된 예시 -  종결 조건이 없음   
            def sum1(n):
                print(n)
                return n + sum1(n -1) # 자신을 재귀호출하고있음.
            # a = int (input("Number:"))
            # print(sum(a))
            Number:30
            30
            29
            28
            27
            26
            25
            24
            23
            22
            21
            -995..
            ..... 에러가 남....
            
            def sum2(n):
                print(n)
                if n<= 1:
                    return n
                else:
                    return n+ sum2(n-1)
            n=10일때 콘솔에 찍히는 결과 
            10
            9
            8
            7
            6
            5
            4
            3
            2
            1
            
            sum2(10) = 55
            a = int(input("Number:"))
            print(sum2(a))
            
        '''
        return JsonResponse({"MESSAGE": "Hello"}, status=200)
# 2. 선형 배열 알고리즘 풀이
class ProgrammersExample2View(View):
    def get(self, request):
        '''(02) 정렬된 리스트에 원소 삽입
        리스트 L 과 정수 x 가 인자로 주어질 때, 리스트 내의 올바른 위치에 x 를 삽입하여 그 결과 리스트를 반환하는 함수 solution 을 완성하세요.

        인자로 주어지는 리스트 L 은 정수 원소들로 이루어져 있으며 크기에 따라 (오름차순으로) 정렬되어 있다고 가정합니다.

        예를 들어, L = [20, 37, 58, 72, 91] 이고 x = 65 인 경우, 올바른 리턴 값은 [20, 37, 58, 65, 72, 91] 입니다.

        힌트: 순환문을 이용하여 올바른 위치를 결정하고 insert() 메서드를 이용하여 삽입하는 것이 한 가지 방법입니다.

        주의: 리스트 내에 존재하는 모든 원소들보다 작거나 모든 원소들보다 큰 정수가 주어지는 경우에 대해서도 올바르게 처리해야 합니다.
        '''
        x = 65
    
        L = [20, 37, 58, 72, 91]
        
        def solution1(L, x): # 풀이 실패 -> 시간 초과 및 반복문 멈추는 것 고려하지 않음
            answer = []
            for y in L:
                if x > y:
                    if L.index(y) != len(L)-1:
                        L.insert(L.index(y)+1,x)
                    else: L.append(x)
                elif x < y:
                    if L.index(y) == 0:
                        L.insert(0,x)
                    else:
                        L.insert(L.index(y)-1,x)
                        
            answer = L        
            return answer
        
        def solution2(L, x): # 풀이 실패 -> enumerate를 사용하였으나, 역시 시간 초과 및 반복문을 멈추는 것을 고려하지 않음.
            answer = []
            for index, value in enumerate(L) :
                if x > value:
                    if index != len(L)-1:
                        L.insert(index+1,x)
                    else: L.append(x)
                elif x < value:
                    if index == 0:
                        L.insert(0,x)
                    else:
                        L.insert(index,x)
            answer = L        
            return answer
        
        def solution3(L, x): # PASS!!!
            # 반복문이 계속 도는 것이 문제였으며, 이로인해 시간이 초과되는 것을 깨달음. 이를 잡아주니 풀이 성공!!!!! 
            for index, value in enumerate(L) :
                if x > value:
                    if index == len(L)-1:
                        L.append(x)
                        break
                    else:
                        continue
                else: 
                    L.insert(index,x)
                    break
            return L 
        
        def solution4(L, x): # 나와 비슷한 풀이
            for idx, num in enumerate(L):
                if num > x:
                    L.insert(idx,x)
                    break

                if L[-1] < x: # L[-1]은 리스트 맨 끝에 있는 수를 지칭 한다!!, 맨 끝자리이면서, x가 값이 크다는 것을 모두 충족함.
                    L.append(x)
                else:
                    pass
            return L
        
        def solution5(L, x): # 오름차순이라는 문제의 함정을 이용한 문제 풀이
            L.append(x)
            L.sort()
            return L

        return JsonResponse({"RESULT": solution3(L,x)}, status=200)

    def post(self, request):
        
        '''
        문제 설명
        인자로 주어지는 리스트 L 내에서, 또한 인자로 주어지는 원소 x 가 발견되는 모든 인덱스를 구하여 
        이 인덱스들로 이루어진 리스트를 반환하는 함수 solution 을 완성하세요.

        리스트 L 은 정수들로 이루어져 있고 그 순서는 임의로 부여되어 있다고 가정하며, 동일한 원소가 반복하여 들어 있을 수 있습니다. 
        이 안에 정수 x 가 존재하면 그것들을 모두 발견하여 해당 인덱스들을 리스트로 만들어 반환하고, 
        만약 존재하지 않으면 하나의 원소로 이루어진 리스트 [-1] 를 반환하는 함수를 완성하세요.

        예를 들어, L = [64, 72, 83, 72, 54] 이고 x = 72 인 경우의 올바른 리턴 값은 [1, 3] 입니다.
        또 다른 예를 들어, L = [64, 72, 83, 72, 54] 이고 x = 83 인 경우의 올바른 리턴 값은 [2] 입니다.
        마지막으로 또 다른 예를 들어, L = [64, 72, 83, 72, 54] 이고 x = 49 인 경우의 올바른 리턴 값은 [-1] 입니다.

        힌트 1: 리스트의 index() 메서드와 리스트 슬라이싱을 활용하는 것이 한 가지 방법이 됩니다. 리스트 슬라이싱은 아래와 같이 동작합니다.

        L = [6, 2, 8, 7, 3] 인 경우
        L[1:3] = [2, 8]
        L[2:] = [8, 7, 3]
        L[:3] = [6, 2, 8]

        힌트 2: 리스트의 index() 메서드는, 인자로 주어지는 원소가 리스트 내에 존재하지 않을 때 ValueError 를 일으킵니다. 
        이것을 try ... except 로 처리해도 되고, "if x in L" 과 같은 조건문으로 특정 원소가 리스트 내에 존재하는지를 판단해도 됩니다.
        '''
        x= 72
        L= [64, 72, 83, 72, 54]
        def solution1(L,x): # 나의 풀이 ) PASS!!
            answer =[]
            validate=True
            for indx, num in enumerate(L):
                if x == num:
                    answer.append(indx)
                    validate=False
            if validate:
                answer=[-1]   
            return answer
        
        def solution2(L, x): # 다른 풀이 : 리스트 컴프리헨션으로 깔끔하게!
            if x in L:
                return [i for i, y in enumerate(L) if y == x] # 조건문이 만족 할 떄, i를 리스트에 담는다.
            else:
                return [-1]
            
        
        
        return JsonResponse({"RESULT": solution1(L,x)}, status=200)
    
  
# 3. 정렬, 탐색 알고리즘 풀이
class ProgrammersExample3View(View):
    
    def get (self, request):
        '''
        (03) 이진탐색
        
        문제 설명
        리스트 L 과, 그 안에서 찾으려 하는 원소 x 가 인자로 주어질 때, 
        x 와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution() 을 완성하세요. 
        만약 리스트 L 안에 x 와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1 을 리턴합니다. 
        리스트 L 은 자연수 원소들로 이루어져 있으며, 크기 순으로 정렬되어 있다고 가정합니다. 
        또한, 동일한 원소는 두 번 이상 나타나지 않습니다.

        예를 들어,
        L = [2, 3, 5, 6, 9, 11, 15]
        x = 6
        의 인자들이 주어지면, L[3] == 6 이므로 3 을 리턴해야 합니다.

        또 다른 예로,
        L = [2, 5, 7, 9, 11]
        x = 4
        로 주어지면, 리스트 L 내에 4 의 원소가 존재하지 않으므로 -1 을 리턴해야 합니다.

        이 연습문제에서는 알고리즘의 효율성도 평가합니다. 만약 순차 (선형) 탐색 알고리즘을 구현하는 경우에는
        제한 시간 요구사항을 만족하지 못하여 효율성 테스트 케이스들을 통과하지 못할 수도 있습니다.

        '''
        L = [2, 3, 5, 6, 9, 11, 15]
        #L = [] 
        x = 15
        #x = 20
        
        def solution1(L, x):
            indx = -1 
            if len(L) == 0:
                return indx

            lower=0
            upper=len(L)-1
            tmp =[]
            
            while lower <= upper:
                middle=(lower+upper)//2
               
                if x > L[middle]:
                    lower=middle+1
                elif x < L[middle]:
                    upper=middle-1
                elif x == L[middle]:
                    indx = middle
                    return indx
                tmp = L[lower:upper+1] # 뭔가 이 과정에서 시간을 많이 잡아 먹는 다는 생각이 들었고, 최종 lower와 upper 만을 사용하여 , tmp 리스트를 구하면 될것같았다.
            
            if x not in tmp:
                return indx
                    
                #L=L[lower:upper+1] # L를 슬라이싱 해버리면, 인덱스가 0부터 시작하므로 IndexError: list index out of range가 계속 뜬다는 점 유의!!!
            return indx
        
              
        def solution2(L, x): # PASS!!!! 
            # [1] 빈 리스트가 들어올 때와 [2] 리스트에 없는 값이 들어올 때의 예외 처리에 유의 하여야겠다.
            '''
            정확성: 55.6
            효율성: 44.4
            합계: 100.0 / 100.0
            '''
            indx = -1 
            lower=0
            upper=len(L)-1
            
            if len(L) == 0:
                return indx

            while lower <= upper:
                middle=(lower+upper)//2
               
                if x > L[middle]:
                    lower=middle+1
                elif x < L[middle]:
                    upper=middle-1
                elif x == L[middle]:
                    indx = middle
                    return indx
            
            if x not in L[lower:upper+1]:
                return indx
        
        def solution3(L, x): # PASS!!!! 
            # -1의 중복을 줄어 효율성을 높여보자.
            '''
            정확성: 55.6
            효율성: 44.4
            합계: 100.0 / 100.0
            '''
            lower=0
            upper=len(L)-1

            while lower <= upper:
                middle=(lower+upper)//2
               
                if x > L[middle]:
                    lower=middle+1
                elif x < L[middle]:
                    upper=middle-1
                else:
                    return middle
            return -1
                    
        return JsonResponse({"RESULT": solution3(L,x)}, status=200)
    
class ProgrammersExample4View(View):
    
    def get (self, request):
    
        '''
        (04) 피보나치 순열
        문제 설명
        인자로 0 또는 양의 정수인 x 가 주어질 때, 
        Fibonacci 순열의 해당 값을 구하여 반환하는 함수 solution() 을 완성하세요.

        Fibonacci 순열은 아래와 같이 정의됩니다.
        F0 = 0
        F1 = 1
        Fn = Fn - 1 + Fn - 2, n >= 2

        재귀함수 작성 연습을 의도한 것이므로,
        재귀적 방법으로도 프로그래밍해 보고, 반복적 방법으로도 프로그래밍해 보시기 바랍니다.
        '''
        n=int(input("Number"))
        
        # 1) 재귀함수로 풀기
        def solution1_F(n):
            if n <=1:
                return n
            else:
                return solution1_F(n-1) + solution1_F(n-2)   
        
        def solution2_F(x):
            return n if n <=1 else solution2_F(n-1) + solution2_F(n-2) 
        
        # 2) 반복함수로 풀기 난이도 ⭐️⭐️⭐️⭐️⭐️
        def solution3_F(n):
            answer=0 # n=3
            fa = 0
            fb = 1
            # if n == 0: return 0 //  answer가 0으로 초기화 되어있으므로 안써줘도 상관없음. 
            while n>0:
                n-=1
                fa, fb = fb(1), fa+fb(0+1) # 값변경 사용
                answer = fa
            return answer       
         
        return  JsonResponse({"RESULT": solution2_F(n)}, status=200)
    
class ProgrammersExample5View(View):
    '''
    # (05) 재귀적 이진탐색

    문제 설명

    리스트 L 과, 그 안에서 찾으려 하는 원소 x 가 인자로 주어지고, 
    
    또한 탐색의 대상이 되는 리스트 내에서의 범위 인덱스가 l 부터 u 까지로 (인자로) 정해질 때, 
    
    x 와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution() 을 완성하세요. 
    
    만약 리스트 L 안에 x 와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1 을 리턴합니다. 
    
    리스트 L 은 자연수 원소들로 이루어져 있으며, 크기 순으로 정렬되어 있다고 가정합니다. 또한, 동일한 원소는 두 번 이상 나타나지 않습니다.

    인덱스 범위를 나타내는 l 과 u 가 인자로 주어지는 이유는, 이 함수를 재귀적인 방법으로 구현하기 위함입니다. 
    
    빈 칸에 알맞은 내용을 채워서 재귀 함수인 solution() 을 완성하세요.

    예를 들어,L = [2, 3, 5, 6, 9, 11, 15]x = 6l = 0u = 6의 인자들이 주어지면, L[3] == 6 이므로 3 을 리턴해야 합니다.

    또 다른 예로,L = [2, 5, 7, 9, 11]x = 4l = 0u = 4로 주어지면, 리스트 L 내에 4 의 원소가 존재하지 않으므로 -1 을 리턴해야 합니다.
    '''
    def get (self, request):
        '''
        정확성: 55.6
        효율성: 0.0
        합계: 55.6 / 100.0
        '''
        L = [2, 5, 7, 9, 11]
        x = 4
        l = 0
        u = 4
        def solution1(L, x, l, u):
            if "x not in L":
                return -1
            mid = (l + u) // 2
            if x == L[mid]:
                return mid
            elif x < L[mid]:
                return "solution1(L, x, l, mid-1)" 
            else:
                return "solution1(L, x, mid+1, u)"
        
        
        def solution2(L, x, l, u):
            '''
            난이도 ⭐️⭐️⭐️⭐️⭐️ 효율성 생각하기!!!
            채점 결과
            정확성: 55.6
            ⭐️ 효율성: 44.4  
            합계: 100.0 / 100.0
            '''
            if "l>u":  # ⭐️ x가 리스트 L에 없다면,  
                        #x=10 L=[11,15]일때, lower는 0, mid=0.5, upper=1로 까지 가게 되므로, u=-0.5, l=1.5가 된다. => 뒤바뀜. 
                        #x=16 L=[11,15]일때, lower는 0, mid=0.5, upper=1로 까지 가게 되므로, u=1, l=1.5가 된다. => 뒤바뀜. 
                return -1
            mid = (l + u) // 2
            if x == L[mid]:
                return mid
            elif x < L[mid]:
                return "solution2(L, x, l, mid-1)" 
            else:
                return "solution2(L, x, mid+1, u)"
        
        return  JsonResponse({"RESULT": solution2(L, x, l, u)}, status=200)

class ProgrammersExample7View(View):
    '''
    (07) 연결 리스트 순회
    문제 설명
    제 7 강에서 소개된 추상적 자료구조로 LinkedList 라는 이름의 클래스가 정의되어 있다고 가정하고, 이 리스트를 처음부터 끝까지 순회하는 메서드 traverse() 를 완성하세요.

    메서드 traverse() 는 리스트를 리턴하되, 이 리스트에는 연결 리스트의 노드들에 들어 있는 데이터 아이템들을 연결 리스트에서의 순서와 같도록 포함합니다. 예를 들어, LinkedList L 에 들어 있는 노드들이 43 -> 85 -> 62 라면, 올바른 리턴 값은 [43, 85, 62] 입니다.

    이 규칙을 적용하면, 빈 연결 리스트에 대한 순회 결과로 traverse() 메서드가 리턴해야 할 올바른 결과는 [] 입니다.

    [참고] "실행" 을 눌렀을 때 통과하는 것은 아무 의미 없습니다. 
    '''
    def get (self, request):
        class Node:
            def __init__(self, item):
                self.data = item
                self.next = None

        class LinkedList:
            def __init__(self):
                self.nodeCount = 0
                self.head = None
                self.tail = None

            def getAt(self, pos):
                if pos < 1 or pos > self.nodeCount:
                    return None
                i = 1
                curr = self.head
                while i < pos:
                    curr = curr.next
                    i += 1
                return curr

            def traverse(self):
                answer=[]
                a = self.head
                while a != None:            # 빈 리스트라면 head와 tail이 None
                    answer.append(a.data) 
                                            # 빈 리스트가 아니라면 헤더가 존재하므로 추가, 
                                            # a는 노드의 순서만 의미하므로, 노드이 데이터에 접근하려면 a.data를 해주어야함. 
                    a = a.next              # 헤드의 다음 연결 노드로 접근
                return answer

            def solution(x):
                return 0
        
        return  JsonResponse({"RESULT": []}, status=200)
 
class ProgrammersExample8View(View):
    '''
    문제 설명
    제 8 강에서 소개된 추상적 자료구조 LinkedList 클래스의 메서드로서 popAt() 메서드를 강의 내용에 소개된
    요구조건을 만족시키도록 구현하세요.

    초기 코드로 들어 있는 것은 solution() 함수를 포함하여 다른 부분은 수정하지 말고, 
    def popAt(self, pos): 의 메서드 몸체만 구현하세요.

    만약, 인자로 주어진 pos 가 올바른 범위의 값을 가지지 않는 경우에는 IndexError exception 을 발생시키도록 합니다. 
    이렇게 하기 위한 코드는 raise IndexError 입니다.
'''
    def get (self, request):
        class Node:
            
            def __init__(self, item):
                self.data = item
                self.next = None


        class LinkedList:

            def __init__(self):
                self.nodeCount = 0
                self.head = None
                self.tail = None


            def getAt(self, pos):
                if pos < 1 or pos > self.nodeCount:
                    return None

                i = 1
                curr = self.head
                while i < pos:
                    curr = curr.next
                    i += 1

                return curr


            def insertAt(self, pos, newNode):
                if pos < 1 or pos > self.nodeCount + 1:
                    return False

                if pos == 1:
                    newNode.next = self.head
                    self.head = newNode

                else:
                    if pos == self.nodeCount + 1:
                        prev = self.tail
                    else:
                        prev = self.getAt(pos - 1)
                        newNode.next = prev.next
                        prev.next = newNode

                if pos == self.nodeCount + 1:
                    self.tail = newNode

                self.nodeCount += 1
                return True

            # 1차 작성 코드
            def popAt_1(self, pos):
                #인덱스 벗어났을 때,
                if pos < 1 or pos > self.nodeCount: 
                    raise IndexError
                '''
                1) head를 없애는 경우, pos == 1
                2) tail을 없애는 경우, pos == nodeCount
                3) nodeCount ==1, pos ==1,  유일한 노드를 없애는 경우 + 2) tail을 없애는 경우, pos == nodeCount
                4) nodeCount > 1 1<post<nodeCount
                '''
                
                if pos == self.nodeCount: # tail의 노드를 없앨 경우  + 빈리스트
                    prev = self.getAt(pos-1)
                    curr = self.tail
                    self.tail = prev

                if pos == 1: # head의 노드를 없앨 경우 +  빈리스트
                    curr = self.head
                    self.head = curr.next
                else:
                    prev = self.getAt(pos-1)
                    if pos == self.nodeCount:
                        curr = self.tail
                        self.tail = prev
                    else:
                        curr = prev.next
                        prev.next = curr.next
                        
                    if self.nodeCount == 1:

                        curr = self.head

                self.nodeCount -=1

                return curr.data
            
            # 2차 작성 코드
            def popAt_2(self, pos):
                '''
                테스트 1 〉	통과 (0.05ms, 16.8MB)
                테스트 2 〉	통과 (0.06ms, 16.6MB)
                테스트 3 〉	통과 (0.04ms, 16.6MB)
                테스트 4 〉	통과 (0.08ms, 16.7MB)
                채점 결과
                정확성: 100.0
                합계: 100.0 / 100.0
                '''
                if pos < 1 or pos > self.nodeCount :
                    raise IndexError
                
                # head 제거
                if pos == 1:
                    # 유일한 원소 head + tail 제거  
                    if self.nodeCount == 1:
                        curr = self.tail
                        self.head = None
                        self.tail = None # ⭐️ tail도, head도 None
                    # 여러원소 중 head 제거  
                    else:
                        curr = self.head
                        self.head = curr.next
                        curr.next = None # ⭐️ 잘라낸 curr의 next는 끊겨있으므로 None!
                else : 
                    # tail 제거
                    if pos == self.nodeCount:
                        prev = self.getAt(pos-1)
                        self.tail = prev
                        curr = prev.next
                        prev.next = None  # ⭐️ prev가 꼬리가 되므로 prev.next는 None
                        curr.next = None 
                    # head와 tail사이의 원소 제거
                    else:
                        prev = self.getAt(pos-1)
                        curr = prev.next
                        prev.next = curr.next
                        curr.next = None
                
                self.nodeCount -= 1
                return curr.data 


            def traverse(self):
                result = []
                curr = self.head
                while curr is not None:
                    result.append(curr.data)
                    curr = curr.next
                return result

            def solution(x):
                return 0
    
        return  JsonResponse({"RESULT": []}, status=200)
    
class ProgrammersExample9View(View):
    '''
    (09) dummy head 를 가지는 연결 리스트 노드 삭제
    문제 설명
    제 9 강에서 소개된 추상적 자료구조 LinkedList 는 dummy head node 를 가지는 연결 리스트입니다.
    이 클래스의 아래와 같은 메서드들을, 강의 내용에 소개된 요구조건을 만족시키도록 구현하세요.

    popAfter()
    popAt()
    이 때, popAt() 메서드의 구현에서는 popAfter() 를 호출하여 이용하도록 합니다. 
    (그렇게 하지 않을 수도 있지만, 여기에서는 popAfter() 의 이용에 의해서 코드 구현이 보다 쉬워지는 것을 확인하기 위함입니다.)

    초기 코드로 들어 있는 것은 solution() 함수를 포함하여 다른 부분은 수정하지 말고, 
    def popAfter(self, prev): 와 def popAt(self, pos): 의 메서드 몸체만 구현하세요.

    만약, popAt() 메서드에 인자로 주어진 pos 가 올바른 범위의 값을 가지지 않는 경우에는 
    IndexError exception 을 발생시키도록 합니다. 이렇게 하기 위한 코드는 raise IndexError 입니다.
    '''
    def get (self, request):
        class Node:
            
            def __init__(self, item):
                self.data = item
                self.next = None


        class LinkedList:

            def __init__(self):
                self.nodeCount = 0         # ⭐️ nodeCount는 dumyNode를 제외함.
                self.head = Node(None) 
                self.tail = None           # ⭐️ 노드 삭제시  tail None이어야함. 
                self.head.next = self.tail # ⭐️ head와 tail의 연결관계 생성


            def traverse(self):
                result = []
                curr = self.head
                while curr.next:
                    curr = curr.next
                    result.append(curr.data)
                return result


            def getAt(self, pos):
                if pos < 0 or pos > self.nodeCount:
                    return None

                i = 0
                curr = self.head
                while i < pos:
                    curr = curr.next
                    i += 1

                return curr


            def insertAfter(self, prev, newNode):
                newNode.next = prev.next
                if prev.next is None:
                    self.tail = newNode
                prev.next = newNode
                self.nodeCount += 1
                return True


            def insertAt(self, pos, newNode):
                if pos < 1 or pos > self.nodeCount + 1:
                    return False

                if pos != 1 and pos == self.nodeCount + 1:
                    prev = self.tail
                else:
                    prev = self.getAt(pos - 1)
                return self.insertAfter(prev, newNode)

            
            '''
            테스트 1 〉	통과 (0.06ms, 16.6MB)
            테스트 2 〉	통과 (0.05ms, 16.6MB)
            테스트 3 〉	통과 (0.05ms, 16.8MB)
            테스트 4 〉	통과 (0.06ms, 16.6MB)
            테스트 5 〉	실패 (0.15ms, 16.7MB)
            '''
            # 초기 나의 풀이
            def popAfter_1(self, prev):
                # prev가 끝일때,
                if prev.next is None:
                    return None
                curr = prev.next
                # post가 1일때,
                if prev == self.head:#******
                    prev.next = curr.next
                    if curr.next is None:
                        prev.next = None
                        self.tail = prev
                elif curr.next is None: # pos가 끝일때
                    prev.next = None
                    self.tail = prev
                else:# 중간
                    prev.next = curr.next
                curr.next = None
                self.nodeCount -=1
                return curr.data


            def popAt_1(self, pos):
                if pos < 1 and pos >= self.nodeCount:
                    raise IndexError
                # pos == 1

                if pos == 1:
                    prev = self.head
            # 1<pos<nodeCount
                else:
                    prev = self.getAt(pos-1)
                return self.popAfter(prev)
            
            
            '''
            테스트 1 〉	통과 (0.05ms, 16.6MB)
            테스트 2 〉	통과 (0.07ms, 16.7MB)
            테스트 3 〉	통과 (0.05ms, 16.5MB)
            테스트 4 〉	통과 (0.07ms, 16.6MB)
            테스트 5 〉	통과 (0.05ms, 16.6MB)
            '''
            # 진화된 나의 풀이 - # ⭐️ ⭐️  dummy head 를 가지는 연결 리스트에서는 pos가 끝일 때만 유의하면됨.
            def popAfter_2(self, prev):
                # 빈 리스트 일때, count=0
                if prev.next is None:
                    return None
                curr = prev.next
                    
                if curr.next == None:    # 👈 pos가 끝자리 일때 유의
                    if self.nodeCount == 1:
                        self.tail = None
                    else:
                        self.tail = prev
                prev.next = curr.next
                curr.next = None
                self.nodeCount -=1
                return curr.data


            def popAt_2(self, pos):
                if pos < 1 or pos > self.nodeCount: # ⭐️ or 주의 하기 ,  nodeCount는 dumyNode를 제외
                    raise IndexError
                prev = self.getAt(pos-1)
                return self.popAfter_2(prev)    
            
            def solution(x):
                return 0
    
        return  JsonResponse({"RESULT": []}, status=200)
    
    
    
class ProgrammersExample10_1View(View):
    
    '''
    (10-1) 양방향 연결 리스트 역방향 순회
    문제 설명
    제 10 강에서 소개된 추상적 자료구조 DoublyLinkedList 에 대하여, 또한 강의 내용에서 언급한 reverse() 메서드를 구현하세요.

    이 reverse() 메서드는 양방향 연결 리스트를 끝에서부터 시작해서 맨 앞에 도달할 때까지 (tail 방향에서 head 방향으로) 순회하면서, 
    방문하게 되는 node 에 들어 있는 data item 을 순회 순서에 따라 리스트에 담아 리턴합니다.

    예를 들어, DoublyLinkedList L 에 들어 있는 노드들이 43 -> 85 -> 62 라면, 올바른 리턴 값은 [62, 85, 43] 입니다.

    이 규칙을 적용하면, 빈 연결 리스트에 대한 역방향 순회 결과로 reverse() 메서드라 리턴해야 할 올바른 결과는 [] 입니다.

    '''    
    def get(self,request):
        
        '''
        테스트 1 〉	통과 (0.04ms, 16.6MB)
        테스트 2 〉	통과 (0.04ms, 16.6MB)
        '''
        
        class Node:
            
            def __init__(self, item):
                self.data = item
                self.prev = None
                self.next = None


        class DoublyLinkedList:

            def __init__(self):
                self.nodeCount = 0
                self.head = Node(None)
                self.tail = Node(None)
                self.head.prev = None
                self.head.next = self.tail
                self.tail.prev = self.head
                self.tail.next = None

            # 나의 풀이
            def reverse(self):
                result = []
                
                curr = self.tail
                while curr.prev.prev !=None:            
                    curr = curr.prev
                    result.append(curr.data)
                    
                return result


            def getAt(self, pos):
                if pos < 0 or pos > self.nodeCount:
                    return None

                if pos > self.nodeCount // 2:
                    i = 0
                    curr = self.tail
                    while i < self.nodeCount - pos + 1:
                        curr = curr.prev
                        i += 1
                else:
                    i = 0
                    curr = self.head
                    while i < pos:
                        curr = curr.next
                        i += 1

                return curr


            def insertAfter(self, prev, newNode):
                next = prev.next
                newNode.prev = prev
                newNode.next = next
                prev.next = newNode
                next.prev = newNode
                self.nodeCount += 1
                return True


            def insertAt(self, pos, newNode):
                if pos < 1 or pos > self.nodeCount + 1:
                    return False

                prev = self.getAt(pos - 1)
                return self.insertAfter(prev, newNode)


        def solution(x):
            return 0
        
        return  JsonResponse({"RESULT": self.reverse(self)}, status=200)
    
class ProgrammersExample10_2View(View):
    
    '''
    (10-2) 양방향 연결 리스트 노드 삽입
    문제 설명
    제 10 강에서 소개된 추상적 자료구조 DoublyLinkedList 의 메서드로 insertBefore() 를 구현하세요.

    이 insertBefore() 메서드에는 두 개의 인자가 주어지는데, next 는 어느 node 의 앞에 새로운 node 를 삽입할지를 지정하고, 
    newNode 는 삽입할 새로운 node 입니다.

    강의 내용에서 소개된 insertAfter() 메서드의 구현과 매우 유사하게 할 수 있습니다.
    '''    
    def get(self,request):
        '''
        테스트 1 〉	통과 (0.06ms, 16.8MB)

        '''
        
        class Node:
        
            def __init__(self, item):
                self.data = item
                self.prev = None
                self.next = None

        class DoublyLinkedList:

            def __init__(self):
                self.nodeCount = 0
                self.head = Node(None)
                self.tail = Node(None)
                self.head.prev = None
                self.head.next = self.tail
                self.tail.prev = self.head
                self.tail.next = None

            def traverse(self):
                result = []
                curr = self.head
                while curr.next.next:
                    curr = curr.next
                    result.append(curr.data)
                return result

            #나의 풀이
            def insertBefore(self, next, newNode):
                # if next == self.head:
                #     return False
                prevNode = next.prev
                nextNode = next
                nextNode.prev  = newNode
                prevNode.next = newNode   
                newNode.next  = nextNode
                newNode.prev  = prevNode 
                self.nodeCount +=1
                return True

            def solution(x):
                return 0
        
        return JsonResponse({"RESULT": self.insertBefore(self,1)}, status=200)
        
class ProgrammersExample10_3View(View):
    
    '''
    (10-3) 양방향 연결 리스트 노드 삭제
    문제 설명
    제 10 강에서 소개된 추상적 자료구조 DoublyLinkedList 에 대하여 node 의 삭제 연산에 관련한 아래와 같은 메서드들을 구현하세요.

    popAfter()
    popBefore()
    popAt()
    popAfter(prev) 는 인자 prev 에 의하여 주어진 node 의 다음에 있던 node 를 삭제하고, popBefore(next) 는 인자 next 에 의하여
    주어진 node 의 이전에 있던 node 를 삭제합니다. 그리고 삭제되는 node 에 담겨 있던 data item 을 리턴합니다.

    popAt(pos) 는 인자 pos 에 의하여 지정되는 node 를 삭제하고 그 node 에 담겨 있던 data item 을 리턴하는데,
    위 popAfter() 또는 popBefore() 를 호출하여 이용하는 방식으로 구현하세요. 또한, 만약 인자 pos 가 올바른 범위 내에 있지 않은 경우에는
    raise IndexError 를 이용하여 IndexError exception 을 일으키도록 구현하세요.

    테스트 케이스 1-3 은 각각 (1) popAfter(), (2) popBefore(), (3) popAt() 메서드의 올바른 동작을 검증하는 케이스입니다.

    '''    
    def get(self,request):
        
        '''
        테스트 1 〉	통과 (0.07ms, 16.7MB)
        테스트 2 〉	통과 (0.06ms, 16.6MB)
        테스트 3 〉	통과 (0.07ms, 16.7MB)

        '''
        
        class Node:
    
            def __init__(self, item):
                self.data = item
                self.prev = None
                self.next = None


        class DoublyLinkedList:

            def __init__(self):
                self.nodeCount = 0
                self.head = Node(None)
                self.tail = Node(None)
                self.head.prev = None
                self.head.next = self.tail
                self.tail.prev = self.head
                self.tail.next = None


            def traverse(self):
                result = []
                curr = self.head
                while curr.next.next:
                    curr = curr.next
                    result.append(curr.data)
                return result


            def getAt(self, pos):
                if pos < 0 or pos > self.nodeCount:
                    return None

                if pos > self.nodeCount // 2:
                    i = 0
                    curr = self.tail
                    while i < self.nodeCount - pos + 1:
                        curr = curr.prev
                        i += 1
                else:
                    i = 0
                    curr = self.head
                    while i < pos:
                        curr = curr.next
                        i += 1

                return curr


            def insertAfter(self, prev, newNode):
                next = prev.next
                newNode.prev = prev
                newNode.next = next
                prev.next = newNode
                next.prev = newNode
                self.nodeCount += 1
                return True


            def insertAt(self, pos, newNode):
                if pos < 1 or pos > self.nodeCount + 1:
                    return False

                prev = self.getAt(pos - 1)
                return self.insertAfter(prev, newNode)

            # 나의 풀이
            def popAfter(self, prev):       
                curr = prev.next
                nextN = curr.next
                nextN.prev = prev
                prev.next = nextN
                self.nodeCount -=1        
                return curr.data  

            # 나의 풀이
            def popBefore(self, nextN):      
                curr = nextN.prev
                prev = curr.prev
                prev.next = nextN
                nextN.prev = prev
                self.nodeCount -=1
                return curr.data

            # 나의 풀이
            def popAt(self, pos):
                if pos <1 or pos>self.nodeCount:
                    raise IndexError
                prev = self.getAt(pos-1)
                return self.popAfter(prev)
        
        return  JsonResponse({"RESULT": self.popAt(self,1)}, status=200)
    
    
        
class ProgrammersExample10_4View(View):    
    '''
   (10-4) 양방향 연결 리스트의 병합
    문제 설명
    제 10 강에서 소개된 추상적 자료구조 DoublyLinkedList 에 대하여 두 개의 양방향 연결 리스트를 앞뒤로 이어 붙이는 메서드 concat() 을 구현하세요.

    예를 들어, 양방향 연결 리스트 L1 에는 1 -> 2 -> 3 의 원소가 순서대로 들어 있고, 또다른 양방향 연결 리스트 L2 에는 4 -> 5 의 순서로 원소가 들어 있을 때,
    메서드 호출 L1.concat(L2) 의 결과로 L1 은 1 -> 2 -> 3 -> 4 -> 5 의 양방향 연결 리스트가 됩니다. 물
    론, L1 또는 L2 또는 둘 다가 비어 있는 양방향 연결 리스트인 경우도 고려되도록 코드를 작성해야 합니다.
    '''
    def get(self,request):
        '''
        테스트 1 〉	통과 (0.05ms, 16.7MB)
        테스트 2 〉	통과 (0.07ms, 16.6MB)
        테스트 3 〉	통과 (0.05ms, 16.6MB)
        '''

        class Node:
            
            def __init__(self, item):
                self.data = item
                self.prev = None
                self.next = None


        class DoublyLinkedList:

            def __init__(self):
                self.nodeCount = 0
                self.head = Node(None)
                self.tail = Node(None)
                self.head.prev = None
                self.head.next = self.tail
                self.tail.prev = self.head
                self.tail.next = None

            # 나의 풀이 - 양방향 연결리스트에서는 각각의 리스트가 빈리스트일때를 고려하지 않아도 해결된다.  
            def concat(self, L):
                L1Last = self.tail.prev
                L2First = L.head.next
                L1Last.next = L2First
                L2First.prev = L1Last
                self.tail = L.tail
                L.head = self.head
                self.nodeCount +=L.nodeCount
                return self


            def traverse(self):
                result = []
                curr = self.head
                while curr.next.next:
                    curr = curr.next
                    result.append(curr.data)
                return result

            
            def getAt(self, pos):
                if pos < 0 or pos > self.nodeCount:
                    return None

                if pos > self.nodeCount // 2:
                    i = 0
                    curr = self.tail
                    while i < self.nodeCount - pos + 1:
                        curr = curr.prev
                        i += 1
                else:
                    i = 0
                    curr = self.head
                    while i < pos:
                        curr = curr.next
                        i += 1

                return curr

            def insertAfter(self, prev, newNode):
                next = prev.next
                newNode.prev = prev
                newNode.next = next
                prev.next = newNode
                next.prev = newNode
                self.nodeCount += 1
                return True


            def insertAt(self, pos, newNode):
                if pos < 1 or pos > self.nodeCount + 1:
                    return False

                prev = self.getAt(pos - 1)
                return self.insertAfter(prev, newNode)


        def solution(x):
            return 0
        
        return JsonResponse({"RESULT": self.concat(self,1)}, status=200)
        
        
class ProgrammersExample11View(View):    
    '''
    (11) 수식의 괄호 검사 (스택)
    문제 설명
    소괄호: ( )
    중괄호: /{ /}
    대괄호: [ ]
    를 포함할 수 있는 수식을 표현한 문자열 expr 이 인자로 주어질 때, 이 수식의 괄호가 올바르게 여닫혀 있는지를 판단하는 함수 solution() 을 완성하세요. 이 함수는 수식의 괄호가 유효하면 True 를, 그렇지 않으면 False 를 리턴합니다.

    스택을 활용하여 수식 내의 괄호 여닫음의 유효성을 검사하는 알고리즘에 대해서는 동영상 강의 내용을 참고하세요.
        '''
    def get(self,request):
        '''
        테스트 1 〉	통과 (0.01ms, 10.2MB)
        테스트 2 〉	통과 (0.01ms, 10.2MB)
        테스트 3 〉	통과 (0.01ms, 10.3MB)
        테스트 4 〉	통과 (0.01ms, 10.4MB)
        테스트 5 〉	통과 (0.01ms, 10.2MB)
        테스트 6 〉	통과 (0.01ms, 10.2MB)
        '''
        class ArrayStack:

            def __init__(self):
                self.data = []

            def size(self):
                return len(self.data)

            def isEmpty(self):
                return self.size() == 0

            def push(self, item):
                self.data.append(item)

            def pop(self):
                return self.data.pop()

            def peek(self):
                return self.data[-1]


        def solution(expr):
            match = {
                ')': '(',
                '}': '{',
                ']': '['
            }
            S = ArrayStack()
            for c in expr:
                if c in '({[':
                    S.push(c)

                elif c in match:
                    if S.isEmpty():
                        return False
                    else:
                        t = match[c]

                        if t != S.pop():
                            return False
            return S.isEmpty()
        
        return JsonResponse({"RESULT": solution(self.expr)}, status=200)
    
class ProgrammersExample12View(View):    
    
    '''
        (12) 중위표현 수식 --> 후위표현 수식
    문제 설명
    중위 표기법을 따르는 수식 S 가 인자로 주어질 때, 이 수식을 후위 표기법을 따르는 수식으로 변환하여 반환하는 함수 solution() 을 완성하세요.

    인자로 주어지는 수식 문자열 S 는 영문 대문자 알파벳 한 글자로 이루어지는 변수 A - Z 까지와 4칙연산을 나타내는 연산자 기호 +, -, *, /, 그리고 여는 괄호와 닫는 괄호 (, ) 로 이루어져 있으며 공백 문자는 포함하지 않는 것으로 가정합니다. 또한, 올바르게 구성되지 않은 수식은 인자로 주어지지 않는다고 가정합니다. (수식의 유효성은 검증할 필요가 없습니다.)

    문제에서 미리 주어진, 연산자의 우선순위를 표현한 python dict 인 prec 을 활용할 수 있습니다.

    또한, 스택의 기초 강의에서 이미 구현한, 배열을 이용한 스택의 추상적 자료 구조 코드가 이미 포함되어 있으므로 그대로 이용할 수 있습니다.

    (참고) 테스트 케이스를 보완하여 문제가 2019년 9월 24일에 수정되었습니다.
    (추가 참고) 테스트 케이스를 또 보완하여 문제가 2021년 7월 21일에 수정되었습니다. 추가된 테스트 케이스들은 9번부터 12번까지입니다. 관련하여 질문과 답변 (https://programmers.co.kr/questions/19360) 을 참고할 수 있습니다.
    '''
    def get(self,request):
        class ArrayStack:
    
            def __init__(self):
                self.data = []

            def size(self):
                return len(self.data)

            def isEmpty(self):
                return self.size() == 0

            def push(self, item):
                self.data.append(item)

            def pop(self):
                return self.data.pop()

            def peek(self):
                return self.data[-1]

        prec = {
            '*': 3, '/': 3,
            '+': 2, '-': 2,
            '(': 1
        }

        ## 처음 접근 방식(오답)
        def solution(S):
            opStack = ArrayStack()
            answer = ''
            
            for a in S:
                if a in prec:# 딕셔너리에 있을 때
                    opStack.push(a)
                    opStack.peek()
                elif a == ')': # 닫기 괄호를 만났을 때,
                    while not opStack.isEmpty:
                        b = opStack.pop()
                        if prec[b] > 1:
                            answer+=b
                else:# 피연산자일때
                    answer+=a
            return answer
        
        
        '''
        테스트 1
        입력값 〉	"(A+B)*(C+D)"
        기댓값 〉	"AB+CD+*"
        실행 결과 〉	테스트를 통과하였습니다.
        테스트 2
        입력값 〉	"A*B+C"
        기댓값 〉	"AB*C+"
        실행 결과 〉	테스트를 통과하였습니다.
        테스트 3
        입력값 〉	"A+B*C"
        기댓값 〉	"ABC*+"
        실행 결과 〉	테스트를 통과하였습니다.
        테스트 4
        입력값 〉	"A+B+C"
        기댓값 〉	"AB+C+"
        실행 결과 〉	테스트를 통과하였습니다.
        테스트 5
        입력값 〉	"(A+B)*C"
        기댓값 〉	"AB+C*"
        실행 결과 〉	테스트를 통과하였습니다.
        테스트 6
        입력값 〉	"A*(B+C)"
        기댓값 〉	"ABC+*"
        실행 결과 〉	테스트를 통과하였습니다.
        '''
        ## 나의 풀이
        def solution(S):
            opStack = ArrayStack()
            answer = ''
            
            for a in S:
                if a in prec:# 딕셔너리에 있을 때
                    if opStack.isEmpty():
                        opStack.push(a)
                    elif a == '(':
                        opStack.push(a)
                    elif prec[opStack.peek()] < prec[a]:
                        opStack.push(a)
                    else:
                        while not opStack.isEmpty() and prec[opStack.peek()]>=prec[a]:
                            answer += opStack.pop()
                        opStack.push(a) # 우선순위가 peek보다 낮을 때, stack의 데이터 꺼내고 새로 담아주기
                            
                elif a == ')': # 닫기 괄호를 만났을 때,
                    while not opStack.isEmpty():
                        top = opStack.peek()
                        opStack.pop()
                        if top != '(': 
                            answer+=top
                            
                else:# 피연산자일때
                    answer+=a
                    
            while not opStack.isEmpty():
                answer += opStack.pop()
                
            return answer
        
        # 다른 풀이1
        def solution(S):
            opStack = ArrayStack()
            answer = ''
            #tmp=[]

            for var in S:
                # <prec>에 있을때
                if var in prec:
                    # 비어있을때
                    if opStack.isEmpty():
                        opStack.push(var)
                    # 스택에서 이보다 높거나 같은 우선순위는 pop
                    elif var == '(':
                        opStack.push(var)
                    # 스택에서 이보다 작은 priority를 갖는다면 push
                    elif prec[opStack.peek()] < prec[var]:
                        opStack.push(var)
                    # 스택에서 이보다 큰 priority를 갖는다면 pop
                    else:
                        while not opStack.isEmpty() and prec[opStack.peek()]>=prec[var]:
                            answer += opStack.pop()
                        opStack.push(var)
                # <괄호닫기>일때
                # elif var == ')':
                #     while opStack.peek() != '(':
                #         answer += opStack.pop()
                #     opStack.pop()
                    
                elif var == ')':
                    topToken = opStack.pop()
                    while topToken != '(':
                        answer += topToken
                        topToken = opStack.pop()
                
                # <인수>일때
                else:
                    answer += var
            # 남은 인자 출력        
            while not opStack.isEmpty():
                answer += opStack.pop()
                
                
        # 다른 풀이2
        def solution(S):
            opStack = ArrayStack()
            answer = ''
            for c in S:
                if c not in "*+-/()":
                    answer += c
                if c == "(":
                    opStack.push(c)
                if c == ")":
                    while opStack.peek() != "(":
                        answer += opStack.pop()
                    opStack.pop()
                if c in "*+/-":
                    if opStack.isEmpty():
                        opStack.push(c)
                    else:
                        while prec[opStack.peek()] >= prec[c]:
                            answer += opStack.pop()
                            if opStack.isEmpty():
                                break
                        opStack.push(c)
            while not opStack.isEmpty():
                answer += opStack.pop()
            return answer
        
        return JsonResponse({"RESULT": solution("(A+B)*(C+D)")}, status=200)
    
    
class ArrayStack:
        
        def __init__(self):
            self.data = []

        def size(self):
            return len(self.data)

        def isEmpty(self):
            return self.size() == 0

        def push(self, item):
            self.data.append(item)

        def pop(self):
            return self.data.pop()

        def peek(self):
            return self.data[-1]

class ProgrammersExample13View(View):  
    '''
    # (13) 후위표현 수식 계산

    ### **문제 설명**

    인자로 주어진 문자열 expr 은 소괄호와 사칙연산 기호, 그리고 정수들로만 이루어진 중위 표현 수식입니다. 함수 `solution()` 은 
    이 수식의 값을 계산하여 그 결과를 리턴하도록 작성되어 있습니다. 이 함수는 차례로 `splitTokens()`, `infixToPostfix()`, 
    그리고 `postfixEval()` 함수를 호출하여 이 수식의 값을 계산하는데,

    - `splitTokens()` - 강의 내용에서와 같은 코드로 이미 구현되어 있습니다.
    - `infixToPostfix()` - 지난 강의의 연습문제에서 작성했던 코드를 수정하여, 문자열이 아닌 리스트를 리턴하도록 작성합니다.
    - `postfixEval()` - 이번 강의의 연습문제입니다. 함수의 내용을 완성하세요.

    즉, 두 개의 함수 `infixToPostfix()` 와 `postfixEval()` 을 구현하는 연습입니다. 스택을 이용하기 위하여 `class ArrayStack` 이 정의되어 있으므로 그것을 활용하세요.

    [참고] Python 에는 `eval()` 이라는 built-in 함수가 있어서, 이 함수에 문자열을 인자로 전달하면, 
    그 문자열을 그대로 Python 표현식으로 간주하고 계산한 결과를 리턴하도록 되어 있습니다. 이 built-in 함수 `eval()` 을 이용하면 
    이 연습문제는 전혀 직접 코드를 작성하지 않고도 정답을 낼 수 있을 것이지만, 스택을 이용하여 중위표현식을 계산하는 프로그래밍 연습을 위한 것이니, 
    강의 내용에서 설명한 절차를 수행하도록 코드를 작성해 보세요.
   
    '''
      
    def get(self,request):

        def splitTokens(exprStr):
            tokens = []
            val = 0
            valProcessing = False
            
            # (5+3)*(5-4)
            # ['(', 5, '+', 3, ')' ,*, '(', 5, '-', 4, ')']
            for c in exprStr:
                if c == ' ':
                    continue
                if c in '0123456789':
                    val = val * 10 + int(c)
                    valProcessing = True
                else:
                    if valProcessing:
                        tokens.append(val)
                        val = 0
                    valProcessing = False
                    tokens.append(c) 
            if valProcessing:
                tokens.append(val)

            return tokens


        def infixToPostfix(tokenList):
            prec = {
                '*': 3,
                '/': 3,
                '+': 2,
                '-': 2,
                '(': 1,
            }

            opStack = ArrayStack()
            postfixList = []
            
            for token in tokenList:
                if type(token) is int:# 피연산자가 올 때, 
                    postfixList.append(token)
                elif token == '(': # 여는 괄호가 올때, 
                    opStack.push(token)
                    
                elif token == ')':# 닫는 괄호가 올때, 
                    while not opStack.peek() == '(':
                        postfixList.append(opStack.pop())
                    opStack.pop()
                    
                else:# 연산자가 올 때, 
                    while not opStack.isEmpty():
                        if prec[opStack.peek()] >= prec[token]:
                            postfixList.append(opStack.pop())
                        else : break #*** 반복문 끊어주기
                    opStack.push(token)
                
            while not opStack.isEmpty():
                postfixList.append(opStack.pop())

            return postfixList


        def postfixEval(tokenList):
            valStack = ArrayStack()
            
            for token in tokenList:
                if type(token) is int:
                    valStack.push(token)
                elif token == '*':
                    val1 =valStack.pop()
                    val2 =valStack.pop()
                    valStack.push(val2*val1)
                elif token == '/':
                    val1 =valStack.pop()
                    val2 =valStack.pop()
                    valStack.push(val2/val1)
                elif token == '+':
                    val1 =valStack.pop()
                    val2 =valStack.pop()
                    valStack.push(val2+val1)
                elif token == '-':
                    val1 =valStack.pop()
                    val2 =valStack.pop()
                    valStack.push(val2-val1)
                    
            return valStack.pop()

        def solution(expr):
            tokens = ProgrammersExample13View.splitTokens(expr)
            postfix = ProgrammersExample13View.infixToPostfix(tokens)
            val = ProgrammersExample13View.postfixEval(postfix)
            return val
        
        '''
         테스트 1
        입력값 〉	"5 + 3"
        기댓값 〉	8
        실행 결과 〉	테스트를 통과하였습니다.
        출력 〉	[5, '+', 3]
        테스트 2
        입력값 〉	"(1 + 2) * (3 + 4)"
        기댓값 〉	21
        실행 결과 〉	테스트를 통과하였습니다.
        출력 〉	['(', 1, '+', 2, ')', '*', '(', 3, '+', 4, ')']
        테스트 3
        입력값 〉	"7 * (9 - (3+2))"
        기댓값 〉	28
        실행 결과 〉	테스트를 통과하였습니다.
        출력 〉	[7, '*', '(', 9, '-', '(', 3, '+', 2, ')', ')']
        '''
        return JsonResponse({"RESULT": solution("(5+4)*(6-7)")}, status=200)
    
class ProgrammersExample14View(View):  
        '''
        (14) 양방향 연결 리스트로 구현하는 큐
        문제 설명
        양방향 연결 리스트를 활용하여 큐 (queue) 의 추상적 자료구조 (abstract data structure) 구현을 완성하세요.

        정의하고자 하는 큐의 추상적 자료구조는 class LinkedListQueue 로 구현됩니다. 
        이 문제는 해당 클래스의 메서드들의 구현을 빈칸 채우기 형태로 완성하는 것으로 되어 있으며, 이 클래스의 구현은 L120 부터 시작합니다.

        그 위에는 (LL1-117) 이 추상적 자료구조를 구현하기 위해서 이용할 class DoublyLinkedList 와, 
        또한 여기서 이용하는 class Node 의 구현이 정의되어 있습니다. 이 코드는 이전의 "양방향 연결 리스트" 강의에서 다루어진 것과 완전히 동일합니다.

        정확성 테스트는 class LinkedListQueue 의 각 메서드가 올바르게 구현되어 있는지를 검사합니다. 
        "코드 실행" 을 눌렀을 때 예시 테스트 케이스를 통과하는 것은 아무런 의미가 없습니다.

        '''
        
def get(self,request):
        class Node:

            def __init__(self, item):
                self.data = item
                self.prev = None
                self.next = None


        class DoublyLinkedList:

            def __init__(self):
                self.nodeCount = 0
                self.head = Node(None)
                self.tail = Node(None)
                self.head.prev = None
                self.head.next = self.tail
                self.tail.prev = self.head
                self.tail.next = None


            def __repr__(self):
                if self.nodeCount == 0:
                    return 'LinkedList: empty'

                s = ''
                curr = self.head
                while curr.next.next:
                    curr = curr.next
                    s += repr(curr.data)
                    if curr.next.next is not None:
                        s += ' -> '
                return s


            def getLength(self):
                return self.nodeCount


            def traverse(self):
                result = []
                curr = self.head
                while curr.next.next:
                    curr = curr.next
                    result.append(curr.data)
                return result


            def reverse(self):
                result = []
                curr = self.tail
                while curr.prev.prev:
                    curr = curr.prev
                    result.append(curr.data)
                return result


            def getAt(self, pos):
                if pos < 0 or pos > self.nodeCount:
                    return None

                if pos > self.nodeCount // 2:
                    i = 0
                    curr = self.tail
                    while i < self.nodeCount - pos + 1:
                        curr = curr.prev
                        i += 1
                else:
                    i = 0
                    curr = self.head
                    while i < pos:
                        curr = curr.next
                        i += 1

                return curr


            def insertAfter(self, prev, newNode):
                next = prev.next
                newNode.prev = prev
                newNode.next = next
                prev.next = newNode
                next.prev = newNode
                self.nodeCount += 1
                return True


            def insertAt(self, pos, newNode):
                if pos < 1 or pos > self.nodeCount + 1:
                    return False

                prev = self.getAt(pos - 1)
                return self.insertAfter(prev, newNode)


            def popAfter(self, prev):
                curr = prev.next
                next = curr.next
                prev.next = next
                next.prev = prev
                self.nodeCount -= 1
                return curr.data


            def popAt(self, pos):
                if pos < 1 or pos > self.nodeCount:
                    raise IndexError('Index out of range')

                prev = self.getAt(pos - 1)
                return self.popAfter(prev)


            def concat(self, L):
                self.tail.prev.next = L.head.next
                L.head.next.prev = self.tail.prev
                self.tail = L.tail

                self.nodeCount += L.nodeCount

        # 나의 풀이
        class LinkedListQueue:

            def __init__(self):
                self.data = DoublyLinkedList()

            def size(self):
                return self.data.getLength()

            def isEmpty(self):
                return self.size()==0

            def enqueue(self, item):
                node = Node(item)
                self.data.insertAt(self.size()+1, node)

            def dequeue(self):
                return self.data.popAt(1)

            def peek(self):
                return self.data.getAt(1).data

        def solution(x):
            return 0
        
        '''
        정확성  테스트
        테스트 1 〉	통과 (0.06ms, 16.7MB)
        테스트 2 〉	통과 (0.04ms, 16.7MB)
        테스트 3 〉	통과 (0.06ms, 16.8MB)
        테스트 4 〉	통과 (0.06ms, 16.8MB)
        '''

        return JsonResponse({"RESULT": "Sucess"}, status=200)