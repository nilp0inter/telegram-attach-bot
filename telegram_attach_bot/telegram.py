import requests


def send_file(token, chat_id, path, caption):
    data = {"chat_id": chat_id, "caption": caption, "parse_mode": "Markdown"}
    ret = requests.post(f"https://api.telegram.org/bot{token}/sendDocument",
                        data=data,
                        files={"document": open(path, "rb")})
    return ret.json()


def send_message(token, chat_id, text):
    data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    ret = requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                        data=data)
    return ret.json()
