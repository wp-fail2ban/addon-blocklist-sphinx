.. _configuration:

=============
Configuration
=============

Configure Blocklist in the order that information moves through the system.
First ensure that BNS can reach the add-on's REST route. Then decide whether
any existing jail reports matches to another collaborative service. If it
does, isolate Blocklist-derived messages in a dedicated, ban-only jail before
enabling enforcement.

The add-on needs little routine tuning. Participation can be turned off from
QuickStart or the Blocklist settings tab, or locked with
:ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_ENABLED`. Its three Config-backed controls
can be fixed with PHP constants in ``wp-config.php``. With WP fail2ban 6
Premium, the Bronze plan or trial can instead save those controls in the
Blocklist settings; a PHP constant takes priority over a saved value. WP
fail2ban Free shows the effective values without making them editable. See the
individual :ref:`defines` pages for exact values and defaults.

.. toctree::
   :maxdepth: 1

   configuration/service-connectivity
   configuration/quickstart
   configuration/coexistence
   configuration/fail2ban
