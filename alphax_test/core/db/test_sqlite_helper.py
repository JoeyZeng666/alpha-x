import unittest
from peewee import *
from alphax.core.db.database_factory import DatabaseFactory
import os


# 定义一个简单的模型
class User(Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = None


# 简单的测试类
class TestSqliteHelper(unittest.TestCase):
    def setUp(self):
        # 在每次测试前清空表
        self.db, self.db_path = DatabaseFactory.get_sqlite_database("demo_db")
        User._meta.database = self.db
        self.db.create_tables([User])

    # 在每次测试后关闭数据库连接
    def tearDown(self):
        self.db.drop_tables([User])
        self.db.close()
        # 删除对应的数据库文件
        os.remove(self.db_path)
        pass

    def test_create_and_retrieve(self):
        # 创建用户
        User.create(name="张三", age=25)
        # 检索用户
        user = User.get(User.name == "张三")
        self.assertEqual(user.name, "张三")
        self.assertEqual(user.age, 25)

    def test_update(self):
        # 创建用户
        user = User.create(name="李四", age=30)

        # 更新用户
        user.age = 31
        user.save()

        # 检查更新是否成功
        updated_user = User.get(User.id == user.id)
        self.assertEqual(updated_user.age, 31)

    def test_delete(self):
        # 创建用户
        User.create(name="王五", age=40)

        # 删除用户
        User.delete().where(User.name == "王五").execute()

        # 确认用户已被删除
        self.assertEqual(User.select().count(), 0)


if __name__ == '__main__':
    unittest.main()
