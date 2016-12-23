## Django 开发环境 With Docker Compose and Machine

### 准备

安装[Docker](https://www.docker.com/products/docker)及[Docker Toolkit](https://www.docker.com/products/docker-toolbox)

Docker及Python版本:
- Docker v1.12.3
- Docker Compose v1.8.1
- Docker Machine v0.8.2
- Python 2.7

### OS X Instructions

1. Start new machine - `docker-machine create --engine-registry-mirror=https://mhpya9ls.mirror.aliyuncs.com -d virtualbox default`
1. Select machine - `eval $(docker-machine env default)`
1. Build images - `docker-compose build`
1. Start services - `docker-compose up -d`
1. Create migrations - `docker-compose run web /usr/local/bin/python manage.py migrate`
1. Grab IP - `docker-machine ip default` - and view in your browser
