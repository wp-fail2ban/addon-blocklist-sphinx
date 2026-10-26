.. _about:

About Blocklist
===============

WP fail2ban Blocklist lets participating sites benefit from attacks observed
across the Blocklist Network Service (BNS), so a host can ban a selected
address before that address attacks the local site. Once connected, the
exchange is automatic and normally needs little operator attention.

The add-on supplies BNS with the time, resolved source address, and event type
for selected security events observed by WP fail2ban. BNS analyses data from
participating sites and returns selected IPv4 and IPv6 addresses. A returned
address is acquired intelligence: it does not establish that the address has
contacted this site or that this site has independently observed an attack.
That distinction matters when other collaborative blocklists are configured;
see :ref:`configuration_coexistence`.

For each accepted address, the add-on writes an immediate-block message to
syslog. It does not keep a local denylist or intercept each WordPress request
to test list membership. An installed fail2ban filter can match the message, a
jail can invoke a local ban action, and the host firewall can then reject later
traffic from the address. The message alone does not prove that any of those
later stages happened.

This keeps the normal WP fail2ban boundary intact: WordPress provides the
security context and messages, while the host administrator controls the
privileged fail2ban and firewall configuration. The main WP fail2ban manual's
:ref:`logging model <wp-fail2ban:operating_logging>` explains that general
message-to-ban path.
