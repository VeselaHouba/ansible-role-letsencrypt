# letsencrypt role

## Let'sencrypt certificates

Tested with nginx

Not standalone! It's expected that you'll take care of
forwarding traffic like this on port 80

```
location ~ /\.well-known/acme-challenge/ {
   root /var/www/letsencrypt/;
   index index.html index.htm;
   try_files $uri =404;
}
```

Example

```
ssl_certs_letsencrypt_list:
  - name: certificate1_fqdn
    mail: support@example.com

  - name: certificate2_fqdn
    altnames:
      - www.certificate2_fqdn
      - dev.certificate2_fqdn
    mail: support@example.com

  - name: certificate3_fqdn
    state: absent
```

NOTES:
  - `altnames` MUST be list, not single line string!
  - If you want more generic role, following https://github.com/geerlingguy/ansible-role-certbot is highly recommended.


Author Information
------------------

Jan Michalek
