class FringeElement:
    def __init__(self, state, costSoFar, heuristic):
        self.state = state
        self.costSoFar = costSoFar
        self.heuristic = heuristic

def fringePriority(FringeElement):
    cost = FringeElement.costSoFar
    heu = FringeElement.heuristic
    priority = cost + heu
    return priority

def createElement(state, cost, heu):
    return FringeElement(state,cost, heu)