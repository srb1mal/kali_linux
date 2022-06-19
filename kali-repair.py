import os
def Edit_Sources_File():
	while True:
		os.system("clear")
		banner()
		print("""
	1) Automatic
	2) Manual
	0) Back
		""")
		menu = input(">> ")
		if menu == "1":
			text= """deb http://http.kali.org/kali kali-rolling main contrib non-free
# For source package access, uncomment the following line
# deb-src http://http.kali.org/kali kali-rolling main contrib non-free"""
			file = open("/etc/apt/sources.list", "w")
			file.write(text)
			file.close
			print("Done, Thank you for using this service, Now Enjoy :)")
			exit()
		elif menu == "2":
			select = input("Enter name of text editor (like mousepad or nano or vim) : ")
			os.system(select + " /etc/apt/sources.list")
			print("Thank you for using this service, Now Enjoy :)")
			exit()
		elif menu == "0":
			os.system("clear")
			main()
		else:
			continue
def Updating_System():
	while True:
		os.system("clear")
		banner()
		print("""
	1) Normal Update 
	2) Full Update (With upgrade)
	0) Back
		""")
		menu = input(">> ")
		if menu == "1":
			os.system("clear")
			os.system("apt-get update")
			exit()
		elif menu == "2":
			os.system("clear")
			os.system("apt-get update && apt-get full-upgrade -y")
			exit()
		elif menu == "0":
                        os.system("clear")
                        main()
		else:
			continue
def Fix_PGP_Error():
	os.system("clear")
	banner()
	key = input("Enter key here : ")
	os.system("apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys " + key)
	print("Done, Thank you for using this service, Now Enjoy:)")
	exit()
def VMware_Tools():
	os.system("clear")
	banner()
	os.system("apt -y install open-vm-tools-desktop fuse")
	Ask_Rebooting = input("Done, Now you've to reboot your system, reboot now? [y/n] ")
	if Ask_Rebooting == "y" or Ask_Rebooting == "yes" or Ask_Rebooting == "Y" or Ask_Rebooting == "Yes":
		os.system("reboot")
	else:
		print("Done, Thank you for using this service, Now Enjoy:)")
		exit()
def Virtualbox_Tools():
	os.system("clear")
	banner()
	os.system("apt-get install -y virtualbox-guest-x11")
	Ask_Rebooting = input("Done, Now you've to reboot your system, reboot now? [y/n] ")
	if Ask_Rebooting == "y" or Ask_Rebooting == "yes" or Ask_Rebooting == "Y" or Ask_Rebooting == "Yes":
		os.system("reboot")
	else:
		print("Done, Thank you for using this service, Now Enjoy :)")
		exit()
def main():
	while True:
		os.system("clear")
		banner()
		print("""
	1) Edit sources.list
	2) Updating & Upgrading System
	3) Fix pgp error
			""")
		menu = input(">> ")
		if menu == "1":
			Edit_Sources_File()
		elif menu == "2":
			Updating_System()
		elif menu == "3":
			Fix_PGP_Error()
			else:
			continue
def banner():
	print("""
                          (                                
                           @  @                            
                            @@ @                           
                  @%,*@@@@@@ *@%@@                         
               ,@@@@@@@@@@@@@@@@@@@@                       
               @@@@@@@.   .@@@@@@@@@@@                     
              @@@@@            @@@@@@@@@                   
             &@@@@               @@@@@@@@                  
              @@@@                 @@@@@@@@                
              @@@@%                  @@@@@@                
               &@@@@                    @@@@@              
                @ @@@@                   *@@@#             
                    (@@@@&                @@               
                        #@@@@@                             
                             @@@@                          
                                @@@                        
                                   @                       
                                    @                      
                                    *                      
 _         _ _     _ _                  
| | ____ _| (_)   | (_)_ __  _   ___  __
| |/ / _` | | |   | | | '_ \| | | \ \/ /
|   < (_| | | |   | | | | | | |_| |>  < 
|_|\_\__,_|_|_|___|_|_|_| |_|\__,_/_/\_\

~ A simple tool to repair some of your kali linux problem.
		""")
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nThanks You so much for using this tool. Now Enjoy 😊 :)")
