# Contributing Guide

Welcome!
Thank you for contributing to this project.
Follow the steps below to set up your environment and contribute correctly.

---

## 1. Clone the Repository

```bash
git clone <REPO-LINK>
cd <PROJECT-FOLDER>
```

---

## 2. Create Your Virtual Environment

```bash
python3 -m venv myenv
```

---

## 3. Activate the Environment

### macOS / Linux:

```bash
source myenv/bin/activate
```

### Windows:

```bash
myenv\Scripts\activate
```

You should see:

```
(myenv)
```

---

## 4. Install Dependencies

### macOS Users (XGBoost Requirement)

If you are on macOS, you need to install `libomp` for XGBoost to work:

```bash
brew install libomp
```

### Install Python Packages

```bash
pip install -r requirements.txt
```

---

## 5. Running the Project

### Backend (FastAPI)

Open **Terminal 1**:

```bash
source myenv/bin/activate
uvicorn api:app --reload
```

Runs at:

```
http://127.0.0.1:8000
```

### Frontend (Streamlit)

Open **Terminal 2**:

```bash
source myenv/bin/activate
streamlit run app.py
```

Runs at:

```
http://localhost:8501
```

> Make sure the backend is running before Streamlit.

---

## 6. Working on a New Feature

1. Pull latest updates:

```bash
git pull
```

2. Create a new branch:

```bash
git checkout -b feature/<feature-name>
```

3. Make changes.
4. Commit:

```bash
git add .
git commit -m "Add <feature-name>"
```

5. Push:

```bash
git push -u origin feature/<feature-name>
```

6. Open a Pull Request.

---

## 7. Adding New Libraries

```bash
pip install <package>
pip freeze > requirements.txt
```

Commit the updated file.

---

## 8. Do NOT Commit

- `myenv/`
- `__pycache__/`
- `.env`
- `.DS_Store`
- Large model files

---

## Thank You

Your contributions help improve this project!
