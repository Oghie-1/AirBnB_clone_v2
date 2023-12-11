# Configures a web server for deployment of web_static.

# Nginx configuration file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
} ->

file { '/data':
  ensure  => 'directory',
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
} ->

file { '/var/www':
  ensure => 'directory',
} ->

file { '/var/www/html':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
} ->

file { '/data/web_static':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
} ->

file { '/data/web_static/releases':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
} ->

file { '/data/web_static/releases/test':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
} ->

file { '/data/web_static/shared':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Holberton School Puppet\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
} ->

file { '/data/web_static/current':
  ensure  => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
} ->

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School Nginx\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
} ->

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf,
} ->

service { 'nginx':
  ensure => 'running',
  enable => true,
  require => [Package['nginx'], File['/etc/nginx/sites-available/default']],
} ->

exec { 'nginx-config-test':
  command => '/usr/sbin/nginx -t',
  path    => '/usr/bin/:/usr/sbin/',
  require => Service['nginx'],
}
