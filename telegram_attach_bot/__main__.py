import os
import sys
import zipfile
from tempfile import TemporaryDirectory

from slugify import slugify

import parser
import filters
import scanner
import telegram
import caption


args = parser.parse_args(sys.argv[1:])

entries = scanner.scantree(args.path)
entries = filters.only_files(entries)
entries = filters.filter_by_extension(args.include_ext, entries)
entries = filters.filter_by_entry_size(args.max_entry_size, entries)
entries = filters.takewhile_size_quota(args.max_total_size, entries)

with TemporaryDirectory() as tmpdir:
    filename = slugify(args.name if args.name else args.path,
                       max_length=128,
                       lowercase=False) + '.zip'
    filepath = os.path.join(tmpdir, filename)
    totalfiles = 0
    with zipfile.ZipFile(filepath, 'w') as zf:
        for e in entries:
            newpath = os.path.relpath(e.path, os.path.dirname(args.path))
            print(f"{e.path} => {newpath}")
            zf.write(e.path, arcname=newpath)
            totalfiles += 1

    c = caption.render(
        caption.TITLE_AND_DESCRITION if args.name else caption.ONLY_DESCRIPTION,
        args.name,
        args.metadata if args.metadata else {})

    for chat in args.chat:
        if totalfiles > 0:
            telegram.send_file(args.token, chat, filepath, c)
        else:
            telegram.send_message(args.token, chat, c)

