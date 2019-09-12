#2부터 100까지 numbers 리스트에 넣기
numbers=[]
for i in range(2,100,1):
    numbers.append(i)

prime=[]    #소수를 저장할 리스트
for i in numbers:
    am_i_prime=True     #일단 i 가 소수라고 가정
#i가 소수인지 판단하기 위해, 자기보다 작은 수로 나누어 떨어지는지 검사
#소수가 아니면 am_i_prime=false
    for j in range(2,i,1):
        if i%j==0:
            am_i_prime=False
            break
#i가 소수이면 prime 리스트에 추가
    if am_i_prime:
        prime.append(i)

print(prime)
