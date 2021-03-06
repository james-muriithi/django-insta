# Insta
created by James Muriithi on 06/03/2022

## Description
This is an instagram clone where users follow each other and can see the images they post. One can like and comment on posted images

## Technologies Used
The following technologies have been used on this project:

* HTML
* CSS
* JS
* Bootstrap
* Django
* Python
* Cloudinary (for image upload)

# Setup / Installation
* clone the repo:

```shell
git clone https://github.com/james-muriithi/django-insta.git
```

```
cd blog
```
* create virtual environment 

```shell
python3.8 -m venv --without-pip venv
```

* To activate the virtual environment
```shell
source venv/bin/activate
```

* install the packages from requirements.txt
```shell
pip install -r requirements.txt 
```

* setup environment variables
```shell
cp .env.example .env
```
* Execute the shell script and start the server
```shell
python3.8 manage.py runserver
```
* open the browser and navigate to http://127.0.0.1:8000/ to see the application in action

## Design
Here is the Design
![Design](./screenshots/Home.png)
![Modal](./screenshots/Profile.png)
![Modal](./screenshots/Signup.png)
![Modal](./screenshots/Login.png)
## Screenshot
![Screnshot](./screenshots/screenshot.png)
![Screnshot](./screenshots/screenshot2.png)
![Screnshot](./screenshots/screenshot3.png)
![Screnshot](./screenshots/screenshot4.png)
## Live link
[Here is the link to the live site](https://django-insta-jm.herokuapp.com/)
## Contact details
Email: james@student.moringaschool.com

## MIT licence

<p>Copyright (c) 2022 Moringa School </p>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.