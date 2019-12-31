# Run project

1. Clone this repo

Create a new folder with project name, cd into it, and then run:

```
git init
git pull https://github.com/kryvokhyzha/basic-flask-app.git
```

2. Add your favorite Python modules to requirements.txt. For example:

```
statsmodels
torch==1.3
```

3. Change image name in docker-compose file:
```
...
    image: docker_user/app_name:tag
...
```

4. Run containers:

```
docker-compose up
```
or
```
docker-compose up --build
```