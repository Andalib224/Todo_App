from Backend import functions
import PySimpleGUI as pg

label = pg.Text("Type in a todo")
input_box = pg.InputText(tooltip='Enter todo', key='todo')
add_button = pg.Button('Add')

window = pg.Window('My To-do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 10))


while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case 'Add':
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            todos.append(new_todo)
            functions.write_todos(todos)

        case pg.WIN_CLOSED:
            break

print("Bye...")
window.close()
