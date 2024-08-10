from Backend import functions
import time

now = time.strftime("%B %d, %Y %H:%M:%S")
print(f"It is {now}")

while True:
    # Get user input and strip space chars from it.
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action[0:3].lower().startswith("add"):
        todo = user_action[len('add '):]
        todo = todo.strip() + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

        todo = todo.strip('\n')
        message = f"Your todo: {todo} added."
        print(message)

    elif user_action[0:4].lower().startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action[0:4].lower().startswith("edit"):
        try:
            number = int(user_action[len("edit "):])
            index = number - 1

            todos = functions.get_todos()

            existing_todos = todos[index]
            todo_to_edit = existing_todos.strip('\n')
            print(f"{number}-{todo_to_edit}")
            todos.remove(existing_todos)

            new_todo = input("Enter a new todo: ")
            todos.insert(index, new_todo + "\n")

            print("Hey! Your changes has been done.")
            print(f"{number}-{new_todo}")

            functions.write_todos(todos)

        except ValueError:
            print("Invalid Command! Please enter todo number.")
            continue

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action[0:8].lower().startswith("complete"):
        try:
            number = int(user_action[len("complete "):])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
            print(f"Your todo : {todo_to_remove} is completed and removed from todos.")

        except IndexError:
            print("There is no item with that number.")
            continue

        except ValueError:
            print("Invalid Command! Please enter todo number.")
            continue

    elif user_action.startswith("exit"):

        break
    else:
        print("Command is not valid.")


print("Bye!!!")




