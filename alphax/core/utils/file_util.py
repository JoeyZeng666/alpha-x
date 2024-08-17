import os


class FileUtil:

    @staticmethod
    def mkdirs(path: str):
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def create_file(file_path: str):
        # 确保目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 创建文件
        with open(file_path, 'w') as file:
            pass  # 创建空文件
