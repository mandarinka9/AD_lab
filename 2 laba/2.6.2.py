"""Задача 6 (3 балла). Файл mbox.txt содержит метаданные почтового сервера.
Мы знаем, что строка с адресом автора письма начинается с "From ". Найти
адреса всех авторов сообщений и найти того из них, кто пишет больше всех
писем."""
import requests

def process_email_data():
    try:
        # Загрузка данных из интернета
        mbox_data = requests.get('https://www.py4e.com/code3/mbox.txt', timeout=15)
        mbox_data.raise_for_status()

        # Преобразование текста в список строк
        email_lines = mbox_data.text.splitlines()

        print(f"Обработано строк в файле: {len(email_lines)}")

        # Словарь для кол-ва соо отправителей
        email_counters = {}

        for line in email_lines:
            line = line.strip()  # лишние пробелы
            # Проверяем, содержит ли строка информацию об отправителе
            if line[:5] == 'From ' and '@' in line:
                words = line.split()
                # Убеждаемся, что в строке хотя бы 2 слова
                if len(words) > 1:
                    potential_email = words[1]
                    if '@' in potential_email and potential_email.count('@') == 1:
                        # Обновляем счетчик для данного email
                        current_count = email_counters.get(potential_email, 0)
                        email_counters[potential_email] = current_count + 1

        # Анализ результатов подсчета
        if email_counters:
            most_active_email = None
            highest_count = 0

            # Определяем наиболее активного отправителя
            for sender, count in email_counters.items():
                if count > highest_count:
                    highest_count = count
                    most_active_email = sender

            # Вывод результатов анализа
            print(f"Обнаружено уникальных адресов отправителей: {len(email_counters)}")
            print(f"Наибольшая активность у: {most_active_email}")
            print(f"Отправлено сообщений: {highest_count}")

        else:
            print("В данных не найдено информации об отправителях")

    except requests.exceptions.RequestException as network_error:
        print(f"Сетевая ошибка: {network_error}")
    except Exception as unexpected_error:
        print(f"Неожиданная ошибка: {unexpected_error}")


process_email_data()