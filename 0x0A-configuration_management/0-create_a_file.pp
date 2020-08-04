#!/usr/bin/env bash
#Create a file in /tmp named holberton
file {'/tmp/holberton':
    ensure  => 'file',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I Love Puppet',
}
