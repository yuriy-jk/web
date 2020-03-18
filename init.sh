sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
#gunicorn -c /etc/gunicorn.d/hello.py hello:wsgi_hello
sudo ln -sf /home/box/web/etc/django_conf.py /etc/gunicorn.d/django_conf.py
sudo gunicorn -c /etc/gunicorn.d/django_conf.py ask.wsgi:application
