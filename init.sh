sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-avaliable/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
gunicorn -c /etc/gunicorn.d/hello.py wsgi_hello
