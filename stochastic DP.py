

from stochasticdp import StochasticDP
# Number of stages
number_of_stages = 4
# List of states
states = [0, 5000, 10000]
# List of decisions
decisions = ['A', 'B', 'no investment']
# Initialize stochastic dynamic program - we want to maximize, so minimize = False
dp = StochasticDP(number_of_stages, states, decisions, minimize=False)
# Transition probabilities and contributions from state n = 5000
for t in range(number_of_stages - 1):
# Investment A
    dp.add_transition(stage=t, from_state=5000, decision='A', to_state=10000,
                      probability=0.7, contribution=0)
    dp.add_transition(stage=t, from_state=5000, decision='A', to_state=0,
                      probability=0.3, contribution=0)
# Investment B
    dp.add_transition(stage=t, from_state=5000, decision='B', to_state=10000,
                      probability=0.1, contribution=0)
    dp.add_transition(stage=t, from_state=5000, decision='B', to_state=5000,
                      probability=0.9, contribution=0)
# No investment
    dp.add_transition(stage=t, from_state=5000, decision='no investment',
                      to_state=5000, probability=1, contribution = 0)
# Transition probabilities and contributions from state n = 0
for t in range(number_of_stages - 1):
# No investment
    dp.add_transition(stage=t, from_state=0, decision='no investment', to_state=0,
                      probability=1, contribution = 0)
# Transition probabilities and contributions from state n = 10000
for t in range(number_of_stages - 1):
# No investment
    dp.add_transition(stage=t, from_state=10000, decision='no investment',
                      to_state=10000, probability=1, contribution = 0)
# Boundary conditions
dp.add_boundary(state=10000, value=1)
dp.add_boundary(state=5000, value=0)
dp.add_boundary(state=0, value=0)
value, policy = dp.solve()

print(value)
print(policy)