# YouTube RAG Agent

A Retrieval-Augmented Generation (RAG) agent for extracting and analyzing information from YouTube videos.

## Project Structure

```
youtube-rag-agent/
├── backend/
│   ├── main.py              # Main backend application
│   └── src/
│       ├── ingest.py        # Data ingestion module
│       ├── rag.py           # RAG implementation
│       └── vector_store.py  # Vector store management
├── frontend/
│   └── app.py               # Frontend application
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Features

- **YouTube Video Processing**: Extract and process content from YouTube videos
- **RAG Pipeline**: Retrieval-Augmented Generation for intelligent responses
- **Vector Store**: Store and retrieve embeddings for semantic search
- **Web Interface**: User-friendly frontend for interaction

## Installation

1. Clone the repository:
```bash
git clone https://github.com/NITISH-RSM/youtube-rag-agent.git
cd youtube-rag-agent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Backend
```bash
cd backend
python main.py
```

### Running the Frontend
```bash
cd frontend
python app.py
```

## Dependencies

See `requirements.txt` for all required packages.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Author

NITISH-RSM
