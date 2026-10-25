.. _configuration__fail2ban:
.. _configuration_fail2ban:

Dedicated fail2ban jail
=======================

A dedicated jail gives Blocklist-derived messages their own action list. Use
it whenever an ordinary WP fail2ban jail could report its matches to another
service. Blocklist can otherwise use the standard hard jail, but the dedicated
arrangement is the clearest way to preserve evidence provenance.

.. _configuration__fail2ban__custom_jail:
.. _custom-jail:

Enable the distinct message
---------------------------

Add the following to ``wp-config.php`` before WordPress's "stop editing" line:

.. code-block:: php

   define('WP_FAIL2BAN_ADDON_BLOCKLIST_CUSTOM_JAIL', true);

The add-on then prefixes delivered-address messages as follows::

   (WPf2b++/blocklist) Immediately block connections from 192.0.2.10

When WP fail2ban uses inline-host formatting, ``on example.com`` appears before
``from``. The shipped ``wpf2b-blocklist-hard`` filter matches both forms. The
main ``wordpress-hard`` filter does not match this prefixed message, which
keeps it out of ordinary reporting jails that use the unmodified core filter.

Install the filter and jail
---------------------------

Copy ``filters.d/wpf2b-blocklist-hard.conf`` from the installed add-on to the
host's fail2ban ``filter.d`` directory. WordPress cannot maintain this
privileged copy; compare and update it after relevant add-on upgrades.

Create a jail such as ``jail.d/wpf2b-blocklist.conf``. Replace ``logpath`` with
the file that actually receives the selected facility:

.. code-block:: ini

   [wpf2b-blocklist-hard]
   enabled = true
   filter = wpf2b-blocklist-hard
   logpath = /var/log/auth.log
   port = http,https
   maxretry = 1
   bantime = 3600
   action = %(action_)s

In fail2ban's shipped configuration, ``%(action_)s`` is the simplest ban-only
action. Check the effective action list on this host, particularly if
``[DEFAULT]`` or the interpolation has been customised. It must omit
``blocklist_de``, ``abuseipdb``, XARF, and any other script or API action that
reports the address externally. The host's firewall backend, ports, and ban
duration remain local policy.

``maxretry = 1`` is essential because each delivered address represents an
immediate local-ban decision. Site Health can find a matching filter and check
this threshold, but it does not inspect the action list, the freshness of the
installed filter, or firewall state.

For a systemd journal jail, use the setup in the main manual's
:ref:`fail2ban configuration <wp-fail2ban:configuration__fail2ban>`. The
shipped filter selects ``SYSLOG_IDENTIFIER=wordpress``; enable WP fail2ban's
inline-host format so the identifier is stable, or deliberately adjust the
installed filter if the host uses the short ``wp`` identifier.

Validate and reload fail2ban after installing or changing the files::

   fail2ban-client -t
   fail2ban-client reload

Optional facility and destination
---------------------------------

With the custom message enabled, :ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_LOG` can
send Blocklist messages through a separate syslog facility. Routing, for
example, ``LOG_LOCAL3`` to a dedicated log can make bursts of delivered
addresses easier to inspect and gives the jail a narrow source to read.

The host logging service must route that facility, and the jail's ``logpath``
must read the resulting destination. Selecting a facility without both steps
can leave the jail reading the wrong source. A separate destination improves
visibility and routing; the dedicated filter and ban-only jail actions provide
the safety boundary.

Finish with :ref:`operating_verify_enforcement` to test each host-side stage.
