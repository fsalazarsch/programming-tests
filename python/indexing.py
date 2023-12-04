import json

documents = [
    {
        "age": 12,
        "name": "Mateo",
        "last_name": "González",
    }, 
    {
        "age": 25,
        "name": "Arturo",
        "last_name": "González",
    }, 
    {
        "age": 12,
        "name": "Julián",
        "last_name": "Fernández",
    },
]

def multilevel_indexing(documents, keys):
    aux = {}

    for doc in documents:
      rama = aux

      for key in keys:
        val = doc[key]

        #try:
        # aux[rama[val]] = {}                      
        # except KeyError:
        # aux[rama[val]] = {}
        #pass

        if val not in rama:
          rama[val] = {}
          rama = rama[val]
          #rama.append(doc)            
          rama.update(doc)

  return aux

multilevel_indexing(documents, ["age", "last_name"])