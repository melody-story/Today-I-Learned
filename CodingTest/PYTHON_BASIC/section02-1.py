# Section02-1
# 파이썬 기초코딩
# print 구문의 이해

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Seperator 옵션 사용

print('T', 'E', 'S', 'T')
# 출력 : T E S T
print('T', 'E', 'S','T', sep='')
# 출력 : TEST
print('T', 'E', 'S','T', sep='-')
# 출력 : T-E-S-T
print('niceman', 'google.com',sep='@')
# 출력 : niceman@google.com

# end 옵션 사용, 다음 라인과 연결
print('Welcome To', end=' ')
print("Melody's page", end=' ')
print('Thank you')
# 출력 : Welcome To Melody's page Thank you

# <format 사용> [](대괄호),{}(중괄호),()(소괄호)
print('{} and {}'.format('You','Me'))
# 출력 : You and Me
print("{0} and {1} and {0}".format('You','Me'))
# 출력 : You and Me and You
print('{var1} are {var2}'.format(var1='You', var2='Niceman'))
# 출력 : You are Niceman
print("Test1: {0:5d}, Price:{1:4.2f}".format(776, 6534.123)) # 중괄호로 묶으면, 코딩을 확실히 할 수 잇음
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))

# <format함수를 안쓰는 방법>
# 참조 : https://www.python-course.eu/python3_formatted_output.php
# %d: 정수, %f:실수, %s:문자
print("%s's favorite number is %d" % ('Eunki', int(45)))
print("Test1: %5d, Price: %4.2f" % (776, 6534.123)) # 5d :5자리의 정수, 4.2 : 4자리의 정수, 2자리의 소수


"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자 -> 표시 : \
\' : 문자 -> 표시 : '
\" : 문자 -> 표시 : '


\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""