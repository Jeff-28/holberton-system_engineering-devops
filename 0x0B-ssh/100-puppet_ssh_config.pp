# Makes changes to the ~/.ssh/config file using puppet

exec {'echo':
    path    =>  'usr/bin:/bin',
    command =>  'echo "    IdentityFile ~/.ssh/holberton\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
