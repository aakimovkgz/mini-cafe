from datetime import datetime, date

from validates import validate_name, validate_address, validate_phone_number, \
    validate_work_time, validate_work_days, validate_percent, validate_cafe_status, \
    validate_update_time


class Base:
    def __init__(self, id: int) -> None:
        self.__id = id
        self.__created_date = datetime.now()
        self.__updated_date = datetime.now()
        
    @property
    def id(self):
        return self.__id
        
    @property
    def created_date(self):
        return self.__created_date
    
    @property
    def updated_date(self):
        return self.__updated_date
    
    @updated_date.setter
    def updated_date(self, updated_date: datetime):
        is_valid = validate_update_time(
            time=updated_date,
            create_time=self.__created_date
        )
        if is_valid:
            self.__updated_date = updated_date
            print('Updated date success!')
        else:
            print(f'Updated date is inccorect!')


class Cafe(Base):
    
    STATUS_TYPES = {
        '1': 'Work',
        '2': 'Unwork',
        '3': 'Repair',
        '99':  'Cleaning day'
    }
    
    def __init__(self, id: int, name: str, 
                 address: str, phone_number: str,
                 ) -> None:
        super().__init__(id)
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        self.__work_start_time = '10:00'
        self.__work_end_time = '18:00'
        self.__work_days = ('1', '2', '3', '4', '5')
        self.__service_percent = 0.05
        self.__status = '1'
        self.__is_active = True
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        is_valid = validate_name(name=name)
        if is_valid:
            self.__name = name
            print('Name edited success!')
        else:
            print('Name is inccorect!')
            
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address: str):
        is_valid = validate_address(address=address)
        if is_valid:
            self.__address = address
            print('Address edited success!')
        else:
            print('Address is inccorect!')
            
    @property
    def phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number: str):
        is_valid = validate_phone_number(phone_number=phone_number)
        if is_valid:
            self.__phone_number = phone_number
            print('Phone number edited success!')
        else:
            print('Phone number is inccorect!')
            
    @property
    def work_start_time(self):
        return self.__work_start_time
    
    @work_start_time.setter
    def work_start_time(self, work_start_time: str):
        is_valid = validate_work_time(work_time=work_start_time)
        if is_valid:
            self.__work_start_time = work_start_time
            print('Work start time edited success!')
        else:
            print('Work start time is inccorect! Example "HH:mm" "08:00"!!!')
            
    @property
    def work_end_time(self):
        return self.__work_end_time
    
    @work_end_time.setter
    def work_end_time(self, work_end_time: str):
        is_valid = validate_work_time(work_time=work_end_time)
        if is_valid:
            self.__work_end_time = work_end_time
            print('Work end time edited success!')
        else:
            print('Work end time is inccorect! Example "HH:mm" "08:00"!!!')
            
    @property
    def work_days(self):
        return self.__work_days
    
    @work_days.setter
    def work_days(self, work_days: str):
        is_valid = validate_work_days(work_days=work_days)
        if is_valid:
            self.__work_days = work_days
            print('Work days edited success!')
        else:
            print('Work days is inccorect! Example 1,2,3,4,5,6,7 !!!')
            
    @property
    def service_percent(self):
        return self.__service_percent
    
    @service_percent.setter
    def service_percent(self, service_percent: float):
        is_valid = validate_percent(percent=service_percent)
        if is_valid:
            self.__service_percent = service_percent
            print('Service percent edited success!')
        else:
            print('Service percent is inccorect! format 2% -> 0.02')
            
    @property
    def status(self):
        status = self.STATUS_TYPES.get(self.__status, 'Нету статуса')
        return status
        
    @status.setter
    def status(self, status):
        is_valid = validate_cafe_status(
                status=status, 
                EXAMPLE=self.STATUS_TYPES
            )
        if is_valid:
            self.__status = status
            print('Status edited success!')
        else:
            print(f'Status is inccorect! {self.STATUS_TYPES}!')
    
    @property
    def is_active(self):
        return self.__is_active
    

class Employee(Base):
    
    STATUS_TYPES = {
        '1': 'Work',
        '2': 'Unwork',
        '3': 'Sick',
        '4':  'Decree',
        '5':  'Dismissed',
        '6': 'Holiday'
    }
    
    def __init__(self, id: int, cafe_id:int, first_name: str, last_name: str, 
                 phone_number: str, password: str, date_of_birth: date, 
                 passport_id: int, work_start_date: date, 
                 work_end_date: date, status=list(STATUS_TYPES.keys())[0], is_active=True) -> None:
        super().__init__(id)
        self.cafe_id = cafe_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.password = password
        self.date_of_birth = date_of_birth
        self.passport_id = passport_id
        self.status = status
        self.work_start_date = work_start_date
        self.work_end_date = work_end_date
        self.is_active = is_active
        
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Food(Base):
    
    CATEGORY = {
        '1': 'First',
        '2': 'Second',
        '3': 'Candy',
        '4': 'Hot drink',
        '5': 'Drink',
        '6': 'Breakfast',
        '7': 'Salad',
        '8': 'Snacks'
    }
    
    def __init__(self, id: int, name: str, image: str, 
                 description: str, category: str,
                 employee_id: int, weight=0, price=0) -> None:
        super().__init__(id)
        self.name = name
        self.image = image
        self.description = description
        self.category = category
        self.employee_id = employee_id
        self.weight = weight
        self.price = price
        
    def __str__(self) -> str:
        return str(self.name)
        
        
class Menu(Base):
    
    def __init__(self, id: int, name: str, foods: list,
                 start_date: datetime, end_date: datetime,
                 employee_id: int, is_active=True) -> None:
        super().__init__(id)
        self.name = name
        self.foods = foods
        self.start_date = start_date
        self.end_date = end_date
        self.employee_id = employee_id
        self.is_active = is_active
        
    def info(self, all_foods):
        foods_menu_description = ''
        
        for food in self.foods:
            food = all_foods[int(food)]
            foods_menu_description += f"""
            
            Food name: {food.name}
            Price: {food.price}
            Wieght: {food.weight}
            Type: {Food.CATEGORY[food.category]}
            
            Img: {food.image}
            
            Description: {food.description}
            
            -------------------------------------
            """
            
        print(f'Menu name: {self.name}\n\n{foods_menu_description}')
        
    def __str__(self) -> str:
        return str(self.name)
        
        
class Order(Base):
    
    def __init__(self, id: int, employee_id: int, 
                 foods: list, total: float, cafe_id: int) -> None:
        super().__init__(id)
        self.employee_id = employee_id
        self.foods = foods
        self.total = total
        self.cafe_id = cafe_id


class Receipt(Base):
    
    STATUS = {
        '1': 'Unpayed',
        '2': 'Payed',
        '3': 'Rejection',
        '4': 'Free'
    }
    
    def __init__(self, id: int, order_id: int,
                 status=list(STATUS.keys())[0]) -> None:
        super().__init__(id)
        self.order_id = order_id
        self.status = status
