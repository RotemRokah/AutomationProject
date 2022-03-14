from selenium.webdriver import Chrome


def get_screenshot(driver, name):
    driver.get_screenshot_as_file("C:/Users/Public/AllProjects/Siber1/MyFinalProject/TestCases/" + name + ".png")
