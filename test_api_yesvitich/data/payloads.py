def create_object_payload():
    return {
        "name": "Yegor's object",
        "data": {
            "name": "Yegor",
            "surname": "Svitich",
        }
    }

def update_object_payload():
    return {
        "name": "Yegor's object (updated)",
        "data": {
            "name": "Yegor (updated)",
            "surname": "Svitich (updated)"
        }
    }

def patch_object_payload():
    return {
        "data": {
            "name": "Yuri",
            "surname": "Svitich"
        }
    }

CREATE_OBJECT_DATA = [
    ("Yegor's object 1", {"Yegor 1": "Svitich 1"}),
    ("Yegor's object 2", {"Yegor 2": "Svitich 2"}),
    ("Yegor's object 3", {"Yegor 3": "Svitich 3"})
]
