#function to add items
def additems(input):
    #add the user input as a key with a value of not done
    dict[input] = "not done"
    return dict

#function to change to completed
def changeCompleted(complete):
    #changes the specified key have a value of "done"
    dict[complete] = "done"
    return dict

#function to delete items
def deleteItems(delete):
    #uses the del keyword to delete that key and its value
    del dict[delete]
    return dict

#asks the user what they would like to edit
question = int(input("Click 1 to add new tasks, 2 to view all tasks, 3 to mark tasks as completed, and 4 to delete tasks "))
ToDo = {}
dict = {}

#the if statement for adding tasks
if question == 1:
    howMany = int(input("How many items would you like to add? "))
    x = 0
    while (x < howMany):
        adding = str(input("What would you like to add to the todo list? "))
        ToDo = (additems(adding))
        print(ToDo)
        x += 1
    question = int(input("Click 1 to add new tasks, 2 to view all tasks, 3 to mark tasks as completed, and 4 to delete tasks "))

#the if statement for viewing all tasks
if question == 2:
    print(ToDo)
    question = int(input("Click 1 to add new tasks, 2 to view all tasks, 3 to mark tasks as completed, and 4 to delete tasks "))

#the if statement for marking items as complete
if question == 3:
    complete = input("What item did you complete")
    ToDo = changeCompleted(complete)  
    print(ToDo)  
    question = int(input("Click 1 to add new tasks, 2 to view all tasks, 3 to mark tasks as completed, and 4 to delete tasks "))

#if statement for deleting items
if question == 4:
    delete = input("What item would you like to delete?")
    ToDo = deleteItems(delete)
    print(ToDo)