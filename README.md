# Recipes book

## Short description
Create recipes book using Django and Django REST Framework.

## Model class diagram
![model class diagram](images/class_diagram.jpg)

## Prerequisites
You must have [docker](https://docs.docker.com/get-docker/) installed on your machine.

## User requirements
- [x] User should at least have email, first name, and last name
- [x] Recipe should have a name, recipe text, and ingredients
- [x] Ingredient should have a name
- [x] Rating is number between 1 and 5
- [x] When listing recipes, return an average rating for each recipe.
- [x] Use hunter for verifying email existence on registration
- [x] Use clearbit for getting additional data for the user
- [x] Use JWT for user authentication
- [x] The solution should be posted on any source control

## Basic features
- [x] User registration
- [x] User login
- [x] Recipe creation
- [x] Recipe Rating (you cannot rate your own recipes)
- [x] List all recipes
- [x] List own recipes
- [x] Get most used ingridients (top5)

## Bonus
- [x] Dockerized solution is a plus
- [x] Unit tests are a plus
- [x] Search recipes (name, text, ingredients) is a plus
- [x] Filter recipes with minimum and maximum number of ingredients is a plus

## Docker installation
First thing you want to do is to pull docker image with next command:
```
docker pull milosnikic/recipesbookapi
```

After that run

```
docker ps
```
to verify that image has been successfully pulled.

![docker image](images/docker-images.png)

```
docker run -d -p 8000:8000 milosnikic/recipesbookapi
```
After that, container should be successfully created.

![docker run](images/docker-run.png)

You can verify that by running
```
docker images
```

to see running containers

![docker ps](images/docker-ps.png)

And now you can verify that application is started with visiting [localhost](http://localhost:8000/admin) and login with credentials (test, Test)

## Testing
After successful installation of project, you should access container bash with following command
```
docker exec -it de07 /bin/bash
```
Notice that after '-it' it is first four digits of container id.

Now inside bash, you can run command for running all tests
```
python manage.py test
```
There you can see 27 tests ran.

## Python client
In folder client, you can see clients for running all requirements. After registering, you can try to call any endpoint and you will be prompted to enter credentials. After that, while access token is valid, you will be able to call endpoints. When the token has expired, you will get response from any of endpoints. You only need to call again same endpoint just to reload access token from credentials.json file.

