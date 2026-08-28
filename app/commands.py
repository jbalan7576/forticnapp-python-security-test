import os


def ping_host(host):
    # INTENTIONALLY VULNERABLE: CWE-78 OS Command Injection
    command = "ping -n 2 " + host

    return os.popen(command).read()