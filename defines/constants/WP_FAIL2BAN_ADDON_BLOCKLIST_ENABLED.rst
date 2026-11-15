.. _WP_FAIL2BAN_ADDON_BLOCKLIST_ENABLED:

.. role:: php(code)
   :language: php

WP_FAIL2BAN_ADDON_BLOCKLIST_ENABLED
-----------------------------------

.. rubric:: Lock Blocklist participation on or off.

----

Fixes whether the add-on participates once Freemius is connected. When the
constant is defined, it overrides the saved WordPress option
``wpf2b_addon_blocklist_enabled`` and locks the QuickStart card and the
Blocklist settings **Enabled** control.

A :php:`true` value keeps participation on; a :php:`false` value keeps it off.
Without the constant, a missing option defaults to enabled. Freemius remains a
separate gate: the add-on still needs that connection before it can run, and
disabling participation stops Blocklist hooks, REST handlers, and Site Health
tests without removing the settings UI that turns it back on.

.. code-block:: php
   :caption: Example: Disable Blocklist participation

   define('WP_FAIL2BAN_ADDON_BLOCKLIST_ENABLED', false);

**Accepted values:** :php:`true` or :php:`false`

**Default:** enabled (the option is absent or stores ``'1'``)

The option stores only the strings ``'0'`` and ``'1'``. This control is not one
of the Premium Config-backed defines; Free and Premium both save the option
unless a PHP constant locks it.

.. seealso::
   * :ref:`configuration_quickstart`
   * :ref:`installation`

.. rubric:: History
.. versionadded:: 3.1.0
