import time
from datetime import date

# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import numpy as np

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--window-size=1325x744')
options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome('C:\\Users\\Sagar\\Webkeying\\chromedriver_win32\\chromedriver.exe')
driver.maximize_window()
time.sleep(1)
driver.get("https://tdex.unidex.ai/auth/login")
waits = WebDriverWait(driver, 10)
time.sleep(10)
# email= By.XPATH, f"//input[@placeholder='Email"
# waits.until(EC.presence_of_element_located(email))
email = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
email.clear()
email.send_keys("Sagar@stellaripl.com")
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.clear()
password.send_keys("Sagar@4483")
login = driver.find_element(By.XPATH, "//button[contains(text(), ' Log In ')]")
login.click()
time.sleep(15)
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//span[contains(text(), 'Deed ')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@href='/batches/deed/list']").click()
time.sleep(3)
# driver.find_element(By.XPATH, "//a[@class='dropdown-toggle text-dark px-2 pb-2 fw-bold']").click()
# time.sleep(4)
# driver.find_element(By.XPATH, "//a[@class='dropdown-toggle text-dark px-2 pb-2 fw-bold']/..//button[6]").click()
# time.sleep(5)

driver.find_element(By.XPATH, "//div/app-new-date-range-picker/div").click()
# custom_date = (By.XPATH, "//app-new-date-range-picker/div/div/button[contains(text(),'Custom Range')]")
driver.find_element(By.XPATH, "//app-new-date-range-picker/div/div/button[contains(text(),'Custom Range')]").click()
# select_month = (By.XPATH, "//ngb-datepicker-navigation-select/select[@title = 'Select month']")
sel_mn = Select(driver.find_element(By.XPATH, "//ngb-datepicker-navigation-select/select[@title = 'Select month']"))
sel_mn.select_by_visible_text('May')
sel_date = (By.XPATH, "(//ngb-datepicker-month/div/div/span[contains(text(),'1')])[1]")
driver.find_element(By.XPATH, "(//ngb-datepicker-month/div/div/span[contains(text(),'1')])[1]").click()
time.sleep(2)
# driver.find_element(By.XPATH, "(//ngb-datepicker-month/div/div/span[contains(text(),'1')])[1]").click()
sel_mnth = Select(driver.find_element(By.XPATH, "//ngb-datepicker-navigation-select/select[@title = 'Select month']"))
sel_mnth.select_by_visible_text('Aug')

date_today = date.today().strftime('%B %#d, %Y')

driver.find_element(By.XPATH, f"//div[contains(@class,'ngb-dp-day ng-star-inserted')][contains(@aria-label, '{date_today}')]").click()
driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]").click()
time.sleep(2)


filter_search = driver.find_element(By.XPATH, "//input[@placeholder='Type to filter...']")
filter_search.clear()
batch_id = "06085-20240711-D001"
filter_search.send_keys(batch_id)
driver.find_element(By.XPATH, "//app-ida-table/div[2]/div/div[3]/div/button/i").click()
batch = By.XPATH, f"//a[contains(text(), '{batch_id}')]"
waits.until(EC.presence_of_element_located(batch))
time.sleep(5)
# s = Select(driver.find_element(By.XPATH, f"//a[contains(text(), '{batch_id}')]/../../following-sibling::datatable-body-cell/div/div/select[1]"))
# s.select_by_visible_text('DEED')
summary_button = driver.find_element(By.XPATH, "//button[contains(text(), ' Summary ')]")
time.sleep(1)
summary_button.click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Img name']").clear()
time.sleep(5)
ImageName = "CASCLR-25660816"
ImageName1 = ImageName+".TIF"
driver.find_element(By.XPATH, "//input[@placeholder='Img name']").send_keys(ImageName)
time.sleep(5)
driver.find_element(By.LINK_TEXT, f'{ImageName}').click()

