FROM alpine:latest
RUN apk add --update nginx && \
	rm -rf /var/cache/apk/* && \
	mkdir -p /tmp/nginx/
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
#RUN rm /etc/nginx/conf.d/default.conf
COPY flask_site_nginx.conf /etc/nginx/conf.d/
EXPOSE 8000/tcp
ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]