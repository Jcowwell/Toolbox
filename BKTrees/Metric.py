from typing import List

# from ..Meta.decorators import disuse
from .MetricEnums import *

class StringMetric():
    """
    From Wikipedia: https://en.wikipedia.org/wiki/String_metric:

        A string metric (also known as a string similarity metric or string distance function) is a metric that measures distance ("inverse similarity") 
        between two text strings for approximate string matching or comparison and in fuzzy string searching.
        A requirement for a string metric (e.g. in contrast to string matching) is fulfillment of the triangle inequality.
        For example, the strings "Sam" and "Samuel" can be considered to be close.[1] A string metric provides a number indicating an algorithm-specific indication of distance. 
    """
    # List taken from:  https://en.wikipedia.org/wiki/String_metric#List_of_string_metrics
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def levenshtein_distance(a: str, b: str , algorithm: Levenshtein = Levenshtein.Full_Matrix) -> int:
        """
        From Wikipedia:https://en.wikipedia.org/wiki/Levenshtein_distance#Definition

            The Levenshtein Distance between two strings a,b (of length |a| and |b| respectively) 
            is given by lev(a,b) where:

                if |b| == 0 : the Levenshtein Distance is |a|
                else if |a| == 0 : the Levenshtein Distance is |b|
                else if a[0] == b[0] : the Levenshtein Distance is lev(tail(a),tail(b))
                else 1 + min(
                    lev(tail(a),b), 
                    lev(a,tail(b)),
                    lev(tail(a),tail(b))
                )

                where where the tail of some string x is a string of all but the first character 
                of x and x[n] is the n nth character of the string x, counting from 0.

            Note that the first element in the minimum corresponds to deletion (from a to b), 
            the second to insertion and the third to replacement.

            This definition corresponds directly to the naive recursive implementation. 
        """
        if algorithm == Levenshtein.Full_Matrix:
            return StringMetric.levenshtein_full_matrix(a=a, b=b)
        if algorithm == Levenshtein.Two_Matrix:
            pass
        if algorithm == Levenshtein.Recursive:
            return StringMetric.levenshtein_recursive(a=a, b=b)

    @staticmethod
    def levenshtein_full_matrix(a: str, b: str) -> int:
        """
        From Wikipedia: https://en.wikipedia.org/wiki/Levenshtein_distance#iterative_with_full_matrix

            Computing the Levenshtein distance is based on the observation that if we reserve a matrix to hold the Levenshtein distances 
            between all prefixes of the first string and all prefixes of the second, then we can compute the values in the matrix in a 
            dynamic programming fashion, and thus find the distance between the two full strings as the last value computed.

            This algorithm, an example of bottom-up dynamic programming, is discussed, with variants, 
            in the 1974 article The String-to-string correction problem by Robert A. Wagner and Michael J. Fischer.[4]
        """

        a = '_' + a
        b = '_' + b

        d: List[List[int]] = [[0] * (len(b)) for _ in range(len(a))]

        for i in range(1,len(a)):
            d[i][0] = i
        for j in range(1,len(b)):
            d[0][j] = j

        for i in range(1,len(a)):
            for j in range(1, len(b)):
                if a[i] == b[j]:
                    substitutionCost: int = 0
                else:
                    substitutionCost: int = 1
                
                d[i][j] = min(
                    min(
                        d[i-1][j] + 1,  # deletion
                        d[i][j-1] + 1   # insertion
                    ),
                        d[i-1][j-1] + substitutionCost # substitution
                )
        return d[len(a[1:])][len(b[1:])]

    @staticmethod
    # @disuse("This implementation is very inefficient because it recomputes the Levenshtein distance of the same substrings many times.")
    def levenshtein_recursive(a: str, b: str) -> int:
        """
        From Wikipedia: https://en.wikipedia.org/wiki/Levenshtein_distance#Recursive

            This implementation is very inefficient because it recomputes the Levenshtein distance of the same substrings many times.
        """
        if len(b) == 0:
            return len(a)
        elif len(a) == 0:
            return len(b)
        elif a[0] == b[0]:
            return StringMetric.levenshtein_distance(a[1:],b[1:])
        else:
            return 1 + min(min(StringMetric.levenshtein_distance(a[1:],b), StringMetric.levenshtein_distance(a,b[1:])), StringMetric.levenshtein_distance(a[1:],b[1:]))

    @staticmethod
    def damerau_levenshtein_distance(a: str, b: str, algorithm: Damerau_Levenshtein=Damerau_Levenshtein.Distance_With_Adjacent_Transpositions):
        """
        From Wikipedia: https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance

            The Damerau–Levenshtein distance (named after Frederick J. Damerau and Vladimir I. Levenshtein[1][2][3]) 
            is a string metric for measuring the edit distance between two sequences. 
            Informally, the Damerau–Levenshtein distance between two words is the minimum number of operations 
            (consisting of insertions, deletions or substitutions of a single character, or transposition of two adjacent characters) 
            required to change one word into the other.

            The Damerau–Levenshtein distance differs from the classical Levenshtein distance by 
            including transpositions among its allowable operations in addition to the three classical single-character edit operations 
            (insertions, deletions and substitutions).
        """
        if algorithm == Damerau_Levenshtein.Optimal_String_Alignment_Distance or algorithm == Damerau_Levenshtein.Restricted_Edit_Distance:
            # Note: https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance#Optimal_string_alignment_distance
            return StringMetric.optimal_string_alignment(a=a,b=b) 
        elif algorithm == Damerau_Levenshtein.Distance_With_Adjacent_Transpositions:
            # Note: https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance#Distance_with_adjacent_transpositions
            return StringMetric.distance_adjacent_transpositions(a=a,b=b)
        
    @staticmethod
    def optimal_string_alignment(a: str, b: str) -> int:
        """
        From Wikipedia: https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance#Algorithm

            Computes what is known as the 'optimal string alignment distance' or 'restricted edit distance'.
            Computes the number of edit operations needed to make the strings equal under the condition that no substring is edited more than once.
            Note that for the optimal string alignment distance, the triangle inequality does not hold: OSA(CA, AC) + OSA(AC, ABC) < OSA(CA, ABC), and so it is not a true metric.
        """
        a = '_' + a
        b = '_' + b
        d: List[List[int]] = [[0] * (len(b)) for _ in range(len(a))]

        for i in range(len(a)):
            d[i][0] = i
        for j in range(len(b)):
            d[0][j] = j
        
        for i in range(1,len(a)):
            for j in range(1,len(b)):
                if a[i] == b[j]:
                    substitutionCost: int = 0
                else:
                    substitutionCost: int = 1
                d[i][j] = min(
                    min(
                        d[i-1][j] + 1, # deletion
                        d[i][j-1] + 1 # insertion
                    ),
                    d[i-1][j-1] + substitutionCost # substitution
                )
                if i > 1 and j > 1 and a[i] == b[j-1] and a[i-1] == b[j]:
                    d[i][j] = min(
                        d[i][j],
                        d[i-2][j-2] + 1 # transposition 
                    )
        return d[len(a[1:])][len(b[1:])]
    
    @staticmethod
    def distance_adjacent_transpositions(a: str, b: str) -> int:
        """
        From Wikipedia: https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance#Distance_with_adjacent_transpositions
        
        Computes the Damerau–Levenshtein distance with adjacent transpositions. Adding transpositions adds significant complexity.
        Does not need the follwing restriciton: no substring is edited more than once
        """

        a = '_' + a
        b = '_' + b

        da : dict = StringMetric.__construct_alphabet(a=a[1:], b=b[1:])
        d: List[List[int]] = [[-1] * (len(b)+1) for _ in range(len(a)+1)]

        maxdist: int = len(a[1:]) + len(b[1:])
        d[-1][-1] = maxdist
        for i in range(len(a)):
            d[i][-1] = maxdist
            d[i][0] = i
        for j in range(len(b)):
            d[-1][j] = maxdist
            d[0][j] = j

        for i in range(1,len(a)):
            db: int  = 0
            for j in range(1,len(b)):
                k: int = da[b[j]]
                l : int = db
                if a[i] == b[j]:
                    substitutionCost: int = 0
                    db = j
                else:
                    substitutionCost: int = 1
                d[i][j] = min(
                    min(
                        d[i-1][j-1] + substitutionCost, # substitution
                        d[i][j-1] + 1, # insertion
                    ),
                    min(
                        d[i-1][j] + 1, # deletion
                        d[k-1][l-1] + (i-k-1) + 1 + (j-l-1) # transposition
                    )
                )
            da[a[i]] = 1
        return d[len(a[1:])][len(b[1:])]

    @staticmethod
    def __construct_alphabet(a: str, b: str) -> dict:
        alphabet: dict = {}
        def construct(string: str, alphabet: dict) -> None:
            for char in string:
                if char not in alphabet:
                    alphabet[char] = 0
        construct(string=a,alphabet=alphabet)
        construct(string=b,alphabet=alphabet)
        return alphabet