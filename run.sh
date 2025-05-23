docker run -dit \
    --env VIRTUAL_HOST=turbosail.it,padussolarchallenge.it \
    --env LETSENCRYPT_HOST=turbosail.it,padussolarchallenge.it \
    --env LETSENCRYPT_SINGLE_DOMAIN_CERTS=true \
    --restart unless-stopped \
    --network website \
    -v $(pwd)/website:/usr/share/nginx/html \
    -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf \
    nginx
