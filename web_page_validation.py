import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://adnabu-arjun.myshopify.com/")
driver.maximize_window()
title = driver.title
expected_title = "adnabu-Sumit"
if title == expected_title:
    print("URL navigation validation is passed")
else:
    print(f"URL navigation validation is failed {expected_title} , but got {title}.")

driver.find_element(By.LINK_TEXT,"14k Solid Bloom Earrings").click()
time.sleep(2)


add_to_cart=driver.find_element(By.XPATH,"//span[normalize-space()='Add to cart']")
product_title=driver.find_element(By.XPATH,"//h1[normalize-space()='14k Solid Bloom Earrings']")
product_price=driver.find_element(By.XPATH,"//span[@class='price-item price-item--sale']")
print("Add to cart button display status: ",add_to_cart.is_displayed())
print("Product title display status: ",product_title.is_displayed())
print("Product Price of Rs. 50,000.00 display status: ",product_price.is_displayed())
print("Add to Cart Button status as Enabled: ",add_to_cart.is_enabled())
add_to_cart.click()
time.sleep(3)
cart_img=driver.find_element(By.XPATH,"//img[@alt='14k Solid Bloom Earrings']")
print("In Cart Menu selected product image display status: ",cart_img.is_displayed())
cart_prod_price=driver.find_element(By.XPATH,"//*[@id='shopify-section-cart-template']/div/form/table/tbody/tr[1]/td[3]")
print("In Cart Menu selected product Price display status: ",cart_prod_price.is_displayed())
cart_prod_qty=driver.find_element(By.XPATH,"//*[contains(@id,'updates_large_40428607504481')]")
print("In Cart Menu selected product Quantity display status: ",cart_prod_qty.is_displayed())
cart_prod_name=driver.find_element(By.XPATH,"//tbody/tr[1]/td[2]/div[1]/a[1]")
print("In Cart Menu selected product Title display status: ",cart_prod_name.is_displayed())
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Remove").click()
time.sleep(3)
updated_cart_page=driver.find_element(By.XPATH,"//*[@id='shopify-section-cart-template']/div/div/h1")
print("The Updated cart page Title display status: ",updated_cart_page.is_displayed())
disp_text=driver.find_element(By.XPATH,"//p[@class='cart--empty-message']").text
print("The empty Cart display test displaying",{disp_text})
driver.find_element(By.XPATH,"//*[@id='shopify-section-cart-template']/div/div/a").click()
home_menu=driver.find_element(By.XPATH,"//*[@id='shopify-section-header']/div/header/div/div[1]/h1/a")
print("the Home page Title validation: ",home_menu.is_displayed())
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='shopify-section-header']/div/header/div/div[2]/div/div").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='shopify-section-header']/div/header/div/div[2]/div/div/form/input").send_keys("14k Wire Bloom Earrings ...")
driver.find_element(By.XPATH,"//*[@id='shopify-section-header']/div/header/div/div[2]/div/div/form/button").click()
search_prod_title=driver.find_element(By.XPATH,"//*[@id='MainContent']/div/div/h1")
print("The search Product result validation status: ",search_prod_title.is_displayed())
time.sleep(3)
result_search=driver.find_element(By.XPATH,"//*[@id='MainContent']/div/div/h1")
print("The srearch result Text is: ",result_search.text)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='SiteNav']/li[1]/a/span").click()
time.sleep(2)
title = driver.title
expected_title = "adnabu-Sumit"
if title == expected_title:
    print("URL navigation validation is passed")
else:
    print(f"URL navigation validation is failed {expected_title} , but got {title}.")

dropdown_currency=driver.find_element(By.XPATH,"//*[@id='CurrencySelector']")
drop=Select(dropdown_currency)
drop.select_by_visible_text("AFN")
display_currency=driver.find_element(By.XPATH,"//*[@id='CurrencySelector']")
print("changed currency is {display_currency}")
print("The changed currency validation status: ",display_currency.is_displayed())

driver.find_element(By.XPATH,"//*[@id='SiteNav']/li[2]/a/span").click()
catlg_page=driver.find_element(By.XPATH,"//*[@id='shopify-section-collection-template']/div/header/div[1]/div/h1/span")
print("The Catlog page title validation status: ",catlg_page.is_displayed())
time.sleep(2)
dropdown_filter=driver.find_element(By.XPATH,"//*[@id='FilterTags']")
dropfil=Select(dropdown_filter)
dropfil.select_by_visible_text("Rose Gold")
Set_filter=driver.find_element(By.XPATH,"//*[@id='FilterTags']")
val=Set_filter.is_displayed()
print("The activated set filter validation value :Rose Gold ",{val})

Sort_by=driver.find_element(By.XPATH,"//*[@id='SortBy']")
dropfil=Select(Sort_by)
dropfil.select_by_visible_text("Featured")
Set_sort=driver.find_element(By.XPATH,"//*[@id='SortBy']")
valu=Set_sort.is_displayed()
print("The activated set filter  validation value :Featured ",{valu})

driver.close()
