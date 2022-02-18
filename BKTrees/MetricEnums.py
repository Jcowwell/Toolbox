from enum import Enum, auto

class Levenshtein(Enum):
    Full_Matrix = auto()
    Two_Matrix = auto()
    Recursive = auto()

class Damerau_Levenshtein(Enum):
    # Note: Damerau–Levenshtein Distance Approaches
    Restricted_Edit_Distance = auto()
    Optimal_String_Alignment_Distance = Restricted_Edit_Distance
    Distance_With_Adjacent_Transpositions = auto()
    Recursive = auto()