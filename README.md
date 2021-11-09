# telegram-attach-bot

Zip and send a directory or file via Telegram.

## Requirements

Python 3.8+

## General usage

```console
$ ./attachbot
usage: attachbot [-h] --token TOKEN --chat CHAT [--name NAME]
                 [--max-entry-size MAX_ENTRY_SIZE] [--max-total-size MAX_TOTAL_SIZE]
                 [--include-ext INCLUDE_EXT] [--metadata METADATA]
                 path
attachbot: error: the following arguments are required: --token, --chat, path
```

## Use with `qbittorrent`

1. Download `attachbot` from *Releases* and put it inside the PATH. Make sure it has the execution bit set.

2. Go to Tools->Options->Downloads.

3. Check `Run external program on torrent completion` and paste the following in the command box:

```
attachbot --token=<telegram_bot_token> --chat=<telegram_chat_id> "--name=%N" "--max-entry-size=200 MiB" "--max-total-size=2 GiB" --metadata "Category=%L" --metadata "Tags=%G" --metadata "Number of files=%C" --metadata "Torrent size=%Z" --metadata "Current tracker=%T" --metadata "Info hash=%I" "%F"
```
