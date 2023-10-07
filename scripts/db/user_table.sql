CREATE TABLE IF NOT EXISTS "user" (
	id UUID PRIMARY KEY,
	external_id VARCHAR ( 50 ) NOT NULL,
	user_name TEXT NOT NULL,
	created_time TIMESTAMP NOT NULL
);
