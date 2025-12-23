"""Задача 6 (3 балла). Файл mbox.txt содержит метаданные почтового сервера.
Мы знаем, что строка с адресом автора письма начинается с "From ". Найти
адреса всех авторов сообщений и найти того из них, кто пишет больше всех
писем."""
def analyze_emails_fast():
    print("Анализируем локальный файл...")

    try:
        with open('2.6.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        print(f"Прочитано {len(lines)} строк")

        # Считаем письма
        email_counts = {}
        total_emails = 0

        for line in lines:
            if line.startswith('From '):
                parts = line.split()
                if len(parts) > 1:
                    email = parts[1]
                    email_counts[email] = email_counts.get(email, 0) + 1
                    total_emails += 1

        print(f"Найдено писем: {total_emails}")
        print(f"Уникальных авторов: {len(email_counts)}")

        # Находим самого активного
        if email_counts:
            # Сортируем по количеству писем
            sorted_emails = sorted(email_counts.items(), key=lambda x: x[1], reverse=True)

            print("\nТоп-5 самых активных авторов:")
            for i, (email, count) in enumerate(sorted_emails[:5], 1):
                print(f"{i}. {email}: {count} писем")

            # Самый активный
            most_active = sorted_emails[0]
            print(f"\nСамый активный автор:")
            print(f"Email: {most_active[0]}")
            print(f"Писем: {most_active[1]}")

        else:
            print("Не найдено писем для анализа")

    except FileNotFoundError:
        print("Файл '2.6.txt' не найден!")
    except Exception as e:
        print(f"Ошибка: {e}")

analyze_emails_fast()