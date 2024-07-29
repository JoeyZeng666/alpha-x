from alphax.core.logger import AlphaxLogger
from alphax.core.utils.local_dir_util import _LocalDirUtil
import alphax.core.logger as logger

_singleLocalDirHelper = _LocalDirUtil()


def local_dir():
    return _singleLocalDirHelper.local_dir()


def set_local_dir(path: str):
    _singleLocalDirHelper.set_local_dir(path)


def get_logger(tag=None) -> AlphaxLogger:
    return logger.get_logger(tag=tag)
