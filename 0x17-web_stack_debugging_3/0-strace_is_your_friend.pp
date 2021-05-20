# Fixes php settings

exec { 'php fix':
    path    => '/bin', '/usr/bin', '/usr/sbin',
    command =>  "sed -i -e 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
