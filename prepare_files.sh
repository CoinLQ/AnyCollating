eval $(docker-machine env default)
docker-compose down
docker-compose build
docker-compose up -d
docker cp web/conf/db.sqlite3 anycollating_web_1:/usr/src/app/conf/.
echo yes | docker-compose exec web /usr/local/bin/python manage.py collectstatic
