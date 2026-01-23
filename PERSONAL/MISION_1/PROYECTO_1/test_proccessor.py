from proccessor import clean_id, merge_name

def test_clean_id(): # Prueba para la función clean_id - puede tener cualquier nombre
    assert clean_id("cc-75.077.60") == "7507760"

#assert es una palabra reservada en python que se usa para hacer afirmaciones en las pruebas unitarias

# Name

def test_merge_name():
    assert merge_name("Laura", "Ospina") == "Laura Ospina"



