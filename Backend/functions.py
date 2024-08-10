FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read the text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH ):
    """Write the to-do items in todos text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
