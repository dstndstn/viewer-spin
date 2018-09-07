# viewer-spin
A Spin container for the Legacy Survey Viewer

    docker build -t viewer-nginx docker-nginx
    docker build -t viewer-app docker-viewer
    docker-compose up
    open localhost:8000

Link "data" directory to the real thing (Docker bind mount).

Currently retrieves tiles from the production viewer.
