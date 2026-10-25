.. _reference_filters:

=======
Filters
=======

The optional ``wpf2b-blocklist-hard.conf`` filter matches only the prefixed
message written when :ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_CUSTOM_JAIL` is enabled.
It accepts the ``wordpress`` or ``wp`` syslog identifier, an optional inline
site name, and an IPv4 or IPv6 address. A match identifies a message; the jail
still decides the threshold and action. See :ref:`configuration_fail2ban`.

The filter shown below is included directly from the generated package input,
so the reference cannot acquire a separate hand-maintained expression.

``wpf2b-blocklist-hard.conf``
-------------------------------

.. include:: autogen/filters.d/wpf2b-blocklist-hard.inc

Packaged soft filter
--------------------

The package also contains ``wpf2b-blocklist-soft.conf``, which matches the
prefixed text ``Consider blocking connections``. Blocklist 3.0 has no active
path that writes that message, so do not create an operational jail for this
filter.

.. include:: autogen/filters.d/wpf2b-blocklist-soft.inc
