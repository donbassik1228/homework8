from datetime import datetime, timedelta, date

def get_birthdays_per_week(users):
    birthdays_per_week = {}
    today = date.today()

    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()

        if today > birthday_this_year:
            birthday_next_year = datetime(today.year + 1, birthday.month, birthday.day).date()
        else:
            birthday_next_year = birthday_this_year

        if birthday_next_year.weekday() == 5:  # Суббота
            birthday_next_year += timedelta(days=2)
        elif birthday_next_year.weekday() == 6:  # Воскресенье
            birthday_next_year += timedelta(days=1)

        time_left_until_bd = birthday_next_year - today
        days_left = time_left_until_bd.days

        if 0 <= days_left <= 7:
            day_of_week = birthday_next_year.strftime('%A')

            if day_of_week not in birthdays_per_week:
                birthdays_per_week[day_of_week] = [name.split()[0]]
            else:
                birthdays_per_week[day_of_week].append(name.split()[0])

    return birthdays_per_week

if __name__ == "__main__":
    users = [
        {"name": "Bogdan", "birthday": datetime(2004, 12, 24).date()},
        {"name": "Maria", "birthday": datetime(2006, 6, 30).date()},
        {"name": "Sergiy", "birthday": datetime(2005, 7, 15).date()},
        {"name": "Martin", "birthday": datetime(2003, 3, 12).date()},
        {"name": "Vlad", "birthday": datetime(1999, 2, 7).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)

    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
