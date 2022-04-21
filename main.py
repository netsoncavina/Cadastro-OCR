from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Formulário de cadastro")

label_0 = Label(root, text="Formulário de cadastro",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Nome",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="CPF",width=20,font=("bold", 10))
label_3.place(x=68,y=230)

entry_3 = Entry(root)
entry_3.place(x=240,y=230)

# label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
# label_3.place(x=70,y=230)
# var = IntVar()
# Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
# Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Idade:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)


entry_2 = Entry(root)
entry_2.place(x=240,y=280)

Button(root, text='Upload RG',width=8,height=10   ,bg='brown',fg='white').place(x=380,y=130)
Button(root, text='Enviar',width=20,bg='brown',fg='white').place(x=180,y=380)
# it is use for display the registration form on the window
root.mainloop()
