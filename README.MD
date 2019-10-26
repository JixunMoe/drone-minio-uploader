Simple minIO uploader for drone
===============================

pipeline config:

```yml
steps:
- name: build
  # ...
- name: upload
  image: jixun/drone-minio-uploader:1.0
  commands:
  - upload --file package.tar.gz
  environment:
    ACCESS_KEY:
      from_secret: access_key
    SECRET_KEY:
      from_secret: secret_key
    UPLOAD_BUCKET: build
    S3_SERVER: example.com
```

## CLI options

```
upload --file path/to/file [--name specific-name.zip]
```

If `name` is not specified, object name will be `{BRANCH}-{BUILD_NUMBER}-{DATE}.{FILE_EXT}`.

## Note

The author does not know too much about python, please exam the code for any defects.

This module had ZERO automated test. Use at your own risk, as stated in the license.
