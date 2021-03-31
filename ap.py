"""
Program to check if an element is a part of a given AP
"""
def arithmetic_progression(A, B, C):
    """
    function to check if a given element is a part of a given AP
    """
    if A==B:
        return 1
    if C==0:
        if A==B:
            return 1
        else:
            return 0
    if (B-A)%C==0 and (B-A)/C>0:
        return 1
    return 0

if __name__ == "__main__":
    print(arithmetic_progression(1,3,2))