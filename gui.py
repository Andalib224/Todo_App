from Backend import functions
import PySimpleGUI as pg

label = pg.Text("Type in a todo")
input_box = pg.InputText(tooltip='Enter todo', key='todo')
add_button = pg.Button('Add')

list_box = pg.Listbox(values=functions.get_todos(), size=(45, 12),
                      key="todos",
                      enable_events=True)
edit_button = pg.Button('Edit')
complete_button = pg.Button('Complete')
exit_button = pg.Button('Exit')


window = pg.Window('My To-do App',
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button, complete_button], [exit_button]],
                   font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)

    match event:
        case 'Add':
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            input_box.update(value='')

        case 'Edit':
            todo_to_edit = values['todos'][0]
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"

            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            list_box.update(todos)
            functions.write_todos(todos)

        case 'Complete':
            todo_to_complete = values['todos'][0]

            todos = functions.get_todos()

            index = todos.index(todo_to_complete)
            todos.pop(index)
            functions.write_todos(todos)
            input_box.update(value='')
            list_box.update(values=todos)

        case 'todos':
            selected_todo = values['todos'][0].replace('\n', '')
            input_box.update(value=selected_todo)

        case "Exit":
            break

        case pg.WIN_CLOSED:
            break


print("Bye...")
window.close()
