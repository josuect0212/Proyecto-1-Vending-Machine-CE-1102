from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from datetime import date

key = False
payment = 0
code = '1379'
tran = 0

ventas = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
montos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lista_existencias = [20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20]

lista_bebidas = [['1', 'Coca Cola Classic', '20', '20', '250', '500', '0'], ['2', 'Coca Cola Zero', '20', '20', '250', '500', '0'], ['3', 'Coca Cola Light', '20', '20', '250', '500', '0']
                    , ['4', 'Sprite', '20', '20', '250', '500', '0'], ['5', '7up', '20', '20', '200', '400', '0'], ['6', 'Fanta', '20', '20', '250', '500', '0']
                    , ['7', 'Nestea', '20', '20', '250', '500', '0'], ['8', 'Pepsi', '20', '20', '200', '400', '0'], ['9', 'Diet Pepsi', '20', '20', '200', '400', '0']
                    , ['10', 'Dasani Purified Water', '20', '20', '250', '500', '0']]

lista_productos = [['11', 'Doritos Nacho Cheese', '20', '20', '200', '500', '0'], ['12', 'Doritos Cool Ranch', '20', '20', '200', '500', '0']
                    , ['13', 'Walkers Cheese&Onion', '20', '20', '100', '300', '0'], ['14', 'Walkers Salt&Vinegar', '20', '20', '100', '300', '0']
                    , ['15', 'Hersheys', '20', '20', '400', '1000', '0'], ['16', 'Fanta', '20', '20', '350', '700', '0']]

lista_ventas = []
resumen_ventas = []

with open('notas.txt', 'w') as txt_file:
    for line in lista_bebidas:
        txt_file.write(' '.join(line)+'\n')
    for line in lista_productos:
        txt_file.write(' '.join(line)+'\n')

