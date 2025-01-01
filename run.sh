docker run -dit \
    --env VIRTUAL_HOST=turbosail.it \
    --env LETSENCRYPT_HOST=turbosail.it \
    --restart unless-stopped \
    --network website \
    -v $(pwd)/website:/usr/share/nginx/html \
    -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf \
    nginx