# test.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("✅ Tous les tests sont passés avec succès !")

test_add()
