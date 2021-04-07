# Installs and configures nginx

exec {'update':
    command => 'sudo apt-get -y update',
    path    => '/usr/bin',
    returns =>  ['0', '100', ],
}

exec {'install':
    path    =>  '/usr/bin',
    command =>  'sudo apt-get -y install nginx',
}
