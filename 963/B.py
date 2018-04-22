class Node:
    def __init__(self, data):
        self.parent = None  # type: Node
        self.children = list()
        self.data = data

    def get_degree(self):
        if self.parent is not None:
            return len(self.children) + 1
        else:
            return len(self.children)

    def get_recursion_string(self, s):
        result = "%s%s\n" % (s, self.data)
        # result.append(self.data)
        for child in self.children:
            result += child.get_recursion_string(s + "\t")
        return result


class Tree:
    def __init__(self):
        self.roots = list()
        self.nodes = list()
        self.left = list()
        self.label2node = dict()

    def add_node(self, node_id, parent):
        node = Node(node_id)
        self.label2node[node.data] = node
        self.nodes.append(node)
        self.left.append(node)
        if parent == 0:
            self.roots.append(node)
        else:
            parent = self.label2node.get(parent)
            parent.children.append(node)
            node.parent = parent
            if parent in self.left:
                self.left.remove(parent)

    def remove(self, node_id):
        """

        :param Node node:
        :return:
        """
        node = self.label2node[node_id]
        if node.parent is not None:
            node.parent.children.remove(node)
            if len(node.parent.children) == 0:
                self.left.append(node.parent)
        if node in self.left:
            self.left.remove(node)
        for child in node.children:
            child.parent = None
            self.roots.append(child)
        if node in self.roots:
            self.roots.remove(node)
        self.nodes.remove(node)
        del self.label2node[node_id]
        node.children = list()

    def get_left(self):
        return [node.data for node in self.left]

    def print_tree(self):
        for root in self.roots:
            print root.get_recursion_string("")


def main_2():
    n = int(raw_input())
    a = map(int, raw_input().split())
    tree = Tree()
    for i in range(len(a)):
        tree.add_node(i + 1, a[i])

    # for node in tree.nodes:
    #     print node.data, node.get_degree()
    list_remove = list()
    while True:
        check = False
        # if len(tree.get_left()) == 0:
        #     break
        # print tree.get_left()
        for node_id in tree.get_left():
            # print "node: %s" % node_id
            node = tree.label2node[node_id]

            while node.get_degree() % 2 == 1:
                if node.parent is not None:
                    node = node.parent
                else:
                    break
            if node.get_degree() % 2 == 0:
                # print "Remove: %s" % node.data
                tree.remove(node.data)
                check = True
                list_remove.append(node.data)
        if not check:
            break
    if len(tree.get_left()) == 0:
        print "YES"
        for node_id in list_remove:
            print node_id
    else:
        print "NO"


def main_1():
    a = [0, 1, 2, 1, 2]
    tree = Tree()
    for i in range(len(a)):
        print "add node %s" % (i + 1)
        tree.add_node(i + 1, a[i])
        # tree.add_node(Node(2), 1)
        # tree.add_node(Node(3), 2)
        # tree.add_node(Node(4), 1)
        # tree.add_node(Node(5), 2)

        tree.print_tree()
        # print tree.roots
        # print tree.nodes
        # print tree.left
        # print tree.label2node
        print "======================================"
    tree.remove(2)
    tree.print_tree()
    print "======================================"
    for node in tree.nodes:
        print node.data, node.get_degree()


if __name__ == '__main__':
    main_2()
