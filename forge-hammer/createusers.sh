#!/bin/bash

# Create liip and manger users
adduser --gecos "" --disabled-password manager
adduser --gecos "" --disabled-password liip
# Copy root ssh keys to new users
mkdir -p /home/manager/.ssh
mkdir -p /home/liip/.ssh
cp .ssh/authorized_keys /home/manager/.ssh/
cp .ssh/authorized_keys /home/liip/.ssh/
chmod 0600 /home/manager/.ssh/authorized_keys; chown -R manager:manager /home/manager/.ssh/
chmod 0600 /home/liip/.ssh/authorized_keys; chown -R liip:liip /home/liip/.ssh/
# Allow manager to run sudo commands without password
echo -e "manager ALL=(ALL) NOPASSWD:ALL" | tee -a /etc/sudoers.d/10_liip
# Allow liip to run sudo commands with password
echo -e "liip ALL=(ALL) ALL" | tee -a /etc/sudoers.d/10_liip
# Allow manager to run docker without sudo
usermod -aG docker manager
# Prevent Root login over SSH
sed -i '/^PermitRootLogin[ \t]\+\w\+$/{ s//PermitRootLogin no/g; }' /etc/ssh/sshd_config
service sshd restart
