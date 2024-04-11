# add spaces.py

print("Enter any Phrase:")
mainString = input() 

finalString = ""

for x in mainString:
    add = x + " "
    finalString += add
print(f"\n\b {finalString} \n")