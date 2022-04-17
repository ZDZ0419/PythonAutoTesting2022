
from time import sleep
import pytest
from main import Main

class TestAdd:

    def setup(self):
        self.main = Main()

    def test_add(self):
        el = self.main.goto_AddPersonPage()
        el.add_person_page()
        sleep(5)
        # assert "张华天" in el.Assert_Result()

if __name__ == '__main__':
    pytest.main()
