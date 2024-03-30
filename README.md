# Задание (Телефонный справочник)

# Телефонный справочник

Простое консольное приложение для управления контактами.

## Функционал

- Просмотр списка контактов
- Добавление нового контакта
- Удаление контакта
- Поиск контакта по имени
- Обновление информации о контакте

## Объяснение кода

### Класс Contact:

<img width="595" alt="1" src="https://github.com/imalikov13943/Telephone/assets/102352450/f4289609-78b3-43f4-9ee9-95a9f07f1ce5">

Этот код определяет **класс Contact**, который представляет собой контакт в телефонной книге.

### Класс PhoneDirectory:

<img width="728" alt="2" src="https://github.com/imalikov13943/Telephone/assets/102352450/f6cfcbaf-76c9-4d30-bb57-2b9fd6161603">

Этот код определяет **класс PhoneDirectory**, который представляет собой телефонную книгу с функционалом по загрузке, сохранению, добавлению, удалению, поиску и обновлению контактов.

Метод **load_contacts** загружает контакты из файла JSON. Если данные контакта содержат ключи "Имя", "Телефон" и "Email", то создается объект **Contact** и добавляется в список контактов contacts. Если данные некорректны, выводится сообщение об ошибке.

#### Функция save_contacts

<img width="923" alt="3" src="https://github.com/imalikov13943/Telephone/assets/102352450/ecb1f720-736f-4116-af76-541eaf403e8a">

Метод **save_contacts** сохраняет список контактов в файл JSON, предварительно преобразовав объекты **Contact** в словари. 

#### Функция add_contact

<img width="220" alt="4" src="https://github.com/imalikov13943/Telephone/assets/102352450/35a8c500-aa4c-4bf4-8329-c2b56ee425bd">

Метод **add_contact** добавляет контакт в файл JSON, предварительно преобразовав объекты **Contact** в словари.

#### Функция delete_contact

<img width="249" alt="5" src="https://github.com/imalikov13943/Telephone/assets/102352450/d0897550-f011-417a-850b-bba2cb4eaf17">

Метод **delete_contact** удаляет контакт из файла JSON, предварительно преобразовав объекты **Contact** в словари.

#### Функция search_contacts

<img width="577" alt="6" src="https://github.com/imalikov13943/Telephone/assets/102352450/33eb0cb3-791a-48b0-9c1c-1b9abfe80485">

Метод **search_contacts** ищет контакт в файле JSON, предварительно преобразовав объекты **Contact** в словари.

#### Функция update_contact

<img width="323" alt="7" src="https://github.com/imalikov13943/Telephone/assets/102352450/79a6a633-cff8-4e50-8ffd-486514b75797">

Метод **update_contact** обновляет контакт в файле JSON, предварительно преобразовав объекты **Contact** в словари.
