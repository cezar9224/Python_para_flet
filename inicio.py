# Projeto aula de app usando Python e a biblioteca flet 
# pip install flet {para instalar o flet} 

# import flet as ft

# def main (pagina): # => função para criação de elementos #
  
#   titulo = ft.Text("HinoZap")

#   def eventobotao(abrirbotao):
#    print("Ola mundo")
#    botao = ft.ElevatedButton("Enviar" , on_click=eventobotao)

#    pagina.add(titulo)
#    pagina.add(botao)
  
# ft.app(main)


import flet as ft

def main(page: ft.Page):
    page.title = "Flet contação examplo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)
