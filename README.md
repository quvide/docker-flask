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
* You cannot access folders without typing in the trailing slash! Due to the design of nginx, `try_files $uri/` will try to autoindex root and then throw a 403 because it is not allowed thus preventing it from ever reaching flask. Root could be handled with a special case but that brings us to the next problem.
* Nginx redirects work incorrectly on dev machines if they don't use port 80. Nginx thinks it's serving on port 80 (which it is inside the image) but a different one on the outside. So redirects would go like this: name.domain:8080/folder -> name.domain/folder/. You can probably see the problem. You probably won't need folder redirection anyways when using flask but you can modify the default configuration yourself if required. If you can think of a configuration that solves both of these problems, let me know!
