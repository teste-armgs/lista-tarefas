#!/bin/bash

# Espera o MySQL iniciar
echo "Aguardando MySQL..."

./wait-for-it.sh -h mysql -p 3306 -t 60 -- echo "MySQL está pronto."

echo "MySQL iniciado."

# Executa comando SQL
mysql -h mysql -u root <<EOF
CREATE DATABASE IF NOT EXISTS dblista_tarefa;
USE dblista_tarefa;
CREATE TABLE IF NOT EXISTS tarefas (
    idtarefa INT(11) AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    prioridade int(1) NOT NULL,
    status varchar(10) NOT NULL
);

EOF

echo "Comandos SQL executados."
