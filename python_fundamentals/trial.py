for a in range(1, 4):       # a goes
    for b in range(a):      # b goes
        print(f'a: {a}, b: {b}')

for x in range(1, 4):           # x = 1 to 3
    for y in range(1, x+1):     # y = 1 to x
        print(f'{y} ')
    print()                     # move to next line after inner loop

for i in range(2):      # i goes 0, then 1
    for j in range(3):  # j goes 0, 1, 2
        print(f'i: {i}, j: {j}')




for i in range(1,5):
    for j in range(1,6):
      print("*", end=" ")
    print()



for i in range(1 , 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


r = 5

for i in range( 0 , 10):
    for j in range(1, i + 1):
        print( j, end=" ")
    print()


r = 10
for i in range(r, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()




r = 5
a= "*"

for i in range(0, r):
    print(a * i)



for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


r = 5

for i in range(r, 0, -1):
    for j in range(i, 0 , -1):
        print(j, end=" ")
    print()

# a = "*"
# for i in range(0, 6):
#     for j in range(0, i + 1)




rows = 7
# Upper half
for i in range(1, rows + 1):
    print(' ' * (rows - i) * 2, end='')
    for j in range(1, i):
        print(j, end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()
# Lower half (inverted)
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) * 2, end='')
    for j in range(1, i):
        print(j, end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()




for i in range(0, 5):
    for j in range(0, 5 - i ):
        print(" ", end= "")
    for j in range(0, i + 1):
        print(" *", end="")
    print()

    for x in range(1, 4):  # x = 1,2,3
        for y in range(2, 5):  # y = 2,3,4
            if (x + y) % 2 == 0:
                print(f'x={x}, y={y}')


