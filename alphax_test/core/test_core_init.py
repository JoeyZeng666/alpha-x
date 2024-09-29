import os
from unittest import TestCase

import alphax.core as core


class TestCoreInit(TestCase):

    def test_auto_local_dir(self):
        print(core.local_dir())
        assert core.local_dir().__contains__('alpha-x/LOCAL')

    def test_manual_local_dir(self):
        print(core.local_dir())
        print(f"修改前 {core.local_dir()}")
        # 获取当前目录
        root_dir = os.path.dirname(os.path.abspath(__file__))
        new_dir = f"{root_dir}/LOCAL_TEST"
        print(f"new_dir: {new_dir}")
        core.set_local_dir(new_dir)
        after_dir = core.local_dir()
        print(f"修改后 {after_dir}")
        assert os.path.exists(new_dir)
        # 删除测试目录
        os.rmdir(after_dir)
        assert core.local_dir() == new_dir
        



