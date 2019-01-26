name1string = input("pls enter first name : ")
namestring = input("pls nter last name : ")




print(name1string[::-1] +" " + namestring[::-1])

a = int(input("enter first number: "))
b = int(input("enter second number: "))

sum = a + b
diff = a - b
mul = a * b
div = a / b
rem = a % b
print("sum:", sum)
print("diff:", diff)
print("mul:", mul)
print("div:", rem)



string = input("pls enter string : ")
digits=letters=0
for c in string:
    if c.isdigit():
        digits=digits+1
    elif c.isalpha():
        letters=letters+1
    else:
        pass
print("Letters", letters)
print("Digits", digits)
