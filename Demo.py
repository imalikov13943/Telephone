class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Имя: {self.name}, Телефон: {self.phone_number}, Email: {self.email}"

import json

class PhoneDirectory:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.file_path, 'r') as file:
                contacts_data = json.load(file)
                contacts = []
                for data in contacts_data:
                    if "Имя" in data and "Телефон" in data and "Email" in data:
                        contacts.append(Contact(name=data["Имя"], phone_number=data["Телефон"], email=data["Email"]))
                    else:
                        print("Ошибка загрузки контактов: некорректные данные.")
                return contacts
        except FileNotFoundError:
            return []


    def save_contacts(self):
        contacts_data = [{"name": str(contact.name), "phone_number": str(contact.phone_number), "email": str(contact.email)} for contact in self.contacts]
        with open(self.file_path, 'w') as file:
            json.dump(contacts_data, file, indent=4)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def delete_contact(self, contact):
        self.contacts.remove(contact)
        self.save_contacts()

    def search_contacts(self, keyword):
        return [contact for contact in self.contacts if keyword.lower() in contact.name.lower()]

    def update_contact(self, old_contact, new_contact):
        index = self.contacts.index(old_contact)
        self.contacts[index] = new_contact
        self.save_contacts()

def main():
    file_path = "contacts.json"
    phone_directory = PhoneDirectory(file_path)
    
    while True:
        print("\nТелефонный справочник")
        print("1. Посмотреть контакты")
        print("2. Добавить контакт")
        print("3. Удалить контакт")
        print("4. Найти контакты")
        print("5. Обновить контакт")
        print("6. Выход")
        
        choice = input("Напишите цифру: ")
        
        if choice == "1":
            if len(phone_directory.contacts) == 0:
                 print("Список контактов пуст.")
            else:
                for contact in phone_directory.contacts:
                    print(contact)
        elif choice == "2":
            name = input("Добавьте имя: ")
            phone_number = input("Добавьте номер контакта: ")
            email = input("Добавьте email: ")
            new_contact = Contact(name, phone_number, email)
            phone_directory.add_contact(new_contact)
        elif choice == "3":
            if len(phone_directory.contacts) == 0:
                 print("Список контактов пуст.")
            else:
                keyword = input("Добавьте имя для удаления: ")
                contacts_to_delete = phone_directory.search_contacts(keyword)
                if contacts_to_delete:
                    for i, contact in enumerate(contacts_to_delete):
                        print(f"{i + 1}. {contact}")
                    choice = input("Добавьте контакт для удаления: ")
                    if choice.isdigit():
                        choice = int(choice)
                        phone_directory.delete_contact(contacts_to_delete[choice - 1])
                    else:
                        print("Неверный ввод.")
                else:
                    print("Контакт не найден.")
        elif choice == "4":
            if len(phone_directory.contacts) == 0:
                 print("Список контактов пуст.")
            else:
                keyword = input("Добавьте имя для поиска: ")
                found_contacts = phone_directory.search_contacts(keyword)
                if found_contacts:
                    for contact in found_contacts:
                        print(contact)
                else:
                    print("Контакт не найден.")
        elif choice == "5":
            if len(phone_directory.contacts) == 0:
                 print("Список контактов пуст.")
            else:
                keyword = input("Добавьте имя чтобы обновить: ")
                contacts_to_update = phone_directory.search_contacts(keyword)
                if contacts_to_update:
                    for i, contact in enumerate(contacts_to_update):
                        print(f"{i + 1}. {contact}")
                    choice = input("Добавьте номер контакта чтобы обновить: ")
                    if choice.isdigit():
                        choice = int(choice)
                        if 1 <= choice <= len(contacts_to_update):
                            old_contact = contacts_to_update[choice - 1]
                            name = input("Введите новое имя: ")
                            phone_number = input("Введите новый номер телефона: ")
                            email = input("Введите новый email: ")
                            new_contact = Contact(name, phone_number, email)
                            phone_directory.update_contact(old_contact, new_contact)
                        else:
                            print("Неверный ввод.")
                    else:
                        print("Неверный ввод.")
                else:
                    print("Контакт не найден.")
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Повторите снова.")

    print("Выход из Телефонного справочника")
    phone_directory.save_contacts()

if __name__ == "__main__":
    main()
