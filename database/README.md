# Arete Ethik Database

Run the following command to get SQLAlchemy Models from Database

```
sqlacodegen --outfile test.py postgresql://postgres:postgres@localhost/ae
```

To delete all Tables and Sequences from Database run the following command

```{sql}
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
```
