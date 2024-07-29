import os


class FileUtil:

    @staticmethod
    def mkdirs(path: str):
        os.makedirs(path, exist_ok=True)
