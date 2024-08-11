from Backend import functions
import PySimpleGUI as pg

label = pg.Text("Type in a todo")
input_box = pg.InputText(tooltip='Enter todo', key='todo')
add_button = pg.Button('Add')

list_box = pg.Listbox(values=functions.get_todos(), size=(45, 12),
                      key="todos",
                      enable_events=True)
edit_button = pg.Button('Edit')


window = pg.Window('My To-do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
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

        case 'Edit':
            print('It is Edit button...')

            todo_to_edit = values['todos'][0]
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"

            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            list_box.update(todos)
            functions.write_todos(todos)

        case 'todos':
            selected_todo = values['todos'][0].replace('\n', '')
            input_box.update(value=selected_todo)

        case pg.WIN_CLOSED:
            break

print("Bye...")
window.close()
