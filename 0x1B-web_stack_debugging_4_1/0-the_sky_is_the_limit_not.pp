# Increasing the amount of traffic Nginx can handle 

# Increase the ULIMIT of the default Nginx file
exec { 'fix--for-nginx':
  # Modify the ULIMIT value from 15 to 2000
  command => '/bin/sed -i "s/15/2000/" /etc/default/nginx',
}

# Restart Nginx
->exec { 'nginx-restart':
  # Restart Nginx service
  command => '/etc/init.d/nginx restart',
}
