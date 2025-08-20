# Quick start for MQTT (Mosquitto) & Pico W on Windows


(WIP: Will add images and more detail soon, as well as how to work the secure options).

This is mainly for me, however hopefully some else may find it useful.

Using Windows because ceebs swapping between dual boot

## MQTT (Insecure)

1) Install an MQTT Broker (such as Mosquitto)
2) Modify the .conf file (user must be admin)
3) !IMPORTANT! Add an Inbound Rule to Windows Defender Firewall.

This is insecure, so this Inbound Rule should be disabled (or deleted) when not in use!
All connections must be allowed, or else the Pico W cannot connect to the broker.



