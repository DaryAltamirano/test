from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["DB_USER"]
password = os.environ["DB_PASSWORD"]
host = os.environ["DB_HOST"]
database = os.environ["DB_DATABASE"]
port = os.environ["DB_PORT"]


DATABASE_CONNECTION_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
#DATABASE_CONNECTION_URI = f'oracle+crx_oracle://{user}:{password}@{host}:{port}/{database}'