time.sleep(15)
driver.switch_to.window(driver.window_handles[1])
w_list = []
W_venderSourceCode = driver.find_element(By.XPATH, "//label[contains(text(), ' Vendor Source Code ')]/..//input").get_attribute("value")
W_RecordDate = driver.find_element(By.XPATH, "//label[contains(text(),' Record Date ')]/..//input").get_attribute("value")
W_RecordDate = W_RecordDate.replace("/", "").strip()
b = W_RecordDate[4:]
c = W_RecordDate[0:4]
W_RecordDate = b+c
W_RecordDate = int(W_RecordDate)
W_VendorOperatorCode = driver.find_element(By.XPATH, "//label[contains(text(),' Vendor Operator Code ')]/..//input").get_attribute("value")
W_ImageName = driver.find_element(By.XPATH, "//label[contains(text(),' Image Name ')]/..//input").get_attribute("value")
W_CountyName = driver.find_element(By.XPATH, "//label[contains(text(),' County Name ')]/..//input").get_attribute("value")
W_State = driver.find_element(By.XPATH, "//label[contains(text(),' State ')]/..//input").get_attribute("value")
# W_FIPS = driver.find_element(By.XPATH, "//label[contains(text(),' FIPS ')]/..//input").get_attribute("value")
W_FIPS = driver.find_element(By.XPATH, "//label[contains(text(),' FIPS ')]/..//input").get_attribute("value")
driver.find_element(By.XPATH, "//a[contains(text(), 'Header')]").click()
W_ContractDate = driver.find_element(By.XPATH, "//label[contains(text(),' Contract Date ')]/..//input").get_attribute("value")
W_ContractDate = W_ContractDate.replace("/", "").strip()
b = W_ContractDate[4:]
c = W_ContractDate[0:4]
W_ContractDate = b+c
W_ContractDate = int(W_ContractDate)
W_RecordingDate = driver.find_element(By.XPATH, "(//label[contains(text(),' Recording Date ')]/..//input)[1]").get_attribute("value")
W_RecordingDate = W_RecordingDate.replace("/", "").strip()
b = W_RecordingDate[4:]
c = W_RecordingDate[0:4]
W_RecordingDate = b+c
W_RecordingDate = int(W_RecordingDate)
W_BookNumberType = driver.find_element(By.XPATH, "(//label[contains(text(),' Book # Type  ')]/..//input)[1]").get_attribute("value")
W_BookNumberParsed = driver.find_element(By.XPATH, "//label[contains(text(),' Book # Parsed  ')]/..//input").get_attribute("value")
W_PageNumber = driver.find_element(By.XPATH, "//label[contains(text(),' Page # ')]/..//input").get_attribute("value")
W_DocumentNumber = driver.find_element(By.XPATH, "//label[contains(text(),' Document Number ')]/..//input").get_attribute("value").strip()
# W_DocumentNumber = int(W_DocumentNumber)
print(type(W_DocumentNumber))
W_DocumentTitle = driver.find_element(By.XPATH, "//label[contains(text(), ' Document Title ')]/..//input").get_attribute("value")
W_PartialInterestTransfer = driver.find_element(By.XPATH, "//label[contains(text(), ' Partial Interest Transfer ')]/..//input").get_attribute("value")
W_SalesPriceforthisRecord = driver.find_element(By.XPATH, "//label[contains(text(), ' Sales Price for this Record ')]/..//input").get_attribute("value")
W_TotalSalePrice = driver.find_element(By.XPATH, "//label[contains(text(), ' Total Sale Price ')]/..//input").get_attribute("value")
W_CityTransferTax = driver.find_element(By.XPATH, "//label[contains(text(), ' City Transfer Tax ')]/..//input").get_attribute("value")
W_CountyTransferTax = driver.find_element(By.XPATH, "//label[contains(text(), ' County Transfer Tax ')]/..//input").get_attribute("value")
W_StateTransferTax = driver.find_element(By.XPATH, "//label[contains(text(), ' State Transfer Tax ')]/..//input").get_attribute("value")
W_UnlabeledTransferTax = driver.find_element(By.XPATH, "//label[contains(text(), ' Unlabeled Transfer Tax ')]/..//input").get_attribute("value")
W_TaxStatuteReference = driver.find_element(By.XPATH, "//label[contains(text(), ' Tax Statute Reference ')]/..//input").get_attribute("value")
W_ExciseTaxNo = driver.find_element(By.XPATH, "//label[contains(text(), ' Excise Tax No ')]/..//input").get_attribute("value")
W_AttorneyName = driver.find_element(By.XPATH, "//label[contains(text(), ' Attorney Name ')]/..//input").get_attribute("value")
TitleCo1Name = driver.find_element(By.XPATH, "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[1]//input[@name='Name']").get_attribute("value")
TitleCo1Branch = driver.find_element(By.XPATH, "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[1]//input[contains(@id, 'custom-input_branch')]").get_attribute("value")
if TitleCo1Name != "":
    TitleCo1AddressString = driver.find_element(By.XPATH, "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[1]//input[contains(@id, 'custom-input_addressString')]").get_attribute("value")
else:
    TitleCo1AddressString = ""
TitleCo1Type = driver.find_element(By.XPATH, "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[1]//select[contains(@id, 'select_type')]").get_attribute("value")
TitleCo1DocLocation = ""
if driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[1]//input[contains(@id, 'radio_DocLocation')])[1]").is_selected():
    TitleCo1DocLocation = "R"
elif driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[1]//input[contains(@id, 'radio_DocLocation')])[2]").is_selected():
    TitleCo1DocLocation = "S"
elif driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[1]//input[contains(@id, 'radio_DocLocation')])[3]").is_selected():
    TitleCo1DocLocation = "E"
elif driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[1]//input[contains(@id, 'radio_DocLocation')])[4]").is_selected():
    TitleCo1DocLocation = "H"
elif driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[1]//input[contains(@id, 'radio_DocLocation')])[5]").is_selected():
    TitleCo1DocLocation = ""
else:
    pass
