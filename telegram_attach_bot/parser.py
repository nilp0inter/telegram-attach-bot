import argparse

UNITS = {"B": 1,
         "KB": 10**3,
         "MB": 10**6,
         "GB": 10**9,
         "TB": 10**12,
         "KiB": 2**10,
         "MiB": 2**20,
         "GiB": 2**30,
         "TiB": 2**40
         }


def parse_size(size):
    """
    >>> parse_size("1024")
    1024
    >>> parse_size("10.43 KB")
    10430
    >>> parse_size("11 GB")
    11000000000
    >>> parse_size("343.1 MB")
    343100000

    """
    if ' ' in size:
        number, unit = [string.strip() for string in size.split()]
    else:
        number, unit = size, 'B'
    try:
        return int(float(number)*UNITS[unit])
    except KeyError as exc:
        raise ValueError(
            f"Unknown UNIT '{unit}'. Valids are {', '.join(UNITS.keys())}.")


class ParseSizeAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, parse_size(values))


class KeyValueAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        d = getattr(namespace, self.dest)
        if d is None:
            d = dict()
        key, value = values.split('=', 1)
        d[key] = value
        setattr(namespace, self.dest, d)


def parse_args(args):
    """
    >>> parse_args(["--token", "foo", "--chat", "bar", "--name", "aname", "somepath"])
    Namespace(token='foo', chat=['bar'], name='aname', max_entry_size=None, max_total_size=None, include_ext=None, metadata=None, path='somepath')

    >>> parse_args(["--token", "foo", "--chat", "bar", "--chat", "baz", "somepath"])
    Namespace(token='foo', chat=['bar', 'baz'], name=None, max_entry_size=None, max_total_size=None, include_ext=None, metadata=None, path='somepath')

    >>> parse_args(["--token", "foo", "--chat", "bar", "--max-entry-size", "100 MB", "--max-total-size", "2 GB", "somepath"])
    Namespace(token='foo', chat=['bar'], name=None, max_entry_size=100000000, max_total_size=2000000000, include_ext=None, metadata=None, path='somepath')

    >>> parse_args(["--token", "foo", "--chat", "bar", "--include-ext", "jpg", "--include-ext", "pdf", "somepath"])
    Namespace(token='foo', chat=['bar'], name=None, max_entry_size=None, max_total_size=None, include_ext=['jpg', 'pdf'], metadata=None, path='somepath')

    >>> parse_args(["--token", "foo", "--chat", "bar", "--metadata", "key1=value1", "--metadata", "key2=this is value=2", "somepath"])
    Namespace(token='foo', chat=['bar'], name=None, max_entry_size=None, max_total_size=None, include_ext=None, metadata={'key1': 'value1', 'key2': 'this is value=2'}, path='somepath')


    """
    parser = argparse.ArgumentParser(
        description='Zip and send directories via Telegram')

    parser.add_argument("--token", required=True)
    parser.add_argument("--chat", required=True, action="append")
    parser.add_argument("--name")
    parser.add_argument("--max-entry-size", action=ParseSizeAction)
    parser.add_argument("--max-total-size", action=ParseSizeAction)
    parser.add_argument("--include-ext", action="append")
    parser.add_argument("--metadata", action=KeyValueAction)
    parser.add_argument("path")

    return parser.parse_args(args)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
