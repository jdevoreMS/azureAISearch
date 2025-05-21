**User Guide: Azure AI Search (Document Analyzer)
**This guide will walk you through the setup and usage of your application, assuming you already have your Azure AI Endpoint and API Key from the Foundry.

**1. Installation & Setup
**Step 1: Clone the Repository
If you haven't already downloaded the project, clone it from GitHub:
git clone git@github.com:jdevoreMS/azureAISearch.git
cd azureAISearch


**Step 2: Set Up a Virtual Environment
**To ensure dependencies are managed properly:
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows


**Step 3: Install Dependencies
**Run the following to install the required Python packages:
pip install -r requirements.txt


**Step 4: Configure Environment Variables
**Create a .env file in the project root and add your Azure AI credentials:
AZURE_ENDPOINT=https://your-foundry-url.eastus.models.ai.azure.com
AZURE_API_KEY=your-api-key-here
FLASK_SECRET_KEY=your-random-secret-key



2. Running the Application
Start the Flask Server
Run the app:
python app.py


Once started, Flask will display:
Running on http://127.0.0.1:5000/


Open this URL in your browser.

3. Using the Web Interface
Step 1: Upload a File
- Supported file types: PDF, TXT, DOCX, PNG, JPG, JPEG
- Click "Choose File" and select your document.
Step 2: Enter Your Query
- Type in a question or request related to the document.
- Example: "Summarize the main points of this document"
Step 3: Adjust Response Length
- The AI can generate responses from 50 to 10,000 tokens (word chunks).
- Default: 100 tokens
Step 4: Get Your AI-Generated Answer
- Click Submit.
- The extracted text from the file will be displayed.
- The AI-generated response will appear below.

4. Troubleshooting
Issue: Flask App Won't Start
✔️ Check if the virtual environment is active.
✔️ Ensure your .env file is properly configured.
✔️ Run pip install -r requirements.txt to confirm dependencies are installed.
Issue: AI Response Isn't Working
✔️ Double-check your Azure API credentials in .env.
✔️ Ensure you are not exceeding token limits.
✔️ Run git pull origin main to update your app.
Issue: File Upload Errors
✔️ Confirm the file type is supported.
✔️ Refresh the page and try uploading again.
✔️ Check the console for errors (Ctrl + Shift + I in Chrome).

5. Deployment (Optional)
If you wish to deploy your Flask app:
- Use Gunicorn for production (pip install gunicorn)
- Host it on Azure App Services or Heroku
- Set DEBUG=False in your Flask settings before deploying

6. Contributing & Updates
To update the application, pull the latest changes:
git pull origin main


Want to improve the project? Fork the repo and submit a pull request!
