.. _WP_FAIL2BAN_ADDON_BLOCKLIST_DEBUG_TRY_ALL_KEYS:

.. role:: php(code)
   :language: php

WP_FAIL2BAN_ADDON_BLOCKLIST_DEBUG_TRY_ALL_KEYS
----------------------------------------------

.. rubric:: Broaden secret-key lookup during authentication diagnosis.

----

The exact boolean :php:`true` makes Blocklist try every Freemius site secret
stored in the shared accounts option, rather than only keys associated with the
add-on's current basename and known slugs. Other values do not enable it.

.. code-block:: php
   :caption: Temporary support setting

   define('WP_FAIL2BAN_ADDON_BLOCKLIST_DEBUG_TRY_ALL_KEYS', true);

**Accepted value:** :php:`true` to enable

**Default:** disabled; the constant is not defined

The constant is available in all supported editions and has no settings-field
equivalent.

This widens authentication's candidate-key search and is intended only for a
temporary support diagnosis. Remove it afterwards. It operates independently
of :ref:`WP_FAIL2BAN_ADDON_BLOCKLIST_DEBUG`; enabling this control does not
write the detailed diagnostic log.

.. rubric:: History
.. versionadded:: 2.2.0
