import mysql.connector

# Подключение к базе данных MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

# Создание курсора для выполнения SQL-запросов
cursor = mydb.cursor()


# 9. Заполнение низкоуровневых таблиц данными
def fill_animal_tables():
    # Вставка данных в таблицу "Собаки"
    dogs_data = [
        ("Рекс", "Поворот вправо", "2019-01-15"),
        ("Бобик", "Сидеть", "2018-03-12"),
        ("Шарик", "Лежать", "2020-06-27")
    ]
    insert_query = "INSERT INTO Dogs (name, command, birth_date) VALUES (%s, %s, %s)"
    cursor.executemany(insert_query, dogs_data)

    # Вставка данных в таблицу "Кошки"
    cats_data = [
        ("Мурзик", "Мяукать", "2017-09-08"),
        ("Барсик", "Царапать", "2019-11-20"),
        ("Васька", "Прятаться", "2016-07-04")
    ]
    insert_query = "INSERT INTO Cats (name, command, birth_date) VALUES (%s, %s, %s)"
    cursor.executemany(insert_query, cats_data)

    # Вставка данных в таблицу "Хомяки"
    hamsters_data = [
        ("Буся", "Крутиться в колесе", "2020-02-01"),
        ("Чебурашка", "Есть семечки", "2018-12-10"),
        ("Шура", "Бегать по трубам", "2019-06-18")
    ]
    insert_query = "INSERT INTO Hamsters (name, command, birth_date) VALUES (%s, %s, %s)"
    cursor.executemany(insert_query, hamsters_data)

    # Вставка данных в таблицу "Лошади"
    horses_data = [
        ("Булан", "Скачать", "2015-05-25"),
        ("Белка", "Прыгать через препятствия", "2017-08-14"),
        ("Рыжик", "Тянуть плуг", "2016-11-30")
    ]
    insert_query = "INSERT INTO Horses (name, command, birth_date) VALUES (%s, %s, %s)"
    cursor.executemany(insert_query, horses_data)

    # Вставка данных в таблицу "Ослы"
    donkeys_data = [
        ("Дон", "Нести груз", "2019-03-06"),
        ("Кики", "Брать на покатушки", "2018-01-22"),
        ("Гоша", "Ходить по горам", "2020-07-11")
    ]
    insert_query = "INSERT INTO Donkeys (name, command, birth_date) VALUES (%s, %s, %s)"
    cursor.executemany(insert_query, donkeys_data)

    mydb.commit()


# 10. Удаление верблюдов и объединение таблиц "Лошади" и "Ослы"
def delete_camels_and_merge_tables():
    # Удаление данных о верблюдах
    delete_query = "DELETE FROM Camels"
    cursor.execute(delete_query)

    # Объединение таблиц "Лошади" и "Ослы"
    merge_query = "INSERT INTO Equines (name, command, birth_date) SELECT name, command, birth_date FROM Horses UNION SELECT name, command, birth_date FROM Donkeys"
    cursor.execute(merge_query)

    mydb.commit()


# 11. Создание таблицы "Молодые животные" и подсчет возраста
def create_young_animals_table():
    # Создание таблицы "Молодые животные"
    create_table_query = "CREATE TABLE YoungAnimals (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), command VARCHAR(255), birth_date DATE, age_months INT)"
    cursor.execute(create_table_query)

    # Заполнение таблицы данными и подсчет возраста
    insert_query = "INSERT INTO YoungAnimals (name, command, birth_date, age_months) SELECT name, command, birth_date, TIMESTAMPDIFF(MONTH, birth_date, CURDATE()) AS age_months FROM (SELECT * FROM Dogs UNION SELECT * FROM Cats UNION SELECT * FROM Hamsters) AS animals WHERE TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) < 3"
    cursor.execute(insert_query)

    mydb.commit()


