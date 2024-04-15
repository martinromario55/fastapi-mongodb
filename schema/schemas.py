

def individual_serial(todo) -> dict:
    """
    Serializes an individual todo item into a dictionary.
    """
    return {
        "_id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "complete": todo["complete"],
    }
    
def list_serial(todos) -> list:
    """
    Serializes a list of todo items into a list of dictionaries.
    """
    return [individual_serial(todo) for todo in todos]