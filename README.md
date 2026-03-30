**Copilot TestRail Refactor & Priority Assistant**

Пайплайн для TestRail:
1. бере кейси з секції,
2. нормалізує/рефакторить текст,
3. перевіряє пріоритети за Jira story + acceptance criteria,
4. створює оновлені кейси,
5. пише звіти в `output/`.

Головний файл запуску: `Copilot-AI-TestRail.py`.

Що потрібно:
1. Встановлений `Python 3.12+`
2. Встановлені пакети:
   - `aiohttp`
   - `python-dotenv`
   - `pydantic`
   - `tenacity`
3. Заповнений файл `.env` ()
4. Доступи:
   - валідний доступ до TestRail API 
   - валідний доступ до Jira API 
   - валідний доступ до GitHub Models API / Copilot Models


Кроки для локального розгортання проєкту:   

1. **Встановіть Python 3.12+**  
   Перевірте у терміналі:
   ```
   python3 --version
   ```

2. **Клонувати репозиторій**
   ```
   git clone <URL_вашого_репозиторію>
   cd <назва_папки>
   ```

3. **Створіть та активуйте віртуальне середовище**
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Встановіть залежності вручну**  
   ```
   pip install aiohttp python-dotenv pydantic tenacity
   ```

5. **Створіть `.env`:**
   ```
   cp .env.example .env
   ```

6. **Заповніть .env**
   ```
   TESTRAIL_URL=
   TESTRAIL_EMAIL=
   TESTRAIL_API_KEY=
   TESTRAIL_SECTION_ID=

   LLM_BACKEND=github_models
   GITHUB_MODELS_TOKEN=
   GITHUB_MODELS_MODEL=openai/gpt-4.1

   JIRA_BASE_URL=
   JIRA_USER_EMAIL=
   JIRA_API_TOKEN=
   ```

7. **Запустіть скрипт**
   ```
   python3 Copilot-AI-TestRail.py
   ```   
