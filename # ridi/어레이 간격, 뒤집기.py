# array[::]

arr = list(range(10))
print(arr)

# arr [처음:끝:간격]
# arr[A:B:C] : indexA부터 indexB까지 C의 간격으로 배열을 만들어라

print(arr[1:6:2]) # 1번 : 6번 : 2칸 간격

print(arr[1::2]) # 1번 : 끝 : 2칸 간격


print(arr[::2]) # 처음 : 끝 : 2칸 간격

print(arr[::-1]) # 처음 : 끝 : -1칸 간격 (역순 1칸)

print(arr[::-2]) # 처음 : 끝 : -2칸 간격 (역순 2칸)

print(arr[3::-1]) # 3번 : 끝 : -1칸 간격 (역순 1칸)


# 문자열도 가능

a = 'abcdefg'
print(a[::2]) # 처음 : 끝 : 2칸

print(a[::-1]) # 처음 : 끝 : -1칸