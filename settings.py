# st2 config
ST2_REST_PROTOCAL = "http"
ST2_SERVER_IP = "127.0.0.1"
ST2_USER = "st2admin"
ST2_PWD = "Ch@ngeMe"
ST2_API_PORT = "9101"
ST2_AUTH_PORT = "9100"

ST2_EXECUTION_URL = ST2_REST_PROTOCAL + "://" + ST2_SERVER_IP + ":" \
                    + ST2_API_PORT + "/v1/executions/"
ST2_AUTH_URL = ST2_REST_PROTOCAL + "://" + ST2_SERVER_IP + ":" \
               + ST2_AUTH_PORT + "/tokens"

ROLE_MASTER = "master"
ROLE_AGENT = "agent"
ROLE_ZK = "zookeeper"

# ansible config
PLAY_BOOK_BASE_DIR = "/data/mesos_ops/work"
# PLAY_BOOK_BASE_DIR = "/tmp/mesos_ops/work"


INVENTORY_FILE_NAME = "inventory"
EXTRA_VARS_FILE_NAME = "all.yml"
MASTER_PLAYBOOK_PATH = "/data/mesos_ops/playbooks/master.yml"
AGENT_PLAYBOOK_PATH = "/data/mesos_ops/playbooks/agent.yml"

BASE64_KEYS = ["MASTER_ACLS_CONTENT", "MASTER_CREDENTIALS_CONTENT",
               "MASTER_WHITELIST_CONTENT", "AGENT_MESOS_CREDENTIAL_CONTENT",
               "DOCKER_STORAGE_OPTS", "DOCKER_DNS", "DOCKER_DNS_SEARCH",
               "DOCKER_HOSTS", "DOCKER_LOG_OPTS", "DOCKER_REGISTRY_MIRRORS",
               "DOCKER_INSECURE_REGISTRIES"]

MASTER_DEFAULT_KEYS = ["MASTER_MESOS_ZK", "MASTER_MESOS_PORT",
                       "MASTER_MESOS_WORK_DIR", "MASTER_MESOS_QUORUM",
                       "MASTER_MESOS_ACLS", "MASTER_ACLS_CONTENT",
                       "MASTER_MESOS_CREDENTIALS", "MASTER_CREDENTIALS_CONTENT",
                       "MASTER_MESOS_AUTHENTICATE_FRAMEWORKS",
                       "MASTER_MESOS_AUTHENTICATE_HTTP_FRAMEWORKS",
                       "MASTER_MESOS_HTTP_FRAMEWORK_AUTHENTICATORS",
                       "MASTER_MESOS_AUTHENTICATE_AGENTS",
                       "MASTER_MESOS_AUTHENTICATE_HTTP_READONLY",
                       "MASTER_MESOS_AUTHENTICATE_HTTP_READWRITE",
                       "MASTER_MESOS_REGISTRY_FETCH_TIMEOUT",
                       "MASTER_MESOS_REGISTRY_STORE_TIMEOUT",
                       "MASTER_MESOS_LOGBUFSECS", "MASTER_MESOS_LOGGING_LEVEL",
                       "MASTER_MESOS_LOG_AUTO_INITIALIZE",
                       "MASTER_MESOS_OFFER_TIMEOUT",
                       "MASTER_MESSOS_MAX_COMPLETED_FRAMEWORKS",
                       "MASTER_MESOS_MAX_COMPLETED_TASKS_PER_FRAMEWORK",
                       "MASTER_MESOS_REGISTRY", "MASTER_MESOS_ROOT_SUBMISSIONS",
                       "MASTER_MESOS_AGENT_PING_TIMEOUT",
                       "MASTER_MESOS_MAX_AGENT_PING_TIMEOUTS",
                       "MASTER_MESOS_AGENT_REREGISTER_TIMEOUT",
                       "MASTER_MESOS_ZK_SESSION_TIMEOUT",
                       "MASTER_MESOS_ALLOCATION_INTERVAL",
                       "MASTER_MESOS_LOG_DIR",
                       "MASTER_MESOS_AGENT_REMOVAL_RATE_LIMIT",
                       "MASTER_MESOS_RECOVERY_AGENT_REMOVAL_LIMIT",
                       "MASTER_MESOS_WHITELIST",
                       "MASTER_WHITELIST_CONTENT"]

