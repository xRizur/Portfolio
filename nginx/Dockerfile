FROM nginx

# Override the default nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf
COPY ../app/default.conf /etc/nginx/nginx.conf