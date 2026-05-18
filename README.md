# Project_Agenda

Este documento contém os comandos específicos e caminhos necessários para executar, migrar e gerenciar o projeto Django **Project_Agenda** utilizando o interpretador Python correto da sua máquina.

---

## Comandos de Execução (Compilação)

Devido à presença do ambiente MSYS2 no sistema, o comando padrão `python` pode falhar. Utilize sempre o caminho absoluto do executável Python oficial instalado no seu usuário para garantir o funcionamento correto.

### 1. Aplicar Migrações (Banco de Dados PostgreSQL)
Sempre que modificar os modelos ou inicializar o banco de dados pela primeira vez, execute este comando para estruturar as tabelas no PostgreSQL:

```bash
C:\\Users\\kaiqu\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe manage.py migrate

```

### 2. Iniciar o Servidor de Desenvolvimento

Para compilar e rodar a aplicação localmente no navegador, utilize o comando abaixo:

```bash
C:\\Users\\kaiqu\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe manage.py runserver

```

Após executar, o projeto estará disponível no endereço: [http://127.0.0.1:8000/](https://www.google.com/search?q=http://127.0.0.1:8000/)

### 3. Criar novos Módulos/Apps (Se necessário)

Caso precise criar uma nova aplicação isolada dentro do projeto futuramente:

```bash
C:\\Users\\kaiqu\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe manage.py startapp nome_do_app

```

### 4. Criar um Superusuário (Painel Administrativo)

Para criar uma conta de administrador e acessar o painel em `/admin`:

```bash
C:\\Users\\kaiqu\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe manage.py createsuperuser

```

---

## Estrutura do Projeto Atual

* **`core/`**: Configurações principais do Django (`settings.py`, `urls.py`).
* **`agenda_app/`**: Aplicativo principal onde ficarão as regras de negócio da agenda.
* **`templates/`**: Arquivos HTML estruturais da aplicação.
* **`static/`**: Arquivos estáticos (CSS, JavaScript, Imagens).
* **`media/`**: Arquivos de upload dinâmicos enviados por usuários.
* **`manage.py`**: Script de gerenciamento de comandos do Django.

### comandos
- user: kayque
- pass: asdfjkll



> Conteudos:
- Criando e editando a senha de um super usuário Django.
- Sobre base de dados, tabelas e documentação do Django
- make makemigrations sempre quando altera algo no codigo no model e etc

> python.exe manage.py migrate
> C:\\Users\\kaiqu\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe manage.py makemigrations
> C:\\Users\\kaiqu\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe manage.py migrate