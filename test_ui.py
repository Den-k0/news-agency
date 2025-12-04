import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    print("1. Відкриваємо сайт...")
    driver.get("http://localhost:8000/registration/login/")
    time.sleep(1)

    print("2. Вводимо логін та пароль...")
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys("admin")
    password_input.send_keys("adminpass")
    password_input.send_keys(Keys.RETURN)

    time.sleep(2)

    print("3. Перевіряємо результат...")
    page_source = driver.page_source
    current_url = driver.current_url

    # Перевірка на стандартну помилку Django
    error_message = "Please enter a correct username and password"

    if error_message in page_source:
        print("❌ ТЕСТ ПРОВАЛЕНО: Система показала помилку входу.")
    elif "Logout" in page_source:
        print("✅ ТЕСТ ПРОЙДЕНО: Знайдено кнопку Logout.")
    elif "login" not in current_url:
        print("✅ ТЕСТ ПРОЙДЕНО: URL змінився (успішний редірект).")
    else:
        print("❌ ТЕСТ ПРОВАЛЕНО: Незрозумілий стан (ні помилки, ні успіху).")

except Exception as e:
    print(f"❌ Виникла помилка виконання: {e}")

finally:
    driver.quit()
