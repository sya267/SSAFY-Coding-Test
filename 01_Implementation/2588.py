A=int(input())
B=int(input())
print(A * (B % 10))        # 일의 자리
print(A * ((B // 10) % 10)) # 십의 자리
print(A * (B // 100))       # 백의 자리
print(A * B)   