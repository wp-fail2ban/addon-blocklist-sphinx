.. code-block:: ini

   # Fail2Ban filter for WP fail2ban: Blocklist hard failures
   #

   [INCLUDES]

   before = common.conf

   [Definition]

   _daemon = (?:wordpress|wp)
   _tail = (?: on <F-SITE_INLINE>\S+(?:/\S+)?</F-SITE_INLINE>)? from <ADDR>

   failregex = ^%(__prefix_line)s\(WPf2b\+\+/blocklist\) Immediately block connections<_tail>$

   ignoreregex =

   journalmatch = SYSLOG_IDENTIFIER=wordpress

   # DEV Notes:
   # Requires the 'WP fail2ban' plugin:
   # https://wp-fail2ban.com/
   #
   # Author: Charles Lecklider
   # Version: 3.0.0-rc1
   # Build Date: 2026-11-05T14:49:31+00:00
