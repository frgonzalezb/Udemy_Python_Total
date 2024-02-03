import datetime
import random

from tkinter import *
from tkinter import filedialog, messagebox


# Funcionalidad calculadora
operador = ''
precios_comidas = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebidas = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def clic_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    # Comidas
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1
    # Bebidas
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1
    # Postres
    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1


def obtener_total():
    # Comidas
    subtotal_comida = 0
    p = 0
    for cantidad in texto_comida:
        subtotal_comida += (float(cantidad.get()) * precios_comidas[p])
        p += 1
    # Bebidas
    subtotal_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebida += (float(cantidad.get()) * precios_bebidas[p])
        p += 1
    # Postres
    subtotal_postre = 0
    p = 0
    for cantidad in texto_postre:
        subtotal_postre += (float(cantidad.get()) * precios_postres[p])
        p += 1
    
    subtotal = subtotal_comida + subtotal_bebida + subtotal_postre
    impuesto = subtotal * 0.07
    total = subtotal + impuesto

    var_costo_comida.set(f'$ {round(subtotal_comida, 2)}')
    var_costo_bebida.set(f'$ {round(subtotal_bebida, 2)}')
    var_costo_postre.set(f'$ {round(subtotal_postre, 2)}')
    var_subtotal.set(f'$ {round(subtotal, 2)}')
    var_impuesto.set(f'$ {round(impuesto, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def obtener_recibo():
    # Nro. orden, fecha y títulos
    texto_recibo.delete(1.0, END)
    num_recibo = f'#{random.randint(1000, 9999)}'
    hoy = datetime.datetime.now()
    fecha_recibo = f'{hoy.day}/{hoy.month}/{hoy.year} - {hoy.hour}:{hoy.minute}'
    texto_recibo.insert(END, f'Orden {num_recibo}\t\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, f'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    # Comida
    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t$ {int(comida.get()) * precios_comidas[x]}\n')
        x += 1
    # Bebida
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t$ {int(bebida.get()) * precios_bebidas[x]}\n')
        x += 1
    # Postre
    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t$ {int(postre.get()) * precios_postres[x]}\n')
        x += 1
    # Subtotales por categoría
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Costo comida:\t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo bebida:\t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo postre:\t\t\t{var_costo_postre.get()}\n')
    # Subtotal, impuesto y total
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Subtotal:\t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuesto:\t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total:\t\t\t{var_total.get()}\n')
    # Saludo al cliente
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, f'Gracias por su visita')


def guardar_recibo():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo ha sido guardado.')


def resetear():
    texto_recibo.delete(0.1, END)
    
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for variable in variables_comida:
        variable.set(0)
    for variable in variables_bebida:
        variable.set(0)
    for variable in variables_postre:
        variable.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


# Inicializar tkinter
aplicacion = Tk()

# Tamaño y posición (xy) de la ventana
aplicacion.geometry('1024x640+0+0')

# Evitar maximizar
aplicacion.resizable(0, 0)

# Título de la ventana
aplicacion.title('El Pollo Farsante - Sistema de Facturación')

# Color de fondo de la ventana
aplicacion.config(bg='burlywood')

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta título
etiqueta_titulo = Label(
    panel_superior, 
    text='Sistema de Facturación',
    fg='azure4',
    font=('Dosis', 58),
    bg='burlywood',
    width=27
)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4')
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(
    panel_izquierdo, 
    text='Comidas', 
    font=('Dosis', 18, 'bold'), 
    bd=1,
    relief=FLAT,
    fg='azure4'
)
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(
    panel_izquierdo, 
    text='Bebidas', 
    font=('Dosis', 18, 'bold'), 
    bd=1,
    relief=FLAT,
    fg='azure4'
)
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(
    panel_izquierdo, 
    text='Postres', 
    font=('Dosis', 18, 'bold'), 
    bd=1,
    relief=FLAT,
    fg='azure4'
)
panel_postres.pack(side=LEFT)

# Panel derecho
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(
    panel_derecho,
    bd=1,
    relief=FLAT,
    bg='burlywood'
)
panel_calculadora.pack()    # Si nada, por defecto, se ubicará arriba

# Panel recibo
panel_recibo = Frame(
    panel_derecho,
    bd=1,
    relief=FLAT,
    bg='burlywood'
)
panel_recibo.pack()

# Panel botones
panel_botones = Frame(
    panel_derecho,
    bd=1,
    relief=FLAT,
    bg='burlywood'
)
panel_botones.pack()

# Lista de productos
lista_comidas = ['pollo', 'pavo', 'pato', 'vacuno', 'cerdo', 'salmón', 'merluzo', 'atún']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino', 'cerveza', 'whisky', 'mojito']
lista_postres = ['helado', 'frutas', 'brownies', 'flan', 'mousse', 'torta', 'pie', 'kuchen']

# Generar items comida
contador = 0
variables_comida = []
cuadros_comida = []
texto_comida = []
for comida in lista_comidas:
    # Crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(
        panel_comidas,
        text=comida.title(),
        font=('Dosis', 18, 'bold'),
        onvalue=1,
        offvalue=0,
        variable=variables_comida[contador],
        command=revisar_check
    )
    comida.grid(row=contador, column=0, sticky=W)
    # Crear cuadro de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(
        panel_comidas,
        font=('Dosis', 18, 'bold'),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=texto_comida[contador]
    )
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1

