import customtkinter as ctk

# Aparencia do aplicativo
ctk.set_appearance_mode("dark")

# Configurações da tela
app = ctk.CTk()
app.title("Contador de Calorias")
app.geometry('400x650')

# Nome do aplicativo
NomeApp = ctk.CTkLabel(app, text="AppCaloria", font=("Arial", 20))
NomeApp.pack(pady=10)

app.mainloop()