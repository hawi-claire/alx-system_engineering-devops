# Install flask from pip3
class { 'python3': }

package { 'flask':
  ensure => present,
  provider => 'pip3',
  version: '2.1.0'
  require => Class['python3'],
}