TitleCo2Name = ""
TitleCo2Branch = ""
TitleCo2AddressString = ""
TitleCo2Type = ""
TitleCo2DocLocation = ""
TitleCo3Name = ""
TitleCo3Branch = ""
TitleCo3AddressString = ""
TitleCo3Type = ""
TitleCo3DocLocation = ""
TitleCo4Name = ""
TitleCo4Branch = ""
TitleCo4AddressString = ""
TitleCo4Type = ""
TitleCo4DocLocation = ""
TitleCo5Name = ""
TitleCo5Branch = ""
TitleCo5AddressString = ""
TitleCo5Type = ""
TitleCo5DocLocation = ""
try:
    TitleCo2Name = driver.find_element(By.XPATH, "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[2]//input[@name='Name']").get_attribute("value")
    TitleCo2Branch = driver.find_element(By.XPATH, "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[2]//input[contains(@id, 'custom-input_branch')]").get_attribute("value")
    if TitleCo2Name != "":
        TitleCo2AddressString = driver.find_element(By.XPATH, "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[2]//input[contains(@id, 'custom-input_addressString')]").get_attribute("value")
    else:
        TitleCo2AddressString = ""
    TitleCo2Type = driver.find_element(By.XPATH, "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[2]//select[contains(@id, 'select_type')]").get_attribute("value")
    TitleCo2DocLocation = ""
    if driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[2]//input[contains(@id, 'radio_DocLocation')])[1]").is_selected():
        TitleCo2DocLocation = "R"
    elif driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[2]//input[contains(@id, 'radio_DocLocation')])[2]").is_selected():
        TitleCo2DocLocation = "S"
    elif driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[2]//input[contains(@id, 'radio_DocLocation')])[3]").is_selected():
        TitleCo2DocLocation = "E"
    elif driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[2]//input[contains(@id, 'radio_DocLocation')])[4]").is_selected():
        TitleCo2DocLocation = "H"
    elif driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[2]//input[contains(@id, 'radio_DocLocation')])[5]").is_selected():
        TitleCo2DocLocation = ""
    else:
        pass
    if TitleCo2Name != "":
        TitleCo3Name = driver.find_element(By.XPATH,
                                           "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[3]//input[@name='Name']").get_attribute(
            "value")
        TitleCo3Branch = driver.find_element(By.XPATH,
                                             "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[3]//input[contains(@id, 'custom-input_branch')]").get_attribute(
            "value")
        if TitleCo3Name != "":
            TitleCo3AddressString = driver.find_element(By.XPATH,
                                                        "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[3]//input[contains(@id, 'custom-input_addressString')]").get_attribute(
                "value")
        else:
            TitleCo3AddressString = ""
        TitleCo3Type = driver.find_element(By.XPATH,
                                           "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[3]//select[contains(@id, 'select_type')]").get_attribute(
            "value")
        TitleCo3DocLocation = ""
        if driver.find_element(By.XPATH,
                               "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[3]//input[contains(@id, 'radio_DocLocation')])[1]").is_selected():
            TitleCo3DocLocation = "R"
        elif driver.find_element(By.XPATH,
                                 "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[3]//input[contains(@id, 'radio_DocLocation')])[2]").is_selected():
            TitleCo3DocLocation = "S"
        elif driver.find_element(By.XPATH,
                                 "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[3]//input[contains(@id, 'radio_DocLocation')])[3]").is_selected():
            TitleCo3DocLocation = "E"
        elif driver.find_element(By.XPATH,
                                 "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[3]//input[contains(@id, 'radio_DocLocation')])[4]").is_selected():
            TitleCo3DocLocation = "H"
        elif driver.find_element(By.XPATH,
                                 "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[3]//input[contains(@id, 'radio_DocLocation')])[5]").is_selected():
            TitleCo3DocLocation = ""
        else:
            pass
        if TitleCo3Name != "":
            TitleCo4Name = driver.find_element(By.XPATH, "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[4]//input[@name='Name']").get_attribute("value")
            TitleCo4Branch = driver.find_element(By.XPATH, "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[4]//input[contains(@id, 'custom-input_branch')]").get_attribute(
                "value")
            if TitleCo4Name != "":
                TitleCo4AddressString = driver.find_element(By.XPATH, "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[4]//input[contains(@id, 'custom-input_addressString')]").get_attribute(
                    "value")
            else:
                TitleCo4AddressString = ""
            TitleCo4Type = driver.find_element(By.XPATH, "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[4]//select[contains(@id, 'select_type')]").get_attribute(
                "value")
            TitleCo4DocLocation = ""
            if driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[4]//input[contains(@id, 'radio_DocLocation')])[1]").is_selected():
                TitleCo4DocLocation = "R"
            elif driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[4]//input[contains(@id, 'radio_DocLocation')])[2]").is_selected():
                TitleCo4DocLocation = "S"
            elif driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[4]//input[contains(@id, 'radio_DocLocation')])[3]").is_selected():
                TitleCo4DocLocation = "E"
            elif driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[4]//input[contains(@id, 'radio_DocLocation')])[4]").is_selected():
                TitleCo4DocLocation = "H"
            elif driver.find_element(By.XPATH, "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[4]//input[contains(@id, 'radio_DocLocation')])[5]").is_selected():
                TitleCo4DocLocation = ""
            else:
                pass
            if TitleCo4Name != "":
                TitleCo5Name = driver.find_element(By.XPATH,
                                                   "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[5]//input[@name='Name']").get_attribute(
                    "value")
                TitleCo5Branch = driver.find_element(By.XPATH,
                                                     "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[5]//input[contains(@id, 'custom-input_branch')]").get_attribute(
                    "value")
                if TitleCo5Name != "":
                    TitleCo5AddressString = driver.find_element(By.XPATH,
                                                                "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[5]//input[contains(@id, 'custom-input_addressString')]").get_attribute(
                        "value")
                else:
                    TitleCo5AddressString = ""
                TitleCo5Type = driver.find_element(By.XPATH,
                                                   "(//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[5]//select[contains(@id, 'select_type')]").get_attribute(
                    "value")
                TitleCo5DocLocation = ""
                if driver.find_element(By.XPATH,
                                       "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[5]//input[contains(@id, 'radio_DocLocation')])[1]").is_selected():
                    TitleCo5DocLocation = "R"
                elif driver.find_element(By.XPATH,
                                         "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[5]//input[contains(@id, 'radio_DocLocation')])[2]").is_selected():
                    TitleCo5DocLocation = "S"
                elif driver.find_element(By.XPATH,
                                         "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[5]//input[contains(@id, 'radio_DocLocation')])[3]").is_selected():
                    TitleCo5DocLocation = "E"
                elif driver.find_element(By.XPATH,
                                         "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[5]//input[contains(@id, 'radio_DocLocation')])[4]").is_selected():
                    TitleCo5DocLocation = "H"
                elif driver.find_element(By.XPATH,
                                         "((//label[contains(text(), ' Attorney Name ')]/../../../..//app-aerepeate-section//div[@class = 'ng-star-inserted'])[5]//input[contains(@id, 'radio_DocLocation')])[5]").is_selected():
                    TitleCo5DocLocation = ""
                else:
                    pass
