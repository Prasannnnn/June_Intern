def power(a,b):
  if b == 0:
    return 1
  return a * power(a,b-1)


a = int(input("Enter the number"))
b = int(input("Enter the number"))
print(power(a,b))
