import subprocess
import platform
import sys
import re

HEADERS_SIZE = 28

if len(sys.argv) < 2:
    print('No host')
    exit(1)
host = sys.argv[1]
HOST_PATTERN = re.compile(
    r"^(https?:\/\/)?((?:[-a-z0-9._~!$&\'()*+,;=]|%[0-9a-f]{2})+(?::(?:[-a-z0-9._~!$&\'()*+,;=]|%[0-9a-f]{2})+)?@)?(?:((?:(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5]))|((?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z][a-z0-9-]*[a-z0-9]))(:\d+)?((?:\/(?:[-a-z0-9._~!$&\'()*+,;=:@]|%[0-9a-f]{2})+)*\/?)(\?(?:[-a-z0-9._~!$&\'()*+,;=:@\/?]|%[0-9a-f]{2})*)?(\#(?:[-a-z0-9._~!$&\'()*+,;=:@\/?]|%[0-9a-f]{2})*)?$"
)

if not HOST_PATTERN.match(host):
    print(f"Bad host format for {host}")
    exit(1)


print(f'Host: {host}')

IS_ICMP_DISABLE = subprocess.run(
    ["cat", "/proc/sys/net/ipv4/icmp_echo_ignore_all"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True,
)

if IS_ICMP_DISABLE.stdout == 1:
    print(
        "ISCMP is disabled. Change 0 to 1 in /proc/sys/net/ipv4/icmp_echo_ignore_all if you want to enable it."
    )
    exit(1)

current_os = platform.system().lower()


def ping(host_to_ping: str, number_of_bytes: int, os: str) -> bool:
    if os == 'darwin':
        cmd = f'ping -D -s {number_of_bytes} {host_to_ping} -c 1 -W 3000'
    else:
        cmd = f'ping -M do -s {number_of_bytes} {host_to_ping} -c 1 -W 3'
    cmd = cmd.split(' ')
    result = subprocess.run(cmd, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, universal_newlines=True)
    return result.returncode == 0


if not ping(host, number_of_bytes=0, os=current_os):
    print(f'host {host} is unavailable')
    exit(0)

l, r = 0, 1502 - HEADERS_SIZE
while l + 1 < r:
    mid = (l + r) // 2
    if ping(host, number_of_bytes=mid, os=current_os):
        print(f'MTU {mid} is ok')
        l = mid
    else:
        print(f'MTU {mid} bad')
        r = mid

print(f'minimal MTU for {host} = {l}')
