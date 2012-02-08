Description
======================
A couple of fence agents for Red Hat Cluster.

All listed models do not correctly handle concurrent connections.
To avoid a mutual fencing, we add a little delay to each fence call: 
every node involved will sleep for (node_id - 1)*5 seconds. 
So, for example, node with id 3 will wait for 15 seconds and node with id 1
will not wait at all.


Supported devices
======================

Currently supported models:
* Aviosys IP9258 (fence_ip9258)
* EpowerSwitch 4m (fence_eps_4m)


Tested on:
* CentOS 5.3
* CentOS 6.2


Installation
======================

#### Centos 5.3
Copy all files from directory *5* to directory */usr/lib/fence*

#### Centos 6.2
Copy all files from directory *6* to directory */usr/share/fence*


License
======================

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
