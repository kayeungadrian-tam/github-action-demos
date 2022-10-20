import json
import sys

import requests

# LINE_NOTIFY_TOKEN


def send_line_notify(notification_message: str, token: str):

    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"message": f"\n\n{notification_message}"}
    requests.post(line_notify_api, headers=headers, data=data)


def main(TOKEN: str) -> None:

    message = "Hello world!"

    send_line_notify(message, TOKEN)


if __name__ == "__main__":
    TOKEN = sys.argv[1]

    main(TOKEN)
