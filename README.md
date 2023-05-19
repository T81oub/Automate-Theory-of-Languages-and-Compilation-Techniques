# Automaton Determinization

This is a Python script that demonstrates automaton determinization. It includes a class called `Automate` that represents a non-deterministic automaton and provides methods for determinization and checking if a string is accepted by the automaton.

## Installation

To run this script, you need to install the `graphviz` package. You can install it using pip:
pip install graphviz

## Usage

```python
from graphviz import Digraph

class Automate:
    def __init__(self, alphabet, states, initial_state, final_states, transitions):
        # Constructor code...

    def is_deterministic(self):
        # Method code...

    def has_epsilon_transitions(self):
        # Method code...

    def to_graphviz(self):
        # Method code...

    def determinize(self):
        # Method code...

    def display(self):
        # Method code...

    def epsilon_closure(self, states):
        # Method code...

    def determinize_with_epsilon(self):
        # Method code...

    def accepts_string(d_automaton, input_string):
        # Method code...

# Example usage

if __name__ == '__main__':
    # Create an instance of the Automate class
    automate = Automate(alphabet, states, initial_state, final_states, transitions)

    # Display the input Automate
    automate.display()

    if automate.is_deterministic():
        print("The automaton is deterministic.")
    else:
        print("The automaton is not deterministic.")

        if automate.has_epsilon_transitions() == False:
            print("The automaton does not use epsilon transitions.")
            d_automate = automate.determinize()
            print("New deterministic automaton:")
            d_automate.display()
        else:
            print("The automaton uses epsilon transitions.")
            d_automate = automate.determinize_with_epsilon()
            print("New deterministic automaton:")
            d_automate.display()

        dot = d_automate.to_graphviz()
        dot.format = 'png'
        dot.render('automaton', view=True)

    if d_automate != None:
        automate = d_automate

    if automate.accepts_string(input_string):
        print(f"The automaton accepts the input string '{input_string}'")
    else:
        print(f"The automaton does not accept the input string '{input_string}'")
```
Make sure to replace the variables alphabet, states, initial_state, final_states, transitions, and input_string with your own values.
## Documentation
For detailed documentation and explanations of the code, please refer to the accompanying PowerPoint presentation here.

Feel free to modify and enhance this script to meet your specific requirements and additional features.
