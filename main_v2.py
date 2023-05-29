#import all the impotant utility 
import os
import shutil

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
    '.rar': 'archive',
    '.tar': 'archive',
    '.zip': 'archive',
}

#path to the folder wich you want to arrange 
download_folder = "/home/kamal/Downloads"


#function to  organise file
def organiser(folder_path):
    #find all the file on the folde and full path to the file 
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path,file_name)
        
        #check if the selected opject is a file or not 
        if os.path.isfile(file_path):
            #find the file extension | seprate file extension from file name 
            _,extension = os.path.splitext(file_name)
            
            #check if the file extension is known or not and giving the folder location to be moved to 
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
            
            #move the file to the aproprate location
            new_file_path = os.path.join(target_folder,file_name)
            shutil.move(file_path, new_file_path)
        
        elif os.path.isdir(file_path):
            organiser(file_path)
            

organiser(download_folder)
print("sucessfull")
