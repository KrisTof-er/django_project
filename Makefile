.PHONY: d-run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up --build

.PHONY: d-run-i-db
d-run-i-db:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up --build postgres

.PHONY: d-run-i-extended
d-run-i-extended:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down --timeout 0 && \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up --build --detach && \
	make d-logs-follow

.PHONY: d-logs-follow
d-logs-follow:
	@docker-compose logs --follow

.PHONY: d-stop
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down

.PHONY: d-purge
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down --volumes --remove-orphans --rmi local --timeout 0

.PHONY: migrate
migrate:
	@python manage.py migrate

.PHONY: migrations
migrations:
	@python manage.py makemigrations

.PHONY: init-configs-i-dev
init-configs-i-dev:
	@cp docker-compose.override.dev.yml docker-compose.override.yml && \
	cp .env.dev .env


.PHONY: d-homework-i-run
d-homework-i-run:
	@make init-configs-i-dev && \
	make d-run

.PHONY: d-homework-i-purge
d-homework-i-purge:
	@make d-purge
