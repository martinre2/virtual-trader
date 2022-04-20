IMAGE_NAME = virtual-trader

up:
	test -f .env | cp .env.dist .env
	docker-compose build && docker-compose up --detach

down:
	docker-compose down
