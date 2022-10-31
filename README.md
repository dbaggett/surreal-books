# Surreal Books API
Provides a REST API for book content generation using the [Transformers](https://huggingface.co/docs/transformers) library from [HuggingFace](https://huggingface.co/).

WIP. Stay Tuned...

## Installation
---
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the API
---
```
flask run
```

A default book is available at `localhost:5000/books/test` for now. Subject to change in future iterations.

## Running API Tests
---
```
pytest
```