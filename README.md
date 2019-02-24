# Django-Music-App--Docker
<p>Music App is an application for storing, managing, listening and sharing music. <br><b> Access to admin account</b> login: test, password: testy123<br>
Use admin panel to storing bands, playlists and songs.
<h3>Run</h3>
To run app use docker-compose.yml by command <code>docker-compose up</code> or use docker image <code>docker run -p 8000:8000 kowal20x7/music-app</code>.<br>
To run app on your localhost use <code>python manage.py runserver</code>.
<h3>Simple Api</h3>
/api-token-auth/ => Get auth token, -d '{"username":"","password":""}' <br>
Bearer Token is required
<h5>Users</h5>
POST /api/users => add user<br>
GET /users, /user/{id} <br>
PUT /user/{id}<br>
DELETE /user/{id}<br>
<h5>Bands</h5>
POST /bands<br>
GET /bands, /band/{id}<br>
PUT /band/{id}<br>
DELETE /band/{id}
<h5>Playlists</h5>
POST /playlists<br>
GET /playlists, /playlist/{id}<br>
PUT /playlist/{id}<br>
DELETE /playlist/{id}<br>
