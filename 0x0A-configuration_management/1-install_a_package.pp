#!/usr/bin/pup
# Install a specific version of flask (2.1.0)
 class { 'python3': }
 
package { 'flask':
	ensure => present,
	provider => 'pip3',
	version: '2.1.0'
	require => Class['python3'],
}