'''
Esta función se encarga de crear la ventana principal, donde se muestra la máquina expendedora.
Parámetros:
    None
Retorna:
    No retorna
'''
def ventana():
    ventana = Tk()
    ventana.title("Vending Machine")
    ventana.minsize(1280, 720)
    ventana.resizable(width=NO, height=NO)
    ventana.configure(background="#DAF7A6")
    
    '''
    Está función se encarga de agregar los valores de los bótones a una entrada específica
    Parámetros:
        num: valor del botón que se presiona
    Retorna:
        No retorna
    '''
    def btn_click(num):
        current = test0.get()
        test0.delete(0, END)
        test0.insert(0, str(current) + str(num))
    
    '''
    Está función se encarga de eliminar los números contenidos en la entrada para que no se sobreescriban
    Parámetros:
        None
    Retorna:
        No retorna
    '''
    def delete():
        test0.delete(0, END)
    
    '''
    Esta función se encarga de cambiar entre los estados de la llave
    Parámetros:
        None
    Retorna:
        No retorna
    '''
    def Admin():
        global key
        if key == True:
            key = False
            print(key) 
        else:
            key = True
            print(key)
    
    '''
    Está función se encarga de cambiar el resumen de ventas y la lista detallada de las ventas con cada compra, y además se encarga de dar el cambio de la compra, a la vez que reduce la cantidad total de dinero, y también crea una ventana con el producto que se compró, para simular la obtención de este mismo.
    Parámetros:
        None
    Retorna:
        admin_menu, si se introduce el código especial y si la llave esta puesta
    '''
    def buy():
        global key
        global lista_bebidas
        global lista_productos
        global lista_ventas
        global lista_existencias
        global tran
        global buy_win
        global payment
        global ventas
        global montos

        if key == False:
            buy_win = Toplevel(ventana)
            buy_win.geometry('150x100')
            buy_win.config(bg="#b3b3b3")

            valor = test0.get()
            
            if valor == '1' and payment >= 500:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Coca Cola Classic, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=500
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Coca Cola Classic, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_bebidas[0][6]) + 1
                lista_bebidas[0][6] = str(n_ventas)
                label=Label(buy_win, image=img1)
                label.pack()
                payment -= 500
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))

            if valor == '2' and payment >= 500:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Coca Cola Zero, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=500
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Coca Cola Zero, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_bebidas[1][6]) + 1
                lista_bebidas[1][6] = str(n_ventas)
                label=Label(buy_win, image=img2)
                label.pack()
                payment -= 500
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))

            if valor == '3' and payment >= 500:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Coca Cola Light, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=500
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Coca Cola Light, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_bebidas[2][6]) + 1
                lista_bebidas[2][6] = str(n_ventas)
                label=Label(buy_win, image=img3)
                label.pack()
                payment -= 500
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))

            if valor == '4' and payment >= 500 and lista_existencias[int(valor)-1] > 0:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Sprite, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=500
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Sprite, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_bebidas[3][6]) + 1
                lista_bebidas[3][6] = str(n_ventas)
                label=Label(buy_win, image=img4)
                label.pack()
                payment -= 500
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))

            if valor == '5' and payment >= 400 and lista_existencias[int(valor)-1] > 0:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: 7up, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=400
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: 7up, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_bebidas[4][6]) + 1
                lista_bebidas[4][6] = str(n_ventas)
                label=Label(buy_win, image=img5)
                label.pack()
                payment -= 400
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))

            if valor == '6' and payment >= 500:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Fanta, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=500
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Fanta, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_bebidas[5][6]) + 1
                lista_bebidas[5][6] = str(n_ventas)
                label=Label(buy_win, image=img6)
                label.pack()
                payment -= 500
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))

            if valor == '7' and payment >= 500:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Nestea, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=500
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Nestea, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_bebidas[6][6]) + 1
                lista_bebidas[6][6] = str(n_ventas)
                label=Label(buy_win, image=img7)
                label.pack()
                payment -= 500
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))
            
            if valor == '8' and payment >= 400:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Pepsi, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=400
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Pepsi, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_bebidas[7][6]) + 1
                lista_bebidas[7][6] = str(n_ventas)
                label=Label(buy_win, image=img8)
                label.pack()
                payment -= 400
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))
            
            if valor == '9' and payment >= 400:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Diet Pepsi, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=400
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Diet Pepsi, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_bebidas[8][6]) + 1
                lista_bebidas[8][6] = str(n_ventas)
                label=Label(buy_win, image=img9)
                label.pack()
                payment -= 400
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))
            
            if valor == '10' and payment >= 500:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Dasani Purified Water, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=500
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Dasani Purified Water, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_bebidas[9][6]) + 1
                lista_bebidas[9][6] = str(n_ventas)
                label=Label(buy_win, image=img10)
                label.pack()
                payment -= 500
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))
            
            if valor == '11' and payment >= 500:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Doritos Nacho Cheese, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=500
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Doritos Nacho Cheese, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_productos[0][6]) + 1
                lista_productos[0][6] = str(n_ventas)
                label=Label(buy_win, image=img11)
                label.pack()
                payment -= 500
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))
            
            if valor == '12' and payment >= 500:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Doritos Cool Ranch, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=500
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Doritos Cool Ranch, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_productos[1][6]) + 1
                lista_productos[1][6] = str(n_ventas)
                label=Label(buy_win, image=img12)
                label.pack()
                payment -= 500
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))
            
            if valor == '13' and payment >= 300:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Walkers Cheese&Onion, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=300
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Walkers Cheese&Onion, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_productos[2][6]) + 1
                lista_productos[2][6] = str(n_ventas)
                label=Label(buy_win, image=img13)
                label.pack()
                payment -= 300
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))
            
            if valor == '14' and payment >= 300:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Walkers Salt&Vinegar, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=300
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Walkers Salt&Vinegar, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_productos[3][6]) + 1
                lista_productos[3][6] = str(n_ventas)
                label=Label(buy_win, image=img14)
                label.pack()
                payment -= 300
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))
            
            if valor == '15' and payment >= 1000:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Hersheys, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=1000
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: Hersheys, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_productos[4][6]) + 1
                lista_productos[4][6] = str(n_ventas)
                label=Label(buy_win, image=img15)
                label.pack()
                payment -= 1000
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))
            
            if valor == '16' and payment >= 700:
                tran+=1
                lista_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: m&ms, '  + 'Número de transacción: ' + str(tran) + ', ' + 'Fecha: ' + str(date.today()) + ', '+ 'Hora: ' + str(datetime.now())])
                lista_existencias[int(valor)-1]-=1
                ventas[int(valor)-1]+=1
                montos[int(valor)-1]+=700
                resumen_ventas.append(['Código: ' + str(valor) + ', ' + 'Descripción: m&ms, '  + 'Existencia: ' + str(lista_existencias[int(valor)-1]) + ', ' + 'Unidades Vendidas: ' + str(ventas[int(valor)-1]) + ', '+ 'Monto ventas: ' + str(montos[int(valor)-1])])
                n_ventas = int(lista_productos[5][6]) + 1
                lista_productos[5][6] = str(n_ventas)
                label=Label(buy_win, image=img16)
                label.pack()
                payment -= 700
                messagebox.showinfo('Cambio / Change', 'Su cambio es de: / Your change is: \n₡' + str(payment))
                label_cant.config(text='Total: ' + str(payment))

        elif key == True and test0.get() == code:
            return admin_menu()
        else:
            messagebox.showerror('Error','Por favor, remueva la llave / Please remove the key')

    '''
    Esta función muestra el menu de administración de la máquina
    Parámetros:
        None
    Retorna:
        No retorna
    '''
    def admin_menu():
        ventana_admin = Tk()
        ventana_admin.title('Administración de la máquina / Admin Menu')
        ventana_admin.minsize(500,500)
        ventana_admin.resizable(width=NO, height=NO)
        ventana_admin.config(background='#DAF7A6')
        
        '''
        Esta función se encarga de mostrar la lista detallada de las ventas en una nueva ventana
        Parámetros:
            None
        Retorna:
            No retorna
        '''
        def get_lista_ventas():
            listaV = Toplevel(ventana)
            listaV.geometry('900x600')
            listaV.config(bg="#b3b3b3")
            
            labelLV=Message(listaV, text=str(lista_ventas), font=('Baskerville Old Face', 12))
            labelLV.pack()
        
        '''
        Esta función se encarga de mostrar el resumen de ventas en una nueva ventana
        Parámetros:
            None
        Retorna:
            No retorna
        '''
        def get_resumen_ventas():
            listaR = Toplevel(ventana)
            listaR.geometry('900x600')
            listaR.config(bg="#b3b3b3")
            
            labelRV=Message(listaR, text=str(resumen_ventas), font=('Baskerville Old Face', 12))
            labelRV.pack()
        
        btnLV = Button(ventana_admin, text='Reporte de ventas detallado', font=('Baskerville Old Face', 12), command=get_lista_ventas)
        btnLV.pack()
        btnLR = Button(ventana_admin, text='Resumen de ventas', font=('Baskerville Old Face', 12), command=get_resumen_ventas)
        btnLR.pack()

        with open('notas.txt', 'w') as txt_file:
            for line in str(lista_bebidas):
                txt_file.write(' '.join(line)+'\n')
            for line in str(lista_bebidas):
                txt_file.write(' '.join(line)+'\n')

        '''
        Esta función se encarga de mostrar la lista de bebidas
        Parámetros:
            x: variable que se aumenta en 1 por cada bebida de la lista de bebidas, hasta llegar a 10 que es el máximo
            i: variable que funciona como indice para mostrar una lista con información de cada bebida, esta se aumenta en 1 por cada llamada recursiva para mostrar la información de cada una de las bebidas
        Retorna:
            lista_label1: Si x es diferente de 10, se aumenta el valor de x en uno y se aumenta en uno el valor de i
        '''
        def lista_label1(x, i):
            if x == 10:
                return None
            else:
                label = Label(ventana_admin, text='Bebida '+ str(x+1) + ': ' + str(lista_bebidas[i]), font=('Baskerville Old Face', 12))
                label.pack()
                return lista_label1(x+1, i+1)
        
        '''
        Esta función se encarga de mostrar la lista de bebidas
        Parámetros:
            x: variable que se aumenta en 1 por cada bebida de la lista de bebidas, hasta llegar a 6 que es el máximo
            i: variable que funciona como indice para mostrar una lista con información de cada producto, esta se aumenta en 1 por cada llamada recursiva para mostrar la información de cada uno de los productos
        Retorna:
            lista_label2: Si x es diferente de 6, se aumenta el valor de x en uno y se aumenta en uno el valor de i
        '''
        def lista_label2(x, i):
            if x == 6:
                return None
            else:
                label = Label(ventana_admin, text='Producto '+ str(x+1) + ': ' + str(lista_productos[i]), font=('Baskerville Old Face', 12))
                label.pack()
                return lista_label2(x+1, i+1)
        
        lista_label1(0,0)
        lista_label2(0,0)

        '''
        Esta función se encarga de reiniciar el valor de todas las ventas
        Parámetros:
            None
        Retorna:
            reset_sales y reset_sales_productos
        '''
        def reset_sales():
            global lista_bebidas
            global lista_productos

            n_b = len(lista_bebidas)
            n_p = len(lista_productos)
            return reset_sales_bebidas(0, n_b), reset_sales_productos(0, n_p)

        '''
        Esta función se encarga de reiniciar el valor de las ventas de las bebidas
        Parámetros:
            i: variable que funciona como indice para reemplazar el valor de las ventas por 0
            n_b: largo de la lista de bebidas
        Retorna:
            reset_sales_bebidas: si  i es distinto del largo de la lista, se aumenta el valor de i en uno
        '''
        def reset_sales_bebidas(i, n_b):
            global lista_bebidas
            if i == n_b:
                with open('notas.txt', 'w') as txt_file:
                    for line in str(lista_bebidas):
                        txt_file.write(' '.join(line)+'\n')
                    for line in str(lista_bebidas):
                        txt_file.write(' '.join(line)+'\n')
                    lista_label1(0,0)
            else:
                lista_bebidas[i][6] = 0
                return reset_sales_bebidas(i+1, n_b)
        
        '''
        Esta función se encarga de reiniciar el valor de las ventas de los productos
        Parámetros:
            i: variable que funciona como indice para reemplazar el valor de las ventas por 0
            n_p: largo de la lista de productos
        Retorna:
            reset_sales_productos: si  i es distinto del largo de la lista, se aumenta el valor de i en uno
        '''
        def reset_sales_productos(i, n_p):
            global lista_productos
            if i == n_p:
                with open('notas.txt', 'w') as txt_file:
                    for line in str(lista_bebidas):
                        txt_file.write(' '.join(line)+'\n')
                    for line in str(lista_bebidas):
                        txt_file.write(' '.join(line)+'\n')
                    lista_label2(0,0)  
            else:
                lista_productos[i][6] = 0
                return reset_sales_productos(i+1, n_p)


        reset_sales_btn = Button(ventana_admin, text='Reset', font=('Baskerville Old Face', 12), command=reset_sales)
        reset_sales_btn.pack()

        ventana_admin.mainloop


    
    '''
    Esta función se encarga de reiniciar el total de dinero
    Parámetros:
        None
    Retorna:
        No retorna
    '''
    def resetMoney():
        global payment
        payment = 0
        label_cant.config(text='Total: 0')
    
    '''
    Esta función se encarga de sumar el dinero y de mostrar el total
    Parámetros:
        x: valor que se suma a la variable payment
    Retorna:
        No retorna
    '''
    def addMon(x):
        global payment
        payment += x
        label_cant.config(text='Total:' + str(payment))

    canvas = Canvas(ventana, width=400, height=400, background='Gray20', highlightbackground="#BFF83A")
    canvas.place(x=700, y=200)
    label_pago = Label(canvas, text='Elija la cantidad de dinero con la que desea pagar:\n Choose the amount of money you wish to pay with:', bg="#b3b3b3", font=('Baskerville Old Face', 12))
    label_pago.place(x=20,y=20)
    
    bil1000 = ImageTk.PhotoImage(Image.open('Imagenes/mil.png').resize((150,60)))
    btn1000 = Button(canvas, image=bil1000, bg='Gray20', command=lambda: addMon(1000))
    btn1000.place(x=40,y=80)
    bil2000 = ImageTk.PhotoImage(Image.open('Imagenes/2mil.png').resize((150,60)))
    btn2000 = Button(canvas, image=bil2000, bg='Gray20', command=lambda: addMon(2000))
    btn2000.place(x=40,y=160)

    mon100 = ImageTk.PhotoImage(Image.open('Imagenes/moneda100.gif').resize((60,60)))
    btn100 = Button(canvas, image=mon100, bg='Gray20', command=lambda: addMon(100))
    btn100.place(x=260,y=80)
    mon500 = ImageTk.PhotoImage(Image.open('Imagenes/moneda500.gif').resize((60,60)))
    btn500 = Button(canvas, image=mon500, bg='Gray20', command=lambda: addMon(500))
    btn500.place(x=260,y=160)

    btnReset = Button(canvas, text='Reiniciar dinero / Reset money', bg='#b3b3b3', font=('Baskerville Old Face', 12), command=resetMoney)
    btnReset.place(x=20,y=250)

    label_cant = Label(canvas, text='Total: 0', bg='#b3b3b3', font=('Baskerville Old Face', 12))
    label_cant.place(x=190, y=300)

    canvas2 = Canvas(ventana, width=550, height=700, background="Gray", highlightbackground="#BFF83A")
    canvas2.place(x=20, y=10)
    canvas2.create_rectangle(400,560,10,10, width=3, fill='#b3b3b3')


    canvas2.create_line(395,125,15,125, width=20, fill='Gray20')
    img1 = ImageTk.PhotoImage(Image.open('Imagenes/CCC.gif').resize((45,90)))
    canvas2.create_image(60,70, image=img1)
    canvas2.create_text(60,125, text='1 | ₡500', fill='white', font=('Baskerville Old Face', 10))
    img2 = ImageTk.PhotoImage(Image.open('Imagenes/CCZ.gif').resize((45,86)))
    canvas2.create_image(130,70, image=img2)
    canvas2.create_text(130,125, text='2 | ₡500', fill='white', font=('Baskerville Old Face', 10))
    img3 = ImageTk.PhotoImage(Image.open('Imagenes/CCL.gif').resize((45,86)))
    canvas2.create_image(200,70, image=img3)
    canvas2.create_text(200,125, text='3 | ₡500', fill='white', font=('Baskerville Old Face', 10))
    img4 = ImageTk.PhotoImage(Image.open('Imagenes/Sprite.gif').resize((44,85)))
    canvas2.create_image(270,70, image=img4)
    canvas2.create_text(270,125, text='4 | ₡500', fill='white', font=('Baskerville Old Face', 10))
    img5 = ImageTk.PhotoImage(Image.open('Imagenes/7up.gif').resize((44,85)))
    canvas2.create_image(340,70, image=img5)
    canvas2.create_text(340,125, text='5 | ₡400', fill='white', font=('Baskerville Old Face', 10))
    
    canvas2.create_line(395,253,15,253, width=20, fill='Gray20')
    img6 = ImageTk.PhotoImage(Image.open('Imagenes/Fanta.gif').resize((44,85)))
    canvas2.create_image(60,200, image=img6)
    canvas2.create_text(60,253, text='6 | ₡500', fill='white', font=('Baskerville Old Face', 10))
    img7 = ImageTk.PhotoImage(Image.open('Imagenes/Nestea.gif').resize((40,85)))
    canvas2.create_image(130,200, image=img7)
    canvas2.create_text(130,253, text='7 | ₡500', fill='white', font=('Baskerville Old Face', 10))
    img8 = ImageTk.PhotoImage(Image.open('Imagenes/Pepsi.gif').resize((44,85)))
    canvas2.create_image(200,200, image=img8)
    canvas2.create_text(200,253, text='8 | ₡400', fill='white', font=('Baskerville Old Face', 10))
    img9 = ImageTk.PhotoImage(Image.open('Imagenes/DietPepsi.gif').resize((44,85)))
    canvas2.create_image(270,200, image=img9)
    canvas2.create_text(270,253, text='9 | ₡400', fill='white', font=('Baskerville Old Face', 10))
    img10 = ImageTk.PhotoImage(Image.open('Imagenes/Dasani.gif').resize((40,100)))
    canvas2.create_image(340,193, image=img10)
    canvas2.create_text(340,253, text='10 | ₡500', fill='white', font=('Baskerville Old Face', 10))
    
    canvas2.create_line(395,381,15,381, width=20, fill='Gray20')   
    img11 = ImageTk.PhotoImage(Image.open('Imagenes/Doritos.gif').resize((44,80)))
    canvas2.create_image(60,330, image=img11)
    canvas2.create_text(60,381, text='11 | ₡500', fill='white', font=('Baskerville Old Face', 10))
    img12 = ImageTk.PhotoImage(Image.open('Imagenes/DoritosCR.gif').resize((44,80)))
    canvas2.create_image(130,330, image=img12)
    canvas2.create_text(130,381, text='12 | ₡500', fill='white', font=('Baskerville Old Face', 10))
    img13 = ImageTk.PhotoImage(Image.open('Imagenes/WalkersC&O.gif').resize((44,80)))
    canvas2.create_image(200,330, image=img13)
    canvas2.create_text(200,381, text='13 | ₡300', fill='white', font=('Baskerville Old Face', 10))
    img14 = ImageTk.PhotoImage(Image.open('Imagenes/WalkersS&V.gif').resize((44,80)))
    canvas2.create_image(270,330, image=img14)
    canvas2.create_text(270,381, text='14 | ₡300', fill='white', font=('Baskerville Old Face', 10))
    img15 = ImageTk.PhotoImage(Image.open('Imagenes/Hershey.gif').resize((35,80)))
    canvas2.create_image(340,330, image=img15)
    canvas2.create_text(340,381, text='15 | ₡1000', fill='white', font=('Baskerville Old Face', 10))

    canvas2.create_line(395,511,15,511, width=20, fill='Gray20')  
    img16 = ImageTk.PhotoImage(Image.open('Imagenes/m&m.gif').resize((35,80)))
    canvas2.create_image(60,460, image=img16)
    canvas2.create_text(60,511, text='16 | ₡700', fill='white', font=('Baskerville Old Face', 10))

    canvas2.create_rectangle(410,190,530,540, width=3, fill='Gray20')
    test0=Entry(canvas2, bg='Gray30', width=14, fg='white', font=('Baskerville Old Face', 10))
    test0.place(x=427, y=200)

    test1 = Button(canvas2, bg="Gray30", text="1", fg="White", width=2, height=1, command=lambda: btn_click(1))
    test1.place(x=430,y=225)
    test2 = Button(canvas2, bg="Gray30", text="2", fg="White", width=2, height=1, command=lambda: btn_click(2))
    test2.place(x=460,y=225)
    test3 = Button(canvas2, bg="Gray30", text="3", fg="White", width=2, height=1, command=lambda: btn_click(3))
    test3.place(x=490,y=225)
    
    test4 = Button(canvas2, bg="Gray30", text="4", fg="White", width=2, height=1, command=lambda: btn_click(4))
    test4.place(x=430,y=255)
    test5 = Button(canvas2, bg="Gray30", text="5", fg="White", width=2, height=1, command=lambda: btn_click(5))
    test5.place(x=460,y=255)
    test6 = Button(canvas2, bg="Gray30", text="6", fg="White", width=2, height=1, command=lambda: btn_click(6))
    test6.place(x=490,y=255)

    test7 = Button(canvas2, bg="Gray30", text="7", fg="White", width=2, height=1, command=lambda: btn_click(7))
    test7.place(x=430,y=285)
    test8 = Button(canvas2, bg="Gray30", text="8", fg="White", width=2, height=1, command=lambda: btn_click(8))
    test8.place(x=460,y=285)
    test9 = Button(canvas2, bg="Gray30", text="9", fg="White", width=2, height=1, command=lambda: btn_click(9))
    test9.place(x=490,y=285)
    
    test10 = Button(canvas2, bg="Gray30", text="0", fg="White", width=2, height=1, command=lambda: btn_click(0))
    test10.place(x=460, y=315)
    test11 = Button(canvas2, bg="Gray30", text="✓OK", fg="White", width=4, height=1, command=buy)
    test11.place(x=487, y=315)
    test12 = Button(canvas2, bg="Gray30", text="DEL", fg="White", width=4, height=1, command=delete)
    test12.place(x=419, y=315)

    img17 = ImageTk.PhotoImage(Image.open('Imagenes/Lock.gif').resize((40,40)))
    testL = Button(canvas2, image=img17, bg='Gray20', command=Admin)
    testL.place(x=445, y=460)
    img18 = ImageTk.PhotoImage(Image.open('Imagenes/CoinSlot.gif').resize((30,70)))
    testCS = Label(canvas2, image=img18, bg='Gray20')
    testCS.place(x=420, y=355)
    img19 = ImageTk.PhotoImage(Image.open('Imagenes/BillAcceptor.gif').resize((60,50)))
    testBA = Label(canvas2, image=img19, bg='Gray20')
    testBA.place(x=460, y=365)

    '''
    Función que se encarga de apagar la máquina
    Parámetros:
        None
    Retorna:
        No retorna
    '''
    def apagar():
        ventana.destroy()
    
    apagar_btn = Button(canvas2, text='Apagar / Turn Off', bg='Gray20', fg='white', font=('Baskerville Old Face', 10), command=apagar)
    apagar_btn.place(x=420,y=20)

    '''
    Esta función se encarga de crear una ventana que muestra información complementaria
    Parámetros:
        None
    Retorna:
        No retorna
    '''
    def about():
        ventana_about = Tk()
        ventana_about.title("About")
        ventana_about.minsize(800, 800)
        ventana_about.resizable(width=NO, height=NO)
        ventana_about.configure(background="#DAF7A6")

        dato1 = Label(ventana_about, text="Costa Rica", font=('Baskerville Old Face', 14))
        dato1.pack()
        dato2 = Label(ventana_about, text="Tecnológico de Costa Rica, Ingeniería en Computadores", font=('Baskerville Old Face', 14))
        dato2.pack()
        dato3 = Label(ventana_about, text="Taller de Programación, II Semestre 2022, Grupo 1", font=('Baskerville Old Face', 14))
        dato3.pack()
        dato4 = Label(ventana_about, text="Profesor: Jeff Schmidt Peralta", font=('Baskerville Old Face', 14))
        dato4.pack()
        dato5 = Label(ventana_about, text="Autor: Josué Calvo Tijerino", font=('Baskerville Old Face', 14))
        dato5.pack()

        dato6 = Label(ventana_about, text="Librerías utilizadas:", font=('Baskerville Old Face', 14))
        dato6.place(x=20, y=200)
        dato7 = Label(ventana_about, text="datetime\ntkinter\nPIL", font=('Baskerville Old Face', 14),width=10, justify=LEFT)
        dato7.place(x=40, y=240)
        
        dato8 = Label(ventana_about, text='Autores de módulos utilizados: ', font=('Baskerville Old Face', 14))
        dato8.place(x=20, y=400)
        dato9 = Label(ventana_about, text='Codemy.com\nLeMaster Tech', font=('Baskerville Old Face', 14), justify=LEFT)
        dato9.place(x=30, y=440)



        dato10 = Label(ventana_about, text='Instrucciones para el uso de la máquina: ', font=('Baskerville Old Face', 14))
        dato10.place(x=340,y=300)
        dato11 = Label(ventana_about, text='La máquina expendedora tiene 13 botones, de los cuales 10 representan \nvalores númericos, estos serán utilizados para elegir el producto que se desea, \nel botón OK tiene la función de seleccionar el item y el botón DELETE permite \neliminar los digitos previamente introducidos, además de estos, existe el botón llave \nque al activarse permite introducir un código especial para acceder al menú de \nadministración de la máquina. Es importante saber que si la llave está puesta sólo \npermitirá el ingreso del código especial, y la máquina solo dispensará un producto \ncuando haya dinero y cuando la llave no esté puesta. Por otro lado tenemos el dinero, \nel cuál consiste en 4 botones, 1 que representa el billete de 1000 colones, otro que \nrepresenta el billete de 2000 colones, y los otros botones representan las monedas de \n100 y 500 colones, por debajo de estos se encuentra el contador de dinero y un botón \nque permite reiniciar este mismo contador, al hacer una compra el total del \ncontador se reduce con respecto al precio del producto que se compró.', font=('Baskerville Old Face', 10), justify=LEFT)
        dato11.place(x=320,y=340)
        ventana_about.mainloop()
    
    menub=Menu(ventana)
    menub.add_command(label="About", command=about)
    ventana.config(menu=menub)
    
    ventana.mainloop()

ventana()