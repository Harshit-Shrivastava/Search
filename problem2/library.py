class FringeElement:
    def __init__(self, state, costSoFar, heuristic, path):
        self.state = state
        self.costSoFar = costSoFar
        self.heuristic = heuristic
        self.path = path

def fringePriority(FringeElement):
    cost = FringeElement.costSoFar
    heu = FringeElement.heuristic
    priority = cost + heu
    return priority

def createElement(state, cost, heu, path):
    return FringeElement(state,cost, heu, path)