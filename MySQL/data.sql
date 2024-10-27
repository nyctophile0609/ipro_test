CREATE DATABASE IF NOT EXISTS ipro_telegram_bot;

CREATE USER IF NOT EXISTS 'ipro_absolute_admin'@'%' IDENTIFIED BY 'iprotbotpasscode';
GRANT ALL PRIVILEGES ON ipro_telegram_bot.* TO 'ipro_absolute_admin'@'%';
FLUSH PRIVILEGES;

USE ipro_telegram_bot;

CREATE TABLE IF NOT EXISTS admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telegram_user_id BIGINT NOT NULL UNIQUE,
    status ENUM('absolute_admin', 'admin') NOT NULL DEFAULT 'admin',
    lang ENUM('uzb', 'rus') NOT NULL DEFAULT 'uzb',
    joined_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telegram_user_id BIGINT NOT NULL UNIQUE,
    lang ENUM('uzb', 'rus') NOT NULL DEFAULT 'uzb',
    joined_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS channels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    for_work_as_admin BOOLEAN DEFAULT FALSE,
    for_post_ads BOOLEAN DEFAULT FALSE,
    for_users_to_follow BOOLEAN DEFAULT FALSE
);

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
);

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
);

CREATE TABLE IF NOT EXISTS ads_partner (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telegram_id BIGINT NOT NULL,
    name VARCHAR(255),
    activity VARCHAR(255),
    phone_number VARCHAR(15),
    territory VARCHAR(255),
    additionals TEXT,
    channel VARCHAR(255)
);
