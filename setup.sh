clear
echo 'downloading files...'
sleep 1
sudo apt-get install python3 figlet 
clear 
sudo pacman -S python3 figlet 
clear 
sudo dnf install python3 figlet 
clear 
echo 'configuring files'
sleep 1
cd ..
mkdir ~/.local/share/NacreousDawn596
mv githelper ~/.local/share/NacreousDawn596
rm ~/.local/share/NacreousDawn596/githelper/setup.sh
echo '' >> ~/.bashrc
echo 'source ~/.local/share/NacreousDawn596/githelper/.help.sh' >> ~/.bashrc
echo '' >> ~/.bashrc
clear
echo 'done!'
echo 'now you can it by writing githelp after restaring the terminal'
