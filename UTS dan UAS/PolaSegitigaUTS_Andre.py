print('* '*19)
a = 8
for b in range(1, a+1):
   print(((a-b+2) * "* ") + ((b) * "  ") +  (((b-1)* "  ")) + (a-b+2) * "* ")

x = 7
for y in range(-1, x+1):
    print(((y+2) * "* ") + ((x-y+1) * "  ") + (((x)-y) * "  ")+((y+2)* "* "))

#
print('* '*19)


a = 10
for b in range(1, a+1):
    print(((a-b) * "  ") + (b * "* ") + ((b-1) * "* "))
a = 9
for b in range(1, a+1):
     print((b * "  ") + ((a-b+1) * "* ") + ((a-b) * "* "))

