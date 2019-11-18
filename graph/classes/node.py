from utils.checks import check_dict


class Node(object):
    """
    TODO multi-weight Node
    label: uncomputable prop of the node
    weight: computable prop of the node
    """

    def __init__(self, nid, adj=None):
        """
        construct a node
        :param nid: node id, unique in a graph
        :param adj:
        """
        self._neighbors = check_dict(adj)  # TODO dict(nid -> _EdgeProp)
        self._nid = nid

    # TODO
    def weight(self, name=None):
        if name is None:
            return self._neighbors

        if name in self._neighbors:
            return self._neighbors[name]
        else:
            return None

    @property
    def id(self):
        return self._nid

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        else:
            return False

    def __hash__(self):
        return hash(self.id)

    def add_neighbor(self, v, weight=None):
        self._neighbors[v] = weight

    def del_neighbor(self, v):
        del self._neighbors[v]

    def has_neighbor(self, v):
        return v in self._neighbors

    @property
    def neighbors(self) -> [1, 2]:
        return list(self._neighbors.keys())

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self._neighbors])

