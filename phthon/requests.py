'''

for i in range(5):
    print("반복이 되네 신기해!!")

#4. for문의 흐름 확인해보기

for i in range(5):
    print("반복이 되네 신기해", i)
    
#5. for 문에서 range()함수 활용하기

for i in range(10,4,-1):
    print(i)
    
#6. for문에서 시퀀스 객체로 반복하기
과일 = ["두리안", "망고", "바나나", "멜론"]

# for i in 과일:
#     print(i)    

# for i in reversed("닥스훈트") : 
#     print(i,end = "")

#7. 예제로 for문 익혀보기 
#문제 : 절대값 정수가 담긴 정수 변수와 그정수의 부호를 차례로 담은 부호 변수가 있다
# 변수를 이용해 실제 정수의 값을 구하라
#True = 양수 False = 음수
정수 = [10,5,8]
부호 = [True ,False, True]

합 =0

for k, v in zip(부호,정수):
    if k: 
        합 += v
    else:
        합 -= v
      
print(f'총 합은 {합}입니다')

i = 0
while i < 10:
    print("하이하이")
    i += 1
    
# 3, while 문 조건식 증감 , 감소
#1. 기본적인 증가 유형

i = 1 
while i < 10:
    print('이정도로 성장할줄이야', i )
    i +=1
#2. 기본적인 감소유형

i = 10
while i > 0:
    print('이정도로 성장할줄이야',i)
    i-=1
    
#4. while문을 조심스럽게 사용해야하는 이유
# 잘 사용하면 for문보다 효율적 . 이상하게 사용하면 무한둘레
   #while True
    print("내가 산 주식 폭등")
'''    
#5. While문이  for문보다 강점인 부분? 
# 무수히 많이 실행해야할때

# import random

# random.randint(1,6)
'''
import random


i = 0
while i !=4:
    i = random.randint(1,6)
    print(i)
    '''
    
    
#6 while 문에도 elserk dlTdjdy
'''
양파 = 10
while 양파 > 10:
    print("양파", 양파, "개 남았습니다.")
    if 양파 ==0:
        break
    양파 -=1
else:
    print("양파 다 팔렸습니다.")
    
'''

#7.반복문에 흐름을 제어하는 continue와 break
'''
i=0
while True :
    print(i)
    i+=1
    if i == 10:
        break
    
for i in range(10):
    print(i)
    if i == 10:
        break
'''
'''
i = 0
while i < 10:
    i+=1
    if i % 2 ==0:
        continue
    print(i)
    
for i in range(100):
    if i % 2 == 0:     
        continue
    print(i)
'''
