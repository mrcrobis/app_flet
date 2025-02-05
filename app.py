import flet as ft
import requests

# funcao alvo para a renderizacao
def main(page: ft.Page):
    
    lista_produtos = ft.ListView()

    def cadastrar(event):
        data = {
            'nome': produto.value,
            'preco': preco.value,
            'categoria_id': 1

        }

        response = requests.post('http://127.0.0.1:8000/produtos/produto/', json=data)

        if response.status_code == 200:
            lista_produtos.controls.append(
                ft.Container(
                    ft.Text(produto.value),
                    bgcolor=ft.colors.BLACK12,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10
                )
            )
        page.update()
            

    txt_erro = ft.Container(ft.Text('Erro ao salvar o produto'), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_acerto = ft.Container(ft.Text('Produto salvo com sucesso'), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)

    page.title = 'Cadastro App'
    txt_titulo = ft.Text('Título do produto')
    produto = ft.TextField(label='Digite o título do produto', text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('Preço do produto')
    preco = ft.TextField(value='0', label='Digite o preço do produto', text_align=ft.TextAlign.LEFT)

    btn_produto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)

    page.add(
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto,
        txt_acerto,
        txt_erro
    )


    page.add(
        lista_produtos
    )

# renderiza a page
ft.app(target=main)