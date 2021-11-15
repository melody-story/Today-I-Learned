import json
from django import views
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
        
        '''
        
        
        
        
        
        return JsonResponse({"MESSAGE": "Hello"}, status=200)


