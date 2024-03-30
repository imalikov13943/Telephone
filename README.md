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


### Главная функция

<img width="312" alt="8" src="https://github.com/imalikov13943/Telephone/assets/102352450/a68b2f44-5980-419f-9f97-4053735e3087">

Устанавливает путь к файлу **contacts.json**, который используется для хранения контактов.

Выводит на экран меню с доступными опциями: просмотр контактов, добавление нового контакта, удаление контакта, поиск контактов, обновление контакта и выход из программы. Ждет, пока пользователь введет цифру, соответствующую выбранной опции (например, "1" для просмотра контактов).

Возвращает введенный пользователем выбор в переменную **choice** в виде строки.

#### Выбор цифры

<img width="326" alt="9" src="https://github.com/imalikov13943/Telephone/assets/102352450/a2c11fe3-57cb-47fb-85cc-d3946106a4d5">

*if choice == "1"*: - Если пользователь выбирает пункт "1", программа проверяет, есть ли контакты в справочнике. Если справочник пуст, выводится сообщение "Список контактов пуст.". В противном случае выводятся все контакты из справочника.

<img width="348" alt="10" src="https://github.com/imalikov13943/Telephone/assets/102352450/b9b7dc83-59df-4133-88ac-03f2609f519c">

*elif choice == "2"*: - Если выбран пункт "2", программа запрашивает у пользователя имя, номер телефона и адрес электронной почты нового контакта, создает новый объект **Contact** с этими данными и добавляет его в справочник с помощью метода **add_contact**.

<img width="492" alt="11" src="https://github.com/imalikov13943/Telephone/assets/102352450/9b4d280c-a38b-43f9-b289-e0d983bea319">

*elif choice == "3"*: - При выборе пункта "3" программа проверяет, есть ли контакты в справочнике. Если справочник пуст, выводится сообщение "Список контактов пуст.". В противном случае пользователю предлагается ввести имя контакта для удаления. После этого программа находит все контакты с указанным именем, выводит их на экран с нумерацией и запрашивает у пользователя номер контакта для удаления, то есть если у вас в контактах несколько одинаковых имен, то вы пишите номер ряда контакта, какой он по списку. Выбранный контакт удаляется из справочника.

<img width="408" alt="12" src="https://github.com/imalikov13943/Telephone/assets/102352450/8d746557-ebbe-421a-bc39-5bf1e9a5711d">

*elif choice == "4"*: - При выборе пункта "4" программа аналогично предыдущему пункту проверяет наличие контактов в справочнике. Если справочник пуст, выводится сообщение "Список контактов пуст.". В противном случае пользователю предлагается ввести имя контакта для поиска. Программа находит все контакты с указанным именем и выводит их на экран.

<img width="468" alt="13" src="https://github.com/imalikov13943/Telephone/assets/102352450/6e7e0944-8849-4a53-910b-22b81faf0ea4">

*elif choice == "5"*: - Если выбран пункт "5", программа снова проверяет наличие контактов в справочнике. Если справочник пуст, выводится сообщение "Список контактов пуст.". В противном случае пользователю предлагается ввести имя контакта для обновления. Программа находит все контакты с указанным именем, выводит их на экран с нумерацией и запрашивает у пользователя номер контакта для обновления. После этого пользователь вводит новые данные (имя, номер телефона, адрес электронной почты) для обновления контакта, который затем сохраняется в справочнике.

<img width="321" alt="14" src="https://github.com/imalikov13943/Telephone/assets/102352450/29bcfba0-ac2d-4379-ba24-3f546b5d4258">

*elif choice == "6"*: - Если выбран пункт "6", программа завершает свою работу, выходя из цикла while. **else:** - Если введен некорректный выбор (не "1", "2", "3", "4", "5" или "6"), программа выводит сообщение "Неверный выбор. Повторите снова.".

<img width="173" alt="15" src="https://github.com/imalikov13943/Telephone/assets/102352450/b3dd4840-b7eb-473c-af76-e55e2575bf3c">

Когда файл запускается напрямую, переменная __name__ получает значение "__main__", что позволяет выполнить определенные действия только в этом случае.
