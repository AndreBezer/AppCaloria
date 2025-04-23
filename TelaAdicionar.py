import customtkinter as ctk

def TelaAdicionar(janela_principal):
    janela_adicionar = ctk.CTkToplevel(janela_principal)
    janela_adicionar.title("Adicionar valor")
    janela_adicionar.geometry("300x400")
    janela_adicionar.resizable(False, False)
    janela_adicionar.grab_set()