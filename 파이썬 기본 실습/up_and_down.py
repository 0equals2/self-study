import random
user=int(input("1~100 사이의 숫자를 입력하세요:"))
com=random.randint(1,100)

count=1
while user!=com:
    if user>com:
        user=int(input("%d보다 작은 수를 입력하세요. Down!"% user))
    else:
        user=int(input("%d보다 큰 수를 입력하세요. Up!"% user))
    count+=1
if user==com:
    print("%d! 정답입니다. %d 회 시도하여 맞췄습니다." % (com,count))
