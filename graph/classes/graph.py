from copy import deepcopy
from typing import Iterable, Union
from .abstract import _Prop, iGraph
from graph.errors import *
from .node import Node


class Graph(iGraph):
    """ undirected graph """

    def __init__(self, nid_type=int, is_digraph=False):
        self._nid_type = nid_type
        self._is_digraph = is_digraph
        self._node_dict = {}  # node ID -> node object

    def get_adjmatrix(self, prop='weight'):
        """get the adjacent matrix"""
        pass

    def add_node(self, v, neighbors=None):
        node = self.check_node(v)

        if node.id in self:
            print("顶点%d已经在该图中" % node.id)
        else:
            self._node_dict[node.id] = node

        if neighbors:
            for u in neighbors:
                self.add_edge(u, v)

    def del_node(self, v):
        """
        删除图中的顶点v，解除与v相关的所有连接
        :param v:
        :return:
        """
        nid = self.check_node_id(v)

        if nid not in self:
            print("顶点%d不在该图中" % nid)
            return

        node = self._node_dict[nid]
        # 解除与node相关的所有连接
        for i in node.neighbors:
            self.get_node(i).del_neighbor(nid)

        del self._node_dict[nid]  # 删除图中的顶点v

    # TODO shortest_path
    def has_path(self, source, target):
        """Returns *True* if *G* has a path from *source* to *target*.

        Parameters
        ----------
        G : NetworkX graph

        source : node
           Starting node for path

        target : node
           Ending node for path
        """
        try:
            self.shortest_path(source, target)
        except PathNotFound:
            return False
        return True

    def copy(self):
        return deepcopy(self)

    def add_edge(self, a, b, weight=None):
        if a not in self:
            self.add_node(a)
        if b not in self:
            self.add_node(b)

        # TODO think about DiGraph
        self._node_dict[a].add_neighbor(self._node_dict[b].id, weight)
        self._node_dict[b].add_neighbor(self._node_dict[a].id, weight)

    def del_edge(self, v, u):
        """
        delete the edge (v,u)
        :param v:
        :param u:
        :return:
        """
        if not isinstance(v, self._nid_type) or not isinstance(u, self._nid_type):
            raise TypeError('a和nbr必须是整型')

        self.get_node(v).del_neighbor(u)
        self.get_node(u).del_neighbor(v)

    def get_node(self, v) -> Node:
        if v in self._node_dict:
            return self._node_dict[v]
        else:
            return None
            # raise NodeNotFound("顶点%d不在该图中" % n)

    def get_nodes(self) -> dict:
        return self._node_dict

    def empty(self) -> bool:
        """
        该图是否为空，即不包含任何节点
        :return:
        """
        return True if not self._node_dict else False

    def has_node(self, v) -> bool:
        nid = self.check_node_id(v)
        return nid in self._node_dict

    def has_nodes(self, v: Iterable) -> bool:
        for i in v:
            if not self.has_node(i):
                return False
        return True

    def has_edge(self, v, u) -> bool:
        return self.has_nodes([v, u]) \
               and u in self.get_node(v).neighbors \
               and v in self.get_node(u).neighbors

    def __contains__(self, n) -> bool:
        if isinstance(n, self._nid_type):  # 节点ID对应的节点是否在图中
            return self.has_node(n)
        elif isinstance(n, list):  # 路径是否在图中
            if len(n) < 2:
                raise ValueError("路径太短：", n)

            first_id = n.pop(0)
            while n:
                next_id = n.pop(0)
                if not self.has_edge(first_id, next_id):
                    return False
                first_id = next_id
            return True
        else:
            raise TypeError("不支持的输入类型：", n)

    def __iter__(self):
        return iter(self._node_dict.values())

    def check_node(self, v, construct=False):
        """ make sure v is a node object, will construct in need"""
        if isinstance(v, Node):
            return v
        elif isinstance(v, self._nid_type):
            return Node(v)
        else:
            raise TypeError('v必须是Node或者整型')

    def check_node_id(self, v):
        """ make sure v is a node id"""
        if isinstance(v, Node):
            return v.id
        elif isinstance(v, self._nid_type):
            return v
        else:
            raise TypeError('v必须是Node或者整型')