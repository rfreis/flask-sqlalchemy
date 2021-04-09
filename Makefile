load-db:
	docker-compose exec flask flask db init 
	docker-compose exec flask flask db migrate 
	docker-compose exec flask flask db upgrade 

local-bash:
	docker-compose exec flask /bin/bash

logs:
	docker-compose logs --follow flask&
	docker-compose logs --follow flask-worker

start-local:
	docker-compose up -d

stop:
	docker-compose stop flask
	docker-compose stop flask-worker
	docker-compose stop db
	docker-compose stop redis
