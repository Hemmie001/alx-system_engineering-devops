# This manifest Kills a process named killmenow.

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/',
}
