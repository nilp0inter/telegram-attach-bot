import os
import sys

import parser
import filters

args = parser.parse_args(sys.argv[1:])

entries = os.scandir(args.path)
entries = filters.only_files(entries)
entries = filters.filter_by_extension(args.include_ext, entries)
entries = filters.filter_by_entry_size(args.max_entry_size, entries)
entries = filters.takewhile_size_quota(args.max_total_size, entries)


