# ReabilitaSUS

Projeto Django para apresentação institucional da plataforma ReabilitaSUS.

## Como rodar

1. Crie e ative um ambiente virtual Python:

```bash
python -m venv venv
venv\\Scripts\\activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute as migrações:

```bash
python manage.py migrate
```

4. Crie um superusuário (opcional):

```bash
python manage.py createsuperuser
```

5. Inicie o servidor:

```bash
python manage.py runserver
```

6. Acesse `http://127.0.0.1:8000/` no navegador.

## Estrutura

- `reabilitasus/`: configurações do projeto
- `core/`: app principal com páginas e formulário de contato
- `templates/`: templates Django
- `static/css/`: estilos CSS
