# Building a Home Firewall with Raspberry Pi 4 using a TP-Link USB to Ethernet Adapter

Overview
Transform your Raspberry Pi 4 into a powerful home firewall using Raspbian OS and a TP-Link USB to Ethernet Gigabit USB 3.0 adapter. This setup is ideal for enhancing network security and managing traffic effectively.

## Prerequisites

	•	Raspberry Pi 4
	•	Raspbian OS installed
	•	TP-Link USB to Ethernet Gigabit USB 3.0 adapter

## Configuration Details

	•	Built-in Ethernet (eth0) for LAN
	•	TP-Link adapter (eth1) for ISP connection
	•	Wireless adapter (wlan0) disabled for security

## Instructions

>STEP 1: Initial Raspberry Pi Setup

	1.	Install Raspbian Buster with desktop and recommended software.
	2.	Complete initial setup (network, localization, preferences).
	3.	Update the system and install utilities:

sudo apt-get update && sudo apt-get dist-upgrade
sudo apt-get install htop tcpdump



>STEP 2: Networking Setup

	1.	Connect RPi4’s built-in Ethernet (eth0) to the LAN.
	2.	Plug the TP-Link USB to Ethernet adapter into the RPi4 and connect it to the ISP router; this will be recognized as eth1.
	3.	Enable SSH and VNC via the desktop GUI’s Raspberry Pi Configuration settings.
	4.	Secure and configure SSH by editing /etc/ssh/sshd_config, considering changes like port adjustment.

>STEP 3: User Configuration

	1.	Add a new administrative user and disable the default ‘pi’ user for security.

>STEP 4: System Configuration

	1.	Edit /etc/sysctl.conf to adjust kernel settings, enabling features like IP forwarding.

>STEP 5 & 6: Configure DHCP and DNS

	1.	Set static IP addresses and DNS servers in /etc/dhcpcd.conf for both eth0 and eth1 (TP-Link adapter).
	2.	Fine-tune /etc/dnsmasq.conf to handle DHCP and DNS, specifying the interfaces correctly.

>STEP 7: Service Reliability

	1.	Create a monitoring script to auto-restart dnsmasq if it stops, ensuring consistent network services.

>STEP 8: Firewall Configuration

	1.	Use iptables to define network rules, ensuring secure and functional internet connectivity.

>STEP 9: Log Management

	1.	Configure log rotation in /etc/logrotate.conf to manage syslog effectively.

>STEP 10: Intrusion Detection with Snort

	1.	Install Snort with sudo apt-get install snort and confirm the installation using sudo snort -V.
	2.	Edit /etc/rc.local to auto-start Snort on boot:

echo "Loading snort"
/usr/sbin/snort -D -u snort -g snort -c /etc/snort/snort.conf -i eth1 -l /var/log/snort


	3.	Customize /etc/snort/snort.conf to align with your network setup and security needs, paying particular attention to monitoring the TP-Link adapter interface (eth1).

Finishing Touches

	•	With the setup complete, your Raspberry Pi is now a robust firewall.
	•	Regular updates and log reviews are essential for ongoing security and performance.

Changelog

	•	Include changes here, especially those related to the TP-Link adapter setup and configuration enhancements.