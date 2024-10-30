# parse-epravda-news
Парсинг новинного сайту "Економічна правда" та збереження даних до csv файлу

## Опис проєкту

Цей Python-скрипт розроблений для парсингу головної сторінки розділу новин сайту *Економічна правда*, щоб зібрати інформацію про новини за поточний день. Скрипт отримує заголовки новин, посилання на повний текст, дату публікації та короткий опис. Зібрані дані зберігаються у CSV-файлі для подальшого використання або аналізу.

## Технічні вимоги

1. **Бібліотеки**:
   - `requests` для завантаження HTML-коду сторінки.
   - `BeautifulSoup` з пакету `bs4` для парсингу HTML.

2. **Цільова сторінка**:
   - Сайт [Економічна правда](https://www.epravda.com.ua/rus/archives/date), з можливістю вибору новин за поточний день.
   - Для завантаження поточної дати новин використовується URL, динамічно сформований на основі поточного дня, місяця та року.

3. **Інформація для збору**:
   - **Заголовок новини**.
   - **Посилання** на повний текст новини.
   - **Дата публікації**.
   - **Короткий опис** або анотація новини.

## Структура скрипту

Скрипт складається з основних функцій для завантаження та обробки даних:

1. **`get_url(url)`**:
   - Завантажує HTML-код сторінки за вказаним URL та повертає `BeautifulSoup`-об'єкт.
  
2. **`parse_news(soup)`**:
   - Отримує `soup`-об'єкт сторінки, витягує всі новини у вигляді списку словників з ключами `title`, `link`, `date`, `summary`.

3. **`save_to_csv(data)`**:
   - Приймає список новин та зберігає його у CSV-файлі з назвою `news.csv`.

## Запуск скрипту

1. Встановіть залежності:
   ```bash
   -r requirements.txt
2. Запустити скрипт.
