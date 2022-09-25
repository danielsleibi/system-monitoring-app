import psutil
from modules.log_wrap import *


@wrap(entering, exiting)
def get_cpu_util():
    return {"utilization": psutil.cpu_percent()}


@wrap(entering, exiting)
def get_disk_usage():
    total = int()
    used = int()
    for disk in psutil.disk_partitions():
        if disk.fstype:
            total += int(psutil.disk_usage(disk.mountpoint).total)
            used += int(psutil.disk_usage(disk.mountpoint).used)
    total = round(total / (1024.0 ** 3), 4)
    used = round(used / (1024.0 ** 3), 4)
    return {"total": total, "used": used}


@wrap(entering, exiting)
def get_memory_usage():
    total = psutil.virtual_memory()[0]
    used = psutil.virtual_memory()[1]
    total = round(total / (1024.0 ** 3), 4)
    used = round(used / (1024.0 ** 3), 4)
    return {"total": total, "used": used}
