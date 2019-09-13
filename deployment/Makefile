PROJECT_ID := project

SHELL := /bin/bash

# ----------------------------------------------------------------------------
#    P R O D U C T I O N     C O M M A N D S
# ----------------------------------------------------------------------------
default: web
run: build web migrate collectstatic

deploy: build web migrate collectstatic
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Bringing up fresh instance "
	@echo "You can access it on http://localhost:5000"
	@echo "------------------------------------------------------------------"

build:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) build uwsgi

web:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) up -d web
	@# Dont confuse this with the dbbackup make command below
	@# This one runs the postgis-backup cron container
	@# We add --no-recreate so that it does not destroy & recreate the db container
	@docker-compose -p $(PROJECT_ID) up --no-recreate --no-deps -d dbbackups

db:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running db in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) up -d db

nginx:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running nginx in production mode"
	@echo "Normally you should use this only for testing"
	@echo "In a production environment you will typically use nginx running"
	@echo "on the host rather if you have a multi-site host."
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) up -d nginx
	@echo "Site should now be available at http://localhost"

migrate:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running migrate static in production mode"
	@echo "------------------------------------------------------------------"
	@#http://stackoverflow.com/questions/29689365/auth-user-error-with-django-1-8-and-syncdb-migrate
	@#and
	@#http://stackoverflow.com/questions/3143635/how-to-ignore-mv-error
	@# We add the '-' prefix to the next line as the migration may fail
	@# but we want to continue anyway.
	@#We need to migrate accounts first as it has a reference to user model
	-@docker-compose -p $(PROJECT_ID) run uwsgi python manage.py migrate auth
	@docker-compose -p $(PROJECT_ID) run uwsgi python manage.py migrate

update-migrations:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running update migrations in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) run uwsgi python manage.py makemigrations

collectstatic:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Collecting static in production mode"
	@echo "------------------------------------------------------------------"
	#@docker-compose -p $(PROJECT_ID) run uwsgi python manage.py collectstatic --noinput
	#We need to run collect static in the same context as the running
	# uwsgi container it seems so I use docker exec here
	@docker exec -t -i $(PROJECT_ID)-uwsgi python manage.py collectstatic --noinput

reload:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Reload django project in production mode"
	@echo "------------------------------------------------------------------"
	@docker exec -t -i $(PROJECT_ID)-uwsgi uwsgi --reload  /tmp/django.pid

kill:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Killing in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) kill

rm: dbbackup rm-only


rm-only: kill
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Removing production instance!!! "
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) rm

shell:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Shelling in in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) run --rm uwsgi /bin/bash

runtests:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Run tests in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) run --rm uwsgi python manage.py test; exit $?

superuser:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Creating a superuser in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) run uwsgi python manage.py createsuperuser

dbbash:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Bashing in to production database"
	@echo "------------------------------------------------------------------"
	@docker exec -t -i $(PROJECT_ID)-db /bin/bash

dbshell:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Shelling in in production database"
	@echo "------------------------------------------------------------------"
	@docker exec -t -i $(PROJECT_ID)-db psql -U docker -h localhost gis

dbrestore:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Restore dump from backups/latest.dmp in production mode"
	@echo "------------------------------------------------------------------"
	@# - prefix causes command to continue even if it fails
	-@docker exec -t -i $(PROJECT_ID)-db su - postgres -c "dropdb gis"
	@docker exec -t -i $(PROJECT_ID)-db su - postgres -c "createdb -O docker -T template_postgis gis"
	@docker exec -t -i $(PROJECT_ID)-db pg_restore /backups/latest.dmp | docker exec -i $(PROJECT_ID)-db su - postgres -c "psql gis"

dbbackup:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Create `date +%d-%B-%Y`.dmp in production mode"
	@echo "Warning: backups/latest.dmp will be replaced with a symlink to "
	@echo "the new backup."
	@echo "------------------------------------------------------------------"
	@# - prefix causes command to continue even if it fails
	@# Explicitly don't use -t so we can call this make target over a remote ssh session
	@docker exec -i $(PROJECT_ID)-db-backups /backups.sh
	@docker exec -i $(PROJECT_ID)-db-backups cat /var/log/cron.log | tail -2 | head -1 | awk '{print $4}'
	-@if [ -f "backups/latest.dmp" ]; then rm backups/latest.dmp; fi
	# backups is intentionally missing from front of first clause below otherwise symlink comes
	# out with wrong path...
	@ln -s `date +%Y`/`date +%B`/PG_$(PROJECT_ID)_gis.`date +%d-%B-%Y`.dmp backups/latest.dmp
	@echo "Backup should be at: backups/`date +%Y`/`date +%B`/PG_$(PROJECT_ID)_gis.`date +%d-%B-%Y`.dmp"

# ----------------------------------------------------------------------------
#    DEVELOPMENT C O M M A N D S
# --no-deps will attach to prod deps if running
# after running you will have ssh and web ports open (see dockerfile for no's)
# and you can set your pycharm to use the python in the container
# Note that pycharm will copy in resources to the /root/ user folder
# for pydevd etc. If they dont get copied, restart pycharm...
# ----------------------------------------------------------------------------

devweb: db
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running in DEVELOPMENT mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) up --no-deps -d devweb

build-devweb: db
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building devweb"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) build devweb