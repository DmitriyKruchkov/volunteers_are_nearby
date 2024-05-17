from selenium import webdriver
import os
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# открытие сайта
driver.get('http://188.225.75.29:5000')

try:
    # нажатие кнопки зарегистрироваться
    register_button = driver.find_element("xpath", '//a[text()="Зарегистрироваться"]')
    register_button.click()
    # ввод данных для регистрации
    input_surname = driver.find_element("xpath", '//input[@name="surname"]')
    input_surname.send_keys("Иванов")
    input_name = driver.find_element("xpath", '//input[@name="name"]')
    input_name.send_keys("Иван")
    input_nickname = driver.find_element("xpath", '//input[@name="nickname"]')
    input_nickname.send_keys("Ванька-встанька")
    input_email = driver.find_element("xpath", '//input[@name="email"]')
    input_email.send_keys("vanya_i@mail.ru")
    input_password = driver.find_element("xpath", '//input[@name="password"]')
    input_password.send_keys("ivan123")
    input_password_again = driver.find_element("xpath", '//input[@name="password_again"]')
    input_password_again.send_keys("ivan123")

    photo = "D:/фото/inshot/InShot_20240120_233625922.png"
    file_path = os.path.abspath(photo)
    input_photo = driver.find_element("xpath", '//input[@name="photo"]')
    input_photo.send_keys(file_path)
    input_about = driver.find_element("xpath", '//textarea[@name="about"]')
    input_about.send_keys("Я Иван и я Иван, вместе мы Иваны")
    input_submit = driver.find_element("xpath", '//input[@name="submit"]')
    input_submit.click()

    # нажатие кнопки войти
    register_button = driver.find_element("xpath", '//a[text()="Войти"]')
    register_button.click()

    # ввод данных для входа
    input_email = driver.find_element("xpath", '//input[@name="email"]')
    input_email.send_keys("vanya_i@mail.ru")
    input_password = driver.find_element("xpath", '//input[@name="password"]')
    input_password.send_keys("ivan123")
    input_submit = driver.find_element("xpath", '//input[@name="submit"]')
    input_submit.click()

    personal_cabinet = driver.find_element("xpath", '//button[contains(.,"Личный кабинет")]')
    personal_cabinet.click()

    left_column_info = driver.find_element(By.CLASS_NAME, 'left-column-info').text
    assert "Имя:\nИван" in left_column_info, "Имя не совпадает"
    assert "Фамилия:\nИванов" in left_column_info, "Фамилия не совпадает"
    assert "Никнейм:\nВанька-встанька" in left_column_info, "Никнейм не совпадает"
    assert "Email:\nvanya_i@mail.ru" in left_column_info, "Email не совпадает"
    assert "О себе:\nЯ Иван и я Иван, вместе мы Иваны" in left_column_info, "Описание не совпадает"
    print("Все проверки пройдены успешно")

    # переход на главную страницу
    return_main_page = driver.find_element("xpath",'//a[text()="Волонтеры рядом"]')
    return_main_page.click()

    # нажатие предложить новость
    suggest_item = driver.find_element("xpath", '//button[contains(.,"Предложить новость")]')
    suggest_item.click()

    # ввод инфы для мероприятия
    input_event_name = driver.find_element("xpath", '//input[@name="event_name"]')
    input_event_name.send_keys("Субботник")
    select_event_type = driver.find_element("xpath", '//select[@name="id_event_type"]')
    select_event_type.send_keys("Тип 2")
    input_about_event = driver.find_element("xpath", '//textarea[@name="about"]')
    input_about_event.send_keys("Общегородской субботник")
    input_date = driver.find_element("xpath", '//input[@name="date_of_start"]')
    actions = ActionChains(driver)
    actions.click(input_date)
    actions.send_keys("12052024")
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys("1000")
    actions.perform()
    input_address = driver.find_element("xpath", '//input[@name="address"]')
    input_address.send_keys("Москва, проспект Вернадского, 34")

    photo_event = "D:/фото/inshot/InShot_20240120_233625922.png"
    file_path_event = os.path.abspath(photo_event)
    input_photo_event = driver.find_element("xpath", '//input[@name="photo"]')
    input_photo_event.send_keys(file_path_event)

    input_submit_event = driver.find_element("xpath", '//input[@name="submit"]')
    input_submit_event.click()

    input()
finally:
    driver.quit()

