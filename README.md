# Choreography Library API

## about
This is an API for a choreography library application that allows users to record and search pieces of choreographies created by multiple choreographers. This API is developed using the Django REST Framework. I created this project to teach myself DRF and express my love for dancing.

## features
With this API, you can...
- create user account - registration
- login and logout - authentication & authorization
- create, view, update, and delete a piece of choreography in your user account

## run the app

```bash
$ git clone https://github.com/yunchipang/drf-choreo-library.git
$ cd drf-choreo-library
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## REST API

The REST API to the `choreos` app is described below.

### 1. get list of choreos
#### request

`GET /choreos/`

```
curl -i -H 'Accept: application/json' http://localhost:8000/choreos/
```
#### response
```
HTTP/1.1 200 OK
Date: Tue, 21 Feb 2023 07:03:00 GMT
Server: WSGIServer/0.2 CPython/3.11.2
Content-Type: application/json
Vary: Accept, Cookie
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 396
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

[]
```

### 2. create a new choreo
#### request
`POST /choreos/`

```
curl -i -H 'Accept: application/json' -d 'choreographer=Leejung Lee&&music_title=LALISA&style=k-pop' http://localhost:8000/choreos/ --user "username:password"
```

#### response
```
HTTP/1.1 201 Created
Date: Tue, 21 Feb 2023 07:12:24 GMT
Server: WSGIServer/0.2 CPython/3.11.2
Content-Type: application/json
Vary: Accept, Cookie
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 153
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"id":3,"created":"2023-02-21T07:12:24.058032Z","choreographer":"Leejung Lee","music_title":"LALISA","style":"k-pop","video_url":"","owner":"yunchipang"}
```

### 3. get a specific choreo
#### request
`GET /choreos/id/`

```
curl -i -H 'Accept: application/json' http://localhost:8000/choreos/1/
```
#### response
```
HTTP/1.1 200 OK
Date: Tue, 21 Feb 2023 07:16:38 GMT
Server: WSGIServer/0.2 CPython/3.11.2
Content-Type: application/json
Vary: Accept, Cookie
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 167
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"id":1,"created":"2023-02-21T04:52:00.722810Z","choreographer":"xxxxx","music_title":"xxxxx","style":"xxxxx","video_url":"xxxxx","owner":"xxxxx"}
```