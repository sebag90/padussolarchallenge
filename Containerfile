FROM docker.io/library/caddy:alpine

# Standard Caddy serves /usr/share/caddy on :80 with index.html — no config needed
COPY website /usr/share/caddy
