# Configuration Management and cloud
Puppet is a commonly used configuration management system but also used with following applications Chef, Ansible, CFEngine.

##Puppet Resources

Check out the following links for more information:

    https://puppet.com/docs/puppet/latest/lang_resources.html

    https://puppet.com/blog/deploy-packages-across-your-windows-estate-with-bolt-and-chocolatey/

##More Information About Configuration Management

Check out the following links for more information:

    https://en.wikipedia.org/wiki/Domain-specific_language

    http://radar.oreilly.com/2015/04/the-puppet-design-philosophy.html

DSL - Domain Specific Language (language specific and easier to learn than a general purpose language)

Directory: /cd /etc/puppet/code/environments/production/modules/profile/manifests
file: init.pp

sudo puppet agent -v --test

##More Information About Deploying Puppet Locally

Check out the following links for more information:

    https://puppet.com/docs/puppet/latest/style_guide.html

    https://puppet.com/docs/puppetserver/latest/install_from_packages.html

Command:
    sudo puppet apply -v tools.pp

    sudo apt install puppet-master
    sudo apt install puppet-module-puppetlabs-apache

##More Information about Deploying Puppet to Clients

Check out the following link for more information:

    http://www.masterzen.fr/2010/11/14/puppet-ssl-explained/

    site.pp - information about nodes in the cluster

Commands:
    sudo puppet config --section master set autosign true
    sudo apt install puppet #in machines to manage with puppet
    sudo puppet config set server ubuntu.example.com # connect with master
    sudo puppet agent -v --test #test connection with master and check certificate

    sudo systemctle enable puppet # enable puppet to start
    sudo systemctl start puppet
    sudo systemctl status puppet

##More Information About Updating Deployments

Check out the following links for more information:

    https://rspec-puppet.com/tutorial/ #testing yout puppet modules

    http://puppet-lint.com/ #check puppet manifest conform style guide


#Managing VMs in GCP

Over the last few videos we learned how to create and use virtual machines running on GCP. We then explored how we can use one VM as a template for creating many more VMs with the same setup. You can find a lot more information about this in the following tutorials:

    https://cloud.google.com/compute/docs/quickstart-linux

    https://cloud.google.com/compute/docs/instances/create-vm-from-instance-template

    https://cloud.google.com/sdk/docs

STEPS TO CONFIGURE A SERVICE
>hello_cloud.service
[Unit]
After=network.target
[Service]
ExecStart=/usr/local/bin/hello_cloud.py 80

[Install]
Wantedby=default.target

>hello_cloud.py
#!/usr/bin/env python3
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A simple Hello World type app which can serve on port 8000.
Optionally, a different port can be passed.

The code was inspired by:
https://gist.github.com/davidbgk/b10113c3779b8388e96e6d0c44e03a74
"""
import http
import http.server
import socket
import socketserver
import sys

# TCP port for listening to connections, if no port is received
DEFAULT_PORT=8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(http.HTTPStatus.OK)
        self.end_headers()
        # Hello message
        self.wfile.write(b'Hello Cloud')
        # Now get the hostname and IP and print that as well.
        hostname = socket.gethostname()
        host_ip = socket.gethostbyname(hostname)
        self.wfile.write(
            '\n\nHostname: {} \nIP Address: {}'.format(
                hostname, host_ip).encode())


def main(argv):
    port = DEFAULT_PORT
    if len(argv) > 1:
        port = int(argv[1])

    web_server = socketserver.TCPServer(('', port), Handler)
    print("Listening for connections on port {}".format(port))
    web_server.serve_forever()


if __name__ == "__main__":
    main(sys.argv)



sudo cp hello_cloud.py /usr/local/bin/
sudo cp hello_cluod.service /etc/systemd/system
sydo systemctl enable hello_cloud

 #More About Cloud & GCP

Check out the following links for more information:

    Getting started on GCP with Terraform

    Creating groups of unmanaged instances

    Official documentation is here: https://cloud.google.com/load-balancing/docs/https/

    https://geekflare.com/gcp-load-balancer/

Interesting articles about hybrid setups:

    https://blog.inkubate.io/create-a-centos-7-terraform-template-for-vmware-vsphere/

    https://www.terraform.io/docs/enterprise/before-installing/reference-architecture/gcp.html

    https://www.hashicorp.com/resources/terraform-on-premises-hybrid-cloud-wayfair

#More About Cloud Providers

Here are some links to some common Quotas you’ll find in various cloud providers

    https://cloud.google.com/compute/quotas#understanding_vm_cpu_and_ip_address_quotas

    https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html

    https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits#service-specific-limits

#More Information on Monitoring and Alerting

Check out the following links for more information:

    https://www.datadoghq.com/blog/monitoring-101-collecting-data/

    https://www.digitalocean.com/community/tutorials/an-introduction-to-metrics-monitoring-and-alerting

    https://en.wikipedia.org/wiki/High_availability

    https://landing.google.com/sre/books/

Commands:
 cron - to schedule check status and send emails on errors

#Reading: Debugging Problems on the Cloud

Check out the following links for more information:

    https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-instances

    https://docs.microsoft.com/en-us/azure/virtual-machines/troubleshooting/

    https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.htm

Commands:
 sudo systemctl status apache2
 sudo netstat -nlp # To find which processes are listening on which ports
 sudo kill [process-id]
 cat /usr/local/bin/jimmytest.py
 ps -ax | grep python3
 sudo systemctl --type=service | grep jimmy
 sudo systemctl stop jimmytest && sudo systemctl disable jimmytest #stop service and remove it

