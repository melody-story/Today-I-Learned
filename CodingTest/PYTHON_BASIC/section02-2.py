# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

'''
간단히 살펴보기
- 목 차 -
1. 인코딩
2. 변수
3. 조건문
4. 함수, 클래스, 인스턴스(객체)
5. 정보출력
'''

# import this
import sys


# 파이썬 2.x-> 유니코드로 인코딩을 해주었어야했다. vs 3.x 기본 캐릭터 셋 설명-> 기본이 utf-8이다.
# 아래와 같이 인코딩을 검증 가능
# Python 3.x [입력] 인코딩
print(sys.stdin.encoding)
# 출력 : utf-8

# Python 3.x [출력] 인코딩
print(sys.stdout.encoding)
# 출력 : utf-8

# ==================================

# 출력문
print("My name is Goodboy!")

# 변수선언 : 값을 할당
myName = "Goodboy"

# 조건문
if myName == "Goodboy":
    print("OK!")
    

# 반복문(구구단)
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i * j)


# 변수선언(한글)
이름 = "좋은사람"

# 출력
print(이름)


# 함수선언(한글명)
def 인사():
    print("안녕하세요. 반갑습니다.")


# 함수 실행
인사()


# 클래스 선언
class Cookie:
    pass


# 객체 생성
cookie = Cookie()

# 정보 값 출력
print(id(cookie))
print(dir(cookie))
print(cookie.__class__)
print(cookie.__hash__)
