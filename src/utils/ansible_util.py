from collections import namedtuple
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.playbook_executor import TaskQueueManager
from ansible.inventory import Inventory
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
import json
from ansible.plugins.callback import CallbackBase
from file_callback import FileCallbackModule

# https://serversforhackers.com/running-ansible-2-programmatically

class ResultCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in

    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin
    """

    def v2_runner_on_ok(self, result, **kwargs):
        """Print a json representation of the result

        This method could store the result in an instance attribute for retrieval later
        """
        host = result._host
        print result._result
        # print json.dumps({host.name: result._result}, indent=4)
        # with open("test.txt", "a") as myfile:
            # myfile.write(json.dumps({host.name: result._result}, indent=4))


def run_playbook(playbook_path, host_list, extra_vars):
    loader = DataLoader()
    variable_manager = VariableManager()

    inventory = Inventory(loader=loader, variable_manager=variable_manager,
                          host_list=host_list)
    OPTIONS = namedtuple('Options',
                         ['listtags', 'listtasks', 'listhosts', 'syntax',
                          'connection', 'module_path', 'forks', 'remote_user',
                          'private_key_file', 'ssh_common_args',
                          'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args',
                          'become', 'become_method', 'become_user', 'verbosity',
                          'check'])
    options = OPTIONS(listtags=False, listtasks=False, listhosts=False,
                      syntax=False, connection='ssh', module_path=None,
                      forks=100, remote_user="root",
                      private_key_file="/Users/dyc/.ssh/id_rsa",
                      ssh_common_args=None,
                      ssh_extra_args=None, sftp_extra_args=None,
                      scp_extra_args=None, become=True, become_method='sudo',
                      become_user='root', verbosity=True, check=False)

    extra_vars["ansible_ssh_port"] = 22
    variable_manager.extra_vars = extra_vars

    pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory,
                            variable_manager=variable_manager, loader=loader,
                            options=options, passwords={})

    # Instantiate our ResultCallback for handling results as they come in
    results_callback = ResultCallback()
    results_callback = FileCallbackModule()

    pbex._tqm._stdout_callback=results_callback

    pbex.run()
    # results = pbex.run()
    # return results


class AnsibleProxy(object):
    pass


if __name__ == '__main__':
    host_list = ["10.12.10.57"]
    host_list = ["localhost"]
    playbook_path = "cobbler.yml"
    run_playbook(playbook_path, host_list, extra_vars={'FETCH_DIR': "abc"})






