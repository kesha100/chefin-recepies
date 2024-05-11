# CHEFIN 
## _Recipe Web App_


CHEFIN is a django web app that allow user to search recipes by ingredients. 
✨ALso look at the home page and pick the dish and cook it!✨

## Built-With

- Web framework Django (version 5.0.6) for this project
- Open source toolkit Bootstrap for fontend


## Getting started



- [Built With](https://github.com/kesha100/chefin/#Built-With)
- [Getting started](https://github.com/kesha100/chefin/#Getting-started)
- [Database](https://github.com/kesha100/chefin/#Database)
- [Demo](https://github.com/kesha100/chefin/#Demo)
- [Author](https://github.com/kesha100/chefin/#Author)
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
- [Demo Images]](https://github.com/kesha100/chefin/tree/main/DemoImages/)


### Author
- [Aruuke linkedin] (https://www.linkedin.com/in/aruuke-atabekova-b97757274/)

### Process of Design and Development
The process of designing and developing CHEFIN involved the following key steps:

Requirement Gathering: Understanding the needs of the target users and defining the features and functionalities required for the recipe web app.

Wireframing and UI Design: Creating wireframes and designing the user interface (UI) to ensure an intuitive and visually appealing user experience. Bootstrap was used as an open-source toolkit for frontend development, providing a responsive design and pre-styled components.

Backend Development: Utilizing the Django web framework for backend development, including defining models, views, and templates. Django's built-in features, such as authentication, admin interface, and ORM, were leveraged to streamline development.

Frontend Integration: Integrating the frontend UI with the Django backend, ensuring seamless communication between the client-side and server-side components of the application.

Testing and Debugging: Thorough testing of the application to identify and resolve any bugs or issues. Both manual testing and automated testing methodologies were employed to ensure the reliability and stability of the application.




