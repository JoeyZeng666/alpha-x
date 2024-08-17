import os

from alphax.core.utils.file_util import FileUtil


class _LocalDirUtil:
    _local_dir = None

    def __init__(self):
        super().__init__()
        self._local_dir = self._find_matching_parent_folder('alpha-x')


    @staticmethod
    def _find_matching_parent_folder(match_str):
        current_path = os.path.dirname(os.path.abspath(__file__))
        while True:
            folder_name = os.path.basename(current_path)
            if match_str == folder_name:
                root_path = current_path
                break
            current_path = os.path.dirname(current_path)
        if root_path:
            local_path = f"{root_path}/LOCAL"
            FileUtil.mkdirs(local_path)
            return f"{root_path}/LOCAL"
        else:
            raise FileNotFoundError("没有找到根目录 alpha-x")

    def local_dir(self) -> str:
        return self._local_dir

    def set_local_dir(self, path: str):
        FileUtil.mkdirs(path)
        self._local_dir = path



