Setting up and Running EV3Sim
=============================

Installation
------------

Windows Executable
^^^^^^^^^^^^^^^^^^

By far the easiest way to install and use EV3Sim if you have a windows computer is using the one-click installer available on the `releases page on github`_.

.. image:: images/releases.jpg
  :width: 600
  :alt: An image of the releases page on github.

Simply download the asset file named ``one_click.exe``, and follow the prompts to get the executable installed.

Windows Bundle
^^^^^^^^^^^^^^

Another way to get EV3Sim is by downloading the package from the same releases page (``windows_package``). Simply unzip and place this folder in a program directory such as ``Program Files`` or ``Applications``.
In future we aim to also support this method for Mac/Linux, but currently there's not much point to. Let us now if you'd prefer this!

Pip install
^^^^^^^^^^^

If installing via this method, EV3sim requires Python 3.7+ to be installed on your system. If you don't already have Python installed, you can download it from https://www.python.org/ .

You can install this package using pip as follows:

.. code-block:: bash

    python -m pip install -U ev3sim

(This command also updates EV3Sim if you already have it installed.)

Updating
--------

Windows Executable
^^^^^^^^^^^^^^^^^^

If a new one-click installer comes out, you can simply run this and it will update your existing installation of EV3Sim. Your workspace and any settings will remain the same, unless some breaking changes are required.

Pip install
^^^^^^^^^^^

As with any other pip package, you can update ev3sim with the same command you used to install it, passing in the `-U` flag:

.. code-block:: bash

    python -m pip install -U ev3sim

Starting EV3Sim
---------------

Depending on you installation method, you might start EV3Sim differently:

* If you installed on windows with the one click install, EV3Sim should be in your start menu.
* If using the bundle installation, you can go into the folder and run ``ev3sim`` or ``ev3sim.exe``.
* If installed via pip, then run ``ev3sim`` in the command line.

The first time you run EV3Sim, you will be prompted with a dialog, asking you to specify a *workspace folder*.
A workspace folder is where all of your local bots, code and simulation presets are stored.

We'd recommend creating a new folder on your Desktop to be your workspace folder, for easy access.

Running EV3Sim
--------------

Once your workspace folder has been set, you can start using the application.

* The ``Simulate`` tab allows you to run simulations, and select simulations to edit the bots or settings.
* The ``Bots`` tab allows you to edit and create bots to use in the simulation.
* The ``Settings`` tab allows you to change a few configurations when running EV3Sim.


Further Information on installing
---------------------------------

Windows
^^^^^^^


Command not recognised
""""""""""""""""""""""

.. code-block:: batch

    'pip' is not recognized as an internal or external command, operable program, or batch file

Make sure you install python with the "Add python to PATH" option selected. This makes sure that the windows command line will understand the python and pip commands. For more information, see https://docs.python.org/3/using/windows.html#installation-steps


EV3Sim runs, but no pygame window is created
""""""""""""""""""""""""""""""""""""""""""""

This is a known issue with pygame. A possible cause is not having the English (US) Language pack in windows installed. This should install itself after a few minutes, once you've installed the package, but if that doesn't occur, you may wish to try manually installing it.

Unix
^^^^


Dependancy or binary package errors
"""""""""""""""""""""""""""""""""""

Pygame requires binary dependencies that aren't always installed by default.

Debian/Ubuntu/Mint


``sudo apt-get install python3-pygame``

Redhat/CentOS

``sudo yum install python3-pygame``

Arch 

``sudo pacman -S python-pygame``

.. _releases page on github: https://github.com/MelbourneHighSchoolRobotics/ev3sim/releases
