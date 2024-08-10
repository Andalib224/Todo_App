from Backend import functions
import PySimpleGUI as pg

label = pg.Text("Type in a todo")
input_box = pg.InputText(tooltip='Enter todo')
add_button = pg.Button('Add')

window = pg.Window('My To-do App', layout=[[label], [input_box, add_button]])
window.read()
print("hello")
window.close()
