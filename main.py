from datetime import date, timedelta

def get_birthdays_per_week(users):
    today = date.today()
    current_weekday = today.weekday()

    
    monday = today - timedelta(days=current_weekday)

    
    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': [],
    }

    for user in users:
        user_name = user['name']
        user_birthday = user['birthday'].replace(year=today.year)

        
        if user_birthday < today:
            user_birthday = user_birthday.replace(year=today.year + 1)

        
        if today <= user_birthday <= monday + timedelta(days=6):
            
            birthday_weekday = (user_birthday - monday).days

            
            if birthday_weekday == 0 and user_birthday < today:
                birthday_weekday = 7

            
            birthdays_per_week[list(birthdays_per_week.keys())[birthday_weekday - 1]].append(user_name)

    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Maria", "birthday": date(2024, 1, 15)},
        {"name": "Oleg", "birthday": date(2024, 1, 16)},
        {"name": "Bogdan", "birthday": date(2024, 1, 18)},
        {"name": "Vlad", "birthday": date(2024, 1, 20)},
        {"name": "Sergio", "birthday": date(2024, 1, 22)},
    ]

    result = get_birthdays_per_week(users)
    print(result)
