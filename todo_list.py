def additems(input):
    dict[input] = "not done"
    return dict

question = int(input("Click 1 to add new tasks, 2 to view all tasks, 3 to mark tasks as completed, and 4 to delete tasks "))
ToDo = {}
dict = {}

if question == 1:
    howMany = int(input("How many items would you like to add? "))
    x = 0
    while (x < howMany):
        adding = str(input("What would you like to add to the todo list? "))
        ToDo = (additems(adding))
        print(ToDo)
        x += 1
question = int(input("Click 1 to add new tasks, 2 to view all tasks, 3 to mark tasks as completed, and 4 to delete tasks "))

if question == 2:
    print(ToDo)

