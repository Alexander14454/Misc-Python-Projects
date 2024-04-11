# Practice1.py


matrix = [[1, 2, 3],
          [10, 20, 30],
          [100, 200, 300]]

print("")
# for loop to which to each row
for row in matrix:
    #for loop to print each character in string
    for x in row:
        #print each character on the same line, use end=" " to keep each character printed on the same line
        print(x, end=" ")
    print("\n")