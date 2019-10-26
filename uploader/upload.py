from os import getenv as env, path
from uploader.args import args
from uploader.const import S3_SERVER, UPLOAD_BUCKET, UPLOAD_DIR, FILE_PREFIX, ACCESS_KEY, SECRET_KEY
from minio import Minio
from minio.error import ResponseError

print(f'ACCESS_KEY={ACCESS_KEY}')
print(f'SECRET_KEY={SECRET_KEY}')


class Uploader(Minio):
    def __init__(self):
        super().__init__(
            S3_SERVER,
            access_key=ACCESS_KEY,
            secret_key=SECRET_KEY,
            secure=True,
        )

    def upload(self, file, name):
        name = name if name else self.get_renamed(file)
        etag = self.fput_object(bucket_name=UPLOAD_BUCKET, object_name=f'{UPLOAD_DIR}/{name}', file_path=file)
        print(f'upload ok! etag: {etag}')

    @staticmethod
    def get_renamed(file):
        name, ext = path.splitext(file)
        if '.tar.' in file:
            ext = '.tar' + ext
        return FILE_PREFIX + ext


def main():
    uploader = Uploader()
    uploader.upload(args.file, args.name)


if __name__ == '__main__':
    main()
