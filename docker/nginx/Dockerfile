FROM nginx:1.10.1-alpine

USER 0
RUN mkdir -p /srv/http/default
RUN mkdir -p /etc/nginx/sites-enabled
RUN mkdir -p /etc/nginx/config
RUN mkdir -p /etc/nginx/html

COPY ./resources/public/nginx /srv/http/default
COPY ./resources/public/nginx/favicon.ico /etc/nginx/html
COPY ./resources/public/nginx/main.css /etc/nginx/html
COPY ./docker/nginx/sites /etc/nginx/sites
COPY ./docker/nginx/config/error_pages_content.conf /etc/nginx/config
COPY ./docker/nginx/config/error_pages.conf /etc/nginx/config
COPY ./docker/nginx/config/mime.types /etc/nginx

RUN chmod 644 /etc/nginx/html/main.css
RUN chmod 644 /srv/http/default/main.css

CMD ["nginx", "-g", "daemon off;"]