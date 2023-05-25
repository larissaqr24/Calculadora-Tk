from tkinter import *

root = Tk()
root.title('Calculadora Tk') # titulo
root.geometry('408x355')
root.minsize(408,355) 
root.maxsize(408,355)

numero1 = ''
divisao = FALSE 
multiplicao = FALSE
subtracao = FALSE
adicao = FALSE

root.configure(background='black')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='black', bg='#a7a28f', 
    font=('futura',20, 'bold'), justify=CENTER)
e.grid(
    row = 0,
    column= 0,
    columnspan = 4,
    pady = 2
)

#Funções operadores
def botao_click(num): #parametro vai ser num
    e.insert(END, num) # vai pegar a entrada e vai receber um numero no final
def botao_divisao():
    global numero1  #numero1 é o num do botao_click
    global divisao
    divisao = TRUE
    numero1 = e.get() # vai pegar a entrada do numero1 
    e.delete(0, END) #vai pegar aquela entrada e limpar a entrada
def botao_multiplicao():
    global numero1
    global multiplicao
    multiplicao = TRUE
    numero1 = e.get() 
    e.delete(0, END)
def botao_subtracao():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get() 
    e.delete(0, END)
def botao_adicao():
    global numero1
    global adicao   
    adicao = TRUE
    numero1 = e.get() 
    e.delete(0, END)
def botao_limpar():
    e.delete(0, END)
def botao_igual():
    global subtracao
    global adicao
    global multiplicao
    global divisao
    numero2 = e.get()
    e.delete(0, END)
    if adicao == TRUE:
        e.insert(0,int(numero1) + int(numero2))
        adicao = FALSE
    if multiplicao == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplicao = FALSE
    if subtracao == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE
    if divisao == TRUE:
        e.insert(0, int(numero1) / int(numero2))
        divisao = FALSE


divisao = Button(root,
                text = '/',
                padx= 42,
                pady= 20,
                command = botao_divisao,
                fg='#FFFFFF',
                activeforeground= '#FFFFFF',
                bg= 'black',
                activebackground= 'grey',
                relief=FLAT,
                font=('futura', 12, 'bold')
)

divisao.grid(row=0, column=4)

#primeira fileira
um = Button(root,
            text = '1',
            padx= 40,
            pady= 20,
            command=lambda: botao_click(1),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg= 'black',
            activebackground= 'grey',
            relief=FLAT,
            font= ('futura', 12, 'bold')
)
um.grid(row=1, column=1)

dois = Button(root,
            text = '2',
            padx= 40,
            pady= 20,
            command=lambda: botao_click(2),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg= 'black',
            activebackground= 'grey',
            relief=FLAT,
            font= ('futura', 12, 'bold')
)
dois.grid(row=1, column=2)

tres = Button(root,
            text = '3',
            padx= 43.5,
            pady= 20,
            command=lambda: botao_click(3),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg= 'black',
            activebackground= 'grey',
            relief=FLAT,
            font= ('futura', 12, 'bold')
)
tres.grid(row=1, column=3)

multiplicao= Button(root,
                text = '*',
                padx= 43.5,
                pady= 20,
                command = botao_multiplicao,
                fg='#FFFFFF',
                activeforeground= '#FFFFFF',
                bg= 'black',
                activebackground= 'grey',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
multiplicao.grid(row=1, column=4)

#segunda fileira
quatro = Button(root,
            text = '4',
            padx= 40,
            pady= 20,
            command=lambda: botao_click(4),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg= 'black',
            activebackground= 'grey',
            relief=FLAT,
            font= ('futura', 12, 'bold')
)
quatro.grid(row=2, column=1)

cinco = Button(root,
            text = '5',
            padx= 40,
            pady= 20,
            command=lambda: botao_click(5),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg= 'black',
            activebackground= 'grey',
            relief=FLAT,
            font= ('futura', 12, 'bold')
)
cinco.grid(row=2, column=2)

seis = Button(root,
            text = '6',
            padx= 44,
            pady= 20,
            command=lambda: botao_click(6),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg= 'black',
            activebackground= 'grey',
            relief=FLAT,
            font= ('futura', 12, 'bold')
)
seis.grid(row=2, column=3)

subtracao= Button(root,
                text = '-',
                padx= 44,
                pady= 20,
                command = botao_subtracao,
                fg='#FFFFFF',
                activeforeground= '#FFFFFF',
                bg= 'black',
                activebackground= 'grey',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
subtracao.grid(row=2, column=4)

#terceira fileira
sete = Button(root,
            text = '7',
            padx= 40,
            pady= 20,
            command=lambda: botao_click(7),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg= 'black',
            activebackground= 'grey',
            relief=FLAT,
            font= ('futura', 12, 'bold')
)
sete.grid(row=3, column=1)

oito = Button(root,
            text = '8',
            padx= 40,
            pady= 20,
            command=lambda: botao_click(8),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg= 'black',
            activebackground= 'grey',
            relief=FLAT,
            font= ('futura', 12, 'bold')
)
oito.grid(row=3, column=2)

nove = Button(root,
            text = '9',
            padx= 43.5,
            pady= 20,
            command=lambda: botao_click(9),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg= 'black',
            activebackground= 'grey',
            relief=FLAT,
            font= ('futura', 12, 'bold')
)
nove.grid(row=3, column=3)

adicao= Button(root,
                text = '+',
                padx= 42.5,
                pady= 20,
                command = botao_adicao,
                fg='#FFFFFF',
                activeforeground= '#FFFFFF',
                bg= 'black',
                activebackground= 'grey',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
adicao.grid(row=3, column=4)

#quarta fileira
zero = Button(root,
            text = '0',
            padx= 91,
            pady= 20,
            command=lambda: botao_click(0),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg= 'black',
            activebackground= 'grey',
            relief=FLAT,
            font= ('futura', 12, 'bold')
)
zero.grid(row=4, column=1, columnspan=2)

limpar = Button(root,
            text = 'C',
            padx= 42.5,
            pady= 20,
            command= botao_limpar,
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg= 'black',
            activebackground= 'grey',
            relief=FLAT,
            font= ('futura', 12, 'bold')
)
limpar.grid(row=4, column=3)

igual = Button(root,
            text = '=',
            padx= 43,
            pady= 20,
            command = botao_igual,
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg= 'black',
            activebackground= 'grey',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
igual.grid(row=4, column=4)

root.mainloop()