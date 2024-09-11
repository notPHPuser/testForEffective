Данный проект демонстрирует автоматическое тестирование работы с GitHub API. Скрипт создает, проверяет наличие и удаляет репозиторий на GitHub.

1. Убедитесь, что Вы установили python
2. Клонируйте репозиторий
bash:
git clone https://github.com/notPHPuser/testForEffective
cd testForEffective
cd testWork
cd test2
3. Установите зависимость:
bash:
pip install -r requirements.txt
4. Настройте переменные окружения:
Создайте файл '.env' в корневом каталоге проекта и укажите свои данные:
GITHUB_NAME = your_username
GITHUB_TOKEN = your_token
GITHUB_REP = your_test_repo
5. Замените your_username и your_token на имя пользователя Github и на Ваш токен API
6. Запустите тест:
bash:
python test_api.py