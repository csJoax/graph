from abc import ABC, abstractmethod
from utils.checks import check_dict

class iGraph(ABC):
    pass



class _Prop(ABC):
    def __init__(self, weights=None, labels=None):
        self.weights = check_dict(weights)
        self.labels = check_dict(labels)