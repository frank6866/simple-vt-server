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
    conn = get_connection(host)
    ids = conn.listDomainsID()
    for id in ids:
        LOG.debug(id)

    inactived_domains = conn.listDefinedDomains()
    for name in inactived_domains:
        # LOG.debug(name)
        pass

    all_domain_objects = conn.listAllDomains(0)
    for domain in all_domain_objects:
        id = domain.ID()
        name = domain.name()
        uuid_string = domain.UUIDString()
        os_type = domain.OSType()
        current_snapshot_exists = domain.hasCurrentSnapshot()
        managed_save_images_exists = domain.hasManagedSaveImage()
        # hostname = domain.hostname()
        state, maxmem, mem, cpus, cputime = domain.info()
        is_active = domain.isActive()
        is_persistent = domain.isPersistent()
        is_updated = domain.isUpdated()
        max_mem = domain.maxMemory()
        vcpus_count = domain.maxVcpus()
        # time = domain.getTime()

        # LOG.debug(time)
        state, reason = domain.state()
        LOG.debug("%s, %s" % (state, reason))



if __name__ == '__main__':
    host = '10.12.10.14'
    get_dom_list(host)

