# PublicScripts
My personal scripts for public use


Just a reminder for myself
`curl -s <URL-to-your-file> |bash`

# Cofigure Ubuntu server network for a static IP

`nano /etc/netplan/00-installer-config.yaml`

Replace
```
network:
  ethernets:
    enp1s0:
      addresses: [192.168.0.XX/24]
      gateway4: 192.168.0.254
      nameservers:
       addresses: [192.168.0.254]
     # dhcp4: true
  version: 2
```
Then apply the plan

`netplan apply`
---
# Local test server scripts
### Servers without domain or SSL/ with local-network self signed certs

1. Jitsi-meet server 
  - `curl -s https://raw.githubusercontent.com/andzejsp/PublicScripts/main/sh/Jitsi-server-deployment |bash`
2. Mattermost server
  - `curl -s https://raw.githubusercontent.com/andzejsp/PublicScripts/main/sh/Mattermost-omnibus-server-deployment |bash`
3. Jibri server
  - ` curl -s https://raw.githubusercontent.com/andzejsp/PublicScripts/main/sh/Jibri-server-deployment |bash`
  - Some finalize_recording scripts to download, that post a message on mattermost channel. Be sure to ` cd /srv/ ` before you ` curl `  and ` nano finalize_recording.sh ` before you deploy jibri:
    - For *incomming webhooks* use this sample:
      ```
      curl -o finalize_recording_webhook.sh https://raw.githubusercontent.com/andzejsp/PublicScripts/main/sh/Jibri_finalize_recording_webhook
      ```
    - For bot accounts use this sample:
      ```
      curl -o finalize_recording_bot.sh https://raw.githubusercontent.com/andzejsp/PublicScripts/main/sh/Jibri_finalize_recording_bot
      ```
---
# Virtualization using KVM libvirt - HOST -> GUEST networking

As seen on [RedHat](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/virtualization_host_configuration_and_guest_installation_guide/app_macvtap)

Procedure B.3. Creating an isolated network with libvirt

1. Add and save the following XML in the ` /tmp/isolated.xml ` file on HOST. If the 192.168.254.0/24 network is already in use elsewhere on your network, you can choose a different network.
```
<network>
  <name>isolated</name>
  <ip address='192.168.254.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.254.2' end='192.168.254.254' />
    </dhcp>
  </ip>
</network>
```
2. Create the network with this command: ` virsh net-define /tmp/isolated.xml `, on HOST machine
3. Set the network to autostart with the virsh net-autostart isolated command.
4. Start the network with the ` virsh net-start isolated ` command.
5. Using ` virsh edit name_of_guest `, edit the configuration of each guest that uses macvtap for its network connection and add a new ` <interface> ` in the ` <devices> ` section similar to the following (note the <model type='virtio'/> line is optional to include):
```
<interface type='network'>
  <source network='isolated'/>
  <model type='virtio'/>
</interface>
```
6. Shut down, then restart each of these guests.

The guests are now able to reach the host at the address **192.168.254.1**, and the host will be able to reach the guests at the IP address they acquired from DHCP (alternatively, you can manually configure the IP addresses for the guests). Since this new network is isolated to only the host and guests, all other communication from the guests will use the macvtap interface.
---
# Mattermost and Rasa integration
To connect your Rasa bot to mattermost you have to have these in your rasa bot credentials.yml:
```
mattermost:
  url: "http://mattermost server/api/v4"
  token: "bot token not token ID"
  webhook_url: "http://rasa x server:5005/webhooks/mattermost/webhook" # and this has to be set up in mattermost integrations as outgoing webhook and (Callback URLs (One Per Line)) must match the rasa x ip but the port has to be for some unknown reason 5005 not 5002
```