# Generar items bebida
contador = 0
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
for bebida in lista_bebidas:
    # Crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(
        panel_bebidas,
        text=bebida.title(),
        font=('Dosis', 18, 'bold'),
        onvalue=1,
        offvalue=0,
        variable=variables_bebida[contador],
        command=revisar_check
    )
    bebida.grid(row=contador, column=0, sticky=W)
    # Crear cuadro de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(
        panel_bebidas,
        font=('Dosis', 18, 'bold'),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=texto_bebida[contador]
    )
    cuadros_bebida[contador].grid(row=contador, column=1)
    contador += 1

# Generar items postre
contador = 0
variables_postre = []
cuadros_postre = []
texto_postre = []
for postre in lista_postres:
    # Crear checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(
        panel_postres,
        text=postre.title(),
        font=('Dosis', 18, 'bold'),
        onvalue=1,
        offvalue=0,
        variable=variables_postre[contador],
        command=revisar_check
    )
    postre.grid(row=contador, column=0, sticky=W)
    # Crear cuadro de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(
        panel_postres,
        font=('Dosis', 18, 'bold'),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=texto_postre[contador]
    )
    cuadros_postre[contador].grid(row=contador, column=1)
    contador += 1


# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiqueta de costo comida y campo de entrada
etiqueta_costo_comida = Label(
    panel_costos,
    text='Costo comida',
    font=('Dosis', 12, 'bold'),
    bg='azure4',
    fg='white'
)
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida = Entry(
    panel_costos,
    font=('Dosis', 12, 'bold'),
    bd=1,
    width=11,
    state='readonly',
    textvariable=var_costo_comida
)
texto_costo_comida.grid(row=0, column=1)

# Etiqueta de costo bebida y campo de entrada
etiqueta_costo_bebida = Label(
    panel_costos,
    text='Costo bebida',
    font=('Dosis', 12, 'bold'),
    bg='azure4',
    fg='white'
)
etiqueta_costo_bebida.grid(row=0, column=2)
texto_costo_bebida = Entry(
    panel_costos,
    font=('Dosis', 12, 'bold'),
    bd=1,
    width=11,
    state='readonly',
    textvariable=var_costo_bebida
)
texto_costo_bebida.grid(row=0, column=3)

# Etiqueta de costo postre y campo de entrada
etiqueta_costo_postre = Label(
    panel_costos,
    text='Costo postre',
    font=('Dosis', 12, 'bold'),
    bg='azure4',
    fg='white'
)
etiqueta_costo_postre.grid(row=0, column=4)
texto_costo_postre = Entry(
    panel_costos,
    font=('Dosis', 12, 'bold'),
    bd=1,
    width=11,
    state='readonly',
    textvariable=var_costo_postre
)
texto_costo_postre.grid(row=0, column=5)

