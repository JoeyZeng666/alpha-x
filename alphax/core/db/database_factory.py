import os
from typing import Tuple

from alphax.core.utils.file_util import FileUtil
from alphax.core.utils.local_dir_util import _LocalDirUtil
from peewee import SqliteDatabase, Database


class DatabaseFactory:

    @classmethod
    def get_sqlite_database(cls,
                            db_name,
                            db_location=f'{_LocalDirUtil().local_dir()}/databases') -> tuple[SqliteDatabase, str]:
        db_path = os.path.join(db_location, f"{db_name}.db")
        FileUtil.mkdir(db_location)
        db = SqliteDatabase(db_path)
        db.connect()
        return db, db_path

