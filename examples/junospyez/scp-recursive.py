from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP 

dev = Device(host='vsrx3', user='netauto')
dev.open()

with SCP(dev, progress=True) as scp:
        scp.get('/var/tmp/rtsdb', recursive=True)

dev.close()
