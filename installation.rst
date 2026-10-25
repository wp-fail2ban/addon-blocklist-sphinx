.. _installation:

Installation
============

Blocklist 3.0 requires WordPress 4.9 or later, PHP 7.4 or later, and an active
WP fail2ban 5.4 or later installation from the supported 5.x or 6.x series.
Both WP fail2ban Free and Premium are supported. On multisite, install and use
the add-on on the main site; subsites do not run the full Blocklist service.

Install and connect
-------------------

1. Install WP fail2ban and complete its syslog and fail2ban setup.
2. Install and activate WP fail2ban Blocklist in WordPress.
3. Connect the add-on to Freemius and allow the requested event-sharing
   permission. Blocklist uses the resulting site identity and shared secret
   to authenticate BNS requests. A paid licence is not required merely to make
   this connection.
4. Confirm that the site's REST and security layers permit BNS access as
   described in :ref:`configuration_service_connectivity`.
5. Review the actions on the jail that will receive Blocklist messages. If it
   reports matches to any third party, configure the dedicated ban-only jail
   in :ref:`configuration_fail2ban` before relying on Blocklist.

WordPress activation does not install privileged fail2ban configuration,
reload fail2ban, or change the host firewall. If the dedicated mode is needed,
a host administrator must install the shipped filter, create the jail,
validate its action list, and reload fail2ban.

First verification
------------------

Open the Blocklist Dashboard widgets and WordPress **Tools | Site Health**.
The add-on should have an install key, and its signed loopback authentication
check should succeed. A failed loopback is not conclusive evidence that BNS
cannot connect from outside, but a missing route or rejected signature gives a
specific problem to investigate.

After BNS next communicates, the Blocklist Summary shows the most recent GET
and POST times and entry counts. Those counters show that a handler ran; they
do not prove that a syslog message was matched or a ban was installed. Complete
the host-side checks in :ref:`operating_verify_enforcement` before treating the
installation as enforced.
