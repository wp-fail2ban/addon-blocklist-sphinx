.. _defines:

======================
``define()`` constants
======================

These constants provide fixed configuration in ``wp-config.php``.
:ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_ENABLED` locks the shared enable option used
by QuickStart and the Blocklist settings tab. For the three Config-backed
controls (Ignore IPs, Custom Jail, and Blocklist facility), a constant
overrides any saved WP fail2ban 6 Premium setting; WP fail2ban Free displays
those effective values but does not save changes. The two debug controls are
constants only.

.. toctree::
   :maxdepth: 1

   defines/constants/WP_FAIL2BAN_ADDON_BLOCKLIST_ENABLED
   defines/constants/WP_FAIL2BAN_ADDON_BLOCKLIST_IGNORE_IPS
   defines/constants/WP_FAIL2BAN_ADDON_BLOCKLIST_CUSTOM_JAIL
   defines/constants/WP_FAIL2BAN_ADDON_BLOCKLIST_LOG
   defines/constants/WP_FAIL2BAN_ADDON_BLOCKLIST_DEBUG
   defines/constants/WP_FAIL2BAN_ADDON_BLOCKLIST_DEBUG_TRY_ALL_KEYS
