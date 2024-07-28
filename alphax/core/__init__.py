from alphax.core.utils.local_dir_util import _LocalDirUtil

_singleLocalDirHelper = _LocalDirUtil()


def local_dir():
    return _singleLocalDirHelper.local_dir()


def set_local_dir(path: str):
    _singleLocalDirHelper.set_local_dir(path)
