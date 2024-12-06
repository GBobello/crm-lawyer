import shutil
import os
from datetime import datetime


def backup_sqlite():
    # Caminho para o banco de dados SQLite
    db_path = "db.sqlite3"
    # Diretório para salvar os backups
    backup_dir = "backups/"
    os.makedirs(backup_dir, exist_ok=True)

    # Nome do arquivo de backup com timestamp
    backup_file = os.path.join(
        backup_dir, f"db_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sqlite3"
    )

    # Copiando o arquivo do banco de dados
    shutil.copy(db_path, backup_file)
    print(f"Backup criado em: {backup_file}")
