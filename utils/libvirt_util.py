import libvirt
import settings
import mylog

LOG = mylog.setup_custom_logger(__name__)


def get_connection(host):
    """
    get connection by host. the public key should be copy to remote host.
    Notice: on OS X, the conn string should be end with
    ?socket=/var/run/libvirt/libvirt-sock,
    :param host: compute node hostname or ip
    :return: conn object
    """
    conn_str = "qemu+ssh://%s@%s:%s/system?" \
               "socket=/var/run/libvirt/libvirt-sock"\
               % (settings.COMPUTE_NODE_USER, host, settings.COMPUTE_NODE_PORT)
    LOG.debug(conn_str)
    conn = libvirt.open(conn_str)
    return conn


def get_dom_list(host):
    domains = []
    conn = get_connection(host)
    hypervisor_name = conn.getHostname()
    LOG.debug(hypervisor_name)
    # domain_names = conn.listAllDomains()
    caps = conn.getCapabilities()
    LOG.debug(caps)
    # for domain_name in domain_names:
    #     domain = conn.lookupByName(domain_name)
    #     # infos = domain.info()
    #     LOG.debug(domain.name())
    #     # domains.append(infos)
    # conn.close()
    return domains





if __name__ == '__main__':
    host = '10.12.10.14'
    get_dom_list(host)


