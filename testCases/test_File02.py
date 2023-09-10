from selenium import webdriver
from selenium.webdriver.common.by import By
# options= webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)

class Test_Pytest:


    def test_sum_005(self):
        a = 7
        b = 4
        sum = a + b
        #print(sum)
        if sum == 11:
            assert True
        else:
            assert False
# ---------------------------------------------------------------------------------

    def test_Credence_006(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")

        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()

        l = len(driver.find_elements(By.XPATH, "//div[@class = 'quickfinder-description gem-text-output']//p//a"))
        Contact_Number_List = []
        for r in range(1, l+1):
            Contact_number = driver.find_element(By.XPATH, "//div[@class = 'quickfinder-description gem-text-output']//p//a["+str(r)+"]").text
            #print(Contact_number)
            Contact_Number_List.append(Contact_number)
        #print(Contact_Number_List)
        mb = "+91 9579064658"
        if mb in Contact_Number_List:
            print(Contact_Number_List.index(mb))
            assert True
        else:
            assert False


