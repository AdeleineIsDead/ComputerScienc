#for loops alow the programmer to repeatt

(groceries) = ["Milk, eggs, bread, butter, apples"]
for food in groceries:
    print(food)
purchase = input("What was purchased\n>")
if purchase == "Milk":
    str(groceries).remove("Milk")
    print(food)
