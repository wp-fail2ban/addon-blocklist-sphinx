.. _configuration_service_connectivity:

Service connectivity
====================

BNS initiates signed requests to the site's WordPress REST API. The add-on
does not poll or download a list from an external BNS address. A normal service
cycle uses both methods on this registered route:

``GET wp-fail2ban/v1/blocklist``
   BNS collects selected local event records. Each record contains a time,
   WP fail2ban's resolved source address, and an event type.

``POST wp-fail2ban/v1/blocklist``
   BNS delivers batches of selected IPv4 and IPv6 addresses. The add-on
   removes built-in and configured ignores, then produces an immediate-block
   message for each remaining address.

With ordinary WordPress permalinks, the route is commonly
``/wp-json/wp-fail2ban/v1/blocklist``. If WordPress reports a different REST
base URL, allow the URL it actually publishes. ``GET
wp-fail2ban/v1/blocklist/status`` supplies signed status data and is used by
the add-on's local health check; it is separate from the normal GET and POST
exchange.

Allow only what the service needs
---------------------------------

If a REST restriction, web application firewall, reverse proxy, cache,
challenge, or upstream firewall interferes, exempt the Blocklist route rather
than disabling that protection for the entire REST API. The allowance must:

* permit GET and POST on the ``blocklist`` route;
* preserve the ``Authentication`` header and, preferably, the ``Date``
  header;
* pass the POST body unchanged; and
* avoid caching or challenging the service requests.

The authentication time must be within five minutes of the WordPress server's
clock. When an intermediary strips ``Date``, the implemented ``nonce`` query
parameter provides a fallback, but preserving the header is preferable. The
source does not define stable BNS address ranges, so do not build the allowance
around an assumed list of service IP addresses.

Site Health makes a signed request from the WordPress server back to its own
status URL. Success proves that the route and signature work on that loopback
path; it does not prove that an external request passes every upstream layer.
Conversely, a host can block loopback HTTP while remaining reachable from BNS.
Use the Dashboard's last GET and POST times as the evidence of actual service
communication. See :ref:`operating_diagnose_connectivity` when those times stop
advancing.
