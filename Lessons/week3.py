a = [5,10,7,1,0]
print(a)
# [5, 10, 7, 1, 0]

print(f"{a[0]}, {a[1]}")
#5, 10

print(f"Sum of the first two: {a[0]+a[1]}")
#Sum of the first two: 15

#Variable Names
#Should start with a letter
#Can only contain letters and numbers, and underscore
#No spaces, no other chracters such as @ # $ % ^ & * ( ) - +
print([1,2,3][-1])
print(a[0])
# 3, 5

myList = [1, 3, "Four", 5, "Six", 7]
print(myList[2])
print(myList[-1])
# Four, 7

for item in myList:
  print(item)
#1
#3
#Four
#5
#Six
#7

print(a) #[5, 10, 7, 1, 0]

# for is a keyword
for b in a:
  print(b+1)

colors = ["red", "green", "blue"]
print(colors)

nums = [1, 3, 5, 7]
for n in nums:
  if n>2:
    print(n)

print("Done!")


print(myList) #[1, 3, 'Four', 5, 'Six', 7]

# Multiply each item in myList to itself if the item is a number
# 1*1
# 3*3
# 5*5
# 7*7
# Expected output: 
# 1 9 25 49

print("Staring...")
for item in myList:
  if isinstance(item, int):
    print(item*item)
  else:
    print(item)

print("End.")
#Staring...
#1
#9
#Four
#25
#Six
#49
#End.#




