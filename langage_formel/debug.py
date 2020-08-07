from langage_formel.Grammaire import Grammaire


def setup():
    G = Grammaire()
    G.add_variable("S")
    G.set_initial_symbol("S")
    G.add_alphabet("a")

    return G


G = setup()
G.add_alphabet("b")
G.add_alphabet("c")

G.add_rule("S", "aS")
G.add_rule("S", "c")

first_2 = G.get_first_k(2, "S")
print(first_2)
