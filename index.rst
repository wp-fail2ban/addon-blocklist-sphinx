=========================
WP fail2ban Blocklist 3.0
=========================

WP fail2ban Blocklist adds shared, pre-emptive protection to `WP fail2ban
<https://wp-fail2ban.com/>`_. It exchanges selected security-event data with
the Blocklist Network Service (BNS), then turns addresses returned by the
service into messages that fail2ban can use for host-side bans.

Start with :ref:`about` for the division of responsibility between the add-on,
BNS, fail2ban, and the firewall. :ref:`installation` gives the shortest path
to a working installation, while :ref:`configuration` explains the important
service and jail decisions.

.. toctree::
   :caption: Manual
   :maxdepth: 2

   about
   installation
   configuration
   operating

.. toctree::
   :caption: Reference
   :maxdepth: 2

   defines
   filters
   release

