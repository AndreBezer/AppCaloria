import customtkinter as ctk

def TelaAdicionar(janela_principal):
    janela_adicionar = ctk.CTkToplevel(janela_principal)
    janela_adicionar.title("Adicionar valor")
    janela_adicionar.geometry("300x400")
    janela_adicionar.resizable(False, False)
    janela_adicionar.grab_set()

    # Nome na parte superior da tela
    ctk.CTkLabel(janela_adicionar, text="Contagem de calorias", font=("Arial", 16)).pack(pady=20)

    framePrimario = ctk.CTkFrame(janela_adicionar)
    framePrimario.pack(pady=10, padx=10, fill="x")

    # input alimento
    ctk.CTkLabel(framePrimario, text="Alimento").pack()
    opcao = ["maça", "banana", "arroz", "feijão" ,"macarrão"]
    combo_alimentos = ctk.CTkComboBox(framePrimario, values=opcao)
    combo_alimentos.pack(pady=5, fill="x")

    # Input gramas 
    ctk.CTkLabel(framePrimario, text="gramas do alimento").pack()
    entrada_alimento = ctk.CTkEntry(framePrimario, placeholder_text="Gramas")
    entrada_alimento.pack(pady=4, padx=5, fill="x")

    def contagemCalorias():
        try:
            calorias = float(entrada_alimento.get())
            calorias = calorias * 2.5
            print(calorias)

            if calorias <= 0:
                raise ValueError("O valor deve ser maior que 0")
        except ValueError as e:
            if not hasattr(janela_principal, "label_erro"):
                
                janela_adicionar.label_erro = ctk.CTkLabel(janela_adicionar, text="", text_color="red")
                janela_adicionar.label_erro.pack(pady=5)
            janela_adicionar.label_erro.configure(text=f"Erro: {str(e)}")

    ### Botão iniciar contagem calorias
    ctk.CTkButton(framePrimario, text="adicionar", command=contagemCalorias,height=50, font=("Arial", 20)).pack(pady=10, padx=25, fill="x")