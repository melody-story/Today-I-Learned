# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

'''
파이썬 자료구조(딕셔너리, 집합 자료형(set))
1. 딕셔너리 특징
2. 딕셔너리 추가
3. 집합 특징
4. 집합 자료형 함수
5. 자료형 변환
'''

# 딕셔너리 자료형(순서X, **중복X**, 수정O, 삭제O)

# 선언
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
b = {0: 'Hello python!'}
c = {'arr': [1, 2, 3, 4]}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)

# 출력
print('a - ', a['name'])  # 존재X -> 에러 발생
print('a - ', a.get('name'))  # *** 존재X -> None 처리 *** 딕셔너리는 get으로 가져오자
print('b - ', b[0])
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3])
print('c - ', c.get('arr'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)




# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능
print("==============dict_keys=============")
print('a - ', a.keys())
# a -  dict_keys(['name', 'phone', 'birth', 'address', 'rank'])
print('b - ', b.keys())
# b -  dict_keys([0])
print('c - ', c.keys())
# c -  dict_keys(['arr'])

print("==============list로 형변환 dict_keys=============")
print('a - ', list(a.keys()))
# a -  ['name', 'phone', 'birth', 'address', 'rank']
print('b - ', list(b.keys()))
# b -  [0]
print('c - ', list(c.keys()))
# c -  ['arr']

print("==============dict_values=============")
print('a - ', a.values())
# a -  dict_values(['Kim', '01012345678', '870124', 'seoul', [1, 2, 3]])
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values()))
# a -  ['Kim', '01012345678', '870124', 'seoul', [1, 2, 3]]
print('b - ', list(b.values()))
print('c - ', list(c.values()))

print("==============dict_items=============")
print('a - ', a.items())
# a -  dict_items([('name', 'Kim'), ('phone', '01012345678'), ('birth', '870124'), ('address', 'seoul'), ('rank', [1, 2, 3])])
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))
# 리스트 안에 튜플이 들어간 형태로 반환
# a -  [('name', 'Kim'), ('phone', '01012345678'), ('birth', '870124'), ('address', 'seoul'), ('rank', [1, 2, 3])]
print('b - ', list(b.items()))
print('c - ', list(c.items()))

print('a - ', 'name' in a) # name이라는 key가 있는지
print('a - ', 'addr' in a) # addr이라는 key가 있는지








# 집합(Sets) 자료형(순서X, **중복X**) : 머신러닝에 많이 쓰임

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)

# 튜플 변환
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# 리스트 변환
l = list(c)
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print('l - ', s1 & s2)
print('l - ', s1.intersection(s2))
# l -  {4, 5, 6}

# 합집합 
print('l - ', s1 | s2)
print('l - ', s1.union(s2))
# l -  {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 차집합
print('l - ', s1 - s2)
print('l - ', s1.difference(s2))
# l -  {1, 2, 3}

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)
# s1 -  {1, 2, 3, 4, 5}

s1.remove(2)
print('s1 - ', s1)
# s1 -  {1, 3, 4, 5}
