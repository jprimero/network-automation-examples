from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP
import datetime

def log(dev, report):
    with open("scp.log", "a") as log:
        timestamp = datetime.datetime.now()
        format_time = timestamp.strftime("%b %d %X")
        log.write(str(format_time) + ' '  + dev.hostname + ': ' + report + "\n")

dev = Device(host='vsrx3', user='netauto')
dev.open()

with SCP(dev, progress=log) as scp:
    scp.get("/var/log/messages", local_path="logs/" + dev.hostname + "-messages")

dev.close()
