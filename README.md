# Gerenciador de Estoque

Este é um aplicativo web simples para gerenciar um estoque de produtos. Ele permite cadastrar, editar, excluir e listar produtos, utilizando a biblioteca FastHTML para a interface e Supabase como backend.

## Funcionalidades

- Cadastrar novos produtos
- Editar informações de produtos existentes
- Deletar produtos do estoque
- Listar todos os produtos cadastrados

## Tecnologias Utilizadas

- Python
- FastHTML
- Supabase
- dotenv

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Samuel-Gaudencio/sistema-de-estoque.git
   cd sistema-de-estoque
   ```
2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configuração do Supabase:**
     - Crie uma conta no Supabase e crie um novo projeto.
     - Configure a tabela ProductStock com os campos necessários: id, nomeProduto, quantidadeEstoque, preco, fotoProduto.
     - Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
      ```bash
      SUPABASE_URL=sua_url_do_supabase
      SUPABASE_KEY=sua_chave_do_supabase
      ```
6. **Execute o aplicativo:**
   ```bash
   python seu_arquivo_principal.py
   ```
   Substitua seu_arquivo_principal.py pelo nome do arquivo onde está o seu código.

## Uso
- Acesse a aplicação no seu navegador (normalmente em http://127.0.0.1:8000).
- Utilize o formulário para adicionar novos produtos e gerenciar o estoque.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
   
