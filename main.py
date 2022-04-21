# GUI import
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox


# Tesseract import
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\netso\Documents\Programação\Projetos\Python\Tesseract\tesseract.exe'
from PIL import Image


# GUI setup
root = Tk()
root.resizable(width=False, height=False)
root.geometry('500x500')
root.title("Formulário de cadastro")

label_0 = Label(root, text="Formulário de cadastro",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_nome = Label(root, text="Nome",width=20,font=("bold", 10))
label_nome.place(x=80,y=130)
entry_nome = Entry(root)
entry_nome.place(x=240,y=130)

label_email = Label(root, text="Email",width=20,font=("bold", 10))
label_email.place(x=68,y=180)
entry_email = Entry(root)
entry_email.place(x=240,y=180)

label_cpf = Label(root, text="CPF",width=20,font=("bold", 10))
label_cpf.place(x=68,y=230)
entry_cpf = Entry(root)
entry_cpf.place(x=240,y=230)

label_nascimento = Label(root, text="Data de nascimento:",width=20,font=("bold", 10))
label_nascimento.place(x=70,y=280)
entry_nascimento = Entry(root)
entry_nascimento.place(x=240,y=280)

label_password = Label(root, text="Password",width=20,font=("bold", 10))
label_password.place(x=70,y=330)
entry_password = Entry(root, show="*")
entry_password.place(x=240,y=330)

label_confirma_password = Label(root, text="Confirma password",width=20,font=("bold", 10))
label_confirma_password.place(x=70,y=380)
entry_confirma_password = Entry(root, show="*")
entry_confirma_password.place(x=240,y=380)

Button(root, text='Upload RG',width=8,height=10,bg='brown',fg='white', command=lambda:open_file()).place(x=380,y=130)
Button(root, text='Cadastrar',width=20,bg='brown',fg='white', command=lambda:show_message()).place(x=180,y=430)


# Funções
def open_file():
    file = askopenfile(parent=root, mode='rb', title='Escolha um arquivo', filetypes=(("Arquivos de imagem", "*.jpg"), ("Todos os arquivos", "*.*")))
    if file:
        text = image_text(file.name)
        dados = get_dados(text)
        entry_nome.delete(0, END)
        entry_nome.insert(END, dados[0])
        entry_cpf.delete(0, END)
        entry_cpf.insert(END, dados[1])
    

def image_text(image_path):
    img = Image.open(image_path)
    text = tess.image_to_string(img)
    return text

def get_dados(text):
    nome = text[78:91]
    cpf =  text[183:195]
    return nome , cpf

def valida_cpf(cpf):
    if len(cpf) != 12:
        return False
    else:
        return True

def valida_password(password):
    if len(password) < 8:
        return False
    elif password.isdigit():
        return False
    elif password.isalpha():
        return False
    else:
        return True

def valida_password_confirma(password, confirma_password):
    if password == confirma_password:
        return True
    else:
        return False

def valida_data(data):
    if len(data) != 10:
        return False
    else:
        return True

def valida_email(email):
    if len(email) < 5:
        return False
    else:
        return True

def verifica_campos():
    if entry_nome.get() == "" or entry_cpf.get() == "" or entry_password.get() == "" or entry_confirma_password.get() == "" or entry_nascimento.get() == "" or entry_email.get() == "":
        return False
    else:
        return True

def show_message():
    if not verifica_campos():
        messagebox.showerror("Erro", "Preencha todos os campos")
    elif not valida_password(entry_password.get()):
        messagebox.showerror("Erro", "Senha inválida")
    elif not valida_password_confirma(entry_password.get(), entry_confirma_password.get()):
        messagebox.showerror("Erro", "Senhas não conferem")
    elif not valida_cpf(entry_cpf.get()):
        messagebox.showerror("Erro", "CPF inválido")
    elif not valida_data(entry_nascimento.get()):
        messagebox.showerror("Erro", "Data inválida")
    elif not valida_email(entry_email.get()):
        messagebox.showerror("Erro", "Email inválido")
   
    else:
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso")
    


# GUI Loop
root.mainloop()



