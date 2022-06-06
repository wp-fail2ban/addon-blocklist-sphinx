.. _WP_FAIL2BAN_ADDON_BLOCKLIST_LOG:

.. role:: php(code)
  :language: php

WP_FAIL2BAN_ADDON_BLOCKLIST_LOG
-------------------------------

.. versionadded:: 1.0.0

----

The syslog facility to use for a custom jail.

.. code-block:: php

   define('WP_FAIL2BAN_ADDON_BLOCKLIST_LOG', LOG_LOCAL7);

**Default:** :php:`LOG_AUTH` *or* :php:`LOG_AUTHPRIV`

.. seealso::
   * :ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_CUSTOM_JAIL`
   * :ref:`WP_FAIL2BAN_USE_AUTHPRIV <wp-fail2ban:WP_FAIL2BAN_USE_AUTHPRIV>`
