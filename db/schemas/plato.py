def plato_schema(plato) -> dict:
    return {
            "id" : str(plato["_id"]),
            "name": plato["name"],
            "precio": plato["precio"],
            "categoria": plato["categoria"],
            "imagen": plato["imagen"],
            "descripcion" : plato["descripcion"]
            }