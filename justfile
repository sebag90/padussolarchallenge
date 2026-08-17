serve:
    podman run --rm -p 8000:80 -v ./website:/public:ro,z ghcr.io/static-web-server/static-web-server:2
