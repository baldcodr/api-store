build:
	docker compose up --build

run:
	docker run -d \
	--name api-store \
	-p 8000:8082 \
	-v cred:/code/cred/ \
	api-store-image:latest

dev:
	fastapi dev api/main.py

deploy:
	fastapi run

test:
	pytest .