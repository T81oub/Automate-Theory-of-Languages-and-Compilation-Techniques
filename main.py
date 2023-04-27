from collections import deque
class Automate:
    def __init__(self, alphabet, states, initial_state, final_states, transitions):
        self.alphabet = alphabet
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions

    def has_epsilon_transitions(self):
        for state, transitions in self.transitions.items():
            if 'Epsilon' in transitions.keys():
                return True
        return False

    def is_deterministic(self):
        for state in self.states:
            for char in self.alphabet:
                if char in self.transitions[state]:
                    if len(self.transitions[state][char]) != 1:
                        return False
        return True

    def convert_to_deterministic(self):
        if self.is_deterministic():
            return self
        else:
            # Apply the powerset construction algorithm
            new_states = set()
            new_transitions = {}
            new_initial_state = frozenset({self.initial_state})
            new_final_states = set()
            stack = [new_initial_state]

            while stack:
                current_states = stack.pop()
                new_states.add(current_states)

                for char in self.alphabet:
                    next_states = set()
                    for state in current_states:
                        if char in self.transitions[state]:
                            next_states.update(self.transitions[state][char])
                    if next_states:
                        new_transitions.setdefault(current_states, {})[char] = frozenset(next_states)
                        if frozenset(next_states) not in new_states:
                            stack.append(frozenset(next_states))

                if current_states.intersection(self.final_states):
                    new_final_states.add(current_states)

            return Automate(self.alphabet, new_states, new_initial_state, new_final_states, new_transitions)

    def accepts(self, input_string):
        current_state = self.initial_state

        print("Chaîne testée:", input_string)

        for char in input_string:

            if char not in self.alphabet:

                return False
            if char in self.transitions[current_state]:
                if isinstance(current_state, frozenset):
                    print("---{} {}".format(set(current_state), char))
                else:
                    print("---{} {}".format(current_state, char))


                if(len(self.transitions[current_state][char]) == 0):
                    break
                else:
                    if isinstance(self.transitions[current_state][char], frozenset):
                        current_state = self.transitions[current_state][char]
                    else:
                        current_state = self.transitions[current_state][char].pop()





            else:

                if isinstance(current_state, frozenset):
                    print("---{} {}".format(set(current_state), char))
                else:
                    print("---{} {}".format(current_state, char))
                return False
        if isinstance(current_state, frozenset):
            print("---{}".format(set(current_state)))
        else:
            print("---{}".format(current_state))


        result = current_state in self.final_states
        print("Résultat:", result)

    def epsilon_closure(self, state):
        closure = set()
        stack = [state]
        while stack:
            current_state = stack.pop()
            closure.add(frozenset(current_state))
            if current_state in self.epsilon_transitions:
                for next_state in self.epsilon_transitions[current_state]:
                    if next_state not in closure:
                        stack.append(next_state)
        return closure

    def move(self, state, symbol):
        return self.transitions.get(state, {}).get(symbol, set())

    def convert_to_dfa(self):
        dfa_states = set()
        dfa_transitions = {}
        dfa_initial_state = frozenset(self.epsilon_closure(self.initial_state))
        dfa_final_states = set()
        unmarked_states = deque([dfa_initial_state])
        while unmarked_states:
            current_state = unmarked_states.popleft()
            if current_state not in dfa_states:
                dfa_states.add(current_state)
                for symbol in self.alphabet:
                    next_state = frozenset().union(
                        *[self.epsilon_closure(s) for s in [self.move(s, symbol) for s in current_state]])
                    dfa_transitions.setdefault(current_state, {})[symbol] = next_state
                    if next_state not in dfa_states:
                        unmarked_states.append(next_state)
                if any(state in self.final_states for state in current_state):
                    dfa_final_states.add(current_state)
        return Automate(self.alphabet, dfa_states, dfa_initial_state, dfa_final_states, dfa_transitions)

if __name__ == '__main__':
    alphabet = {'a', 'b', 'c'}
    etats = {'q1', 'q2', 'q3', 'q4'}
    etat_initial = 'q1'
    etats_finaux = {'q2','q4'}
    transitions = { 'q1': {'a': {'q2'}}, 'q2': {'a': {'q2'},'b': {'q3'}}, 'q3':{'c': {'q4'}}, 'q4': {'a': {'q2'}} }

    automate = Automate(alphabet, etats, etat_initial, etats_finaux, transitions)
    if automate.has_epsilon_transitions():
        print("The Automate has epsilon transitions.")
        dfa_automate = automate.convert_to_dfa()

        print("DFA states:", dfa_automate.states)
        print("DFA initial state:", dfa_automate.initial_state)
        print("DFA final states:", dfa_automate.final_states)

    else:
        print("The Automate does not have epsilon transitions.")
        if (automate.is_deterministic()):
            print("L'automate est bien deterministe")
        else:
            automate = automate.convert_to_deterministic()
            print("L'automate n'est pas déterministe. Nouvel automate déterminisé :")
            print(automate.alphabet)
            print([list(state) for state in automate.states])
            print(list(automate.initial_state)[0])
            print([list(state) for state in automate.final_states])
            print({tuple(list(key)): {k: list(val) for k, val in value.items()} for key, value in
                   automate.transitions.items()})


    print(automate.accepts('aabc'))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
