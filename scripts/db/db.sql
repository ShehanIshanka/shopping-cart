CREATE DATABASE storage;
CREATE USER storage_user WITH ENCRYPTED PASSWORD 'storage_user';
GRANT ALL PRIVILEGES ON DATABASE storage TO storage_user;