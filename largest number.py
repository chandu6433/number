a = int(input("enter a number:"))
b = int(input("enter b number:"))
c = int(input("enter c number:"))
if a>b and a>c :
  print(f"largest number is: {a}")
elif b>a and b>c :
  print(f"largest number is: {b}")
else:
  print(f"largest number is: {c}")