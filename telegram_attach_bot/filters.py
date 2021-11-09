import os

def filter_by_entry_size(max_entry_size, entries):
    """
    >>> len(list(filter_by_entry_size(None, os.scandir()))) == len(list(os.scandir()))
    True

    >>> len(list(filter_by_entry_size(0, os.scandir())))  # __init__.py
    1

    """
    if max_entry_size is None:
        yield from entries
    else:
        for entry in entries:
            if entry.stat().st_size <= max_entry_size:
                yield entry


def takewhile_size_quota(max_total_size, entries):
    """
    >>> len(list(takewhile_size_quota(None, os.scandir()))) == len(list(os.scandir()))
    True

    >>> len(list(takewhile_size_quota(0, os.scandir())))
    1

    >>> len(list(takewhile_size_quota(1000000000, os.scandir()))) == len(list(os.scandir()))
    True

    """
    if max_total_size is None:
        yield from entries
    else:
        total = 0
        for entry in entries:
            entry_size = entry.stat().st_size
            if total + entry_size <= max_total_size:
                total += entry_size
                yield entry


def filter_by_extension(extensions, entries):
    """
    >>> len(list(filter_by_extension(None, os.scandir()))) == len(list(os.scandir()))
    True

    >>> len(list(filter_by_extension(['.py'], os.scandir()))) < len(list(os.scandir()))  # because of '.' and '..'
    True

    >>> len(list(filter_by_extension(['.tiff'], os.scandir())))
    0

    """
    if extensions is None:
        yield from entries
    else:
        for entry in entries:
            ext = os.path.splitext(entry.name)[1][1:]
            if ext in extensions:
                yield entry


def only_files(entries):
    """
    >>> len(list(only_files(os.scandir()))) < len(list(os.scandir()))  # because of '.' and '..'
    True

    """
    for entry in entries:
        if entry.is_file():
            yield entry


if __name__ == '__main__':
    import doctest
    doctest.testmod()
