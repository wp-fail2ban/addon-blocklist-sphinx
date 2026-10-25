.. _WP_FAIL2BAN_ADDON_BLOCKLIST_CUSTOM_JAIL:

.. role:: php(code)
   :language: php

WP_FAIL2BAN_ADDON_BLOCKLIST_CUSTOM_JAIL
---------------------------------------

.. rubric:: Route Blocklist messages to the dedicated filter format.

----

Set this to :php:`true` when Blocklist-derived addresses need a dedicated
fail2ban jail. The add-on prefixes each delivered-address message with
``(WPf2b++/blocklist)`` so ``wpf2b-blocklist-hard.conf`` matches it and the
main ``wordpress-hard.conf`` filter does not.

The setting also makes :ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_LOG` select the
message's syslog facility. It does not install the filter, create a jail,
choose its actions, or reload fail2ban.

.. code-block:: php
   :caption: Example: Enable the dedicated message format

   define('WP_FAIL2BAN_ADDON_BLOCKLIST_CUSTOM_JAIL', true);

**Accepted values:** :php:`true` or :php:`false`

**Default:** :php:`false`

With :php:`false`, the add-on writes the unprefixed hard message through
``WP_FAIL2BAN_AUTH_LOG`` for the main ``wordpress-hard`` filter. This is safe
only when the receiving jail's actions do not report Blocklist-derived matches
as new attacks. A PHP constant takes priority over an editable WP fail2ban 6
Premium setting.

.. seealso::
   * :ref:`configuration_coexistence`
   * :ref:`configuration_fail2ban`
   * :ref:`reference_filters`

.. rubric:: History
.. versionadded:: 1.0.0
