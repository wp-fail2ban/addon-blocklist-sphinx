.. _WP_FAIL2BAN_ADDON_BLOCKLIST_IGNORE_IPS:

.. role:: php(code)
   :class: highlight
   :language: php

WP_FAIL2BAN_ADDON_BLOCKLIST_IGNORE_IPS
--------------------------------------

.. versionadded:: 1.0.0
.. versionchanged:: 2.0.0
   Entries can include IPv6 addresses.

----

A list of IP addresses to ignore if they appear in a Blocklist update.

.. code-block:: php

   define('WP_FAIL2BAN_ADDON_BLOCKLIST_IGNORE_IPS', [
      '1.2.3.4',
      '2.3.4.5/24'
   ]);

**Default:** :php:`[]` *(empty list)*

Commonly used when accessing a site via shared access (e.g. Campus proxy, 3rd-party VPN, etc).

.. note::
   IPv6 addresses require `WP fail2ban` version 5 or later.

.. tip::
   If you have whitelisted IPs in ``fail2ban`` because of shared access you should also add them here.

.. seealso::
   :ref:`WP_FAIL2BAN_PROXIES <wp-fail2ban:WP_FAIL2BAN_PROXIES>` has the same syntax.

