import os

os.system("clear")

def start():
	choice = input("1- README.md maker \n2- setup.sh maker \n->")
	if choice == "1":
		readme()
	elif choice == "2":
		setup()
	else:
		start()

def readme():
	read = open("README.md", 'w')
	step = []
	name = input("what is the project name?\n->")
	description = input("it can be better if you add a description\n->")
	steps = input("How to launch it? (when you finish steps write EOF)\n->")
	while steps != "EOF":
		step.append(steps)
		steps = input("->")
	body = f'''# {name}
{description}
# HOW TO LAUNCH IT:
```sh

'''
	read.write(''.join(body))
	for steps in step:
		read.write(''.join(steps))
		read.write(''.join('\n'))
	read.write(''.join("```"))
	com = input("do you want a second description or comment? y/n\n->")
	if com == "y":
		com = input("->")
		read.write(''.join(com))
	else:
		pass
	credit = input("is there any credits? y/n\n->")
	if credit == "y":
		credit = []
		credits = input("who? (when you finish credits write EOF)\n->")
		while credits != "EOF":
			credit.append(credits)
			credits = input("->")
		read.write(''.join("\n# Credits:\n---\n"))
		for credits in credit:
			read.write(''.join("```"))
			read.write(''.join(credits))
			read.write(''.join("```"))
			read.write(''.join('\n'))
	else:
		pass
	print("wait while making the file")
	read.close()
	print("done!")

def setup():
	setupsh = open("setup.sh", 'w')
	packages = []
	code = []
	pack = input("which package we should download? (when you finish package write EOF)\n->")
	while pack != "EOF":
		packages.append(pack)
		pack = input("->")
	codes = input("write now the code (when you finish the code write EOF)\n->")
	while codes != "EOF":
		code.append(codes)
		codes = input("->")
	print("cool, let me make you the file...")
	body = f'''clear
echo 'downloading files...'
sleep 1
sudo apt-get install '''
	setupsh.write(''.join(body))
	for pack in packages:
		setupsh.write(''.join(pack))
		setupsh.write(''.join(" "))
	setupsh.write(''.join("\n"))
	setupsh.write(''.join("clear \n"))
	setupsh.write(''.join("sudo pacman -S "))
	for pack in packages:
		setupsh.write(''.join(pack))
		setupsh.write(''.join(" "))
	setupsh.write(''.join("\n"))
	setupsh.write(''.join("clear \n"))
	setupsh.write(''.join("sudo dnf install "))
	for pack in packages:
		setupsh.write(''.join(pack))
		setupsh.write(''.join(" "))
	setupsh.write(''.join("\n"))
	setupsh.write(''.join("clear \n"))

	requirement = input("is there a requirements.txt to download for python? y/n\n->")
	if requirement == "y":
		setupsh.write(''.join("pip install -r requirements.txt\nclear \n"))
	else:
		pass
	setupsh.write(''.join("echo 'configuring files'\nsleep 1\n"))
	for codes in code:
		setupsh.write(''.join(codes))
		setupsh.write(''.join("\n"))
	setupsh.write(''.join("clear\n"))
	setupsh.write(''.join("echo 'done!'\n"))
	com = input("do you want to add a comment? y/n")
	if com == "y":
		com = input("->")
		setupsh.write(''.join("echo '")
		setupsh.write(''.join(com))
		setupsh.write(''.join("'"))
	setupsh.close()
	print("done")

start()
