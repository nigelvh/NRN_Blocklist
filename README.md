# Null Route Networks Shared Blocklist Service

The shared blocklist service accepts entries from participants, which are then combined into an overall list, available in several program-digestible formats, for use in your own firewall rules.

The service will automatically expire entries, and remove them from the list once their expiry time has passed.

## Accessing the List

The list is available over HTTP/HTTPS at https://www.nullroutenetworks.com/blocklist/getlist.php

The default format is a very basic HTML page with a simple list of IPs currently on the list. Additional formats are available by appending `?format=` and the format name. Acceptable format names are `json`, `csv`, and `raw`.

`json` format provides the IP address, the timestamp for when the entry was added, the timestamp for when then entry will expire, and the total number of submissions for this IP (within it's active lifetime).

`csv` format provides the same fields as `json`.

`raw` format provides a plain text list of IPs `\r\n` separated, without the HTML context as in the default format.

## Submitting to the List

The list accepts submissions from participants who have been issued an API key. If you wish to be issued a key and participate, please reach out.

Submission data is handled via a HTTP/HTTPS POST, with the `key`, `host`, `expires`, `type`, and `service` fields populated. A simple and crude python script is given in submit_blacklist.py for example.

`key` is the API key you have been issued.

`host` is the IP address of the host to be added to the blocklist. E.G. '1.2.3.4'

`expires` is the time in seconds *from now* that this entry should expire. This is not a unix timestamp. E.G. '86400' for 1 day.

`type` is a plaintext field for a general category of what type of source this entry is from. Typically something like 'ABUSE' or 'HONEYPOT'.

`service` is a plaintext field for a specific service within the `type` category. Typically something like 'SSH' or 'HTTP' or 'ASTERISK'

Entries are sent to the submission URL at https://www.nullroutenetworks.com/blocklist/submit.php
