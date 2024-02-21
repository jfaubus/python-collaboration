def additems(input):
    dict = {}
    dict[input] = "not done"
    return dict

input = str(input("What would you like to add to the todo list? "))
print(additems(input))