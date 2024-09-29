import unittest
import os
import tempfile
from peewee import SqliteDatabase
from alphax.core.db.database_factory import DatabaseFactory
from alphax.core.utils.local_dir_util import _LocalDirUtil


class TestDatabaseFactory(unittest.TestCase):

    def setUp(self):
        # 创建一个临时目录用于测试
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        # 测试结束后删除临时目录
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)

    def test_create_sqlite_database(self):
        # 测试创建数据库
        db_name = "test_db"
        db,_ = DatabaseFactory.get_sqlite_database(db_name, self.temp_dir)

        # 检查返回的对象是否为 SqliteDatabase 实例
        self.assertIsInstance(db, SqliteDatabase)

        # 检查数据库文件是否被创建
        expected_path = os.path.join(self.temp_dir, f"{db_name}.db")
        self.assertTrue(os.path.exists(expected_path))

        # 检查数据库连接是否正常
        try:
            db.execute_sql('SELECT 1')
            self.assertTrue(True)  # 如果执行成功，说明连接正常
        except Exception as e:
            self.fail(f"数据库连接异常: {str(e)}")

        # 关闭数据库连接
        db.close()

    def test_create_sqlite_database_default_location(self):
        # 测试使用默认位置创建数据库
        db_name = "default_location_db"
        db,_ = DatabaseFactory.get_sqlite_database(db_name)

        # 检查返回的对象是否为 SqliteDatabase 实例
        self.assertIsInstance(db, SqliteDatabase)

        # 检查数据库文件是否被创建在默认位置
        expected_path = os.path.join(_LocalDirUtil().local_dir(), "databases", f"{db_name}.db")
        self.assertTrue(os.path.exists(expected_path))

        # 检查数据库连接是否正常
        # 检查数据库连接是否正常
        try:
            db.execute_sql('SELECT 1')
            self.assertTrue(True)  # 如果执行成功，说明连接正常
        except Exception as e:
            self.fail(f"数据库连接异常: {str(e)}")

        # 关闭数据库连接
        db.close()

        # 清理创建的文件
        os.remove(expected_path)


if __name__ == '__main__':
    unittest.main()
