import pytest

from home import Home


class Testcase:

    def setup(self):
        self.Home = Home()

    def test_result(self):
        al = self.Home.HomePage()
        al.add_person_page()
        assert "张华天" in al.get_person()

if __name__ == '__main__':
    pytest.main()