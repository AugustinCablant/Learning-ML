class Node:
    def __init__(self, name, value, level = 0):
        """ 
        Params 
        ------
        name: str, name of the node
        value: int, value of the node
        level: int, level of the node
        """
        self.name = name
        self.value = value
        self.level = level
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    
    def __repr__(self):
        return f"Node({self.name}, Level {self.level}, Value {self.value})"
    
class Tree:
    def __init__(self, root = None):
        """ 
        Params 
        ------
        root: Node, root of the tree
        """
        self.root = root
        self.graph = {}
        
    
    def add_node(self, parent, data):
        """ 
        Params
        ------
        parent: Node, parent of the new node
        data: tuple, (name, value) of the new node
        """
        name, value = data 
        if parent is None:
            parent_node = Node(name, value)
            self.root = parent_node
            self.graph[name] = parent_node
        else:
            parent_node = self.graph[parent]
        
        level = parent_node.level + 1
        new_node = Node(name, value, level)
        parent_node.add_child(new_node)
        self.graph[name] = new_node
        return parent_node, new_node
    
    def find_best_arm_path(self):
        path = []
        node = self.root
        while node.children:
            best_child_index = max(range(len(node.children)), key=lambda i: node.children[i].value)
            path.append(best_child_index)
            node = node.children[best_child_index]
        return node, path

    def __repr__(self):
        return f"Tree(Root: {self.root})"
