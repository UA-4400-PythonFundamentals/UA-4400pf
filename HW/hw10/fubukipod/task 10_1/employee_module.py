from typing import ClassVar, List
from person_module import Person

class Employee(Person):
    
    _employee_count: ClassVar[int] = 0
    _employees: ClassVar[List['Employee']] = []

    def __init__(self, name: str, salary: float) -> None:
        super().__init__(name)
        if not isinstance(salary, (int, float)) or salary <= 0:
            raise ValueError(f"Невірна зарплата: {salary}")
        self._salary = salary
        Employee._employee_count += 1
        Employee._employees.append(self)

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, new_salary: float) -> None:
        if not isinstance(new_salary, (int, float)) or new_salary <= 0:
            raise ValueError(f"Невірна зарплата: {new_salary}")
        self._salary = new_salary

    def display_info(self) -> None:
        print(f"Співробітник: {self.name}, Зарплата: {self._salary:.2f}")

    def give_raise(self, percent: float) -> None:
        if percent < 0:
            raise ValueError("Процент має бути невід’ємним")
        old = self._salary
        self._salary *= (1 + percent / 100)
        print(f"{self.name} отримав підвищення: {old:.2f} → {self._salary:.2f}")

    @classmethod
    def get_total_employees(cls) -> int:
        return cls._employee_count

    @classmethod
    def display_all_employees(cls) -> None:
        print(f"=== Усього співробітників: {cls.get_total_employees()} ===")
        for emp in cls._employees:
            emp.display_info()