from unittest import TestCase

import alphax.core as core


class TestCoreInit(TestCase):

    def test_auto_local_dir(self):
        print(core.local_dir())
        assert core.local_dir().__contains__('alpha-x/LOCAL')

    def test_manual_local_dir(self):
        print(core.local_dir())
        core.set_local_dir("/Users/zengyan/Excelsior/alpha-x/LOCAL_TEST")
        print(f"修改后 {core.local_dir()}")
        assert core.local_dir().__contains__('alpha-x/LOCAL_TEST')



