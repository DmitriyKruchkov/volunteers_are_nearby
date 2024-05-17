<<<<<<< HEAD
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

    photo = "photo.jpg"
    file_path = os.path.abspath(photo)
    input_photo = driver.find_element("xpath", '//input[@name="photo"]')
    input_photo.send_keys(file_path)
    input_about = driver.find_element("xpath", '//textarea[@name="about"]')
    input_about.send_keys("Я Иван и я Иван, вместе мы Иваны")

    assert input_surname.get_attribute('value') == "Иванов", "Ошибка в фамилии"
    assert input_name.get_attribute('value') == "Иван", "Ошибка в имени"
    assert input_nickname.get_attribute('value') == "Ванька-встанька", "Ошибка в никнейме"
    assert input_email.get_attribute('value') == "vanya_i@mail.ru", "Ошибка в почте"
    assert input_password.get_attribute('value') == "ivan123", "Ошибка в пароле"
    assert input_password_again.get_attribute('value') == "ivan123", "Ошибка в пароле (повтор)"
    assert input_about.get_attribute('value') == "Я Иван и я Иван, вместе мы Иваны", "Ошибка в описании"
    print("Данные для регистрации введены правильно")

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

    assert input_email.get_attribute('value') == "vanya_i@mail.ru", "Ошибка в почте"
    assert input_password.get_attribute('value') == "ivan123", "Ошибка в пароле"
    print("Данные для входа введены правильно")

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
    print("Личный кабинет заполнен правильно")

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

    photo_event = "photo.jpg"
    file_path_event = os.path.abspath(photo_event)
    input_photo_event = driver.find_element("xpath", '//input[@name="photo"]')
    input_photo_event.send_keys(file_path_event)
    assert input_event_name.get_attribute('value') == "Субботник", "Ошибка в названии события"
    assert select_event_type.get_attribute('value') == "2", "Ошибка в типе события"
    assert input_about_event.get_attribute('value') == "Общегородской субботник", "Ошибка в описании события"
    assert input_address.get_attribute('value') == "Москва, проспект Вернадского, 34", "Ошибка в адресе"
    print("Данные мероприятия введены правильно")
    input_submit_event = driver.find_element("xpath", '//input[@name="submit"]')
    input_submit_event.click()

finally:
    driver.quit()

=======
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

>>>>>>> 5478cea234fc1d23a8612adaf6c7b31a55456aa1
