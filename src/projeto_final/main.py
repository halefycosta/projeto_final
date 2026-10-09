from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
api_key = os.getenv("API_KEY")

print(f"Database Host: {db_host}")
print(f"Database User: {db_user}")
print(f"Database Password: {db_password}")
print(f"Conectando em {db_host} com o usuário {db_user}...")
print("Credenciais carregadas com sucesso!")