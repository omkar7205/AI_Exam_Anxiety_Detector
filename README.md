Here is the **complete step-by-step guide to run your AI Exam Anxiety Detector project in VS Code**. Follow these steps in order.

---

# 1️⃣ Open the Project in VS Code

Open the folder:

```
AI_Exam_Anxiety_Detector
```

Your project structure should look like this:

```
AI_Exam_Anxiety_Detector
│
├── api
│   └── server.py
│
├── app
│   ├── model_loader.py
│   └── __init__.py
│
├── frontend
│   └── streamlit_app.py
│
├── bert_anxiety_model
│
├── train_model.py
├── requirements.txt
```

---

# 2️⃣ Open the VS Code Terminal

Click:

```
Terminal → New Terminal
```

Make sure you are inside the project folder:

```
D:\AI_Exam_Anxiety_Detector
```

---

# 3️⃣ Activate the Virtual Environment

Run:

```bash
anxiety_env\Scripts\activate
```

You should see:

```
(anxiety_env)
```

in the terminal.

---

# 4️⃣ Install Project Requirements

Run:

```bash
pip install -r requirements.txt
```

If pip causes errors, use:

```bash
python -m pip install -r requirements.txt
```

---

# 5️⃣ Run the FastAPI Backend

Start the API server:

```bash
uvicorn api.server:app --reload
```

If everything is correct you will see:

```
Uvicorn running on http://127.0.0.1:8000
```

---

# 6️⃣ Test the API

Open this in your browser:

```
http://127.0.0.1:8000/docs
```

You will see the **FastAPI testing interface**.

Test it with:

```
POST → /predict
```

Example input:

```json
{
"text": "I feel very nervous about my exams tomorrow"
}
```

Example output:

```json
{
"prediction": "Anxiety Detected",
"confidence": 87.4
}
```

If this works → **your AI model is working**.

---

# 7️⃣ Open a New Terminal for the Frontend

In VS Code click:

```
Terminal → New Terminal
```

Activate the environment again:

```bash
anxiety_env\Scripts\activate
```

---

# 8️⃣ Run the Streamlit Interface

Run:

```bash
python -m streamlit run frontend/streamlit_app.py
```

You will see something like:

```
Local URL: http://localhost:8501
```

---

# 9️⃣ Open the Web Interface

Open this in your browser:

```
http://localhost:8501
```

Now you will see your **AI Exam Anxiety Detector UI**.

---

# 🔟 Test the System

Example input:

```
I am very stressed and worried about failing my exams
```

Example output:

```
⚠ Anxiety Detected
Confidence: 90%
```

---

# 🎉 Your Full System Is Now Running

System architecture:

```
Streamlit (Frontend UI)
        ↓
FastAPI (Backend API)
        ↓
BERT Model (AI Prediction)
```

---

# ⚠ Important Rules

Always run **backend first**, then **frontend**.

```
1️⃣ uvicorn api.server:app --reload
2️⃣ python -m streamlit run frontend/streamlit_app.py
```

---

✅ If you want, I can also give you:

* **Better Streamlit UI (looks like ChatGPT)**
* **Anxiety level detection (Low / Medium / High)**
* **Student history dashboard**
* **Graphs and analytics**
* **Final Year Project Report (40 pages)**
* **Project PPT for viva**

Just tell me and I will provide it.
