class Grammaire:

    def __init__(self) -> None:
        # rules is a dict where key is symbole
        #   and values is set of outputs associated with symbole
        self._initial_symbol = None
        self._rules = dict()
        self._alphabet = set()
        self._variables = set()

    def set_initial_symbol(self, initial_symbol):
        if initial_symbol not in self._variables:
            raise AttributeError("Initial symbol is not defined in alphabet.")

        self._initial_symbol = initial_symbol

    def add_variable(self, variable: str) -> None:
        self._variables.add(variable)

    def add_alphabet(self, alpha_char: str) -> None:
        self._alphabet.add(alpha_char)

    def add_rule(self, symbole: str, output: str) -> None:

        if symbole not in self._variables:
            raise AttributeError(f"Cannot add rule: {symbole} is not defined in variables.")

        for ltr in output:
            if ltr not in self._alphabet.union(self._variables):
                raise AttributeError(
                    f"Cannot add rule: '{ltr}' in output is not included in alphabet or variables. Add to variables first.")

        if symbole not in self._rules:
            self._rules[symbole] = set()

        self._rules[symbole].add(output)

    def remove_rule(self, symbol: str, output: str) -> None:
        if symbol not in self._rules:
            raise AttributeError("Symbole is not in rules")

        if len(self._rules[symbol]) == 1:
            self._rules.pop(symbol)
        else:
            self._rules[symbol].pop(output)

    def has_rule(self, symbol: str, output: str) -> bool:
        # key in rules checked before second cond
        if symbol in self._rules and output in self._rules[symbol]:
            return True

        return False

    def get_first_k(self, k: int, symbol: str) -> set:
        pass

    def get_lookahead(self, symbol: str, output: str, k: int = 100) -> set:
        first_set = set()
        if symbol not in self._rules:
            return first_set

        if output not in self._rules[symbol]:
            return first_set

        if k > 0:
            return first_set

        if symbol == self._initial_symbol:
            initial_rules = output
        else:
            initial_rules = self._rules[self._initial_symbol]

        for rule in initial_rules:
            rule_words = self._get_words(rule, force_use=(symbol, output), k=k)
            first_set.update(rule_words)

        return first_set

    def _proto_contains_variable(self, proto: str) -> bool:
        for ltr in proto:
            if ltr in self._variables:
                return True

        return False

    def _get_words(self, proto: str, force_use: tuple = (None, None), k: int = 100) -> list():
        words = set()
        word = None

        while len(word) < k:

            for ltr in proto:
                if ltr in self._alphabet:
                    word += ltr

                elif ltr in self._variables:
                    if ltr == force_use[0]:
                        rules = {force_use[1]}
                    else:
                        rules = self._rules[ltr]

                    for rule in rules:
                        for sub_word in self._get_words(rule):
                            words.add(word + sub_word)

                else:
                    raise AttributeError(f"{ltr} of proto is not included in alphabet or variables.")

        return words