# 12. Объединение всех таблиц в одну с полями, указывающими на прошлую принадлежность
def merge_all_tables():
    # Создание таблицы "Все животные"
    create_table_query = "CREATE TABLE AllAnimals (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), command VARCHAR(255), birth_date DATE, animal_type ENUM('Dog', 'Cat', 'Hamster', 'Horse', 'Donkey'), previous_table ENUM('Dogs', 'Cats', 'Hamsters', 'Horses', 'Donkeys'))"
    cursor.execute(create_table_query)

    # Объединение данных из всех таблиц
    merge_query = "INSERT INTO AllAnimals (name, command, birth_date, animal_type, previous_table) SELECT name, command, birth_date, 'Dog', 'Dogs' FROM Dogs UNION SELECT name, command, birth_date, 'Cat', 'Cats' FROM Cats UNION SELECT name, command, birth_date, 'Hamster', 'Hamsters' FROM Hamsters UNION SELECT name, command, birth_date, 'Horse', 'Horses' FROM Horses UNION SELECT name, command, birth_date, 'Donkey', 'Donkeys' FROM Donkeys UNION SELECT name, command, birth_date, 'Camel', 'Camels' FROM Camels"
    cursor.execute(merge_query)

    mydb.commit()


# 13. Создание класса с инкапсуляцией методов и наследованием по диаграмме
class Animal:
    def __init__(self, name, command):
        self._name = name
        self._command = command

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_command(self):
        return self._command

    def set_command(self, command):
        self._command = command


class DomesticAnimal(Animal):
    def __init__(self, name, command):
        super().__init__(name, command)


class PetAnimal(DomesticAnimal):
    def __init__(self, name, command):
        super().__init__(name, command)


class Dog(PetAnimal):
    def __init__(self, name, command):
        super().__init__(name, command)


class Cat(PetAnimal):
    def __init__(self, name, command):
        super().__init__(name, command)


class Hamster(PetAnimal):
    def __init__(self, name, command):
        super().__init__(name, command)


class DraughtAnimal(Animal):
    def __init__(self, name, command):
        super().__init__(name, command)


class Horse(DraughtAnimal):
    def __init__(self, name, command):
        super().__init__(name, command)


class Donkey(DraughtAnimal):
    def __init__(self, name, command):
        super().__init__(name, command)


# 14. Реализация программы для реестра домашних животных
def run_animal_registry():
    animals = []

    while True:
        print("1. Завести новое животное")
        print("2. Определить животное в правильный класс")
        print("3. Увидеть список команд, которые выполняет животное")
        print("4. Обучить животное новым командам")
        print("5. Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя животного: ")
            command = input("Введите команду животного: ")

            # Создание экземпляра класса в зависимости от типа животного
            if name.lower() in ["собака", "dog"]:
                animal = Dog(name, command)
            elif name.lower() in ["кошка", "cat"]:
                animal = Cat(name, command)
            elif name.lower() in ["хомяк", "hamster"]:
                animal = Hamster(name, command)
            elif name.lower() in ["лошадь", "horse"]:
                animal = Horse(name, command)
            elif name.lower() in ["осел", "donkey"]:
                animal = Donkey(name, command)
            else:
                animal = Animal(name, command)

            animals.append(animal)
            print("Животное успешно добавлено!")

        elif choice == "2":
            name = input("Введите имя животного: ")

            # Поиск животного по имени и определение класса
            for animal in animals:
                if animal.get_name() == name:
                    if isinstance(animal, PetAnimal):
                        print("Животное относится к классу домашних животных")
                    elif isinstance(animal, DraughtAnimal):
                        print("Животное относится к классу вьючных животных")
                    else:
                        print("Не удалось определить класс животного")
                    break
            else:
                print("Животное не найдено")

        elif choice == "3":
            name = input("Введите имя животного: ")

            # Поиск животного по имени и вывод списка команд
            for animal in animals:
                if animal.get_name() == name:
                    print(f"Животное {animal.get_name()} выполняет команду: {animal.get_command()}")
                    break
            else:
                print("Животное не найдено")

        elif choice == "4":
            name = input("Введите имя животного: ")
            new_command = input("Введите новую команду для животного: ")

            # Поиск животного по имени и обновление команды
            for animal in animals:
                if animal.get_name() == name:
                    animal.set_command(new_command)
                    print("Команда успешно обновлена!")
                    break
            else:
                print("Животное не найдено")

        elif choice == "5":
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")


# 15. Вызов функции для запуска программы реестра домашних животных
run_animal_registry()
