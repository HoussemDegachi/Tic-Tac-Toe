from project import Table
import pytest


def test_add():
    table = Table()
    with pytest.raises(ValueError):
        table.add("a9", "x")
    with pytest.raises(TypeError):
        table.add("a1", "y")
    table.add("a1", "x") == None
    table.add("a2", "x") == None
    table.add("a3", "x") == "x"
    table = Table()
    table.add("a1", "o") == None
    table.add("a2", "o") == None
    table.add("a3", "o") == "o"
    table = Table()
    table.add("a1", "x") == None
    table.add("b1", "o") == None
    table.add("c1", "x") == None
    table.add("b2", "o") == None
    table.add("a2", "x") == None
    table.add("c2", "o") == None
    table.add("b3", "x") == None
    table.add("a3", "o") == None
    table.add("c3", "x") == "tie"


def test_generate_table():
    assert Table().generate_table() == {
        "a1": None,
        "a2": None,
        "a3": None,
        "b1": None,
        "b2": None,
        "b3": None,
        "c1": None,
        "c2": None,
        "c3": None,
    }

def test_generate_possibilites():
    assert Table().generate_possibilities() == [['a1', 'b2', 'c3'], ['a3', 'b2', 'c1'], ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'], ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3']]