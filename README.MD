# CHEFIN 
## _Recipe Web App_


CHEFIN is a django web app that allow user to search recipes by ingredients. 
✨ALso look at the home page and pick the dish and cook it!✨
The website on render deployed: https://chefin-1.onrender.com/

## Built-With

- Web framework Django (version 5.0.6) for this project
- Open source toolkit Bootstrap for fontend


## Getting started



- [Built With](https://github.com/kesha100/chefin/#Built-With)
- [Getting started](https://github.com/kesha100/chefin/#Getting-started)
- [Demo](https://github.com/kesha100/chefin/#Demo)
- [Author](https://www.linkedin.com/in/aruuke-atabekova-b97757274/)
- [Process of Design and Development] (https://github.com/kesha100/chefin/#Process of Design and Development)



## Installation


```sh
git clone https://github.com/kesha100/chefin.git
```
Install python3 with brew for Mac

```sh
brew install python3
```
Install pip with brew for Mac
```sh
python3 get-pip.py
```
run the django server
```sh
python manage.py runserver
```

Once you press Enter, you should see a message like this below:
```sh
Performing system checks...

System check identified no issues (0 silenced).
June 27, 2019 - 18:49:40
Django version 2.1, using settings 'django_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Copy the url http://127.0.0.1:8000/ above to your browser to see the Demo.


## Database
Inorder to interact with the models, we need to go to python shell.
```sh
python manage.py shell
```
Import the models
```sh
>>> from recipe.models import Recipe
>>> Recipe.objects.all()
```

### Demo

- [Video Recording Demo]](https://youtu.be/2jdSeGbUOOk)


### Author
- [Aruuke linkedin] (https://www.linkedin.com/in/aruuke-atabekova-b97757274/)

