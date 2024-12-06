import os
import subprocess
from datetime import datetime


def backup_postgresql():
    # Configurações do banco
    db_name = "seu_banco"
    db_user = "seu_usuario"
    db_password = "sua_senha"
    backup_dir = "backups/"
    backup_file = (
        f"{backup_dir}postgres_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
    )

    # Criar o diretório de backup, se não existir
    os.makedirs(backup_dir, exist_ok=True)

    # Comando pg_dump
    command = [
        "pg_dump",
        "-U",
        db_user,
        "-F",
        "c",  # Formato customizado
        "-f",
        backup_file,
        db_name,
    ]

    # Configurando variável de ambiente para senha
    env = os.environ.copy()
    env["PGPASSWORD"] = db_password

    # Executando o comando
    try:
        subprocess.run(command, env=env, check=True)
        print(f"Backup criado em: {backup_file}")
    except subprocess.CalledProcessError as e:
        print("Erro ao criar o backup:", e)