except:
    pass
TitleOrderNumber = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_titleOrderNumber')]").get_attribute("value")
MortgageLenderName = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_mortgageLenderName')]").get_attribute("value")
LenderMailStreetAddress = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_lenderMailStreetAddress')]").get_attribute("value")
LenderMailUnit = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_lenderMailUnit')]").get_attribute("value")
LenderMailCity = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_lenderMailCity')]").get_attribute("value")
LenderMailState = driver.find_element(By.XPATH, "//select[contains(@id, 'select_lenderMailState')]").get_attribute("value")
LenderMailZip = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_lenderMailZip')]").get_attribute("value")
LenderMailZipPlus4 = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_lenderMailZipplus4')]").get_attribute("value")
MortgageLoanAmount = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_mortgageLoanAmount')]").get_attribute("value")
MortgageInterestRate = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_mortgageInterestRate')]").get_attribute("value")
MortgageDueDate = driver.find_element(By.XPATH, "//input[contains(@name, 'Mortgage Due Date')]").get_attribute("value")
OriginalDeedRecordingDate = driver.find_element(By.XPATH, "//input[contains(@name, 'Original Deed Recording Date')]").get_attribute("value")
OriginalDeedRecordersBookType = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_originalDeedRecordersBookType')]").get_attribute("value")
OriginalDeedRecordersBookNumber = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_originalDeedRecordersBookNumber')]").get_attribute("value")
OriginalDeedRecordersPageNumber = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_originalDeedRecordersPageNumber')]").get_attribute("value")
OriginalDeedDocumentNumber = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_Original Deed Document Number')]").get_attribute("value").strip()
if W_State in ['MN', 'OR', 'HI']:
    TransferCertificateOfTitle = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_transferCertificateofTitle')]").get_attribute("value")
    DoubleSystemRecordingDate = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_doubleSystemRecordingDate')]").get_attribute("value")
    DoubleSystemDocumentNumber = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_doubleSystemDocumentNumber')]").get_attribute("value")
    RecordingDistrict = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_recordingDistrict')]").get_attribute("value")
    DoubleSystemRecordingFlag = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_doubleSystemRecordingFlag')]").get_attribute("value")
    HICondoCPR_HPR = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_HICondoCPRHPR')]").get_attribute("value")
else:
    TransferCertificateOfTitle = ""
    DoubleSystemRecordingDate = ""
    DoubleSystemDocumentNumber = ""
    RecordingDistrict = ""
    DoubleSystemRecordingFlag = ""
    HICondoCPR_HPR = ""
driver.find_element(By.XPATH, "//a[contains(text(), 'Legal')]").click()
PrimaryParcelNumber = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_primaryParcelNumber')]").get_attribute("value")
SecondaryParcelNumber = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_secondaryParcelNumber')]").get_attribute("value")
PropertyStreetAddress = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_propertyStreetAddress')])[1]").get_attribute("value").upper()
PropertyUnit = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_propertyUnit')])[1]").get_attribute("value")
PropertyCity = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_propertyCity')])[1]").get_attribute("value").upper()
PropertyState = driver.find_element(By.XPATH, "(//select[contains(@id, 'select_propertyState')])[1]").get_attribute("value")
PropertyState = driver.find_element(By.XPATH, f"(//select[contains(@id, 'select_propertyState')])[1]//option[contains(@value,'{PropertyState}')]").text.replace("Select", "")
PropertyZip = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_propertyZip')])[1]").get_attribute("value")
PropertyZip = int(PropertyZip)
PropertyZipplus4 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_propertyZip4')])[1]").get_attribute("value")
FullLegalCollected = ""
NoLegalDescription = ""
if driver.find_element(By.XPATH, "(//input[contains(@id, 'radio_cullLegalCollected')])[1]").is_selected():
    FullLegalCollected = "Y"
elif driver.find_element(By.XPATH, "(//input[contains(@id, 'radio_cullLegalCollected')])[2]").is_selected():
    FullLegalCollected = "N"
    if driver.find_element(By.XPATH, "(//input[contains(@id, 'checkbox_noLegalDescription')])[1]").is_selected():
        NoLegalDescription = "Y"
else:
    pass
PartialPropertyTransfer = ""
if driver.find_element(By.XPATH, "(//input[contains(@id, 'multicheckbox_partialPropertyTransfer')])[1]").is_selected():
    PartialPropertyTransfer = "A"
elif driver.find_element(By.XPATH, "(//input[contains(@id, 'multicheckbox_partialPropertyTransfer')])[2]").is_selected():
    PartialPropertyTransfer = "L"
elif driver.find_element(By.XPATH, "(//input[contains(@id, 'multicheckbox_partialPropertyTransfer')])[3]").is_selected():
    PartialPropertyTransfer = "B"
else:
    pass
MetesandBounds = ""
if driver.find_element(By.XPATH, "(//input[contains(@id, 'multicheckbox_partialPropertyTransfer')])[1]").is_selected():
    MetesandBounds = "Y"
MultipleTownships = ""
MultipleRanges = ""
if driver.find_element(By.XPATH, "(//input[contains(@id, 'checkbox_multipleTownships')])[1]").is_selected():
    MultipleTownships = "Y"
if driver.find_element(By.XPATH, "(//input[contains(@id, 'checkbox_multipleRanges')])[1]").is_selected():
    MultipleRanges = "Y"
