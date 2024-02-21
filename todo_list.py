def additems(input):
    dict = {}
    dict[input] = "not done"
    return dict

question = str(input("Click 1 to add new tasks, 2 to view all tasks, 3 to mark tasks as completed, and 4 to delete tasks "))


if question == 1:
    howMany = int(input("How many items would you like to add? "))
    x = 0
    while (x <= howMany):
        input = str(input("What would you like to add to the todo list? "))
        print(additems(input))
        x += 1
    question = str(input("Click 1 to add new tasks, 2 to view all tasks, 3 to mark tasks as completed, and 4 to delete tasks "))
