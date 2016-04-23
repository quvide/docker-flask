This is a docker boilerplate. It consists of nginx as a uwsgi proxy, and as a static file server. Uwsgi and flask are run on a separate container that exposes a port to communicate with nginx. These two containers are orchestrated by docker-compose.

# Dependencies
* [Docker Engine](https://docs.docker.com/engine/installation/)
* [Docker Compose](https://docs.docker.com/compose/install/)

# Configuration
* `nginx/config/*` will get executed by nginx as config files.
* `nginx/static/*` will get served by nginx as static files.
* `flask/app/uwsgi.ini` controls uwsgi.

# Running
Type `docker-compose up` and check your browser at `localhost:8080` to see if it's working.

# Notes
Autoindexing will not work without some additional twiddling with nginx.conf. Autoindexing apparently apparently only works if `try_files $uri/` is specified. This however breaks developing on a port differing from 80 as it creates a redirect for some reason. The redirect is a problem as nginx is running on port 80 inside the image, but 8080 (or something else) on dev machines. The redirect would omit the port.
