serve:
    podman run --rm -p 8000:80 -v ./website:/usr/share/caddy:ro,z docker.io/library/caddy:alpine
