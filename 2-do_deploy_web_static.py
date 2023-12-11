#!/usr/bin/env bash

# Set up the web servers for the deployment of web_static

# Update package list and upgrade
sudo apt-get -y update && sudo apt-get -y upgrade

# Define paths
WEB_STATIC_PATH="/data/web_static"
RELEASES_PATH="$WEB_STATIC_PATH/releases/test"
SHARED_PATH="$WEB_STATIC_PATH/shared"

# Ensure paths exist
sudo mkdir -p "$RELEASES_PATH" "$SHARED_PATH"

# Create a test index.html file
echo "This is a test" | sudo tee "$RELEASES_PATH/index.html"

# Create symbolic link
sudo ln -sf "$RELEASES_PATH" "$WEB_STATIC_PATH/current"

# Change ownership
sudo chown -hR ubuntu:ubuntu "$WEB_STATIC_PATH"

# Update Nginx configuration
sudo tee /etc/nginx/sites-available/web_static <<EOF
server {
    listen 80 default_server;
    server_name _;

    location /hbnb_static/ {
        alias $WEB_STATIC_PATH/current/;
    }

    # Additional server configuration if needed
}
EOF

# Create a symbolic link to enable the configuration
sudo ln -s /etc/nginx/sites-available/web_static /etc/nginx/sites-enabled/

# Restart Nginx
sudo service nginx restart
