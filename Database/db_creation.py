import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
localhost=os.getenv("MYSQL_HOST")
user=os.getenv("MYSQL_USERNAME")
root_user=os.getenv("MYSQL_ROOT_USER")
root_user_password=os.getenv("MYSQL_ROOT_USER_PASSWORD")
password=os.getenv("MYSQL_PASSWORD")
database=os.getenv("MYSQL_DATABASE")


# db_connection = mysql.connector.connect(
#     host=localhost,
#     user=user,
#     password=password,
#     database=database,
#     auth_plugin="caching_sha2_password"
# )

db_connection = mysql.connector.connect(
    host=localhost,
    user=root_user,
    password=root_user_password,
    auth_plugin="caching_sha2_password"
)
cursor = db_connection.cursor()


cursor.execute(f"CREATE USER IF NOT EXISTS '{user}'@'%' IDENTIFIED BY '{password}';")
cursor.execute(f"GRANT ALL PRIVILEGES ON {database}.* TO '{user}'@'%';")
cursor.execute("FLUSH PRIVILEGES;")

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database};")
cursor.execute(f"USE {database};")


cursor.execute("""
CREATE TABLE IF NOT EXISTS admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telegram_user_id BIGINT NOT NULL UNIQUE,
    status ENUM('absolute_admin', 'admin') NOT NULL DEFAULT 'admin',
    lang ENUM('uzb', 'rus') NOT NULL DEFAULT 'uzb',
    joined_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
db_connection.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telegram_user_id BIGINT NOT NULL UNIQUE,
    lang ENUM('uzb', 'rus') NOT NULL DEFAULT 'uzb',
    joined_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
db_connection.commit()


cursor.execute("""
CREATE TABLE IF NOT EXISTS channels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    for_work_as_admin BOOLEAN DEFAULT FALSE,
    for_post_ads BOOLEAN DEFAULT FALSE,
    for_users_to_follow BOOLEAN DEFAULT FALSE
)
""")
db_connection.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ads_vacancy (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telegram_id BIGINT NOT NULL,
    skills TEXT,
    company VARCHAR(255),
    activity VARCHAR(255),
    hr VARCHAR(255),
    phone_number VARCHAR(15),
    territory VARCHAR(255),
    request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    work_time VARCHAR(255),
    salary VARCHAR(255),
    additionals TEXT,
    channel VARCHAR(255)
)
""")
db_connection.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ads_employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telegram_id BIGINT NOT NULL,
    name VARCHAR(255),
    age VARCHAR(255),
    job VARCHAR(255),
    experience VARCHAR(255),
    phone_number VARCHAR(15),
    territory VARCHAR(255),
    salary VARCHAR(255),
    additionals TEXT,
    channel VARCHAR(255)
)
""")
db_connection.commit()


cursor.execute("""
CREATE TABLE IF NOT EXISTS ads_partner (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telegram_id BIGINT NOT NULL,
    name VARCHAR(255),
    activity VARCHAR(255),
    phone_number VARCHAR(15),
    territory VARCHAR(255),
    additionals TEXT,
    channel VARCHAR(255)
)
""")
db_connection.commit()


cursor.close()
db_connection.close()