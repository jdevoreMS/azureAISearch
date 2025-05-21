import os
import fitz  # PyMuPDF for PDFs
import pytesseract  # OCR for images and scanned PDFs
from PIL import Image
from docx import Document  # For DOCX files
from flask import Flask, render_template, request, flash, redirect
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve credentials
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

# Ensure credentials are available
if not AZURE_ENDPOINT or not AZURE_API_KEY:
    raise ValueError("Azure credentials not set. Check your .env file.")

# Initialize Azure client
client = ChatCompletionsClient(
    endpoint=AZURE_ENDPOINT,
    credential=AzureKeyCredential(AZURE_API_KEY)
)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

# --- Text Extraction Functions ---
def extract_text_from_pdf(uploaded_file):
    uploaded_file.seek(0)
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    extracted_text = []

    for page in doc:
        text = page.get_text("text")
        if text.strip():
            extracted_text.append(text)
        else:
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            extracted_text.append(pytesseract.image_to_string(img))

    return "\n".join(extracted_text)

def extract_text_from_txt(uploaded_file):
    uploaded_file.seek(0)
    return uploaded_file.read().decode("utf-8", errors="ignore")

def extract_text_from_image(uploaded_file):
    uploaded_file.seek(0)
    image = Image.open(uploaded_file)
    return pytesseract.image_to_string(image)

def extract_text_from_docx(uploaded_file):
    uploaded_file.seek(0)
    document = Document(uploaded_file)
    return "\n".join([para.text for para in document.paragraphs])

def extract_text(uploaded_file):
    extension = uploaded_file.filename.split('.')[-1].lower()
    if extension == 'pdf':
        return extract_text_from_pdf(uploaded_file)
    elif extension == 'txt':
        return extract_text_from_txt(uploaded_file)
    elif extension in ['png', 'jpg', 'jpeg']:
        return extract_text_from_image(uploaded_file)
    elif extension == 'docx':
        return extract_text_from_docx(uploaded_file)
    else:
        return "Unsupported file type."

# --- Flask Routes ---
@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = ""
    ai_response = ""

    if request.method == "POST":
        file = request.files.get("uploaded_file")
        user_query = request.form.get("user_query", "")
        max_tokens = request.form.get("max_tokens", 100)

        try:
            max_tokens = int(max_tokens)
        except ValueError:
            max_tokens = 100

        if file:
            extracted_text = extract_text(file)

        if extracted_text and user_query:
            messages = [
                {"role": "system", "content": "Analyze and answer based on the uploaded document."},
                {"role": "user", "content": f"Document:\n{extracted_text}\n\nQuery: {user_query}"}
            ]
            try:
                response = client.complete(model="deepseek-r1", messages=messages, max_tokens=max_tokens)
                ai_response = response.choices[0].message["content"]
            except Exception as e:
                ai_response = f"Error: {str(e)}"
        else:
            flash("Upload a file and enter a query.")

    return render_template("index.html", extracted_text=extracted_text, ai_response=ai_response)

if __name__ == "__main__":
    app.run(debug=True)
