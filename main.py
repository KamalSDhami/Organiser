#import all the impotant utility 
import os
import shutil
import platform

# all the file extension to arrange and there respected folder 
extension_mapping = {
    # Video extensions
    '.3gp': 'video',
    '.avi': 'video',
    '.flv': 'video',
    '.m4v': 'video',
    '.mkv': 'video',
    '.mov': 'video',
    '.mp4': 'video',
    '.mpeg': 'video',
    '.mpg': 'video',
    '.wmv': 'video',

    # Audio extensions
    '.aac': 'audio',
    '.aif': 'audio',
    '.aiff': 'audio',
    '.amr': 'audio',
    '.flac': 'audio',
    '.m4a': 'audio',
    '.mid': 'audio',
    '.midi': 'audio',
    '.mp3': 'audio',
    '.ogg': 'audio',
    '.wav': 'audio',
    '.wma': 'audio',

    # Document extensions
    '.csv': 'document',
    '.doc': 'document',
    '.docx': 'document',
    '.odt': 'document',
    '.pdf': 'document',
    '.ppt': 'presentation',
    '.pptx': 'presentation',
    '.rtf': 'document',
    '.txt': 'document',
    '.xls': 'document',
    '.xlsx': 'document',

    # Image extensions
    '.bmp': 'image',
    '.gif': 'image',
    '.jpeg': 'image',
    '.jpg': 'image',
    '.png': 'image',
    '.svg': 'image',
    '.tiff': 'image',

    # Programming extensions
    '.c': 'c',
    '.cpp': 'cpp',
    '.css': 'css',
    '.html': 'html',
    '.java': 'java',
    '.js': 'javascript',
    '.py': 'python',
    '.rb': 'ruby',

    # Archive extensions
    '.7z': 'archive',
    '.bz2': 'archive',
    '.gz': 'archive',
    '.iso': 'archive',
    '.rar': 'archive',
    '.tar': 'archive',
    '.zip': 'archive',
    
    #Other files extension
    '.vsix': 'vscode-extension',
    '.whl': 'python-extension',
    '.apk': 'Apps',
    
}

def manual_os_identification():
    # Operating system options
    options = {
        "1": os.path.join(os.environ.get("APPDATA", ""), "Downloads"),  # Windows
        "2": os.path.join(os.environ.get("HOME", ""), "Downloads"),     # macOS
        "3": os.path.join(os.environ.get("HOME", ""), "Downloads"),     # Linux
        "4": os.path.join(os.environ.get("EXTERNAL_STORAGE", ""), "Download"), # Android
    }

    # Display OS options to the user
    print("Unable to detect the operating system.")
    print("Please select your operating system:")
    print("1. Windows")
    print("2. macOS")
    print("3. Linux")
    print("4. Android")
    print("5. Manual entry")
    print("6. Exit")

    # Prompt for user input
    choice = input("Enter the number of your choice: ")

    # Process user choice
    if choice in options:
        return options[choice]
    elif choice == "5":
        manual_path = input("Enter the download folder path manually: ")
        return manual_path
    elif choice == "6":
        exit()
    else:
        print("Invalid choice. Using default download folder.")
        return os.path.join(os.environ.get("EXTERNAL_STORAGE", ""), "Download")
    
def Verifing_OS (device_os,download_folder):
    #verifing the detected os is right 
    
    os_verification = input(f"os Detected\nos :{device_os}\nIs it right (Y/n)").lower() or "y"
    if os_verification == "y":
        return download_folder
    elif os_verification == "n":
        return manual_os_identification()
    else:
        print('error :invalid input')
        Verifing_OS()

    # Get the device type
def get_download_folder(device_type = platform.system().lower()):
    """Returns the download folder location for the current device."""

      # Check if ARM-based machine
    is_arm_machine = "arm" in platform.machine().lower() or "aarch" in platform.machine().lower()

    # Get the download folder location for the device type
    # Check if Android or ARM-based Linux
    if device_type == "android" or is_arm_machine:
        device_os = "android"
        download_folder = os.path.join(os.environ["HOME"],"storage/shared/Download")
    elif device_type == "windows":
        device_os = "windows"
        download_folder = os.path.join(os.environ["APPDATA"], "Downloads")
    elif device_type == "darwin":  # macOS
        device_os = "MacOS"
        download_folder = os.path.join(os.environ["HOME"], "Downloads")
    elif device_type == "linux":
        device_os = "Linux"
        download_folder = os.path.join(os.environ["HOME"], "Downloads")
    else:
        # Unknown device type
        print("Error : Unknown device")
        print("You had to manually select the os ")
        return input("enter the path to your download folder ")
    
    #verifing the detected os is right 
    return Verifing_OS(device_os,download_folder)
    
#path to the folder wich you want to arrange 
download_folder = get_download_folder()


#function to  organise file
def organiser(folder_path,sub_folder_organise = False):
    #find all the file on the folde and full path to the file 
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path,file_name)
        
        #check if the selected opject is a file or not.
        if os.path.isfile(file_path):
            #find the file extension | seprate file extension from file name.
            _,extension = os.path.splitext(file_name)
            
            #check if the file extension is known or not and giving the folder location to be moved it.
            if extension.lower() in extension_mapping:
                folder_name = extension_mapping[extension.lower()]
                target_folder = os.path.join(download_folder,folder_name)
            else:
                target_folder = os.path.join(download_folder,"other")
                
            #check if file alrady exist or not 
            try:
                os.makedirs(target_folder)
            except FileExistsError:
                pass
            
            
            #move the file to the aproprate location.
            new_file_path = os.path.join(target_folder,file_name)
            shutil.move(file_path, new_file_path)
        
        elif os.path.isdir(file_path):
            if sub_folder_organise == True:
                organiser(file_path)
            else :
                pass
            
sub_folder = input("Do you want to also transfer the subfolder data (y/N) : ")
organiser(download_folder,True if sub_folder.lower() =="y" else False)
print("sucessfull")