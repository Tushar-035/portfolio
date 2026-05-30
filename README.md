# My Academic Website — Flask App

## Folder Structure
```
portfolio/
├── app.py                  ← main file, edit your info here
├── requirements.txt        ← Python dependencies
├── templates/
│   └── index.html          ← HTML layout (Jinja2 template)
└── static/
    └── css/
        └── style.css       ← all the styling
```

## How to Run Locally

### Step 1 — Install Python
Make sure Python is installed. Open terminal and type:
```
python --version
```
If not installed, download from https://python.org

### Step 2 — Install Flask
In terminal, navigate to this folder:
```
cd portfolio
pip install -r requirements.txt
```

### Step 3 — Run the website
```
python app.py
```
Open your browser and go to:  http://127.0.0.1:5000

### Step 4 — Edit your details
Open `app.py` in any text editor (VS Code recommended).
Edit the ME, RESEARCH, PUBLICATIONS, BLOG_POSTS sections at the top.
Save the file — the website auto-refreshes.

---

## How to Deploy Online for Free (Render.com)

1. Push this folder to a GitHub repository
2. Go to https://render.com and sign up free
3. Click "New Web Service" → connect your GitHub repo
4. Set:  
   - Build command: `pip install -r requirements.txt`  
   - Start command: `gunicorn app:app`
5. Add `gunicorn` to requirements.txt
6. Click Deploy → your site will be live at a free URL!
