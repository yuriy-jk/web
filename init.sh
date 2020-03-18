sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
gunicorn -c /etc/gunicorn.d/hello.py hello:wsgi_hello
sudo ln -sf /home/box/web/etc/unicorn.py /etc/gunicorn.d/unicorn.py
gunicorn -c /etc/gunicorn.d/unicorn.py
