echo "####################################################################"
echo "██████╗ ██████╗ ██████╗ ██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗"
echo "██╔══██╗╚════██╗██╔══██╗╚██╗██╔╝██╔══██╗██║     ██╔═████╗██║╚══██╔══╝"
echo "██████╔╝ █████╔╝██║  ██║ ╚███╔╝ ██████╔╝██║     ██║██╔██║██║   ██║   "
echo "██╔══██╗ ╚═══██╗██║  ██║ ██╔██╗ ██╔═══╝ ██║     ████╔╝██║██║   ██║   "
echo "██║  ██║██████╔╝██████╔╝██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║   "
echo "╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝"
echo "Kali Install On Debian Server"
echo "https://github.com/r3dxpl0it"
echo "####################################################################"



echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list
apt-get -y update
apt-get -y --allow-unauthenticated install kali-archive-keyring
apt-get -y update
apt-cache search kali-linux
apt-get -y install kali-linux-all
apt-get -y update
apt-get -y upgrade
apt-get -y dist-upgrade
apt-get -y autoremove
shutdown now -rf




