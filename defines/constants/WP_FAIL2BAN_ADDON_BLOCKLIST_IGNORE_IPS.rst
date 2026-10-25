.. _WP_FAIL2BAN_ADDON_BLOCKLIST_IGNORE_IPS:

.. role:: php(code)
   :language: php

WP_FAIL2BAN_ADDON_BLOCKLIST_IGNORE_IPS
--------------------------------------

.. rubric:: Exclude protected addresses from BNS deliveries.

----

Lists full IPv4 or IPv6 addresses and CIDR ranges that the add-on must remove
from a service-supplied POST before it writes a Blocklist syslog record or
Premium event. Use it, for example, to protect a required upstream service
whose shared address must never become a local ban request.

This control applies only to addresses received from BNS. It does not stop a
locally observed WordPress event from being supplied to BNS. Use WP fail2ban's
own ignore-address configuration for that inbound-request case, and retain
fail2ban's ``ignoreip`` as an independent host-side safeguard.

Supply an array of complete addresses or ranges. Abbreviated IPv4 CIDR such as
``127/8`` is not supported.

.. code-block:: php
   :caption: Example: Exclude two protected networks

   define('WP_FAIL2BAN_ADDON_BLOCKLIST_IGNORE_IPS', [
       '192.0.2.20',
       '2001:db8:1234::/48',
   ]);

**Accepted values:** an array of full IPv4 or IPv6 addresses and CIDR ranges

**Default:** :php:`[]` (empty list)

Built-in non-public, loopback, link-local, documentation, multicast, and other
special-purpose ranges are excluded independently of this setting. A PHP
constant takes priority over an editable WP fail2ban 6 Premium setting.

.. seealso::
   * :ref:`operating`
   * :ref:`WP_FAIL2BAN_PROXIES <wp-fail2ban:WP_FAIL2BAN_PROXIES>` for the main
     plugin's separate client-address configuration

.. rubric:: History
.. versionadded:: 1.0.0
.. versionchanged:: 2.0.0
   Added IPv6 addresses and ranges.
