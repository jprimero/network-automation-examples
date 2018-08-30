from jnpr.junos.utils.start_shell import StartShell
from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP 

dev = Device(host='vsrx3', user='netauto')
dev.open()

shell = StartShell(dev)
shell.open()
shell.run('cli -c "request support information | save /var/tmp/rsi.txt"')

with SCP(dev) as scp:
        scp.get('/var/tmp/rsi.txt')

shell.close()
