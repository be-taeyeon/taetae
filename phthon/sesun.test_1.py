# 숫자 입력 -> 음수인지 양수인지 '0'인지 구분하는 프로그램을 만들겁니다.
# 음수 < 0 , 0> 양수 , 0은 0 입니다
'''
number = input("정수를 입력해주세요")
number = int(number)      # 입력 받은 값을 정수형 데이터로 변경

# 양수 조건
if number > 0 :
    print("양수입니다")
    
# 음수 조건
if number < 0 :
    print("음수입니다")
    
# 0 조건
if number == 0 :
    print("0입니다")
    
'''

# import datetime

#now = datetime.datetime.now()

# print(now)
# print(now.year,"년")
# print(now.month,"월")  
# print(now.day,"일")  
# print(now.hour,"시")  
# print(now.minute,"분")
# print(now.second,"초")  

#1월~3월 봄 / 4월~8월 여름 / 9월~10월 가을 / 11~12월 겨울
'''
from datetime import datetime

now = datetime.now()  # 현재 날짜와 시간 가져오기

if 1 <= now.month <= 3:
    print("봄입니다")
''''''
number = input ( "정수를 입력해주세요 " )

last_number = number[-1]

last_number = int(last_number)

if  last_number == 0 or last_number == 2 or last_number == 4 or last_number == 6 or last_number == 8 :
    print("짝수입니다")
else :
    print("홀수입니다")
    '''
    
num = 0
while True:
    
    if num < 10:
        print("안녕하세요",num)
    else:
        break
    num += 1
print("여기요 여기")

