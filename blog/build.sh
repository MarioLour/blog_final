#!/usr/bin/env bash
# exit on error
set -o errexit

# Acessa o diretório onde estão os arquivos
cd "$(dirname "$0")"

# Instala os requisitos
pip install -r requirements.txt

# Executa o comando para coletar arquivos estáticos
python manage.py collectstatic --no-input
