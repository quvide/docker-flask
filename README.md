This is a docker boilerplate. It consists of nginx as a uwsgi proxy, and as a static file server. Uwsgi and flask are run on a separate container that exposes a port to communicate with nginx. These two containers are orchestrated by docker-compose.

# Dependencies
* Docker
* Docker Compose

# Running
Type `docker-compose up` and check your browser at `localhost:8080` to see if it's working.
