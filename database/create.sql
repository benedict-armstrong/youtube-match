-- DROP SCHEMA public CASCADE;
-- CREATE SCHEMA public;

-- GRANT ALL ON SCHEMA public TO postgres;
-- GRANT ALL ON SCHEMA public TO public;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS login_sessions (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    uuid uuid DEFAULT uuid_generate_v4()
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    credentials JSONB,
    state VARCHAR(255),
    login_session_id INTEGER,
    CONSTRAINT fk_login_session FOREIGN KEY(login_session_id) REFERENCES login_sessions(id)
);

CREATE TABLE IF NOT EXISTS subscriptions (
    id SERIAL PRIMARY KEY,
    channel_name VARCHAR(255),
    channel_id VARCHAR(255),
    user_id INTEGER,
    UNIQUE (channel_id, user_id),
    CONSTRAINT fk_users FOREIGN KEY(user_id) REFERENCES users(id)
);
