import os
import re
import argparse
from aliyundrive import Aliyundrive
import send



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--token_string', type=str, required=True)
    args = parser.parse_args()
    token_string = args.token_string
    token_string = token_string.split(',')
    ali = Aliyundrive()
    message_all = []

    for idx, token in enumerate(token_string):
        result = ali.aliyundrive_check_in(token)
        message_all.append(str(result))

        if idx < len(token_string) - 1:
            message_all.append('--')

    message_all = '\n'.join(message_all)
    message_all = re.sub('\n+', '\n', message_all).rstrip('\n')
    token = os.getenv('TOKEN')
    chat_id = os.getenv('CHAT_ID')
    sender = send.Send(token)
    sender.tg_send(chat_id, message_all)
    print('finish')


if __name__ == '__main__':
    main()
