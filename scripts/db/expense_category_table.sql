CREATE TABLE IF NOT EXISTS expense_category (
	id UUID PRIMARY KEY,
	user_id UUID NOT NULL,
	name TEXT NOT NULL,
	created_time TIMESTAMP NOT NULL,
	last_modified_time TIMESTAMP NOT NULL
);

ALTER TABLE expense_category
    ADD CONSTRAINT FK_expense_category_user FOREIGN KEY(user_id)
    REFERENCES "user"(id)
    ON DELETE SET NULL;