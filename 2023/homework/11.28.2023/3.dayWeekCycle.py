import calendar

days_of_week = list(calendar.day_name)

for day in days_of_week:
    user_input = input(f"День недели - {day}. Хотите увидеть следующий день? (Введите OK для продолжения): ")
    if user_input.upper() != "OK":
        break

#VN: после Sunday должен снова идти Monday и так бесконечно