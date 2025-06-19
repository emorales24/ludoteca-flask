#!/bin/bash

if [ ! command -v pipenv &> /dev/null ]; then
    echo "pipenv no esta instalado.."
    echo "Instalando pipenv..."
    sudo apt-get update
    sudo apt install pipenv
    echo "pipenv instalado."
fi

cd app-backend
pipenv install -r requirements.txt
cd ..

cd app-frontend
pipenv install -r requirements.txt
cd ..