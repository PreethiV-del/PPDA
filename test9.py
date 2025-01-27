n = int(input("Enter a number:"))
t = n
rev = 0
while n!=0:
 print("value of n is",n)
 r = n % 10
 print("value of r is",r)
 rev = rev * 10 + r
 print("Value of rev is",rev)
 n = n//10
 print("value of n is",n)
print("Reverse of number",t,"is:",rev)
