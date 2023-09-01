# Increasing the amount of traffic Nginx can handle 

# Increase the ULIMIT of the default Nginx file
exec { 'fix--for-nginx':
  # Modify the ULIMIT value from 15 to 4096
  command => '/bin/sed -i "s/15/2000/" /etc/default/nginx',
  # Specify the path for the sed command
  path => '/usr/local/bin/:/bin/,
}

# Restart Nginx
exec { 'nginx-restart':
  # Restart Nginx service
  command => '/etc/init.d/nginx restart',
  # Specify the path for the init.d script
  path => '/etc/init.d/',
}
