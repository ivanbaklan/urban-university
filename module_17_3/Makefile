PROJECT_DIR ?= app

run:
	gunicorn -w 1 -b :8000 -k uvicorn.workers.UvicornWorker app.main:app --reload

lint:
	black .

isort:
	isort .

format: lint isort
	echo "Done"
