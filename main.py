from fasthtml.common import *
from components import *

# Inicializa o aplicativo e as rotas
app, rts = fast_app()

# Rota para a página inicial
@rts("/")
def homepage():
    return Titled("Estoque", render_form(), render_product_list())

# Rota para cadastrar um produto
@rts("/cadastrar-produto", methods=["post"])
def post(nomeProduto: str, quantidadeEstoque: int, preco: float, fotoProduto: str):
    add_product(nomeProduto, quantidadeEstoque, preco, fotoProduto)
    return render_product_list()

# Rota para deletar um produto
@rts("/deletar/{id}")
def delete(id: int):
    pop_product(id)
    return render_product_list()

# Rota para editar um produto
@rts("/editar-produto", methods=["post"])
def post_edit(id: int, nomeProduto: str, quantidadeEstoque: int, preco: float, fotoProduto: str):
    update_product(id, nomeProduto, quantidadeEstoque, preco, fotoProduto)
    return render_product_list()

# Rota para mostrar o formulário de edição
@rts("/editar/{id}")
def edit(id: int):
    entry = supabase.table("ProductStock").select("*").eq('id', id).execute().data[0]
    return render_edit_form(entry)

# Inicia o servidor
serve()
