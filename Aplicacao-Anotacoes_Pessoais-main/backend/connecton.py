from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@db:5432/mydatabase')