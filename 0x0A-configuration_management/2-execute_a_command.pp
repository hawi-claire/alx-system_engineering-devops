# Kill a process using exec
exec {'kill':
	command => 'pkill killmenow',
	path    => '/usr/bin';
}

