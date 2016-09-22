class FringeElement:
    def __init__(self, state, cost_so_far, heuristic, path):
        self.state = state
        self.cost_so_far = cost_so_far
        self.heuristic = heuristic
        self.path = path


def fringe_priority(fringe_element):
    cost = fringe_element.cost_so_far
    heu = fringe_element.heuristic
    priority = cost + heu
    return priority


def create_element(state, cost, heu, path):
    return FringeElement(state, cost, heu, path)
