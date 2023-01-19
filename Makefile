run: start

clean:
	#rm -vf db.sqlite
	find . -name "__pycache__" -type d | xargs rm -rvf {} \;

start:
	uvicorn main:app --reload

populate:
	sh ./populate_db.sh

build:
	docker build . -t workouts:${version};

push:
	docker tag workouts:${version} registry.digitalocean.com/dmtmov/workouts:${version}
	docker push registry.digitalocean.com/dmtmov/workouts:${version}
