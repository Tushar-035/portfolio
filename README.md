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

# My Academic Portfolio Website
A personal academic website built with Python Flask.

## Setting Up on a New Laptop

### Step 1 — Install the basics
- Download and install **PyCharm** from jetbrains.com
- Download and install **Python** from python.org
- During Python install tick **"Add Python to PATH"**

### Step 2 — Clone the project from GitHub
Open terminal and type:
git clone https://github.com/Tushar-035/portfolio.git

### Step 3 — Install Flask
In PyCharm terminal type:
pip install flask

### Step 4 — Run the website
python app.py
Then open http://127.0.0.1:5000 in your browser.

## Updating the Website
Whenever you make any changes:
git add .
git commit -m "what you changed"
git push

## Project Structure
portfolio/
├── app.py                  ← main file, edit all your content here
├── requirements.txt        ← Python dependencies
├── templates/
│   ├── index.html          ← home page
│   ├── about.html          ← about page
│   ├── blog_post.html      ← blog post page
│   └── research.html       ← research page
└── static/
    ├── css/
    │   └── style.css       ← all styling
    ├── logos/              ← university logos
    ├── blog-images/        ← blog post photos
    ├── photo.JPG           ← your profile photo
    └── cv.pdf              ← your CV

## What to Edit
- New blog post → add to top of BLOG_POSTS in app.py
- New publication → add to PUBLICATIONS in app.py
- New research → add to RESEARCH in app.py
- Update group info → edit GROUPS in app.py
- Update personal info → edit ME in app.py
