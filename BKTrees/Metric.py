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
    def levenshtein_distance(a: str,b: str) -> int:
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
        if len(b) == 0:
            return len(a)
        elif len(a) == 0:
            return len(b)
        elif a[0] == b[0]:
            return StringMetric.levenshtein_distance(a[1:],b[1:])
        else:
            return 1 + min(min(StringMetric.levenshtein_distance(a[1:],b), StringMetric.levenshtein_distance(a,b[1:])), StringMetric.levenshtein_distance(a[1:],b[1:]))