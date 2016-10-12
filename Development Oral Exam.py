## EXERCISE 1 ##

n = input("Enter a number:")
if n % 2 == 0:
    print("This number is even:", n)
else:
    print("This number is not even:", n)

## EXERCISE 2 ##

n = int(input("Enter number:"))
v = ""
for i in range(2, 10):
    if i % n == 0:
        v = "V"
    print(i, v)
    v = ""

## EXERCISE 3 ##

n = input("Enter number:")
def is_priem(n):
    for i in range(2,n):
        if (n % i) == 0:
            return "False"
            break
    else:
        return "True"
print(is_priem(n))

## EXERCISE 4 ##

n = int(input("Enter number:"))
n += 1
output = ""
for i in range(n):
  for s in range(n - i):
    output += " "
  for s in range(1, i):
    output += "*"
  for s in range(i, 0, -1):
    output += "*" 
  output += "\n"
print(output)

## EXERCISE 5 ##

n = int(input("Enter number:"))
output = ""
for i in range(n):
  for x in range(n):
    if x == i or x + i == n - 1 or x == n / 2 or i == n / 2:
        output += "*"
    else:
        output += " "
  output += "\n"
print(output)
