.. _operating:

Operating Blocklist
===================

Blocklist normally runs without routine intervention. Its Dashboard widgets
show when BNS last collected local events with GET, when it last delivered
addresses with POST, lifetime request and entry counts, and queued local events.
An advancing GET or POST time confirms service communication; an entry count
does not by itself confirm a syslog write, filter match, or ban.

Recognising a delivered address
-------------------------------

For each accepted address in a BNS POST, the add-on writes one
``Immediately block connections`` record at notice priority. In shared mode it
uses the ordinary hard-message format and ``WP_FAIL2BAN_AUTH_LOG``. In custom
mode it adds the ``(WPf2b++/blocklist)`` prefix and uses
:ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_LOG`. WP fail2ban Premium also stores a
structured event, but fail2ban does not read that event store.

The add-on's :ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_IGNORE_IPS` setting removes
configured addresses from a delivered batch before those outputs. Built-in
non-public and special-purpose ranges are also excluded. The add-on does not
retain the returned addresses as a local list.

.. _operating_verify_enforcement:

Verifying enforcement
---------------------

Trace an accepted address through the host in order:

1. Find the exact Blocklist message in the syslog file or journal.
2. Test that source against the installed filter, for example::

      fail2ban-regex /path/to/wordpress.log /etc/fail2ban/filter.d/wpf2b-blocklist-hard.conf

3. Inspect the live jail with ``fail2ban-client status
   wpf2b-blocklist-hard`` and confirm that it counted and banned the address.
4. Inspect the configured action list and the host firewall with the host's
   administrative tools.

Each checkpoint proves only its own stage. A syslog record does not prove a
filter match, a filter match does not prove that the jail invoked an action,
and a listed fail2ban ban does not replace checking the intended firewall
state. The main manual's :ref:`fail2ban configuration
<wp-fail2ban:configuration__fail2ban>` gives the general verification model.

.. _operating_diagnose_connectivity:

Diagnosing service communication
--------------------------------

When GET and POST times stop advancing, first check the Blocklist status widget
and WordPress Site Health. A missing install key points to the Freemius
connection. A missing route, open unsigned route, or rejected signed request
points to REST routing or authentication. An inconclusive loopback result means
that this server could not test its own URL; check the endpoint from outside
before concluding that BNS is also blocked.

Then review the narrowly scoped REST allowance in
:ref:`configuration_service_connectivity`, the WordPress and proxy logs, and
server clock accuracy. Do not disable the whole WAF or REST policy as a
diagnostic shortcut.

Unavailable or stale service data
---------------------------------

If BNS cannot reach the site, it cannot collect new local events or deliver
new addresses. Free continues to queue local events, up to 16,384 IPv4 records
and 16,384 IPv6 records; a successful normal GET drains those queues. Premium
uses WP fail2ban's event store, and its normal retention policy governs the records.
Existing fail2ban bans continue until their jail ``bantime`` expires or an
administrator removes them. There is no fallback downloaded list or local
request-matching mode.

The GET and POST counters are cumulative. The local health-probe result is
cached for one hour. Syslog or journal retention, installed-filter updates,
and live ban expiry remain host responsibilities; the add-on does not create a
second archive of returned addresses.
