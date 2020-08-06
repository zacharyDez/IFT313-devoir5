class Grammaire:

    def __init__(self) -> None:
        # rules is a dict where key is symbole
        #   and values is set of outputs associated with symbole
        self.rules = dict()

    def add_rule(self, symbole: str, output: str) -> None:
        if symbole not in self.rules:
            self.rules[symbole] = set()

        self.rules[symbole].add(output)

    def remove_rule(self, symbole: str, output: str) -> None:
        if symbole not in self.rules:
            raise AttributeError("Symbole is not in rules")

        if len(self.rules[symbole]) == 1:
            self.rules.pop(symbole)
        else:
            self.rules[symbole].pop(output)

    def has_rule(self, symbole: str, output: str) -> bool:
        # key in rules checked before second cond
        if symbole in self.rules and output in self.rules[symbole]:
            return True

        return False
