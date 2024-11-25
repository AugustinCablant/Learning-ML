import numpy as np 
from Tree import Tree


class NEW:
    def __init__(self, K, s, Niter, eps = 10 ** (-8)):
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
        self.eps = eps


    def set_environment(self, environment):
        self.environment = environment

    def vector_proba(self, scores):
        stable_exp_y = np.exp(scores - np.max(scores))
        proba_vector = stable_exp_y/np.sum(stable_exp_y)
        return proba_vector

    def sample_node_path(self, round):
        node_path = []
        proba_path = []
        reward_path = []
        node = self.environment.tree.root

        while bool(node.children):   # tant que le noeud a des enfants 
            delta = 1 / np.sqrt(round + 1)    # facteur d'exploration
            proba = self.vector_proba(node.scores_children * delta)
            idx_list = range(node.nb_children)
            idx_node = self.rng.choice(idx_list, p=proba)
            child_node = node.children[idx_node]
            node_path.append(idx_node)
            reward_child = self.environment.get_reward_by_node(child_node)
            reward_path.append(reward_child)
            proba_path.append(proba[idx_node])
            node = child_node

        return node_path, proba_path, reward_path

    def scoring_phase(self, tree, )
        
    
    def learn(self):
        regrets, rewards = np.zeros(self.Niter), np.zeros(self.Niter)

        for t in range(self.Niter):
            