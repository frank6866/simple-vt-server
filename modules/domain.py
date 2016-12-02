

class Domain(object):
    def __init__(self, dom_id, name, status, hypervisor_name):
        self.dom_id = dom_id
        self.name = name
        self.status = status
        self.hypervisor_name = hypervisor_name

