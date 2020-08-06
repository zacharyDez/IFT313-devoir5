import pytest
from langage_formel.Grammaire import Grammaire


def test_add_rule_to_G():
    G = Grammaire()
    G.add_rule("S", "a")

    assert G.has_rule("S", "a")


def test_remove_nonexistant_rule_from_G():
    G = Grammaire()
    with pytest.raises(AttributeError) as e_info:
        G.remove_rule("S", "a")


def test_remove_rule_from_G():
    G = Grammaire()
    G.add_rule("S", "a")
    G.remove_rule("S", "a")

    assert not G.has_rule("S", "a")


def test_first_k_expected_matches():
    G = Grammaire()
    G.add_rule("S", "a")

    assert G.first_k(1, "S") == ["a"]