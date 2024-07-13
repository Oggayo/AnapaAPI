from sqlalchemy import MetaData, Table, Column, Integer

metadata = MetaData()

anapa = Table(
   'Anapa',
   metadata,
   Column('id', Integer, primary_key=True),
   Column('Balance', Integer, nullable=False)
)

