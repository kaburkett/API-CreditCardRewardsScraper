PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE categories (id integer, bank varchar(30), card varchar(20), category varchar(20));
INSERT INTO categories VALUES(1,'Discover','it','');
INSERT INTO categories VALUES(2,'Citi','Simplicity','');
COMMIT;
