# Fix 

exec {'replace':
  provider  => shell,
  commander => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before    => Exec['restart'],
}

exec {'restart':
  provider  => shell,
  commander => 'sudo service nginx restart',
}
