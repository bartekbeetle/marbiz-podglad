# Podgląd roboczy strony Marbiz. Statyczny HTML — nginx, nie serve.py
# (serve.py to serwer deweloperski na localhost, nie nadaje się na VPS).
FROM nginx:1.27-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY index.html 404.html robots.txt /usr/share/nginx/html/
COPY css/    /usr/share/nginx/html/css/
COPY fonts/  /usr/share/nginx/html/fonts/
COPY img/    /usr/share/nginx/html/img/
COPY transport-hds/          /usr/share/nginx/html/transport-hds/
COPY roboty-ziemne/          /usr/share/nginx/html/roboty-ziemne/
COPY wywoz-ziemi/            /usr/share/nginx/html/wywoz-ziemi/
COPY transport-materialow/   /usr/share/nginx/html/transport-materialow/
COPY rozbiorki/              /usr/share/nginx/html/rozbiorki/
COPY kontakt/                /usr/share/nginx/html/kontakt/

EXPOSE 80
