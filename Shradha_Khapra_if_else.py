
# Traffic signal  problem and solution
light = str(input("Enter your wish you wana go: "))
if (light=="red"):
    print("stop ")
elif(light=="green"):
    print("go")
elif (light =="yellow"):
    print("look")
print("End of the code")

# Find out  3 number leargest number

a = int (input("Enter your first  number: "))
b = int (input("Enter your second  number: "))
c = int (input("Enter your  third  number: "))

if (a>=b and a>=c):
    print("first number is leargest ",a)
elif (b>=c):
    print("senond number  is leargest ",b)
else:
    print("third number is leargest ",c)
