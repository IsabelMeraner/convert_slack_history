# usr/bin/env python3
# author: Isabel Meraner
# 2022

"""
Conversion from slack channel history for teams migration.

# how to run:
$ python3 convert_slack_history.py --path PATH_TO_INPUT_FOLDER
"""

import argparse
import emoji
import json
import os
from datetime import datetime


def process_msg(msg):
    # print('\tmsg:{}'.format(msg))
    person = msg['user_profile']['real_name']
    text = emoji.emojize(msg['text'], language='alias')
    date = datetime.utcfromtimestamp(float(msg['ts'])).strftime('%Y-%m-%d %H:%M:%S')
    return person, text, date

def prepare_files(channel_path):
    files = list(os.listdir(channel_path))
    files.sort(key=lambda x: datetime.strptime(x.strip('.json'), "%Y-%m-%d"))
    return files

def get_channels(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        if dirs:
            return dirs
def main():
    argparser = argparse.ArgumentParser(
        description='Convert slack json history to channel txt output files.')

    argparser.add_argument(
        '-p', '--path',
        type=str,
        default='',
        help='')

    args = argparser.parse_args()
    root_dir = args.path


    channels = get_channels(root_dir)
    print('# CHANNELS: {}'.format(channels))

    # process single data files for each exported slack channel
    for channel in channels:
        with open('./output_{}.txt'.format(channel), 'w') as outfile:
            channel_path = os.path.join(root_dir, channel)
            print("\t# CHANNEL {}".format(channel))
            # print('\t# CHANNEL PATH{}'.format(channel_path))

            # iterate files
            for json_file in prepare_files(channel_path):
                f = os.path.join(channel_path, json_file)
                if os.path.isfile(f):
                    print("\t\t# PROCESSING FILE: {}".format(f))
                    with open(f, 'r') as infile:
                        json_file = json.load(infile)
                        # print(json_file)
                        for msg in json_file:
                            # print('\t{}'.format(msg))
                            if msg.get('type') == 'message' and msg.get('text') and msg.get('user_profile'):
                                person, text, date = process_msg(msg)
                                outfile.write('{} ({}):\n{}\n\n'.format(person, date, text))


if __name__ == '__main__':
    main()
