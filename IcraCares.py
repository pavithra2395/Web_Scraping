import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import sys
import urllib.request as ul

print("Loading driver...")

def icracares():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    prefs = {"download.default_directory": r"D:\Users\rishi\WebScrapping\download\IcraCares&Ratings"}
    options.add_experimental_option("prefs", prefs)
    # s = Service(r'F:\Software\chromedriver.exe')
    driver = webdriver.Chrome(options=options, executable_path=r'D:\Users\rishi\WebScrapping\chromedriver.exe')
    wait = WebDriverWait(driver, 22)
    isInternet = True
    # wait = WebDriverWait(driver, 20)
    # driver.maximize_window()
    # url = 'https://wixlabs-file-sharing.appspot.com/index?pageId=coey1&compId=TPASection_kewu8ta1&viewerCompId=TPASection_kewu8ta1&siteRevision=1496&viewMode=site&deviceType=desktop&locale=en&tz=Asia%2FKolkata&regionalLanguage=en&width=980&height=5033&instance=dN1mTR_Fi5wLqa97AabUHcsF18rcwxmzUF2XYjSliG8.eyJpbnN0YW5jZUlkIjoiOTQyNTI0ZWYtOTQ3NC00NDI4LWIwNmItOGE4NjMyMDNhYzNkIiwiYXBwRGVmSWQiOiIxNTM3YjI0ZS0yOWQxLTZkOGYtYjhlMS1kNjg2MGYyZjcwYjkiLCJtZXRhU2l0ZUlkIjoiMWYxMTJkMjAtYzkzZC00NTZmLWE0YzQtNjI4Mzg2YWM1NTkyIiwic2lnbkRhdGUiOiIyMDIyLTAxLTIwVDA1OjEzOjI0LjIzOFoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjNiMWNmNWFjLWU4ZTItNGY5Zi05YTI5LTBkM2U0MTMwM2M4ZCIsImJpVG9rZW4iOiI4YjM0MDljZi01ZDQ5LTAxNDctMTRhZi1lODA1YjRhZmY5YWYiLCJzaXRlT3duZXJJZCI6Ijk4NjViODM2LTU0MzktNGNkMi04ZTdmLWEzZjAzNzk3Zjc1ZSJ9&currency=INR&currentCurrency=INR&commonConfig=%7B%22brand%22%3A%22wix%22%2C%22bsi%22%3A%22b19427bf-6edd-4db9-9579-c748c4906c53%7C2%22%2C%22BSI%22%3A%22b19427bf-6edd-4db9-9579-c748c4906c53%7C2%22%7D&target=_top&section-url=https%3A%2F%2Fwww.carerisksolutions.com%2Ffile-share%2F&vsi=b64ffd9a-9f15-46b9-a53f-d513d368e2f0'
    url = 'https://www.carerisksolutions.com/file-share/'
    try:
        driver.get(url)
    except WebDriverException as wde:
        print(f"{wde}")
        isInternet = False

    time.sleep(1)
    if isInternet:
        print("--------Company list---------")
        is_switch = wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='File Share' and @aria-label='File Share']")))
        if is_switch:
            print("driver switch to iframe successfully")
            company_list = driver.find_elements(By.XPATH, '/html/body/div/div/section/div/div/section[2]/ul/li')  # '/html/body/div/div/section/div/div/section[2]/ul')
            if len(company_list) > 0:
                print(f"company list len is : {len(company_list)}")
                print(f"company list type is : {type(company_list)}")
                print(f"company list is : {company_list}")

                cmp_list = []
                count_cmp = 0
                for e in company_list:
                    if count_cmp < 5:
                        try:
                            cmp_list.append(e.text.split('\n')[1])
                            row = e.find_element(by=By.XPATH, value=f"/html/body/div/div/section/div/div/section[2]/ul/li[{count_cmp+1}]/div/div[7]/div/div/label")
                            txt = e.text.split('\n')[1]
                            ids = e.get_attribute('id')

                            driver.execute_script("arguments[0].click();", row)

                            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            time.sleep(2)
                            value = e.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/button[@id='menuitem1']")#f"/html/body/div/div/section/div/div/section[2]/ul/li[{count_cmp+1}]/div/div[7]/div/div/button/button")
                            print(f'Value id is {value.id}')
                            print(f'Value title is {value.text}')
                            x = value.location['x']
                            y = value.location['y']
                            # print(f"Row x is {x} and y is {y}")
                            driver.execute_script("arguments[0].click();", value)
                            # actions = ActionChains(driver)
                            # actions.move_to_element(value)
                            # actions.move_by_offset(x, y)
                            # actions.click(on_element=value)
                            # actions.perform()

                            time.sleep(1)
                            driver.implicitly_wait(2)
                            count_cmp += 1

                            print(f"downloading ...")
                            time.sleep(20)
                            # print(f"Download is {download}")
                        except:
                            print(f"{cmp_list[count_cmp-1]} zip download failed...")

                        # row = e.find_element(by=By.XPATH, value=f"/html/body/div/div/section/div/div/section[2]/ul/li[{count_cmp+1}]/div/section/div[2]/span/div/span[1]")
                        # value = driver.execute_script("arguments[0].click();", row)
                        # last_height = driver.execute_script("return document.body.scrollHeight")
                        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        # ActionChains(driver).click(on_element=row).perform()
                        # down = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menuitem1']"))).click()
                        # down = driver.find_elements(by=By.ID, value='button')

                print(cmp_list)
                print(f'cmp_list: {len(cmp_list)}')
                driver.quit()
            else:
                print("company list not loaded")
                driver.quit()
        else:
            print("driver not switch.")

    driver.quit()