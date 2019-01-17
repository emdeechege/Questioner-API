from app.connect import init_db, test_init_db, create_tables


connector = init_db()
create_tables(connector)
connector_test = test_init_db()
