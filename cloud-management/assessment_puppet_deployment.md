#Install packages

cd /etc/puppet/code/environments/production/modules/packages
cat manifests/init.pp

init.pp
class packages {
   package { 'python-requests':
       ensure => installed,
   }
   if $facts[os][family] == "Debian" {
     package { 'golang':
       ensure => installed,
     }
  }
   if $facts[os][family] == "RedHat" {
     package { 'nodejs':
       ensure => installed,
     }
  }
}

sudo puppet agent -v --test
apt policy golang

# Fetch machine information

cd /etc/puppet/code/environments/production/modules/machine_info
cat manifests/init.pp

class machine_info {
  if $facts[kernel] == "windows" {
       $info_path = "C:\Windows\Temp\Machine_Info.txt"
   } else {
       $info_path = "/tmp/machine_info.txt"
   }
 file { 'machine_info':
       path => $info_path,
       content => template('machine_info/info.erb'),
   }
}

##Puppet Templates

cat templates/info.erb

Machine Information
-------------------
Disks: <%= @disks %>
Memory: <%= @memory %>
Processors: <%= @processors %>
Network Interfaces: <%= @interfaces %>
}

--linux instance not puppet master
sudo puppet agent -v --test


#Reboot machine

cd /etc/puppet/code/environments/production/modules/reboot/manifests
sudo nano init.pp

class reboot {
  if $facts[kernel] == "windows" {
    $cmd = "shutdown /r"
  } elsif $facts[kernel] == "Darwin" {
    $cmd = "shutdown -r now"
  } else {
    $cmd = "reboot"
  }
  if $facts[uptime_days] > 30 {
    exec { 'reboot':
      command => $cmd,
     }
   }
}

sudo nano /etc/puppet/code/environments/production/manifests/site.pp 

node default {
   class { 'packages': }
   class { 'machine_info': }
   class { 'reboot': }
}

-- in client not puppet master 
sudo puppet agent -v --test

