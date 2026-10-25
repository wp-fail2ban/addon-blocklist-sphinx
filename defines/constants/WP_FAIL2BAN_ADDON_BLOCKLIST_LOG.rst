.. _WP_FAIL2BAN_ADDON_BLOCKLIST_LOG:

.. role:: php(code)
   :language: php

WP_FAIL2BAN_ADDON_BLOCKLIST_LOG
-------------------------------

.. rubric:: Select the syslog facility for dedicated Blocklist messages.

----

Sets the facility used for service-delivered addresses when
:ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_CUSTOM_JAIL` is :php:`true`. The host logging
service must route the selected facility, and the dedicated jail must read the
resulting file or journal.

.. code-block:: php
   :caption: Example: Use a local facility

   define('WP_FAIL2BAN_ADDON_BLOCKLIST_LOG', LOG_LOCAL3);

**Accepted values:** ``LOG_AUTH``, ``LOG_AUTHPRIV``, ``LOG_CRON``,
``LOG_DAEMON``, ``LOG_KERN``, ``LOG_LOCAL0`` through ``LOG_LOCAL7``,
``LOG_LPR``, ``LOG_MAIL``, ``LOG_NEWS``, ``LOG_SYSLOG``, ``LOG_USER``, or
``LOG_UUCP``

**Default:** with WP fail2ban 6, the current value of the parent plugin's
:php:`WPF2B_FACILITY_LOG_USER`; with WP fail2ban 5, :php:`LOG_USER`

The setting has no effect while the custom-jail control is :php:`false`; shared
mode continues to use ``WP_FAIL2BAN_AUTH_LOG``. A separate facility can improve
routing and visibility, but it does not isolate jail actions. A PHP constant
takes priority over an editable WP fail2ban 6 Premium setting.

.. seealso::
   * :ref:`configuration_fail2ban`
   * :ref:`WP_FAIL2BAN_AUTH_LOG <wp-fail2ban:WP_FAIL2BAN_AUTH_LOG>`

.. rubric:: History
.. versionadded:: 1.0.0
.. versionchanged:: 3.0.0
   Applied the setting to custom-jail POST messages and made the default follow
   the applicable parent-version adapter.
