# Neptune

Neptune is an innovative e-commerce platform built on the robust Django web framework, providing a comprehensive, secure, and user-centric online shopping experience. At its core, Neptune leverages the power of the Django REST framework, creating a seamless interface between data and presentation, ensuring a smooth and responsive user experience. The platform has been carefully designed to include a range of key features, offering functionality and usability that cater to both shoppers and business owners.

The frontend of Neptune is built using React, bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload if you make edits.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Features

- **User Authentication**: Users can create an account, log in, and manage their sessions securely.

_(More features will be added soon)_

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

To run this project, you need to have Python installed on your machine. The project uses Django and Django REST framework. You can install them using `pip`:

You should also install virtualenv if you haven't installed it yet:


```sh
pip install virtualenv
```
after that you can create a virtual environment for the project:
```sh
python3 -m venv venv
```

To activate the virtual environment, run:

```sh
source venv/bin/activate
```

install django and djangorestframework:
```sh
pip install django
pip install djangorestframework
```

## Installation

A step-by-step series of examples that tell you how to get a development environment running:

1. Clone the repository:

```sh
git clone https://github.com/GamingSeries/Neptune.git
```

2. Navigate to the project directory:

```sh
cd Neptune
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

The requirements.txt file should contain the following:

```sh
asgiref==3.7.0
certifi==2023.5.7
cffi==1.15.1
charset-normalizer==3.1.0
cryptography==41.0.1
defusedxml==0.7.1
Django==4.2.2
django-browser-reload==1.8.0
django-filter==23.2
django-templated-mail==1.1.1
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
djoser==2.2.0
idna==3.4
Markdown==3.4.3
oauthlib==3.2.2
Pillow==9.5.0
psycopg2-binary==2.9.6
pycparser==2.21
Pygments==2.15.1
PyJWT==2.7.0
python3-openid==3.2.0
pytz==2023.3
PyYAML==6.0
requests==2.31.0
requests-oauthlib==1.3.1
social-auth-app-django==5.2.0
social-auth-core==4.4.2
sqlparse==0.4.4
typing_extensions==4.6.0
urllib3==2.0.3
```

4. Run migrations

```sh
python manage.py migrate
```

5. Run the server

```sh
python manage.py runserver
```

## Usage

Once the server is running, navigate to the local server address displayed in your terminal to view the application in your web browser. From there, you can register a new account or log in.

## Contributing

Feel free to fork the project and submit any pull requests! All contributions are welcome.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Django REST framework](https://www.django-rest-framework.org/) - REST API framework for Django
- [PostgreSQL](https://www.postgresql.org/) - Database management system
