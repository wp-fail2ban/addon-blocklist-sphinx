.. _configuration__syslog:

Syslog
------

If you are using a custom jail is it *strongly* recommended that you also use one of the ``local0..7`` facilities.

.. _configuration__syslog__local_facility:

Using a local0..7 Facility
^^^^^^^^^^^^^^^^^^^^^^^^^^

The BNS sends the list of IPs to block as a single batch, and each IP address results in one line written to ``syslog``. With some plans sending as many as 1000 IPs the default log (``/var/log/auth.log``) can be swamped with BNS entries, making it difficult to use for its usual purposes.

To prevent this you should configure the Blocklist to use one of the local facilities, for example, ``local3``.

Configuring ``syslogd``
"""""""""""""""""""""""

It is assumed that you have configured the ``syslogd`` variant you use to write ``local3`` to ``/var/log/wpf2b-block.log``.

Configuring WP fail2ban
^^^^^^^^^^^^^^^^^^^^^^^

Add the following to your ``wp-config.php`` file:

.. code-block:: php

  /**
   * The blocklist messages use the "block" class
   */
  define('WP_FAIL2BAN_PLUGIN_LOG_BLOCK', true);

  /**
   * Use the custom facility we configured earlier for the block messages.
   *
   * Be sure to change this to match the syslog facility you're using.
   */
  define('WP_FAIL2BAN_PLUGIN_BLOCK_LOG', LOG_LOCAL3);

Update your Blocklist jail to use the new log file:

.. code-block:: ini

  [wpf2b-blocklist-hard]
  enabled = true
  filter = wpf2b-blocklist-hard
  logpath = /var/log/wpf2b-block.log
  maxretry = 1
  bantime = 86400

Reload or restart ``fail2ban`` and check everything is working after the next BNS update.