LegalDescriptionText = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_LegalDescriptionText')])[1]").get_attribute("value")
MultipleCountyFlag = driver.find_element(By.XPATH, "(//select[contains(@id, 'select_multipleCountyFlag')])[1]").get_attribute("value")
SupplementalAPN = driver.find_element(By.XPATH, "(//select[contains(@id, 'select_supplementalAPN')])[1]").get_attribute("value")
CountOfUnits = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_countofUnits')])[1]").get_attribute("value")
LegalLotNumber = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_legalLotNumber')])[1]").get_attribute("value")
LegalBlock = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_legalBlock')])[1]").get_attribute("value")
LegalSubdivisionName = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_legalSubdivisionName')])[1]").get_attribute("value")
LegalCityMunicipalityandTownship = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_legalCityMuniTown')])[1]").get_attribute("value")
LegalSection = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_legalSection')])[1]").get_attribute("value")
LegalDistrict = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_legalDistrict')])[1]").get_attribute("value")
LegalLandLot = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_legalLandLot')])[1]").get_attribute("value")
LegalUnit = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_legalUnit')])[1]").get_attribute("value")
CondoPUDName = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_condoPUDName')])[1]").get_attribute("value")
LegalPhaseNumber = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_legalPhase')])[1]").get_attribute("value")
LegalTractNumber = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_legalTract')])[1]").get_attribute("value")
LegalTractNumber = int(LegalTractNumber)
LotSizeSqFt = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_lotSizeSqFt')])[1]").get_attribute("value")
Acreage = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_acreage')])[1]").get_attribute("value")
LegalBriefDescription = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_legalBriefDescription')])[1]").get_attribute("value")
LegalSectionTwnRangeMerid = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_legalSectionTwnRangeMerid')])[1]").get_attribute("value")
MapReferenceType = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_mapReferenceType')])[1]").get_attribute("value")
MapReference1 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_mapReference1')])[1]").get_attribute("value")
MapReference2 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_mapReference2')])[1]").get_attribute("value")
MapReference3 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_mapReference3')])[1]").get_attribute("value")
MapRecordingDate = driver.find_element(By.XPATH, "(//input[@name='Map Recording Date'])[1]").get_attribute("value")
DEDDocPhrase1 = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_dedDocPhrase1')]").get_attribute("value")
DEDDocPhrase2 = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_dedDocPhrase2')]").get_attribute("value")
DEDDocPhrase3 = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_dedDocPhrase3')]").get_attribute("value")
DEDDocPhrase4 = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_dedDocPhrase4')]").get_attribute("value")
DEDDocPhrase5 = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_dedDocPhrase5')]").get_attribute("value")
time.sleep(5)
# # a = ActionChains(driver)
# # a.move_to_element(By.XPATH, "//b[contains(text(), 'Unmatched Parcels')]/..//button")
# ele = (By.XPATH, "//b[contains(text(), 'Unmatched Parcels')]/..//button")
# driver.execute_script("arguments[0].scrollIntoView(true);", ele)
driver.execute_script("window.scrollTo(0, 750)")
driver.find_element(By.XPATH, "//b[contains(text(), 'Unmatched Parcels')]/..//button").click()
time.sleep(10)
UnmatchedParcelID1 = ""
UnmatchedParcelID2 = ""
UnmatchedParcelID3 = ""
UnmatchedParcelID4 = ""
UnmatchedParcelID5 = ""
try:
    if PrimaryParcelNumber != "":
        UnmatchedParcelID1 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_unmatchedParcelID')])[1]").get_attribute("value")
        UnmatchedParcelID2 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_unmatchedParcelID')])[2]").get_attribute("value")
        UnmatchedParcelID3 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_unmatchedParcelID')])[3]").get_attribute("value")
        UnmatchedParcelID4 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_unmatchedParcelID')])[4]").get_attribute("value")
        UnmatchedParcelID5 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_unmatchedParcelID')])[5]").get_attribute("value")
    else:
        pass
except:
    pass
