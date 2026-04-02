## Copilot TestRail Refactor & Priority Assistant


TestRail Pipeline:
1. Fetches test cases from a section
2. Normalizes/refactors the text
3. Validates priorities based on Jira story + acceptance criteria
4. Creates updated test cases
5. Writes reports to the `output/` directory

Main entry file: `Copilot-AI-TestRail.py`.


Requirements:
1. Installed `Python 3.12+`
2. Installed packages:
   - `aiohttp`
   - `python-dotenv`
   - `pydantic`
   - `tenacity`
3. Configured `.env` file
4. Access:
   - valid TestRail API access
   - valid Jira API access
   - valid GitHub Models API / Copilot Models access


Steps to run the project locally:

1. **Install Python 3.12+**  
   Check in terminal:
   ```
   python3 --version
   ```

2. **Clone the repository**
   ```
   git clone <YOUR_REPOSITORY_URL>
   cd <PROJECT_FOLDER_NAME>
   ```

3. **Create and activate a virtual environment**
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies manually**  
   ```
   pip install aiohttp python-dotenv pydantic tenacity
   ```

5. **Create `.env` file:**
   ```
   cp .env.example .env
   ```

6. **Fill in `.env` file**
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

7. **Run the script**
   ```
   python3 Copilot-AI-TestRail.py
   ```   
