User Guide: Azure AI Search (Document Analyzer)
This guide will walk you through the setup and usage of your application, assuming you already have your Azure AI Endpoint and API Key from the Foundry.

**1. Installation & Setup**

Step 1: Clone the Repository<br>
If you haven't already downloaded the project, clone it from GitHub:<br>
git clone git@github.com:jdevoreMS/azureAISearch.git<br>
cd azureAISearch<br>


Step 2: Set Up a Virtual Environment<br>
To ensure dependencies are managed properly:<br>
python -m venv venv<br>
source venv/bin/activate  # On macOS/Linux<br>
venv\Scripts\activate     # On Windows<br>


Step 3: Install Dependencies<br>
Run the following to install the required Python packages:<br>
pip install -r requirements.txt<br>


Step 4: Configure Environment Variables<br>
Create a .env file in the project root and add your Azure AI credentials:<br>
AZURE_ENDPOINT=https://your-foundry-url.eastus.models.ai.azure.com<br>
AZURE_API_KEY=your-api-key-here<br>
FLASK_SECRET_KEY=your-random-secret-key<br><br>

**2. Running the Application**

Step 1: Start the Flask Server<br>
Run the app by using the command: python app.py<br>

Once started, Flask will display:<br>
Running on http://127.0.0.1:5000/<br>

Open this URL in your browser.<br><br>

**3. Using the Web Interface**<br>

Step 1: Upload a File<br>
- Supported file types: PDF, TXT, DOCX, PNG, JPG, JPEG<br>
- Click "Choose File" and select your document.<br>
  
Step 2: Enter Your Query<br>
- Type in a question or request related to the document.<br>
- Example: "Summarize the main points of this document"<br>
  
Step 3: Adjust Response Length<br>
- The AI can generate responses from 50 to 10,000 tokens (word chunks).<br>
- Default: 100 tokens<br>
  
Step 4: Get Your AI-Generated Answer<br>
- Click Submit.<br>
- The extracted text from the file will be displayed.<br>
- The AI-generated response will appear below.<br><br>

**4. Troubleshooting**
Issue: Flask App Won't Start<br>
- Check if the virtual environment is active.<br>
- Ensure your .env file is properly configured.<br>
- Run pip install -r requirements.txt to confirm dependencies are installed.<br><br>

Issue: AI Response Isn't Working<br>
-  Double-check your Azure API credentials in .env.<br>
- Ensure you are not exceeding token limits.<br>
- Run git pull origin main to update your app.<br><br>
  
Issue: File Upload Errors<br>
- Confirm the file type is supported.<br>
- Refresh the page and try uploading again.<br>
- Check the console for errors (Ctrl + Shift + I in Chrome).<br><br>

**5. Deployment (Optional)**
If you wish to deploy your Flask app:<br>
- Use Gunicorn for production (pip install gunicorn)<br>
- Host it on Azure App Services or Heroku<br>
- Set DEBUG=False in your Flask settings before deploying<br>

**Contributing & Updates**<br>
To update the application, pull the latest changes:<br>
git pull origin main<br><br>


Want to improve the project? Fork the repo and submit a pull request!
