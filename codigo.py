# Titulo WeedZap
# Botao de iniciar chat
    # clicou no botão: 
        # pop-up
            # Titulo: Bem Vindo WeedChat
            # campo: escreva seu nome no chat
            # botão: entrar no chat
# chat
# embaixo do chat
    # campo de digite sua mensagem
    # botão de enviar

# flet -> framework do Python
# pip install flet

#1 importar o flet
import flet as ft

#2 Criar a funcao principal (main)
def main(pagina):
    texto = ft.Text("WeedChat")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        # adicionar mensagem no chat
        texto_entrada = ft.Text(mensagem)
        chat.controls.append(texto_entrada)
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print("Enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario}: {campo_mensagem.value}")
        # limpe o campo mensagem 
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem,botao_enviar])
    def entrar_chat(evento):
        # fechar o popup
        popup.open = False
        # tirar o botão iniciar chat
        pagina.remove(botao_iniciar)
        # tirar o titulo WeedChat
        pagina.remove(texto)
        # criar o chat
        pagina.add(chat) 
        pagina.pubsub.send_all(f"{nome_usuario.value} Chegou para lombrar")
        # colocar o campo de digitar mensagem
        pagina.add(linha_enviar)
        # criar o botão de enviar
        pagina.update()

    titulo_popup = ft.Text("Bem vindo ao WeedChat")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
)

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    # No button 2 coisas o que vai ta escrito no botão e a funcao dele 
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)


#3 criar o app chamando a função principal
ft.app(target=main, view=ft.WEB_BROWSER)

