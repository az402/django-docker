FROM ubuntu:12.10
RUN apt-get -y update && \
    apt-get install -y \
    libpq-dev \
    python3 \
    python3-dev \
    python3-setuptools \
    python3-pip \
    nginx \
    wget
RUN easy_install pip
RUN pip install virtualenv
RUN pip install uwsgi
RUN virtualenv --no-site-packages /opt/ve/djdocker
ADD . /opt/apps/djdocker
ADD .docker/supervisor.conf /opt/supervisor.conf
ADD .docker/run.sh /usr/local/bin/run
RUN (cd /opt/apps/djdocker && git remote rm origin)
RUN (cd /opt/apps/djdocker && git remote add origin https://github.com/kencochrane/django-docker.git)
RUN /opt/ve/djdocker/bin/pip install -r /opt/apps/djdocker/requirements.txt
RUN (cd /opt/apps/djdocker && /opt/ve/djdocker/bin/python manage.py syncdb --noinput)
RUN (cd /opt/apps/djdocker && /opt/ve/djdocker/bin/python manage.py collectstatic --noinput)
EXPOSE 8000
CMD ["/bin/sh", "-e", "/usr/local/bin/run"]
