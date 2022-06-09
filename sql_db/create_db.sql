CREATE DATABASE resume_online;
CREATE USER resume_user  WITH PASSWORD 'qwerty123';
ALTER ROLE resume_user SET client_encoding TO 'utf-8';
ALTER ROLE resume_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE resume_user SET timezone TO 'Asia/Bishkek';
GRANT ALL PRIVILEGES ON DATABASE resume_online TO resume_user;
