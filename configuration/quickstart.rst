.. _configuration_quickstart:

QuickStart card
===============

With WP fail2ban 6.3, Blocklist adds a QuickStart card to the parent plugin's
settings. The card turns Blocklist participation on or off by saving the
``wpf2b_addon_blocklist_enabled`` option. Participation defaults to enabled.

Freemius remains a separate requirement. BNS needs that connection for site
identity and the shared secret used to authenticate service requests. Connect
from the Blocklist add-on page under WP fail2ban, as in :ref:`installation`. A
paid licence is not required merely to make the connection. When Freemius is
connected but the card is off, the add-on registers no Blocklist hooks.

The same enable control appears on the Blocklist settings tab while advanced
settings are enabled in the parent plugin. A PHP constant
:ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_ENABLED` takes priority over the saved option
and locks both controls. See the main WP fail2ban
:ref:`QuickStart <wp-fail2ban:configuration_quickstart>` for how that interface
relates to Advanced settings.

.. seealso::
   * :ref:`installation`
   * :ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_ENABLED`
   * :ref:`configuration_service_connectivity`
   * :ref:`defines`
