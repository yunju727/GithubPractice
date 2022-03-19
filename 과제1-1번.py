# 컴퓨터공학부 202103307 조윤주!
#I'm subyunju727
#
n=list(map(int,input("숫자 세개를 입력해주세요.").split()))	#map함수를 이용하면 입력받은 수를 정수로 각각 리스트에 저장할 수 있어서 사용하였다.
def gcd(a, b):	#두수의 최대공약수를 구하는 함수
	while a*b!=0:	#a=0 or b=0이면 while문을 빠져나간다
		if a>b:	#a가 b보다 크면 a는 b로나눈 나머지이다.
			a%=b
		else:	#a가 b보다 작거나 같으면 b는 a로 나눈 나머지이다.
			b%=a
	return a+b	#a+b값이 최대공약수이므로 반환한다.

def lcm(a,b):	#최소공배수 함수
	return a*b/gcd(a,b)	#최소공배수=두 수의 곱/최대공약수임을 이용한다.
'''
세 수의 최대공약수 구하는 법 : 두 수의 최대공약수를 먼저 구한 뒤, 구한 최대공약수와 남은 한 수의 최대공약수를 구한다.
세 수의 최소공배수 구하는 법: 두 수의 최소공배수를 먼저 구한뒤, 구한 최소공배수와 남은 한 수의 최소공배수를 구한다.
'''
gcd_n=gcd(n[0],n[1])
lcm_n=lcm(n[0],n[1])
gcd_n=gcd(gcd_n,n[2])
lcm_n=lcm(lcm_n,n[2])

print(gcd_n,int(lcm_n))
