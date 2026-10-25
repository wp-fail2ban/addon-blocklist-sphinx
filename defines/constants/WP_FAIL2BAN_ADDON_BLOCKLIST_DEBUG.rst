.. _WP_FAIL2BAN_ADDON_BLOCKLIST_DEBUG:

.. role:: php(code)
   :language: php

WP_FAIL2BAN_ADDON_BLOCKLIST_DEBUG
---------------------------------

.. rubric:: Record detailed REST-authentication diagnostics for support.

----

The exact boolean :php:`true` writes Blocklist authentication diagnostics at
``LOG_DEBUG`` through ``WP_FAIL2BAN_AUTH_LOG``. Other values do not enable it.

.. code-block:: php
   :caption: Temporary support setting

   define('WP_FAIL2BAN_ADDON_BLOCKLIST_DEBUG', true);

**Accepted value:** :php:`true` to enable

**Default:** disabled; the constant is not defined

The constant is available in all supported editions and has no settings-field
equivalent. It is a support control, not an ordinary logging option.

The diagnostics can contain Freemius secret keys, signed request material,
POST bodies, and calculated digests. Enable this only when instructed during
support work, restrict access to the resulting log, then remove the constant
and handle the captured log as sensitive data.

This setting does not change which secret keys authentication tries. See
:ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_DEBUG_TRY_ALL_KEYS` for that separate support
control.

.. rubric:: History
.. versionadded:: 2.2.0
