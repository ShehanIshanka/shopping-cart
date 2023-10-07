CREATE TABLE IF NOT EXISTS expense (
	id UUID PRIMARY KEY,
	user_id VARCHAR ( 50 ) NOT NULL,
	cat_id UUID NOT NULL,
	value FLOAT NOT NULL,
	currency VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_time TIMESTAMP NOT NULL,
    last_modified_time TIMESTAMP NOT NULL
);

ALTER TABLE expense
    ADD CONSTRAINT FK_expense_user FOREIGN KEY(user_id)
    REFERENCES "user"(id)
    ON DELETE SET NULL;

ALTER TABLE expense
    ADD CONSTRAINT FK_expense_expense_category FOREIGN KEY(cat_id)
    REFERENCES "expense_category"(id)
    ON DELETE SET NULL;