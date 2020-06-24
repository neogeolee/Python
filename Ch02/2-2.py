"""
날짜 : 2020/06/22
이름 : 이태훈
내용 : 문자열 자료형 실습하기 교재 p44
"""

# 문자열 더하기
str1 = 'Hello\t'
str2 = 'Python!'
str3 = str1+str2

print('str3 : ', str3)

# 문자열 곱하기
str = 'python!'
print('str*5 : ', str*5)

# 문자열 길이
hello = 'Hello World'
print('hello 길이 : ', len(hello))

# 문자열 인덱스
print('hello[0] : ', hello[0])
print('hello[6] : ', hello[6])

#문자열 슬라이스
print('hello[0:7]', hello[0:7])
print('hello[1:7]', hello[1:7])
print('hello[:7]', hello[:7])
print('hello[7:]', hello[7:])
print('hello[-1]', hello[-1])
print('hello[-2]', hello[-2])

# 문자열 분리
animal = '사자,호랑이,코끼리,기린'
a1, a2, a3, a4 = animal.split(',')

print('a1 : ', a1)
print('a2 : ', a2)
print('a3 : ', a3)
print('a4 : ', a4)

# 문자열 포맷
fm1 = '오늘은 %d월 입니다.'
fm2 = '오늘은 %d월 %d입니다.'
fm3 = '오늘은 %s월 입니다.'
fm4 = '오늘은 %s년 %d월 %d일 %s요일 입니다.'

print(fm1 % 6)
print(fm2 % (6, 22))
print(fm3 % '06')
print(fm4 % ('2020', 6, 22, '월'))

# 문자열 관련 함수 교재 p67 ~ p71

# 문자갯수세기
a = "hobby"
print(a.count('b'))
# 위치알려주기
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))
# 위치알려주기
a = "Life is too short"
print(a.index('t'))
# print(a.index('k')) k가 없어서 오류
# 문자열 삽입
print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))
# 대문자로 바꾸기
a = "hi"
print(a.upper())
# 소문자로 바꾸기
a = "HI"
print(a.lower())
# 왼쪽 공백지우기
a = " hi "
print(a.lstrip())
# 오른쪽 공백지우기
a = " hi "
print(a.rstrip())
# 양쪽 공백지우기
a = " hi "
print(a.strip())
# 문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "Your leg"))
# 문자열 나누기
a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(':'))

