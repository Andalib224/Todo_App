import sys

from Backend import functions
import PySimpleGUI as pg
import time

pg.theme("Black")
clock = pg.Text('', key="clock")

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
                   layout=[[clock], [label], [input_box, add_button],
                           [list_box, edit_button, complete_button], [exit_button]],
                   font=('Helvetica', 10))

while True:
    event, values = window.read(timeout=200)
    clock.update(value=time.strftime("%B %d, %Y %H:%M:%S"))

    match event:
        case 'Add':
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            input_box.update(value='')

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"

                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                list_box.update(todos)
                functions.write_todos(todos)
            except IndexError:
                pg.popup("Please select an item first.", font=('Helvetica', 12))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]

                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                todos.pop(index)
                functions.write_todos(todos)
                input_box.update(value='')
                list_box.update(values=todos)
            except IndexError:
                pg.popup("Please select an item first.", font=('Helvetica', 12))

        case 'todos':
            selected_todo = values['todos'][0].replace('\n', '')
            input_box.update(value=selected_todo)

        case "Exit":
            break

        case pg.WIN_CLOSED:
            break

window.close()
