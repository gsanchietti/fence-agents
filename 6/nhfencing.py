import subprocess
import time


def sleep_priority():
	"""Read node id from cluster status and sleep an amount of seconds according to id: 
	higher id, more time to sleep.
	This function avoid concurrent fencing when using fencing device which do not handle concurrency.
	Node with id = 1 will not sleep at all 
	"""
	TIMEOUT=5
        process = subprocess.Popen(['/usr/sbin/cman_tool','status'], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out,err) = process.communicate()
	if process.returncode != 0:
		return;

        id = 0;
        for l in out.splitlines():
                if l.find('Node ID') == 0:
                        tmp = l.split(':')
                        id = int(tmp[1].rstrip().lstrip());
        time.sleep((id-1)*TIMEOUT)

