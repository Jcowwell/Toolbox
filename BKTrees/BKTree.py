from typing import Callable, Optional, Dict
from BKTrees.Metric import StringMetric
from sys import maxsize

class TreeNode:
    def __init__(self, label:str) -> None:
        self.label = label
        self.children: Dict[int:TreeNode] = {} # Distance From Parent : Node

    def __str__(self, level:int=0, distance:int='') -> str:
        ret = "\t"*level+repr(self.label)+f':{distance}'"\n"
        for distance, child in self.children.items():
            ret += child.__str__(level=level+1, distance=distance)
        return ret

    def __repr__(self) -> str:
        return ''

class BKTree():

    def __init__(self, root: str, metric: Callable[[str,str], int] = StringMetric.levenshtein_distance) -> None:
        self.root: TreeNode = TreeNode(label=root)
        self.metric: Callable[[str,str], int] = metric

    def insert(self, w: str) -> None:
        """
        From Wikipedia: https://en.wikipedia.org/wiki/BK-tree#Insertion

            The insertion primitive is used to populate a BK-tree according to a discrete metric d. 

            Input:  
                w: the element to be inserted.
        """

        if not self.root:
            self.root = TreeNode(label=w)
            return

        u: TreeNode = self.root
        while u:
            k = self.metric(u.label, w)
            if k == 0:
                return
            if k not in u.children:
                v = TreeNode(label=w)
                u.children[k] = v
                return
            else:
                u = u.children[k]

    def lookup(self, w: str, maximum_distance: int = maxsize) -> Optional[str]:
        """
        From Wikipedia: https://en.wikipedia.org/wiki/BK-tree#Lookup

            Given a searched element w, the lookup primitive traverses the BK-tree to find the closest element of w. 
            The key idea is to restrict the exploration of t to nodes that can only improve the best candidate found 
            so far by taking advantage of the BK-tree organization and of the triangle inequality (cut-off criterion). 

            Input:
                d: the corresponding discrete metric (e.g. the Levenshtein distance);
                w: the searched element;
                maximum_distance: the maximum distance allowed between the best match and w, defaults to sys.maxsize;
            Output:
                best_w: the closest element to w stored in the BKTree and according to d or None not found;
        """
        if not self.root:
            return None 
        S : set  = {self.root}
        best_w, best_distance  = None, maximum_distance
        while S:
            u: TreeNode = S.pop()
            d  = self.metric(w,u.label)
            if d < best_distance:
                best_w, best_distance = u, d
            for k in u.children:
                v: TreeNode = u.children[k]
                if (self.metric(u.label, v.label) - d) < best_distance:
                    S.add(v)
        return best_w.label if best_w else None

    def __iter__(self):
        if not self.root:
            return
        Q : list = []
        Q.append(self.root)

        while Q:
            v: TreeNode = Q.pop()
            yield v
            for k in v.children:
                Q.append(v.children[k]) 

    def __str__(self) -> str:
        return str(self.root) if self.root else 'Empty BKTree'

    