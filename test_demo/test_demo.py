class TestDemo:
    def test_first_demo(self):
        print("first demo test executed")

    def test_second_demo(self):
        print("second demo test executed")

#  pytest test_demo/test_demo.py::TestDemo::test_first_demo -s -v - execute particular test