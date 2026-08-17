FROM ghcr.io/static-web-server/static-web-server:2

# SWS serves /public on :80 with index.html by default — no config needed
COPY website /public
