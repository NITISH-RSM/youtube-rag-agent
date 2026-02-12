# 🎬 YouTube RAG Agent

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

> A powerful Retrieval-Augmented Generation (RAG) agent for intelligent extraction and analysis of YouTube video content.

---

## 📑 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

✅ **YouTube Video Processing** - Extract and process content from YouTube videos  
✅ **RAG Pipeline** - Retrieval-Augmented Generation for intelligent, context-aware responses  
✅ **Vector Store** - Efficient storage and retrieval of embeddings for semantic search  
✅ **Web Interface** - Clean, intuitive frontend for easy interaction  
✅ **Modular Architecture** - Well-organized, scalable codebase  

---

## 📁 Project Structure

```
youtube-rag-agent/
├── 📂 backend/
│   ├── main.py                    # Main backend application
│   └── 📂 src/
│       ├── ingest.py              # YouTube video ingestion module
│       ├── rag.py                 # RAG pipeline implementation
│       └── vector_store.py        # Vector store management
├── 📂 frontend/
│   └── app.py                     # Frontend web application
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore rules
└── README.md                      # Documentation
```

---

## 📋 Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Git

---

## 🛠️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/NITISH-RSM/youtube-rag-agent.git
cd youtube-rag-agent
```

### Step 2: Create Virtual Environment

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Quick Start

1. **Start the Backend**
   ```bash
   cd backend
   python main.py
   ```

2. **Start the Frontend** (in a new terminal)
   ```bash
   cd frontend
   python app.py
   ```

3. **Open in Browser**
   Navigate to `http://localhost:5000` (or specified port)

---

## 📖 Usage

### Backend API

The backend provides core RAG functionality:

```python
# Main entry point - backend/main.py
python main.py
```

### Frontend Application

Access the user-friendly web interface:

```python
# Frontend - frontend/app.py
python app.py
```

### Module Overview

| Module | Purpose |
|--------|---------|
| `ingest.py` | Handles YouTube video data ingestion |
| `rag.py` | Implements RAG pipeline logic |
| `vector_store.py` | Manages vector embeddings storage |

---

## 🏗️ Architecture

```
User Interface (Frontend)
        ↓
    Web Server
        ↓
  API Endpoints (Backend)
        ↓
   RAG Pipeline
        ↓
  Vector Store
        ↓
  YouTube Content
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 👤 Author

**NITISH-RSM**

- GitHub: [@NITISH-RSM](https://github.com/NITISH-RSM)
- Repository: [youtube-rag-agent](https://github.com/NITISH-RSM/youtube-rag-agent)

---

<div align="center">

**[⬆ back to top](#-youtube-rag-agent)**

</div>