UnmatchedAddress1Street = ""
UnmatchedAddress2Street = ""
UnmatchedAddress3Street = ""
UnmatchedAddress4Street = ""
UnmatchedAddress5Street = ""
UnmatchedAddress1Unit = ""
UnmatchedAddress2Unit = ""
UnmatchedAddress3Unit = ""
UnmatchedAddress4Unit = ""
UnmatchedAddress5Unit = ""
UnmatchedAddress1City = ""
UnmatchedAddress2City = ""
UnmatchedAddress3City = ""
UnmatchedAddress4City = ""
UnmatchedAddress5City = ""
UnmatchedAddress1State = ""
UnmatchedAddress2State = ""
UnmatchedAddress3State = ""
UnmatchedAddress4State = ""
UnmatchedAddress5State = ""
UnmatchedAddress1ZIP = ""
UnmatchedAddress1ZIPplus4 = ""
UnmatchedAddress2ZIP = ""
UnmatchedAddress2ZIPplus4 = ""
UnmatchedAddress3ZIP = ""
UnmatchedAddress3ZIPplus4 = ""
UnmatchedAddress4ZIP = ""
UnmatchedAddress4ZIPplus4 = ""
UnmatchedAddress5ZIP = ""
UnmatchedAddress5ZIPplus4 = ""
try:
    if PropertyStreetAddress != "":
        UnmatchedAddress1Street = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_street')])[1]").get_attribute("value")
        UnmatchedAddress1Unit = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_unit')])[1]").get_attribute("value")
        UnmatchedAddress1City = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_city')])[2]").get_attribute("value")
        UnmatchedAddress1State = driver.find_element(By.XPATH, "(//select[contains(@id, 'select_state')])[1]").get_attribute("value")
        UnmatchedAddress1State = driver.find_element(By.XPATH, f"(//select[contains(@id, 'select_state')])[1]//option[contains(@value,'{UnmatchedAddress1State}')]").text.replace("Select", "")
        UnmatchedAddress1ZIP = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_zip')])[1]").get_attribute("value")
        UnmatchedAddress1ZIPplus4 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_zip')])[2]").get_attribute("value")
        UnmatchedAddress2Street = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_street')])[2]").get_attribute("value")
        UnmatchedAddress2Unit = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_unit')])[2]").get_attribute("value")
        UnmatchedAddress2City = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_city')])[3]").get_attribute("value")
        UnmatchedAddress2State = driver.find_element(By.XPATH, "(//select[contains(@id, 'select_state')])[2]").get_attribute("value")
        UnmatchedAddress2State = driver.find_element(By.XPATH, f"(//select[contains(@id, 'select_state')])[2]//option[contains(@value,'{UnmatchedAddress2State}')]").text.replace("Select", "")
        UnmatchedAddress2ZIP = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_zip')])[3]").get_attribute("value")
        UnmatchedAddress2ZIPplus4 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_zip')])[4]").get_attribute("value")
        UnmatchedAddress3Street = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_street')])[3]").get_attribute("value")
        UnmatchedAddress3Unit = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_unit')])[3]").get_attribute("value")
        UnmatchedAddress3City = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_city')])[4]").get_attribute("value")
        UnmatchedAddress3State = driver.find_element(By.XPATH, "(//select[contains(@id, 'select_state')])[3]").get_attribute("value")
        UnmatchedAddress3State = driver.find_element(By.XPATH, f"(//select[contains(@id, 'select_state')])[3]//option[contains(@value,'{UnmatchedAddress3State}')]").text.replace("Select", "")
        UnmatchedAddress3ZIP = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_zip')])[5]").get_attribute("value")
        UnmatchedAddress3ZIPplus4 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_zip')])[6]").get_attribute("value")
        UnmatchedAddress4Street = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_street')])[4]").get_attribute("value")
        UnmatchedAddress4Unit = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_unit')])[4]").get_attribute("value")
        UnmatchedAddress4City = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_city')])[5]").get_attribute("value")
        UnmatchedAddress4State = driver.find_element(By.XPATH, "(//select[contains(@id, 'select_state')])[4]").get_attribute("value")
        UnmatchedAddress4State = driver.find_element(By.XPATH, f"(//select[contains(@id, 'select_state')])[4]//option[contains(@value,'{UnmatchedAddress4State}')]").text.replace("Select", "")
        UnmatchedAddress4ZIP = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_zip')])[7]").get_attribute("value")
        UnmatchedAddress4ZIPplus4 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_zip')])[8]").get_attribute("value")
        UnmatchedAddress5Street = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_street')])[5]").get_attribute("value")
        UnmatchedAddress5Unit = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_unit')])[5]").get_attribute("value")
        UnmatchedAddress5City = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_city')])[6]").get_attribute("value")
        UnmatchedAddress5State = driver.find_element(By.XPATH, "(//select[contains(@id, 'select_state')])[5]").get_attribute("value")
        UnmatchedAddress5State = driver.find_element(By.XPATH, f"(//select[contains(@id, 'select_state')])[5]//option[contains(@value,'{UnmatchedAddress5State}')]").text.replace("Select", "")
        UnmatchedAddress5ZIP = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_zip')])[9]").get_attribute("value")
        UnmatchedAddress5ZIPplus4 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_zip')])[10]").get_attribute("value")
except:
    pass

if W_State in ['MN', 'OR', 'HI']:
    MultiUnitFlag = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_multiUnitFlag')]").get_attribute("value")
    PlanNumber = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_planNumber')]").get_attribute("value")
    CourtApplicationNumber = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_courtApplicationNumber')]").get_attribute("value")
    LandCourtMapNumber = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_landCourtMapNumber')]").get_attribute("value")
    LandCourtConsolidationNumber = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_landCourtConsolidationNumber')]").get_attribute("value")
else:
    MultiUnitFlag = ""
    PlanNumber = ""
    CourtApplicationNumber = ""
    LandCourtMapNumber = ""
    LandCourtConsolidationNumber = ""
driver.find_element(By.XPATH, "//a[contains(text(), 'Party')]").click()
SellerFullString = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_sellerFullString')]").get_attribute("value")
Seller1FullName = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'FullName')]").get_attribute("value")
Seller1FirstName = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'FirstName')]").get_attribute("value")
Seller1MiddleName = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'MiddleName')]").get_attribute("value")
Seller1LastNameandSuffix = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'LastName')]").get_attribute("value")
Seller1CorporationName = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'Corporation Name')]").get_attribute("value")
Seller1Relationship = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'Relationship')]").get_attribute("value")
Seller1IndividualInterest = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'Individual Interest')]").get_attribute("value")
try:
    Seller2FullName = driver.find_element(By.XPATH,
                                          "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'FullName')]").get_attribute(
        "value")
    Seller2FirstName = driver.find_element(By.XPATH,
                                           "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'FirstName')]").get_attribute(
        "value")
    Seller2MiddleName = driver.find_element(By.XPATH,
                                            "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'MiddleName')]").get_attribute(
        "value")
    Seller2LastNameandSuffix = driver.find_element(By.XPATH,
                                                   "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'LastName')]").get_attribute(
        "value")
    Seller2CorporationName = driver.find_element(By.XPATH,
                                                 "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'Corporation Name')]").get_attribute(
        "value")
    Seller2Relationship = driver.find_element(By.XPATH,
                                              "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'Relationship')]").get_attribute(
        "value")
    Seller2IndividualInterest = driver.find_element(By.XPATH,
                                                    "(//label[contains(text(),' Full Seller String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'Individual Interest')]").get_attribute(
        "value")
