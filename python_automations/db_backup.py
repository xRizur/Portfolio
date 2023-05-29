import subprocess
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv('../.env')

# Database configuration
db_host = "mysql"
db_user = "root"
db_password = os.environ.get('MYSQL_PASSWORD')
db_name = os.environ.get('MYSQL_DATABASE')

# Docker configuration
container_name = "mysql"

# Backup configuration
backup_dir = "/path/to/backup/dir"
backup_file = f"{backup_dir}/backup_{datetime.now().strftime('%Y%m%d%H%M')}.sql"
backup_file_compressed = f"{backup_file}.gz"
backup_file_encrypted = f"{backup_file_compressed}.gpg"

# Encryption configuration
encryption_key = "key"

# Run mysqldump command
dump_cmd = ["docker", "exec", container_name, "mysqldump", "-h", db_host, "-u", db_user, "-p" + db_password, db_name]
with open(backup_file, 'w') as f:
    subprocess.run(dump_cmd, stdout=f, check=True)

# Compress the backup
compress_cmd = ["gzip", backup_file]
subprocess.run(compress_cmd, check=True)

# Encrypt the compressed backup
encrypt_cmd = ["gpg", "--symmetric", "--cipher-algo", "AES256", "--passphrase", encryption_key, "-o", backup_file_encrypted, backup_file_compressed]
subprocess.run(encrypt_cmd, check=True)

# Delete the compressed backup after encryption
subprocess.run(["rm", backup_file_compressed], check=True)