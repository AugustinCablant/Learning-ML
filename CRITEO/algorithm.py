import numpy as np 
from Tree import Tree

class BlueBusRedBusEnvironment:
    def __init__(self, s):
        """ 
        Params:
        ------
        s: int, size of the Structure
        """
        self.name = 'BlueBusRedBus'
        self.s = s
        self.tree = Tree()
        self.root = self.tree.add_node(None, ('root', 0))

    def set(self):
        """
        Create the Tree and find the best path
        """
        self.create_graph()
        _, self.best_strategy_path = self.tree.find_best_arm_path()

        # Construit le chemin optimal à partir des indices
        nodes_path = [self.root]
        node = self.root
        for idx in self.best_strategy_path:
            node = node.children[idx]
            nodes_path.append(node)
        self.best_strategy_nodes_path = nodes_path

    def create_graph(self):
        """
        Crée le graphe de l'environnement (arbre) avec un nombre spécifique d'enfants par noeud.
        """
        self._create_sub_level('root', 2)  # Crée les enfants de la racine
        node_key = 'level_1_child_number_1_of_root'  # Exemple de clé pour l'un des enfants
        self._create_sub_level(node_key, self.nb_assymetric_child)  # Crée des enfants asymétriques

    def _create_sub_level(self, node_key, nb_childs):
        """
        Crée un sous-niveau (enfants) pour un noeud donné.
        :param node_key: Clé du noeud pour lequel créer des enfants.
        :param nb_childs: Nombre d'enfants à créer pour ce noeud.
        """
        node = self.tree.graph[node_key]
        level = node.level + 1
        for n in range(nb_childs):
            name = f'level_{level}_child_number_{n}_of_{node.name}'
            value = self.env_rng.choice(range(1, 9))  # Tirage aléatoire pour la valeur
            self.tree.insert(node, (name, value))

    def get_reward_by_path(self, path):
        """
        Calcule la récompense pour un chemin donné.
        :param path: Liste des noeuds dans le chemin.
        :return: La somme des récompenses sur ce chemin.
        """
        reward = 0
        for node in path[1:]:  # On ignore la racine (premier noeud)
            level_correction = 10 ** (-node.level)
            reward += 0.1 * level_correction * node.value
        return reward

    def get_best_strategy_reward(self):
        """
        Retourne la récompense du meilleur chemin stratégique trouvé.
        """
        return self.get_reward_by_path(self.best_strategy_nodes_path)


class NEW:
    def __init__(self, K, s, Niter):
        """ 
        Args:
            K: int, number of arms
            s: int, size of the Structure
            Niter: int, number of iterations
        """
        self.name = 'NEW'
        self.K = K
        self.s = s
        self.Niter = Niter