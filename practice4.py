def F(s, D):
    """ Returns True if s is a key for D and every element in D[s] is also a key in D.
    Otherwise returns False.
    Precondition: s is a nonempty string and D is a dictionary whose keys are
    strings and whose values are lists of strings.
    """
    if s not in D:  # Check if s is a key in D
        return False
    
    # Check if every element in D[s] is also a key in D
    for element in D[s]: # Iterate over each element in the list
        if element not in D:
            return False
    
    return True


# Example usage:
if __name__ == "__main__":
    # Example dictionary
    D = {
        "key1": ["key2", "key3"],
        "key2": ["key1", "key2"],
        "key3": ["value6", "value7", "value8"]
    }
    
    # Test cases
    print(F("key1", D))  # True - "key1" is a key in D and every element is as well
    print(F("key2", D))  # False - "key2" is a key but "value4" and "value5" aren't
    print(F("key3", D))  # False - value6 not in D
    print(F("key4", D))  # False (key4 is not in D)
    print(F("value1", D))  # False (value1 is not a key in D)

