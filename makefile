install:
	pip install -r requierements.txt

run-local:
	uvicorn app.main:app --reload