#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

# Append the new location block to the Nginx configuration
sudo tee -a /etc/nginx/sites-available/default <<EOF
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
EOF

sudo service nginx restart
