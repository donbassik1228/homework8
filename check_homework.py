from datetime import date, timedelta
from main import get_birthdays_per_week

def run_tests():
    # Test case 1: All birthdays are in the future and do not fall on weekends
    users_case1 = [
        {"name": "Maria", "birthday": date.today() + timedelta(days=2)},
        {"name": "Oleg", "birthday": date.today() + timedelta(days=4)},
    ]
    assert get_birthdays_per_week(users_case1) == {'Monday': ['Maria'], 'Wednesday': ['Oleg']}

    # Test case 2: Some birthdays fall on weekends
    users_case2 = [
        {"name": "Bogdan", "birthday": date.today() + timedelta(days=1)},
        {"name": "Vlad", "birthday": date.today() + timedelta(days=7)},
    ]
    assert get_birthdays_per_week(users_case2) == {'Tuesday': ['Bogdan'], 'Monday': ['Vlad']}

    # Test case 3: Some birthdays have already passed this year
    users_case3 = [
        {"name": "Sergio", "birthday": date.today() - timedelta(days=5)},
        {"name": "Frank", "birthday": date.today() - timedelta(days=2)},
    ]
    assert get_birthdays_per_week(users_case3) == {'Wednesday': ['Sergio', 'Frank']}

    # Test case 4: Empty user list
    assert get_birthdays_per_week([]) == {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}

    # Test case 5: All birthdays have already passed this year
    users_case5 = [
        {"name": "Grace", "birthday": date.today() - timedelta(days=10)},
        {"name": "Henry", "birthday": date.today() - timedelta(days=8)},
    ]
    assert get_birthdays_per_week(users_case5) == {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}

    print("All tests passed successfully!")

if __name__ == "__main__":
    run_tests()
