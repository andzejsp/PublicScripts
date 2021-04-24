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

# Local test server scripts
### Servers without domain or SSL/ with local-network self signed certs

1. Jitsi-meet server 
  - `curl -s https://raw.githubusercontent.com/andzejsp/PublicScripts/main/sh/Jitsi-server-deployment |bash`
2. Mattermost server
  - `curl -s https://raw.githubusercontent.com/andzejsp/PublicScripts/main/sh/Mattermost-omnibus-server-deployment |bash`
3. Jibri server
  - ` curl -s https://raw.githubusercontent.com/andzejsp/PublicScripts/main/sh/Jibri-server-deployment |bash`
