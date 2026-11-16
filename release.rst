.. _release:

===================
Release information
===================

WP fail2ban Blocklist 3.1.0
---------------------------

Version 3.1.0 adds an operator-facing enable switch for Blocklist participation,
separate from the Freemius connection that still gates whether the add-on can
run.

Reader-visible changes in this release include:

* QuickStart and the Blocklist settings **Enabled** control turn
  participation on or off (default enabled);
* :ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_ENABLED` locks that choice from
  ``wp-config.php``;
* with Freemius connected and participation off, Blocklist hooks, REST
  handlers, and Site Health tests stay off while the settings UI remains
  available.

WP fail2ban Blocklist 3.0.0
---------------------------

Version 3.0.0 updates the add-on for the supported WP fail2ban 5.x and 6.x
interfaces. On WP fail2ban 6, Premium operation uses the parent's structured
event store, while Free operation retains the add-on's bounded queues.

Reader-visible changes in this release include:

* Blocklist settings integrated with WP fail2ban 6, while PHP constants retain
  priority;
* signed status and local health checks, with Dashboard visibility of service
  contact and queued events;
* custom-jail messages routed through
  :ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_LOG`, while shared-jail messages continue
  to use the parent authentication facility.

Operators using the dedicated jail should compare the packaged hard filter
with the host-installed copy during the upgrade, validate fail2ban, and reload
it. The add-on does not update privileged host configuration itself.
