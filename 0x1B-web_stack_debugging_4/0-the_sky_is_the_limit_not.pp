# Fix the request of nginx server
exec { 'fix-requests':
    command => "sed -i 's/worker_processes 4;/worker_processes 8;/g' /etc/nginx/nginx.conf; sudo service nginx restart",
    path    => ['/bin', '/usr/bin']
}