except:
    Seller2FullName = ""
    Seller2FirstName = ""
    Seller2MiddleName = ""
    Seller2LastNameandSuffix = ""
    Seller2CorporationName = ""
    Seller2Relationship = ""
    Seller2IndividualInterest = ""
SellerMailStreetAddress = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_sellerMailStreetAddress')]").get_attribute("value")
SellerMailUnit = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_sellerMailUnit')]").get_attribute("value")
SellerMailCity = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_sellerMailCity')]").get_attribute("value")
SellerMailState = driver.find_element(By.XPATH, "//select[contains(@id, 'select_sellerMailState')]").get_attribute("value")
SellerMailState = driver.find_element(By.XPATH, f"//select[contains(@id, 'select_sellerMailState')]//option[contains(@value,'{SellerMailState}')]").text.replace("Select", "")
SellerMailZip = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_sellerMailZip')]").get_attribute("value")
SellerMailZipplus4 = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_sellerMailZip4')]").get_attribute("value")
BuyerFullString = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_fullBuyerString')]").get_attribute("value")
Buyer1FullName = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'FullName')]").get_attribute("value")
Buyer1FirstName = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'FirstName')]").get_attribute("value")
Buyer1MiddleName = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'MiddleName')]").get_attribute("value")
Buyer1LastNameandSuffix = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'LastName')]").get_attribute("value")
Buyer1CorporationName = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'Corporation Name')]").get_attribute("value")
Buyer1Relationship = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'Relationship')]").get_attribute("value")
Buyer1Vesting = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'Vesting')]").get_attribute("value")
Buyer1IndividualInterest = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[1]//input[contains(@name,'Individual Interest')]").get_attribute("value")
# BuyerAdd = driver.find_element(By.XPATH, "(//button[contains(@class, 'btn btn-sm btn-dark active')])[2]/i")
# time.sleep(2)
# BuyerAdd.click()
Buyer2FullName = ""
Buyer2FirstName = ""
Buyer2MiddleName = ""
Buyer2LastNameandSuffix = ""
Buyer2CorporationName = ""
Buyer2Relationship = ""
Buyer2Vesting = ""
Buyer2IndividualInterest = ""
Buyertext = "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])//span[contains(text(), '2')]"
try:
    driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])//span[contains(text(), '2')]").is_displayed()
    Buyer2FullName = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'FullName')]").get_attribute("value")
    Buyer2FirstName = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'FirstName')]").get_attribute("value")
    Buyer2MiddleName = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'MiddleName')]").get_attribute("value")
    Buyer2LastNameandSuffix = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'LastName')]").get_attribute("value")
    Buyer2CorporationName = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'Corporation Name')]").get_attribute("value")
    Buyer2Relationship = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'Relationship')]").get_attribute("value")
    Buyer2Vesting = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'Vesting')]").get_attribute("value")
    Buyer2IndividualInterest = driver.find_element(By.XPATH, "(//label[contains(text(),' Full Buyer String ')]/../../../following-sibling::formly-field/app-aerepeate-section//div[contains(@class,'p-2 mb-1 mx-0 bg-light border rounded ng-star-inserted')])[2]//input[contains(@name,'Individual Interest')]").get_attribute("value")
except:
    pass
