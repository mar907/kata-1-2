from tkinter import Tk, Text, Button, END
import re

class Interfaz:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculadora")

         # Crear los widgets
        #Agregar una caja de texto para que sea la pantalla de la calculadora: 
        self.screen = Text(window, state="disabled", width=40, height=3, background="orchid", foreground="white", font=("Helvetica", 15))
        
        #Ubicar la pantalla en la ventana:
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        #Inicializar la operacion mostrada en pantalla como string vacia:
        self.operation=" "
        
        #Crear los botones:
        button1= self.createButton(7)
        button2= self.createButton(8)
        button3= self.createButton(9)
        button4= self.createButton(u"\u232B", write=False)
        button5= self.createButton(4)
        button6= self.createButton(5)
        button7= self.createButton(6)
        button8= self.createButton(u"\u00F7")
        button9= self.createButton(1)
        button10= self.createButton(2)
        button11= self.createButton(3)
        button12= self.createButton("*")
        button13= self.createButton(".")
        button14= self.createButton(0)
        button15= self.createButton("+")
        button16= self.createButton("-")
        button17= self.createButton("=", write=False, ancho=20, alto=2)
        
        #Ubicar los botones con el gestor grid:
        buttons= [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17]
        count = 0
        for row1 in range(1,5):
            for column1 in range(4):
                buttons[count].grid(row=row1, column=column1)
                count+=1
                
        #Ubicar el ultimo boton al final:
        buttons[16].grid(row=5, column=0, columnspan=4)
        
        return
    
    #Crear un boton mostrando el valor pasado por paramatro:
    def createButton (self, value, write=True, ancho=9, alto=1):
        return Button(self.window,text=value, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.click(value, write)) 

    #Controla el evento disparado al hacer click en un boton:
    def click(self, text, write):
        #Si el parametro 'write' es True, entonces el parametro 'text' debe mostrarse en pantalla. Si es False, no.
        if not write:
            #Solo calcular si hay una operacion a ser evaluada y si el usuario presiono '='.
            if text=="=" and self.operation!=" ":
                #Reemplazar el valor unicode de la division por el operador division de Python '/':
                self.operation=re.sub(u"\u00F7", "/",self.operation)
                result=str(eval(self.operation))
                self.operation=" "
                self.cleanScreen()
                self.showInScreen(result)
                #Si se presiono el boton de borrado, limpiar la pantalla:
            elif text==u"\u232B":
                self.operation=" "
                self.cleanScreen()   
                
        #Mostrar texto:    
        else:
            self.operation+=str(text)
            self.showInScreen(text)
        return    
        
    #Borrar el contenido de la pantalla de la calculadora:
    def cleanScreen(self):
            self.screen.configure(state="normal")
            self.screen.delete("1.0" ,END)
            self.screen.configure(state="disabled")
            return
        
    #Muestra en pantalla el contenido de las operacione sy resultados:
    def showInScreen(self, value):
            self.screen.configure(state="normal")
            self.screen.insert(END, value)
            self.screen.configure(state="disabled")
            return


# Crear la ventana principal
window_1 = Tk()

# Crear la instancia de la calculadora
calculadora = Interfaz(window_1)

# Ejecutar la aplicación
window_1.mainloop()