MASTER_UNIQUE_KEYS = []

AGENT_DEFAULT_KEYS = ["AGENT_MESOS_MASTER", "AGENT_MESOS_PORT",
                      "AGENT_MESOS_WORK_DIR", "AGENT_MESOS_CONTAINERIZERS",
                      "AGENT_MESOS_STRICT", "AGENT_MESOS_GC_DELAY",
                      "AGENT_MESOS_GC_DISK_HEADROOM",
                      "AGENT_MESOS_DISK_WATCH_INTERVAL",
                      "AGENT_MESOS_EXECUTOR_ENVIRONMENT_VARIABLES",
                      "AGENT_EXECUTOR_ENVIRONMENT_VARIABLES_CONTENT",
                      "AGENT_MESOS_RESOURCES",
                      "AGENT_MESOS_DOCKER_STOP_TIMEOUT",
                      "AGENT_MESOS_CGROUPS_LIMIT_SWAP",
                      "AGENT_MESOS_CGROUPS_ENABLE_CFS",
                      "AGENT_MESOS_DOCKER_REMOVE_DELAY",
                      "AGENT_MESOS_EXECUTOR_REGISTRATION_TIMEOUT",
                      "AGENT_MESOS_RECOVERY_TIMEOUT",
                      "AGENT_MESOS_RECOVER",
                      "AGENT_MESOS_DOCKER_KILL_ORPHANS",
                      "AGENT_MESOS_OVERSUBSCRIBED_RESOURCES_INTERVAL",
                      "AGENT_MESOS_EXECUTOR_SHUTDOWN_GRACE_PERIOD",
                      "AGENT_MESOS_CONTAINER_LOGGER",
                      "AGENT_MESOS_LOG_DIR",
                      "AGENT_MESOS_MODULES_DIR",
                      "AGENT_MESOS_CREDENTIAL",
                      "AGENT_MESOS_CREDENTIAL_CONTENT",
                      "AGENT_MESOS_ATTRIBUTES",
                      "DOCKER_STORAGE_DRIVER", "DOCKER_STORAGE_OPTS",
                      "DOCKER_DNS", "DOCKER_DNS_SEARCH",
                      "DOCKER_PIDFILE", "DOCKER_GRAPH", "DOCKER_GROUP",
                      "DOCKER_MAX_CONCURRENT_DOWNLOADS",
                      "DOCKER_MAX_CONCURRENT_UPLOADS",
                      "DOCKER_HOSTS", "DOCKER_LOG_LEVEL",
                      "DOCKER_CGROUP_PARENT", "DOCKER_LOG_DRIVER",
                      "DOCKER_LOG_OPTS", "DOCKER_RAW_LOGS", "DOCKER_BRIDGE",
                      "DOCKER_IPTABLES", "DOCKER_IP_FORWARD",
                      "DOCKER_IP_MASQ", "DOCKER_USERLAND_PROXY",
                      "DOCKER_IP", "DOCKER_ICC", "DOCKER_EXEC_ROOT",
                      "DOCKER_USERNS_REMAP", "DOCKER_DEFAULT_RUNTIME",
                      "DOCKER_OOM_SCORE_ADJUST", "DOCKER_REGISTRY_MIRRORS",
                      "DOCKER_INSECURE_REGISTRIES",
                      "DOCKER_DISABLE_LEGACY_REGISTRY"]

AGENT_UNIQUE_KEYS = ["DOCKER_FIXED_CIDR"]

