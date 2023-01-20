from datetime import datetime

def validate_name(name: str) -> bool:
    if name.isalpha() and (50 >= len(name) >= 2):
        return True
    return False


def validate_address(address: str) -> bool:
    if 5 < len(address) < 150:
        return True
    return False


def validate_phone_number(phone_number: str) -> bool:
    if len(phone_number) == 10 and phone_number.startswith('0'):
        return True
    return False


def validate_work_time(work_time: str) -> bool:
    '22:00'
    '08:00'
    sep_time = work_time.split(':')
    ['08', '00']
    if len(sep_time) == 2 and (len(sep_time[0]) == 2 and len(sep_time[1]) == 2) and \
        (sep_time[0].isdigit(), sep_time[1].isdigit()) and (0 <= int(sep_time[0]) < 24) and \
        (0 <= int(sep_time[1]) < 60):
        return True
    return False


def validate_work_days(work_days: str) -> bool:
    '1,2,3,4,9'
    ['1', '2', '3']
    EXAMPLE = ('1', '2', '3', '4', '5', '6', '7')
    days = work_days.split(',')
    all_exist = all([day in EXAMPLE for day in days])
    return all_exist
    
    
def validate_percent(percent: float) -> bool:
    if 1 >= percent >=  0:
        return True
    return False


def validate_cafe_status(status: str, EXAMPLE: dict) -> bool:
    keys = EXAMPLE.keys()
    return status in keys


def validate_update_time(time, create_time):
    if type(time) == datetime and create_time <= time:
        return True
    return False
        
        
def match_password(password_one, password_two):
    return password_one == password_two
