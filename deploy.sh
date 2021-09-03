#!/bin/sh

ssh -o StrictHostKeyChecking=no ubuntu@$1 << 'ENDSSH'
  cd /home/ubuntu/app
  aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 115646757360.dkr.ecr.us-east-2.amazonaws.com
  docker pull 115646757360.dkr.ecr.us-east-2.amazonaws.com/django-ec2-web
  docker pull 115646757360.dkr.ecr.us-east-2.amazonaws.com/django-ec2-nginx-proxy
  docker-compose -f docker-compose.prod.yml up -d
  docker-compose -f docker-compose.prod.yml exec -T web python manage.py migrate --noinput ; docker-compose -f docker-compose.prod.yml exec -T web python manage.py collectstatic --noinput --clear
ENDSSH
