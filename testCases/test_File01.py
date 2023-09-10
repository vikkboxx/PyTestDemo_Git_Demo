from selenium import webdriver
# options= webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)

class Test_Pytest:


    def test_sum_001(self):
        a = 3
        b = 4
        sum = a + b
        print(sum)
        if sum == 7:
            assert True
        else:
            assert False


    def test_sum_002(self):
        a = 5
        b = 4
        sum = a + b
        print(sum)
        if sum == 9:
            assert True
        else:
            assert False

    def test_mul_003(self):
        a = 5
        b = 4
        mul = a * b
        print(mul)
        if mul == 21:
            assert True
        else:
            assert False

    def test_Url_004(self):
        driver = webdriver.Chrome()
        driver.get("https://automation.credence.in/shop")
        if driver.title == "CredKart":
            print("Correcct")
        else:
            print("Incorrect")




