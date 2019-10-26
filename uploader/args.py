import argparse

parser = argparse.ArgumentParser(description='minIO uploader')

parser.add_argument('--file', dest='file',
                    help='file to upload')

parser.add_argument('--name', dest='name',
                    default=None,
                    help='name to use; leave blank for auto generated.')

args = parser.parse_args()
