.. _configuration__fail2ban:

fail2ban
--------

Standard Filters
^^^^^^^^^^^^^^^^

The filter files included should not be edited; there are no user-serviceable parts inside.

Typical Settings
""""""""""""""""

If you are using the typical settings for *WPf2b* the Blocklist add-on will work without further configuration.

Custom Jail
"""""""""""

#. Copy ``wpf2b-blocklist-hard.conf`` to your ``fail2ban/filters.d`` directory
#. Create a new file in ``fail2ban/jail.d`` called ``wpf2b-blocklist.conf``

.. code-block:: ini

  [wpf2b-blocklist-hard]
  enabled = true
  filter = wpf2b-blocklist-hard
  logpath = /var/log/auth.log
  maxretry = 1
  port = http,https

.. note::

   Make sure you change ``logpath`` to the correct log for your OS. If your OS uses `systemd` it may be simpler and/or easier to install a real syslog service first.

2. Reload or restart ``fail2ban``
