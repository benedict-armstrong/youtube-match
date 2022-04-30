--DROP SCHEMA public CASCADE;
--CREATE SCHEMA public;

--GRANT ALL ON SCHEMA public TO postgres;
--GRANT ALL ON SCHEMA public TO public;

CREATE TYPE USER_ROLE AS ENUM ('admin', 'analyst', 'user');

CREATE TABLE IF NOT EXISTS users (
    id SERIAL,
    name VARCHAR(255) NOT NULL,
    nickname VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role USER_ROLE NOT NULL DEFAULT 'user',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_active BOOL NOT NULL DEFAULT TRUE,
    PRIMARY KEY(id)
);

CREATE TYPE ENTITY_TYPE AS ENUM ('company', 'country');
CREATE TABLE IF NOT EXISTS entities (
    id SERIAL,
    name VARCHAR(500) NOT NULL,
    type ENTITY_TYPE NOT NULL,
    short_name VARCHAR(255),
    ISIN VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS entity_names (
    id SERIAL,
    name VARCHAR(500) NOT NULL,
    entity_id INTEGER NOT NULL,
    CONSTRAINT fk_entity FOREIGN KEY(entity_id) REFERENCES entities(id),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS reports (
    id SERIAL,
    title VARCHAR(500) NOT NULL,
    entity_id INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_entity FOREIGN KEY(entity_id) REFERENCES entities(id),
    PRIMARY KEY(id)
);

CREATE TYPE REPORT_VERSION_TYPE AS ENUM ('initial', 'correction', 'change', 'temp');

CREATE TABLE IF NOT EXISTS report_versions (
    id SERIAL,
    version INTEGER[] NOT NULL,
    version_type REPORT_VERSION_TYPE NOT NULL,
    data JSONB NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER NOT NULL,
    report_id INTEGER NOT NULL,
    UNIQUE (report_id, version),
    CONSTRAINT fk_created_by FOREIGN KEY(created_by) REFERENCES users(id),
    CONSTRAINT fk_report FOREIGN KEY(report_id) REFERENCES reports(id),
    PRIMARY KEY(id)
);

CREATE TYPE REPORT_USER_TYPE AS ENUM ('analyst', 'co-analyst');

CREATE TABLE IF NOT EXISTS report_users (
    id SERIAL,
    type REPORT_USER_TYPE NOT NULL,
    report_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    UNIQUE (report_id, user_id),
    CONSTRAINT fk_report FOREIGN KEY(report_id) REFERENCES reports(id),
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(id),
    PRIMARY KEY(id)
);