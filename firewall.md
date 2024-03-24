# building a residential 1gigabit capable firewall/IDS-IPS with raspi 4. 
--
# SSH
'''
$ sudo vi /etc/ssh/sshd_config

Edit this>>>>> VIM will pop up 

# Modify the default port
Port 15507 (or another one way up there) 

Protocol 2
HostKey /etc/ssh/ssh_host_rsa_key
HostKey /etc/ssh/ssh_host_dsa_key
UsePrivilegeSeparation yes
KeyRegenerationInterval 3600
ServerKeyBits 768
SyslogFacility AUTH
LogLevel INFO
LoginGraceTime 60

# Disable login with the root account
PermitRootLogin no

StrictModes yes
RSAAuthentication yes
PubkeyAuthentication yes
IgnoreRhosts yes
RhostsRSAAuthentication no
HostbasedAuthentication no
PermitEmptyPasswords no
ChallengeResponseAuthentication no
PrintMotd no
PrintLastLog yes
TCPKeepAlive yes
AcceptEnv LANG LC_*
Subsystem sftp /usr/lib/openssh/sftp-server
UsePAM yes

$ sudo rc.d restart sshd
