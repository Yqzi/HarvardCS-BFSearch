import heapq

class Node():
    def __init__(self, state, parent, action, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def __init__(self):
        self.frontier = []
        self.steps = 0

    def add(self, node, prio):
        heapq.heappush(self.frontier, (prio, self.steps, node))
        self.steps += 1
    
    def contains_state(self, state):
        return any(node.state == state for _, _, node in self.frontier)

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            _, _, node = heapq.heappop(self.frontier)
            return node
