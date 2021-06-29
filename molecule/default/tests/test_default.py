import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_file(host):
    f = host.file('/etc/letsencrypt/renewal-hooks/post/nginx.sh')
    assert f.exists


def test_dhparam_file(host):
    f = host.file('/etc/ssl/dhparam.pem')
    assert f.exists
