dev:
	uvicorn app.main:app --reload

prod:
	gunicorn -c gunicorn_conf.py app.main:app

lint:
	flake8 app

black:
	black ./app

docker-compose_up:
	docker-compose up --scale app=2

docker-compose_down:
	docker-compose docker-compose down -v
