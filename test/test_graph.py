from unittest import TestCase
from graph.classes.graph import Graph
from graph.classes.node import Node


class TestGraph(TestCase):
    def test_get_adjmatrix(self):
        # TODO self.fail()
        pass

    def test_add_node(self):
        g = Graph()
        g.add_node(1)
        self.assertIn(1, g.get_nodes())

    def test_del_node(self):
        g = Graph()
        g.add_node(1)
        self.assertIn(1, g.get_nodes())
        g.del_node(1)
        self.assertNotIn(1, g.get_nodes())

    def test_has_path(self):
        # TODO self.fail()
        pass

    def test_copy(self):
        g = Graph()
        cp = g.copy()
        self.assertNotEqual(id(g), id(cp))

    def test_add_edge(self):
        g = Graph()
        g.add_node(1)
        g.add_node(3)
        g.add_node(2, [1, 3])
        self.assertTrue(g.has_edge(1, 2))
        self.assertTrue(g.has_edge(3, 2))
        self.assertFalse(g.has_edge(1, 3))

    def test_del_edge(self):
        g = Graph()
        g.add_node(1)
        g.add_node(3)
        g.add_node(2, [1, 3])
        self.assertTrue(g.has_edge(1, 2))
        self.assertTrue(g.has_edge(3, 2))
        self.assertFalse(g.has_edge(1, 3))
        g.del_edge(1, 2)
        self.assertFalse(g.has_edge(1, 2))

    def test_get_node(self):
        g = Graph()
        g.add_node(1)
        g.add_node(3)
        g.add_node(2, [1, 3])
        n = g.get_node(1)
        self.assertIsInstance(n, Node)
        self.assertEqual(n.id, 1)

    def test_get_nodes(self):
        g = Graph()
        g.add_node(1)
        g.add_node(3)
        g.add_node(2, [1, 3])

        v_ids = [1, 2, 3]
        node_dict = g.get_nodes()
        for i in v_ids:
            self.assertIn(i, node_dict)

    def test_empty(self):
        g = Graph()
        self.assertTrue(g.empty())
        g.add_node(1)
        self.assertFalse(g.empty())

    def test_has_node(self):
        g = Graph()
        self.assertFalse(g.has_node(1))
        g.add_node(1)
        self.assertTrue(g.has_node(1))

    def test_has_nodes(self):
        g = Graph()
        g.add_node(1)
        g.add_node(3)
        g.add_node(2, [1, 3])
        self.assertTrue(g.has_nodes([1, 2, 3]))
        self.assertFalse(g.has_nodes([1, 2, 3, 4]))

    def test_has_edge(self):
        g = Graph()
        g.add_node(1)
        g.add_node(3)
        g.add_node(2, [1, 3])
        self.assertTrue(g.has_edge(1, 2))
        self.assertTrue(g.has_edge(3, 2))
        self.assertFalse(g.has_edge(1, 3))

    def test_check_node(self):
        nid = 1
        node = Node(nid)
        g = Graph()
        self.assertIsInstance(g.check_node(nid), Node)
        self.assertIsInstance(g.check_node(node), Node)

    def test_check_node_id(self):
        nid = 1
        node = Node(nid)
        g = Graph()
        self.assertIsInstance(g.check_node_id(nid), nid.__class__)
        self.assertIsInstance(g.check_node_id(node), nid.__class__)
