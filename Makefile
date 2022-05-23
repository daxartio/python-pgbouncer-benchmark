.DEFAULT_GOAL := all

STATS_OUTPUT_FILE = stats.csv
CODE = app

.PHONY: all
all: up test down

.PHONY: format
format:
	docker-compose run --rm dev black $(CODE)
	docker-compose run --rm dev isort $(CODE)

.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.PHONY: test
test:
	docker-compose run --rm test -h http://flask-1w-1t:80/test -t 12 -c 60 -d 5s --pct
	docker-compose run --rm test -h http://fastapi-1w-1t:80/test-sync -t 12 -c 60 -d 5s --pct
	docker-compose run --rm test -h http://fastapi-async-1w-1t:80/test-async -t 12 -c 60 -d 5s --pct
	docker-compose run --rm test -h http://flask-2w-40t:80/test -t 12 -c 60 -d 5s --pct
	docker-compose run --rm test -h http://fastapi-2w-1t:80/test-sync -t 12 -c 60 -d 5s --pct
	docker-compose run --rm test -h http://fastapi-async-2w-1t:80/test-async -t 12 -c 60 -d 5s --pct

.PHONY: stats
stats:
	docker stats --format "{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"

.PHONY: stats-to-file
stats-to-file:
	while true; do date +"%T" >> $(STATS_OUTPUT_FILE); docker stats --no-stream --format "{{.Name}},{{.CPUPerc}},{{.MemUsage}}" >> $(STATS_OUTPUT_FILE); done

.PHONY: clean
clean:
	rm $(STATS_OUTPUT_FILE) || true
