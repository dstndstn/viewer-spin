# viewer-spin
A Spin container for the Legacy Survey Viewer

    docker build -t viewer-web web
    docker build -t viewer-app app
    docker-compose up
    open localhost:8000

Link "data" directory to the real thing (Docker bind mount).

Currently retrieves tiles from the production viewer.


docker build -t registry.spin.nersc.gov/dstn/viewer-app app
docker build -t registry.spin.nersc.gov/dstn/viewer-web web
docker image push registry.spin.nersc.gov/dstn/viewer-app
docker image push registry.spin.nersc.gov/dstn/viewer-web

