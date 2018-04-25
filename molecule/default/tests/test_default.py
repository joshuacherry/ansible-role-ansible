"""
Runs Default tests
Available Modules: http://testinfra.readthedocs.io/en/latest/modules.html

"""
import os
import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ansible_is_installed(host):
    """
    Tests that ansible is installed
    """
    ansible_version = "ansible --version | grep 'ansible 2'"
    python_version = "ansible --version | grep 'python version'"

    assert "python version = 2." in host.run(python_version).stdout
    assert "ansible 2.5.0" in host.run(ansible_version).stdout
