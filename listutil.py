def unique(lst):
    """Return a list containing only the first occurence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        list: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"])
    ['b', 'a']
    >>> unique([])
    []
    >>> unique([1, 1, 1, 1, 1, 2, 3, 4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    >>> unique([1, 1, [1, 1]])
    [1, [1, 1]]
    >>> unique([1, 2, [1, 1], [1, 1], 1, 1])
    [1, 2, [1, 1]]
    """

    if not isinstance(lst, list):
        raise TypeError
    else:
        new_list = []
        for i in lst:
            if i not in new_list:
                new_list.append(i)
        return new_list


if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
