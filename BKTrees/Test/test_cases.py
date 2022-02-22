from typing import List, Tuple
from ..MetricEnums import *
# NOTE: Test Cases Taken From: https://oldfashionedsoftware.com/tag/levenshtein-distance/
levenshtein_algorithms: list = [
        Levenshtein.Full_Matrix, 
        # Levenshtein.Two_Matrix,
]

damerau_levenshtein_algorithm: list = [
        Damerau_Levenshtein.Optimal_String_Alignment_Distance, 
        Damerau_Levenshtein.Distance_With_Adjacent_Transpositions
]

levenshtein_distance_test_cases: List[Tuple[str,str,int]] = [ # Format: (a, b, answer)
        
        # Empty String Test
        (   "",    "", 0 ),
        (  "a",    "", 1 ),
        (   "",   "a", 1 ),
        ("abc",    "", 3 ),
        (   "", "abc", 3 ),

        # Equal String Test
        (   "",    "", 0 ),
        (  "a",   "a", 0 ),
        ("abc", "abc", 0 ),

        # Insert Detection Test
        (   "",   "a", 1 ),
        (  "a",  "ab", 1 ),
        (  "b",  "ab", 1 ),
        ( "ac", "abc", 1 ),
        ("abcdefg", "xabxcdxxefxgx", 6 ),

        # Deletion Detection Test   
        (  "a",    "", 1 ),
        ( "ab",   "a", 1 ),
        ( "ab",   "b", 1 ),
        ("abc",  "ac", 1 ),
        ("xabxcdxxefxgx", "abcdefg", 6 ),

        # Substition Detection Test
        (  "a",   "b", 1 ),
        ( "ab",  "ac", 1 ),
        ( "ac",  "bc", 1 ),
        ("abc", "axc", 1 ),
        # ("xabxcdxxefxgx", "1ab2cd34ef5g6", 6 ),

        # # Multiple Operations Detection Test
        # ("example", "samples", 3 ),
        # ("sturgeon", "urgently", 6 ),
        # ("levenshtein", "frankenstein", 6 ),
        # ("distance", "difference", 5 ),
        # ("java was neat", "scala is great", 7 ),
]