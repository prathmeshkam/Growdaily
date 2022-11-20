def rem(s,n):
    x = s.replace(n,'')
    return x




s = input()
n = int(input())

for i in s:
    count = s.count(i)
    if count == n:
        s = rem(s,i)
        
print(s)
