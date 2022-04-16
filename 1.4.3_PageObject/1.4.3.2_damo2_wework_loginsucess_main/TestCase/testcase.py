from time import sleep

import pytest

from addperson import Addperson
from main import Main


class TestAdd:

    def setup(self):
        self.main = Main()

    def testadd(self):
        el = self.main.goto_AddPersonPage()
        el.AddpersionPage()
        sleep(5)
        assert "张华天" in el.assert_result()

if __name__ == '__main__':
    pytest.main()
