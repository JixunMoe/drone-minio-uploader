from os import getenv as env
from datetime import datetime

REPO_NAMESPACE = env('DRONE_REPO_NAMESPACE', '')
REPO_NAME = env('DRONE_REPO_NAME', '')
REPO_BRANCH = env('DRONE_REPO_BRANCH', '')
BUILD_NUMBER = int(env('DRONE_BUILD_NUMBER', 0))
BUILD_DATE = datetime.today().strftime('%Y%m%d')

S3_SERVER = env('S3_SERVER')
UPLOAD_BUCKET = env('UPLOAD_BUCKET')
ACCESS_KEY = env('ACCESS_KEY', '')
SECRET_KEY = env('SECRET_KEY', '')

UPLOAD_DIR = f'{REPO_NAMESPACE}/{REPO_NAME}'
FILE_PREFIX = f'{REPO_BRANCH}-{BUILD_NUMBER}-{BUILD_DATE}'
