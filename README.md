This is a quick and dirty script to generate a set of commands to facilitate blocking Windows 10 phone-home stuff on your PAN firewall.  

Usage: `python pan-blockwin10.py`; copy the output to the clipboard and then paste in to your PAN from the `configure` prompt (i.e. the "#" prompt)

This will create the necessary address objects and a dynamic address-group called "Win10 Trackers" that you can then reference in policies.
