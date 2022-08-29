a = True
b = True
c = False
x = 1.5
y = 2.2
x = x + 1
#x = 1.5 + 1 => 2.5
if c or (( x + y > 5) or ( not a and b )):
    z = 0
else:
    z = 1
print(z)
