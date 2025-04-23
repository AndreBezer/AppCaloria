import customtkinter as ctk
from TelaAdicionar import TelaAdicionar

# Aparencia do aplicativo
ctk.set_appearance_mode("dark")

# Configurações da tela
app = ctk.CTk()
app.title("Contador de Calorias")
app.geometry('400x650')

# Nome do aplicativo
NomeApp = ctk.CTkLabel(app, text="AppCaloria", font=("Arial", 20))
NomeApp.pack(pady=10)

# Cria um botão que leva a tela "TelaAdicionar"
BotaoAdicionar = ctk.CTkButton(
    app,
    text="X",
    command=lambda: TelaAdicionar(app),
    width=50,
    height=50,
    corner_radius=25,
    font=("Arial", 20))
# Posicionar o botão no canto inferior direito
BotaoAdicionar.place(
    relx=1.0,
    rely=1.0,
    anchor="se",
    x=-10,
    y=-10)



app.mainloop()