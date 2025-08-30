.RECIPEPREFIX := >
.PHONY: setup dev test

setup:
>python -m venv .venv
>. .venv/bin/activate && pip install -r requirements.txt

dev:
>. .venv/bin/activate && uvicorn apps.backend.main:app --reload

test:
>. .venv/bin/activate && pytest
