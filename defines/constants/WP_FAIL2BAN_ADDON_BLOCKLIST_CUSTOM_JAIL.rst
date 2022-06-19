.. _WP_FAIL2BAN_ADDON_BLOCKLIST_CUSTOM_JAIL:

.. role:: php(code)
  :language: php

WP_FAIL2BAN_ADDON_BLOCKLIST_CUSTOM_JAIL
---------------------------------------

.. versionadded:: 1.0.0

----

Changes the log format to match entries in ``wpf2b-blocklist-hard.conf`` instead of ``wordpress-hard.conf``.

If you cannot set ``maxretry = 1`` in your ``wordpress-hard`` jail you must set this and create a custom jail.

.. code-block:: php

  define('WP_FAIL2BAN_ADDON_BLOCKLIST_CUSTOM_JAIL', true);

**Default:** :php:`false`

.. seealso::
  :ref:`configuration__fail2ban__custom_jail`
