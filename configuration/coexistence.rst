.. _configuration_coexistence:

Coexisting with other blocklists
================================

Keep Blocklist-derived evidence separate from attacks observed at this site.
An address delivered by BNS was selected from shared intelligence. A later
Blocklist message therefore means "apply this acquired intelligence locally",
not "this address has just attacked this site".

This distinction matters when an existing fail2ban jail has an action that
reports every match to another collaborative blocklist. Sending a
Blocklist-derived match through that action presents acquired intelligence as
independent local evidence. If services repeat that pattern, they can amplify
one another's entries and create a feedback loop. This is a provenance problem,
not a criticism of free, open, or collaborative blocklists. Attacks that WP
fail2ban genuinely observes while WordPress handles a local request remain
eligible for reporting under the operator's normal policy.

By default, Blocklist writes the same unprefixed immediate-block message that
the main ``wordpress-hard`` filter recognises. This can be sufficient when the
receiving jail uses local ban actions only. Where that jail has any external
reporting action, isolate Blocklist messages in the prefixed custom mode and a
dedicated jail whose actions only ban locally. An equivalently verified action
boundary is acceptable, but merely choosing another syslog facility is not:
the facility changes message routing, not what a jail does after a match.

:ref:`configuration_fail2ban` provides the supported dedicated-jail setup.
