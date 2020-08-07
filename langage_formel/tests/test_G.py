import pytest
from langage_formel.Grammaire import Grammaire


def setup():
    G = Grammaire()
    G.add_variable("S")
    G.set_initial_symbol("S")
    G.add_alphabet("a")

    return G


def test_add_rule_to_G():
    G = setup()
    G.add_rule("S", "a")

    assert G.has_rule("S", "a")


def test_remove_nonexistant_rule_from_G():
    G = setup()
    with pytest.raises(AttributeError) as e_info:
        G.remove_rule("S", "a")


def test_remove_rule_from_G():
    G = setup()
    G.add_rule("S", "a")
    G.remove_rule("S", "a")

    assert not G.has_rule("S", "a")


def test_first_k_expected_matches_simple_one_rule():
    G = setup()
    G.add_rule("S", "a")

    assert G.get_first_k(1, "S") == {"a"}


def test_first_k_expected_matches_two_rules():
    G = setup()
    G.add_alphabet("b")
    G.add_variable("A")

    G.add_rule("S", "aA")
    G.add_rule("A", "b")

    assert G.get_first_k(1, "S") == {"a"}
    assert G.get_first_k(2, "S") == {"ab"}
    assert G.get_first_k(3, "S") == {"ab"}


def test_first_k_multiple_rules_S():
    G = setup()
    G.add_alphabet("b")
    G.add_alphabet("c")
    G.add_variable("A")

    G.add_rule("S", "aA")
    G.add_rule("S", "c")
    G.add_rule("A", "b")

    assert G.get_first_k(1, "S") == {"a", "c"}
    assert G.get_first_k(2, "S") == {"ab", "c"}
    assert G.get_first_k(3, "S") == {"ab", "c"}


def test_first_k_recursive_rule():
    G = setup()
    G.add_alphabet("b")
    G.add_alphabet("c")

    G.add_rule("S", "aS")
    G.add_rule("S", "c")

    assert G.get_first_k(1, "S") == {"a", "c"}
    assert G.get_first_k(2, "S") == {"c", "aa", "ac"}
    assert G.get_first_k(3, "S") == {"aaa", "aac", "ac", "c"}
