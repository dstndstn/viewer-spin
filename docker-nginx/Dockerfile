# nginx that runs as non-root user
# https://docs.nersc.gov/services/spin/getting_started/lesson-1/

FROM nginx:latest

# Make /var/cache/nginx/ writable by non-root users
RUN chgrp nginx /var/cache/nginx/
RUN chmod g+w /var/cache/nginx/

# Run as port 8080, which is available to non-root users allows us to drop
# all remaining root capabilities from the container, which improves security.
RUN sed --regexp-extended --in-place=.bak 's%(^\s+listen\s+)80(;)%\18080\2%' /etc/nginx/conf.d/default.conf

# Write the PID file to a location where regular users have write access.
RUN sed --regexp-extended --in-place=.bak 's%^pid\s+/var/run/nginx.pid;%pid /var/tmp/nginx.pid;%' /etc/nginx/nginx.conf

EXPOSE 8080

# Pull in static docs for the web service
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates
WORKDIR /app
RUN git clone http://github.com/legacysurvey/decals-web viewer

COPY nginx-proxy.conf /etc/nginx/conf.d/default.conf

