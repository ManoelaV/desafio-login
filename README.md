# Meu Projeto Django

Este projeto é uma aplicação Django que implementa uma tela de login com funcionalidades de validação de e-mail e senha, tratamento de erros e redirecionamento para as telas de registro e menu.

## Estrutura do Projeto

meu_projeto_django
├── meu_projeto_django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── login_app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── README.md

## Instalação

1. Clone o repositório:
  
   git clone <URL_DO_REPOSITORIO>

2. Navegue até o diretório do projeto:
  
   cd meu_projeto_django
  
3. Crie um ambiente virtual:
  
   python -m venv venv
  
4. Ative o ambiente virtual:
   - No Windows:

     venv\Scripts\activate

   - No macOS/Linux:

     source venv/bin/activate

5. Instale as dependências:
  
   pip install django
  
6. Execute as migrações:
  
   python manage.py migrate

7. Inicie o servidor de desenvolvimento:

   python manage.py runserver
  
## Uso

- Acesse a aplicação em seu navegador através do endereço `http://127.0.0.1:8000/`.
- Utilize a tela de login para autenticar-se.
- Caso não tenha uma conta, você pode ser redirecionado para a tela de registro.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Faça um fork do repositório e envie suas pull requests.

## Licença

Este projeto está licenciado sob a MIT License.
