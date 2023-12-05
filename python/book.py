class SQL:

  seq = 0

  def create(self, table_name="books", *args, **kwargs):
    print("Creando registro nuevo")
    print(table_name)
    print(args)
    print(kwargs)
    SQL.seq += 1
    return SQL.seq

  def update(self, record_id, table_name="books", *args, **kwargs):
    print(f"Actulizando {table_name} con id: {record_id}")
    print(f"Valores: {args}")
    print(kwargs)

  def list(self, table_name="books"):
    print(f"Lista de {table_name}")

  def retrieve(self, record_id, table_name="books"):
    print(f"Se obtiene {record_id} desde {table_name}")

  def delete(self, record_id, table_name="books"):
    print(f"Se elimino {record_id} desde {table_name}")



class Book:
  """Aquí implementar la clase"""
  """ La pondré en ingles para estar en concordancia con la nomencaltura"""
  """ Bajo la suposicion, que tenga nombre, autor e isbn"""
  def __init__(self, name, author, isbn, id):
    self.id = id
    self.name = name
    self.author = author
    self.isbn = isbn
  def save(self, querySql):
    if self.id == None:
      item = querySql.create(record_id =self.id, name=self.name, author=self.author, isbn= self.isbn)
    else:
      item = querySql.update(record_id =self.id, name=self.name, author=self.author, isbn= self.isbn)

  def delete(self, querySql):
    if self.id == None:
      item = querySql.delete(record_id=self.id)
    else:
      pass

  def listing(self, querySql):
    querySql.list()

  def retrieve(self, querySql):
    querySql.retrieve(record_id=self.id)



#querysql = SQL()
#libro1 =Book(name="Estudio en escarlata", author="AC Doyle", isbn="1231231", id= SQL.seq)
#libro1.save(querysql)
#libro1 =Book(id= SQL.seq, name="El signo de los 4", author="AC Doyle", isbn="1231231")
#libro1.save(querysql)

#libro1.listing(querysql)
#libro1.delete(libro1.id)