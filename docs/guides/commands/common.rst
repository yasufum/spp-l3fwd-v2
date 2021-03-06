..  SPDX-License-Identifier: BSD-3-Clause
    Copyright(c) 2010-2014 Intel Corporation

Common Commands
===============

status
------

Show the number of connected primary and secondary processes.
It also show a list of secondary IDs

.. code-block:: console

    spp > status
    Soft Patch Panel Status :
    primary: 1
    secondary count: 2
    Connected secondary id: 1
    Connected secondary id: 2


playback
--------

Restore network configuration from a recipe file which defines a set
of SPP commands.
You can prepare a recipe file by using ``record`` command or editing
file by hand.

It is recommended to use extension ``.rcp`` to be self-sxplanatory as
a recipe, although you can use any of extensions such as ``.txt`` or
``.log``.

.. code-block:: console

    spp > playback /path/to/my.rcp


record
------

Start recording user's input and create a recipe file for loading
from ``playback`` commnad.
Recording recipe is stopped by executing ``exit`` or ``playback``
command.

.. code-block:: console

    spp > record /path/to/my.rcp

.. note::

    It is not supported to stop recording without ``exit`` or ``playback``
    command.
    It is planned to support ``stop`` command for stopping record in
    next relase.


history
-------

Show command history. Command history is recorded in a file named
``$HOME/.spp_history``. It does not add some command which are no
meaning for history, ``bye``, ``exit``, ``history`` and ``redo``.

.. code-block:: console

    spp > history
      1  ls
      2  cat file.txt


redo
----

Execute command of index of history.

.. code-block:: console

    spp > redo 5  # exec 5th command in the history


server
------

Show a list of SPP REST API servers and switch to control for multiple
nodes.

Show all of registered REST API servers. Run ``server list`` or simply
``server``.

.. code-block:: console

    spp > server
      1: 192.168.1.101:7777 *
      2: 192.168.1.102:7777

    spp > server list  # same as above
      1: 192.168.1.101:7777 *
      2: 192.168.1.102:7777

Switch to other server with index number displayed in ``server list``.

.. code-block:: console

    spp > server 2
    Switch spp-ctl to "2: 192.168.1.102:7777".

pwd
---

Show current path.

.. code-block:: console

    spp> pwd
    /path/to/curdir


cd
--

Change current directory.

.. code-block:: console

    spp> cd /path/to/dir


ls
--

Show a list of directory contents.

.. code-block:: console

    spp> ls /path/to/dir


mkdir
-----

Make a directory.

.. code-block:: console

    spp> mkdir /path/to/dir


cat
---

Show contents of a file.

.. code-block:: console

    spp> cat /path/to/file


less
----

Show contents of a file.

.. code-block:: console

    spp> less /path/to/file


bye
---

``bye`` command is for terminating SPP processes.
It supports two types of termination as sub commands.

  - sec
  - all

First one is for terminating only secondary processes at once.

.. code-block:: console

    spp > bye sec
    closing:<socket._socketobject object at 0x105750910>
    closing:<socket._socketobject object at 0x105750a60>

Second one is for all SPP processes other than controller.

.. code-block:: console

    spp > bye all
    closing:<socket._socketobject object at 0x10bd95910>
    closing:<socket._socketobject object at 0x10bd95a60>
    closing:('127.0.0.1', 53620)


exit
----

Same as ``bye`` command but just for terminating SPP controller and
not for other processes.

.. code-block:: console

    spp > exit
    Thank you for using Soft Patch Panel


help
----

Show help message for SPP commands.

.. code-block:: console

    spp > help

    Documented commands (type help <topic>):
    ========================================
    bye  cd    help  load_cmd  mkdir     pri  record  status  topo_subgraph
    cat  exit  less  ls        playback  pwd  sec     topo

    spp > help status
    Display status info of SPP processes

        spp > status

    spp > help sec
    Send command to secondary process

        SPP secondary process is specified with secondary ID and takes
        sub commands.

        spp > sec 1;status
        spp > sec 1;add ring 0
        spp > sec 1;patch 0 2