# Etiqueta de subtotal y campo de entrada
etiqueta_subtotal = Label(
    panel_costos,
    text='Subtotal',
    font=('Dosis', 12, 'bold'),
    bg='azure4',
    fg='white'
)
etiqueta_subtotal.grid(row=1, column=0)
texto_subtotal = Entry(
    panel_costos,
    font=('Dosis', 12, 'bold'),
    bd=1,
    width=11,
    state='readonly',
    textvariable=var_subtotal
)
texto_subtotal.grid(row=1, column=1)

# Etiqueta de impuesto y campo de entrada
etiqueta_impuesto = Label(
    panel_costos,
    text='Impuesto',
    font=('Dosis', 12, 'bold'),
    bg='azure4',
    fg='white'
)
etiqueta_impuesto.grid(row=1, column=2)
texto_impuesto = Entry(
    panel_costos,
    font=('Dosis', 12, 'bold'),
    bd=1,
    width=11,
    state='readonly',
    textvariable=var_impuesto
)
texto_impuesto.grid(row=1, column=3)

# Etiqueta de total y campo de entrada
etiqueta_total = Label(
    panel_costos,
    text='Total',
    font=('Dosis', 12, 'bold'),
    bg='azure4',
    fg='white'
)
etiqueta_total.grid(row=1, column=4)
texto_total = Entry(
    panel_costos,
    font=('Dosis', 12, 'bold'),
    bd=1,
    width=11,
    state='readonly',
    textvariable=var_total
)
texto_total.grid(row=1, column=5)

# Botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []
columna = 0
for boton in botones:
    boton = Button(
        panel_botones,
        text=boton.title(),
        font=('Dosis', 14, 'bold'),
        fg='white',
        bg='azure4',
        bd=1,
        width=9
    )
    botones_creados.append(boton)
    boton.grid(row=0, column=columna)
    columna += 1

botones_creados[0].config(command=obtener_total)
botones_creados[1].config(command=obtener_recibo)
botones_creados[2].config(command=guardar_recibo)
botones_creados[3].config(command=resetear)

# Área de recibo
texto_recibo = Text(
    panel_recibo,
    font=('Dosis', 12, 'bold'),
    bd=1,
    width=42,
    height=10
)
texto_recibo.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(
    panel_calculadora,
    font=('Dosis', 16, 'bold'),
    width=32,
    bd=1
)
visor_calculadora.grid(row=0, column=0, columnspan=4)
botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', '=', 'Del', '0', '/']
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(
        panel_calculadora,
        text=boton.title(),
        font=('Dosis', 16, 'bold'),
        fg='white',
        bg='azure4',
        bd=1,
        width=8
    )
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna)
    if columna == 3:
        fila += 1
    columna += 1
    if columna == 4:
        columna = 0

# Ojo aquí!
botones_guardados[0].config(command=lambda: clic_boton('7'))
botones_guardados[1].config(command=lambda: clic_boton('8'))
botones_guardados[2].config(command=lambda: clic_boton('9'))
botones_guardados[3].config(command=lambda: clic_boton('+'))
botones_guardados[4].config(command=lambda: clic_boton('4'))
botones_guardados[5].config(command=lambda: clic_boton('5'))
botones_guardados[6].config(command=lambda: clic_boton('6'))
botones_guardados[7].config(command=lambda: clic_boton('-'))
botones_guardados[8].config(command=lambda: clic_boton('1'))
botones_guardados[9].config(command=lambda: clic_boton('2'))
botones_guardados[10].config(command=lambda: clic_boton('3'))
botones_guardados[11].config(command=lambda: clic_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: clic_boton('0'))
botones_guardados[15].config(command=lambda: clic_boton('/'))

# Evitar que la ventana se cierre
aplicacion.mainloop()
