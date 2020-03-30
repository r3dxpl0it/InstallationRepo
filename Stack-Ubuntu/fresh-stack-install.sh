

sudo apt update -y
sudo apt upgrade -y

#Setup Essenstials :
sudo snap install jq

#Setup Python 
sudo apt install -y python3 
sudo apt install -y ruby 
sudo apt install -y python3-pip
sudo apt install -y virtualenv
sudo apt install -y git
sudo pip3 install virtualenv 
sudo apt install  -y snapd


#Cloning All my Repos to Folder Projects
#mygithubusername="r3dxpl0it"
#mkdir Projects 
#cd Projects && curl -s "https://api.github.com/users/$mygithubusername/repos?per_page=100" | jq -r ".[].git_url" | xargs -L1 git clone

#Downloading And Setting Up Tools Folder 
mkdir Tools 
cd Tools && mkdir MainTools
cd - 
#Setup arachni
cd Tools/MainTools && wget https://github.com/Arachni/arachni/releases/download/v1.5.1/arachni-1.5.1-0.5.12-linux-x86_64.tar.gz &&  tar -zxvf arachni-*.tar.gz
#Setup Nessus 
cd Tools/MainTools && wget -O Nessus.deb https://www.tenable.com/downloads/api/v1/public/pages/nessus/downloads/10202/download?i_agree_to_tenable_license_agreement=true && sudo dpkg -i Nessus.deb 


#Visual Studio Code

sudo snap install vscode --classic

#Setup Telegram

sudo snap install telegram-desktop

#Setup VirtualBox

sudo apt update -y
#wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
#wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
#sudo add-apt-repository "deb http://download.virtualbox.org/virtualbox/debian bionic contrib"
sudo add-apt-repository multiverse
sudo apt update -y
sudo apt install -y virtualbox

#Setup Docker

sudo apt-get update
sudo apt-get install -y docker 

#Setup Slack

wget https://downloads.slack-edge.com/linux_releases/slack-desktop-4.0.2-amd64.deb
sudo apt install ./slack-desktop-*.deb

#Setup Terminator 
sudo apt-get update
sudo apt-get install -y terminator


#Setup Skype 

sudo snap install skype --classic

#install gitkraken 

sudo snap install gitkraken


#install uget

sudo snap install uget --edge

#install Postman

sudo snap install postman 



