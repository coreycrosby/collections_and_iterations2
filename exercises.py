#Exercise 9

grocery_list = ["bananas", "chicken", "chips", "hamburgers", "french fries", "salmon"]

for contents in grocery_list:
    print("*" + ' ' + contents)

grocery_list.append("rice")


print(len(grocery_list))

if "bananas" in grocery_list:
    print("You need to pick up bananas.")

else: 
    print("You don't need to pick up bananas today.")

print(grocery_list[1])

for contents in sorted(grocery_list):
    print("*" + ' ' + contents)

grocery_list.pop(5)
print(grocery_list)

