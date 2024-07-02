from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def list_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, 'p')
    for paragraph in paragraphs:
        print(paragraph.text)
        user_input = input("Нажмите Enter для следующего параграфа или введите 'q' для выхода: ")
        if user_input.lower() == 'q':
            break

def navigate_to_link(browser):
    links = browser.find_elements(By.XPATH, "//div[@id='bodyContent']//a[starts-with(@href, '/wiki/')]")
    for i, link in enumerate(links):
        print(f"{i+1}: {link.text} - {link.get_attribute('href')}")
    link_choice = int(input("Введите номер ссылки, на которую хотите перейти: ")) - 1
    if 0 <= link_choice < len(links):
        browser.get(links[link_choice].get_attribute('href'))
        time.sleep(5)

def main():
    query = input("Что вы хотите найти в Википедии? ")
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
    assert "Википедия" in browser.title
    time.sleep(5)
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Введите номер действия: ")

        if choice == '1':
            list_paragraphs(browser)
        elif choice == '2':
            navigate_to_link(browser)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    browser.quit()

if __name__ == "__main__":
    main()

