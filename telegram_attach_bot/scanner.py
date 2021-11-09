import os


class PseudoDirEntry:
    def __init__(self, path):
        self.name = os.path.basename(path)
        self.path = path

    def stat(self):
        return os.stat(self.path)

    def is_file(self):
        return os.path.isfile(self.path)

    def is_dir(self):
        return os.path.isdir(self.path)


def scantree(path):
    """Recursively yield DirEntry objects for given directory."""
    if os.path.islink(path):
        raise RuntimeError("not following symlinks")
    elif os.path.isfile(path):
        yield PseudoDirEntry(path)
    elif os.path.isdir(path):
        for entry in os.scandir(path):
            if entry.is_dir(follow_symlinks=False):
                yield from scantree(entry.path)
            else:
                yield entry
    else:
        raise RuntimeError("unknown file type")

