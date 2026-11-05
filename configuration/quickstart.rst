.. _configuration_quickstart:

QuickStart card
===============

With WP fail2ban 6.3, Blocklist adds a QuickStart card to the parent plugin's
settings. The card is informational and locked: it reports whether this site
has connected to Freemius for Blocklist, and it cannot turn the add-on on or
off.

BNS needs that connection for site identity and the shared secret used to
authenticate service requests. Connect from the Blocklist add-on page under
WP fail2ban, as in :ref:`installation`. A paid licence is not required merely
to make the connection.

The Blocklist settings tab (Ignore IPs and Advanced options) appears only while
advanced settings are enabled in the parent plugin. See the main WP fail2ban
:ref:`QuickStart <wp-fail2ban:configuration_quickstart>` for how that interface
relates to Advanced settings.

This card changes no setting.

.. seealso::
   * :ref:`installation`
   * :ref:`configuration_service_connectivity`
   * :ref:`defines`
