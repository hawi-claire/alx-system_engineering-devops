#!/usr/bin/env bash
# This code will install the package puppet-lint
class { 'python3:' }

package { 'flask':
  ensure   => present,
  provider => 'pip3',
  version  => '2.1.0',
  require  => Class['python3'],
}
