import os
import string
import random
import subprocess
from dotenv import load_dotenv, set_key

# Load existing .env file
load_dotenv('../.env')

# Generate new password
password_length = 10
password_characters = string.ascii_letters + string.digits + string.punctuation
new_password = ''.join(random.choice(password_characters) for i in range(password_length))

# Update .env file
env_path = '../.env'
old_password = os.environ.get('MYSQL_PASSWORD')
set_key(env_path, "MYSQL_PASSWORD", new_password)

# Set environment variable (Note: this only affects the current script, it does not persist after the script ends)
os.environ['MYSQL_PASSWORD'] = new_password

mysql_command = f"ALTER USER 'root'@'localhost' IDENTIFIED BY '{new_password}';"

# Execute command inside MySQL Docker container
docker_command = f"docker exec -i mysql mysql -u root -p {old_password} -e \"{mysql_command}\""
try:
    subprocess.run(docker_command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f'An error occurred while trying to run command inside Docker container: {e}')
