# raspi_builds
## raspi builds for remote needs and gaming
[https://retropie.org.uk/docs/First-Installation/][https://retropie.org.uk/docs/First-Installation/]

## If you need help with booting the 3.5" LCD screen, see below. 
---
## Step 1.
# First of all enable SPI by using the terminal command:


raspi-config


# Navigate to ‘Advanced options’ and then enable SPI

# Reboot if needed through the command in the terminal:


sudo reboot

# The touch screen should turn on and be white colored.

## Step 2.


# If your still running the Buster beta upgrade to the latest stable kernel

sudo apt-get update –allow-releaseinfo-change

# Give the command time to update and upgrade:

sudo apt-get update
sudo apt-get upgrade
sudo reboot

## Step 3.
# Now to modify the configuration file to configure the display


sudo nano /boot/config.txt


# then add this line to the bottom

dtoverlay=piscreen,speed=16000000,rotate=90

# Save config file, safely eject and boot int Raspi. You should see the Display ight up with the correct terminal output. 

[def]: https://retropie.org.uk/docs/First-Installation/