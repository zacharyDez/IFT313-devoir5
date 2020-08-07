import queue


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

    def _are_first_k_params_valid(self, k: int, symbol: str, rule: str) -> tuple:
        if symbol not in self._variables:
            return False, symbol

        if rule not in self._rules[symbol]:
            return False, rule

        if k <= 0:
            return False, k

        return True

    def _proto_contains_variable(self, proto: str) -> bool:
        for ltr in proto:
            if ltr in self._variables:
                return True

        return False

    def _get_first_k(self, k: int, symbol: str, rules: set) -> set:
        # implementation following
        #   http://www.seanerikoconnor.freeservers.com/ComputerScience/Compiler/ParserGeneratorAndParser/QuickReviewOfLRandLALRParsingTheory.html#FIRSTk
        first_k = set()
        for rule in rules:
            first_k.update(self._get_first_k_single_rule(k, symbol, rule))

        return first_k

    def _get_first_k_single_rule(self, k: int, symbol: str, rule: str, max_depth: int = 30):
        self._are_first_k_params_valid(k, symbol, rule)

        first_set = set()
        if not self._proto_contains_variable(rule):
            first_set.add(rule[:k])

        else:
            words = self._approx_first(rule, max_depth=max_depth)
            for word in words:
                first_set.add(word[:k])

        return first_set

    def get_first_k(self, k: int, symbol: str) -> set:
        rules = self._rules[symbol]
        return self._get_first_k(k, symbol, rules)

    def _approx_first(self, proto, max_depth):
        words = set()

        protos = queue.Queue()
        protos.put(proto)

        cur_depth = 0
        while not protos.empty() and cur_depth < max_depth:
            tmp_proto = protos.get()
            self._approx_first_inner(tmp_proto, protos, words)
            cur_depth += 1

        return words

    def _approx_first_inner(self, proto: str, protos: queue.Queue, words: set) -> None:
        if not self._proto_contains_variable(proto):
            words.add(proto)
            return

        for i in range(len(proto)):
            if proto[i] in self._variables:
                for rule in self._rules[proto[i]]:
                    new_proto = proto[:i] + rule + proto[i + 1:]
                    protos.put(new_proto)
                return
