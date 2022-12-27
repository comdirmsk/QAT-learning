import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_photo_availability(go_to_my_pets):

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

      statistic = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")

      images = pytest.driver.find_elements_by_css_selector('.table.table-hover img')

      number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

      half = number // 2

   # Находим количество питомцев с фотографией
   number_а_photos = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_а_photos += 1

def test_there_is_a_name_age_and_gender(go_to_my_pets):

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   pet_data = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

   
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      result = len(split_data_pet)
      assert result == 3