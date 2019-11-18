from unittest import TestCase
from graph.classes.node import Node


class TestNode(TestCase):
    def test_weight(self):
        n = Node(1)
        self.assertEqual(n.weight(), {})

    def test_id(self):
        keys = [1, "str", 1.1]
        for key in keys:
            n = Node(key)
            self.assertEqual(n.id, key)

    def test_add_neighbor(self):
        n = Node(1)
        n.add_neighbor(2, weight=None)
        self.assertIn(2, n.neighbors)
        return n

    def test_del_neighbor(self):
        n = Node(1)
        n.add_neighbor(2, weight=None)
        self.assertIn(2, n.neighbors)
        n.del_neighbor(2)
        self.assertNotIn(2, n.neighbors)

    def test_has_neighbor(self):
        n = Node(1)
        n.add_neighbor(2, weight=None)
        self.assertFalse(n.has_neighbor(3))
        self.assertTrue(n.has_neighbor(2))

    def test_neighbors(self):
        n = Node(1)
        n.add_neighbor(2, weight=None)
        self.assertListEqual(n.neighbors, [2])
