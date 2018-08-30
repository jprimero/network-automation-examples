from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP

dev = Device(host='vsrx3', user='netauto')
dev.open()

with SCP(dev, progress=True) as scp:
        scp.get("/var/log/messages", local_path="logs/" + dev.hostname + "-messages")

dev.close()
