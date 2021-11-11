import pytest
from selenium import webdriver
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome(
    executable_path='Driver\\chromedriver.exe')
driver.get("https://www.garnethill.com")
driver.delete_all_cookies()
driver.maximize_window()


@pytest.mark.order(1)
def test_verifyTitle():
    ActualTitle = driver.title
    ExpectedTitle = "Garnet Hill | Original Clothing, Bedding and Home Decor"
    assert ActualTitle == ExpectedTitle
    print("\n Header Verified")


@pytest.mark.order(2)
def test_verifyPromoMessage():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    bodyText = driver.find_element_by_class_name("promoBannerWrap").text
    assert "JOIN ST. JUDE AND GARNET HILL IN FIGHTING CHILDHOOD CANCER." in bodyText
    print("\n Promo Message Displayed Correctly")


@pytest.mark.order(3)
def test_verifyShopMenu():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    driver.find_elements_by_id("gwt-uid-34")
    driver.find_elements_by_id("gwt-uid-83")
    driver.find_elements_by_id("gwt-uid-105")
    driver.find_elements_by_id("gwt-uid-111")
    driver.find_elements_by_id("gwt-uid-158")
    driver.find_elements_by_id("gwt-uid-191")
    driver.find_elements_by_id("gwt-uid-194")
    driver.find_elements_by_id("gwt-uid-237")
    print("\n Shop Menu Displayed With All Categories")


@pytest.mark.order(4)
def test_verifySearchBox():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    driver.find_element_by_id("headerBox")
    print("\n Search Box Verified")


@pytest.mark.order(5)
def test_verifyMainHero():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    driver.find_element_by_class_name("main-hero__container")
    print("\n Main Hero Image Displayed Correctly")


@pytest.mark.order(6)
def test_verifySignLink():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    driver.find_element_by_id("login").click()
    driver.find_element_by_id("logonId")
    driver.find_element_by_id("logonPassword")
    print("\n Sign In/Up Page Loaded Successfully")


@pytest.mark.order(7)
def test_verifyForgotPasswordLink():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    driver.find_element_by_link_text("Forgot your password?").click()
    print("\n Forgot Your Password Link Verified")


@pytest.mark.order(8)
def test_verifyForgotPasswordModal():
    assert driver.page_source.find("Your password will be reset and sent to your email account. Enter your Email "
                                   "Address and click 'Continue'") 
    print("\n Forgot Your Password Modal Displayed Correctly")
    driver.close()