BuyerMailCareofName = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_buyerMailCareofName')]").get_attribute("value")
BuyerMailStreetAddress = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_buyerMailStreetAddress')]").get_attribute("value")
BuyerMailUnit = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_buyerMailUnit')]").get_attribute("value")
BuyerMailCity = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_buyerMailCity')]").get_attribute("value")
BuyerMailState = driver.find_element(By.XPATH, "//select[contains(@id, 'select_buyerMailState')]").get_attribute("value")
BuyerMailState = driver.find_element(By.XPATH, f"//select[contains(@id, 'select_buyerMailState')]//option[contains(@value,'{BuyerMailState}')]").text.replace("Select", "")
BuyerMailZip = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_buyerMailZip')])[1]").get_attribute("value")
BuyerMailZipplus4 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_buyerMailZip')])[2]").get_attribute("value")
TaxMailCareofName = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_taxMailCareofName')]").get_attribute("value")
TaxMailStreetAddress = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_taxMailStreetAddress')]").get_attribute("value")
TaxMailUnit = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_taxMailUnit')]").get_attribute("value")
TaxMailCity = driver.find_element(By.XPATH, "//input[contains(@id, 'custom-input_taxMailCity')]").get_attribute("value")
TaxMailState = driver.find_element(By.XPATH, "//select[contains(@id, 'select_taxMailState')]").get_attribute("value")
TaxMailState = driver.find_element(By.XPATH, f"//select[contains(@id, 'select_taxMailState')]//option[contains(@value,'{TaxMailState}')]").text.replace("Select", "")
TaxMailZip = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_taxMailZip')])[1]").get_attribute("value")
TaxMailZipplus4 = driver.find_element(By.XPATH, "(//input[contains(@id, 'custom-input_taxMailZip')])[2]").get_attribute("value")
null = ""
RecordID = "M"
RecordCount = 1
SellerNameAddendum = ""
BuyerNameAddendum = ""
web_values = [W_venderSourceCode, W_RecordDate, W_VendorOperatorCode, ImageName1, null, RecordID, W_CountyName, W_State, W_FIPS, W_ContractDate, W_RecordingDate, W_BookNumberType, W_BookNumberParsed, W_PageNumber, W_DocumentNumber,
              PrimaryParcelNumber, SecondaryParcelNumber, RecordCount, PartialPropertyTransfer, MultipleCountyFlag, SupplementalAPN, W_PartialInterestTransfer, W_TotalSalePrice, W_SalesPriceforthisRecord, W_ExciseTaxNo, W_StateTransferTax, W_CityTransferTax,
              W_CountyTransferTax, W_UnlabeledTransferTax, W_TaxStatuteReference, SellerFullString, Seller1FullName, Seller1FirstName, Seller1MiddleName, Seller1LastNameandSuffix, Seller1CorporationName, Seller1Relationship, Seller1IndividualInterest, Seller2FullName,
              Seller2FirstName, Seller2MiddleName, Seller2LastNameandSuffix, Seller2CorporationName, Seller2Relationship, Seller2IndividualInterest, SellerNameAddendum, SellerMailStreetAddress, SellerMailUnit, SellerMailCity, SellerMailState, SellerMailZip,
              SellerMailZipplus4, BuyerFullString, Buyer1FullName, Buyer1FirstName, Buyer1MiddleName, Buyer1LastNameandSuffix, Buyer1CorporationName, Buyer1Relationship, Buyer1Vesting, Buyer1IndividualInterest, Buyer2FullName, Buyer2FirstName, Buyer2MiddleName,
              Buyer2LastNameandSuffix, Buyer2CorporationName, Buyer2Relationship, Buyer2Vesting, Buyer2IndividualInterest, BuyerNameAddendum, BuyerMailCareofName, BuyerMailStreetAddress, BuyerMailUnit, BuyerMailCity, BuyerMailState, BuyerMailZip, BuyerMailZipplus4,
              TaxMailCareofName, TaxMailStreetAddress, TaxMailUnit, TaxMailCity, TaxMailState, TaxMailZip, TaxMailZipplus4, PropertyStreetAddress, PropertyUnit, PropertyCity, PropertyState, PropertyZip, PropertyZipplus4, LotSizeSqFt, Acreage, LegalLotNumber, LegalBlock,
              LegalSection, LegalDistrict, LegalLandLot, LegalUnit, LegalCityMunicipalityandTownship, LegalSubdivisionName, CondoPUDName, LegalPhaseNumber, LegalTractNumber, LegalBriefDescription, LegalSectionTwnRangeMerid, MapReferenceType, MapReference1, MapReference2,
              MapReference3, MapRecordingDate, NoLegalDescription, MetesandBounds, MultipleTownships, MultipleRanges, FullLegalCollected, W_AttorneyName, TitleCo1Name, TitleCo1AddressString, TitleCo1Branch, TitleCo1DocLocation, TitleCo1Type, TitleCo2Name, TitleCo2AddressString,
              TitleCo2Branch, TitleCo2DocLocation, TitleCo2Type, TitleCo3Name, TitleCo3AddressString, TitleCo3Branch, TitleCo3DocLocation, TitleCo3Type, TitleOrderNumber, MortgageLenderName, LenderMailStreetAddress, LenderMailUnit, LenderMailCity, LenderMailState, LenderMailZip,
              LenderMailZipPlus4, MortgageLoanAmount, MortgageInterestRate, MortgageDueDate, OriginalDeedRecordingDate, OriginalDeedRecordersBookType, OriginalDeedRecordersBookNumber, OriginalDeedRecordersPageNumber, OriginalDeedDocumentNumber, W_DocumentTitle, DEDDocPhrase1, DEDDocPhrase2,
              DEDDocPhrase3, DEDDocPhrase4, DEDDocPhrase5, CountOfUnits, UnmatchedParcelID1, UnmatchedParcelID2, UnmatchedParcelID3, UnmatchedParcelID4, UnmatchedParcelID5, UnmatchedAddress1Street, UnmatchedAddress1Unit, UnmatchedAddress1City, UnmatchedAddress1State, UnmatchedAddress1ZIP,
              UnmatchedAddress1ZIPplus4, UnmatchedAddress2Street, UnmatchedAddress2Unit, UnmatchedAddress2City, UnmatchedAddress2State, UnmatchedAddress2ZIP, UnmatchedAddress2ZIPplus4, UnmatchedAddress3Street, UnmatchedAddress3Unit, UnmatchedAddress3City, UnmatchedAddress3State, UnmatchedAddress3ZIP,
              UnmatchedAddress3ZIPplus4, UnmatchedAddress4Street, UnmatchedAddress4Unit, UnmatchedAddress4City, UnmatchedAddress4State, UnmatchedAddress4ZIP, UnmatchedAddress4ZIPplus4, UnmatchedAddress5Street, UnmatchedAddress5Unit, UnmatchedAddress5City, UnmatchedAddress5State, UnmatchedAddress5ZIP,
              UnmatchedAddress5ZIPplus4, TransferCertificateOfTitle, DoubleSystemRecordingDate, null, null, DoubleSystemDocumentNumber, RecordingDistrict, DoubleSystemRecordingFlag, HICondoCPR_HPR, null, null, null, null, null, MultiUnitFlag, null, PlanNumber, CourtApplicationNumber,
              LandCourtMapNumber, LandCourtConsolidationNumber, null, null, null, null, null]
print (web_values)

hh = pd.read_csv('C:\\Users\\Sagar\\Webkeying\\output.csv')

# cc = hh.columns.to_list()
hh = hh.replace(np.nan, '')
cc = hh.iloc[0].to_list()
d = 0
for i in web_values:
    if cc[d] == i:
        print(i, '-',  cc[d], " -- Both the input and output value are matching ")
    else:
        print(i, '-', cc[d], " -- Fail")
    d = d + 1
# driver.find_element(By.XPATH, Auto.autoform_submit).click()
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.close()
