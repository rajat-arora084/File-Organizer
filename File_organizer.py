'''
Created on Dec 25, 2018

@author: rajat.arora07
'''
import os
import shutil


class File_organizer():
    
    '''
        API for organizing files into respective folders
        
        :Parameters:
               -  source_path - The path where different types of file are present.

        :Returns:
                Nothing

        :Raises:
                Error while moving the files..

        :Logic:
            The API checks the items in the listed directory and on knowing that its a file
            , checks its extension and moves it to respective folder.
            The folders names are given in a dictionary
            
            dict[Folder_name] = [type1, type2, ...]
        
        :Functionality:
            arrange_items:
                Moves the files based on their extensions.
                If exension is not found in the self.get_dict() then moves the file to
                'others' folder.
                
            add_extension_type(folder_name, extension):
            
                Can add different extensions to a folder
                or can add a new type of folder.
                Automatically creates the folder that is not present
                using create_folder function.
                
        :Prerequisites
            Folders Docs, Images, Codes are already present in the input location.
            Otherwise, create it using create_folder.
    '''
    
    
    def __init__(self, path):
        
        self.set_path(path)
        self.__dict = {'Docs' : ['.pdf', '.txt', '.doc', '.docx', '.xml'],
                       'Images' : ['.jpeg', '.jpg', '.png'] ,
                       'Codes' : ['.c', '.py', '.java', '.cpp'] }
        
    # Function to add new extension or a new folder type.
    def add_extension_type(self, folder_name, extension):
        
        # If folder name is already present then append the new extension to it.
        # Otherwise make a new folder entry and append the extension after that.
        if folder_name in self.get_dict():
            if extension not in self.get_dict()[folder_name]:
                self.get_dict()[folder_name].append(extension)
            else:
                print 'File Type already exists in ', folder_name
        else:
            self.get_dict()[folder_name] = [extension]
            # Create the folder in the directory if not already present.
            self.create_folder(folder_name)
            
    # Create Folder function to create a folder if not already present.
    def create_folder(self, folder_name):
        
        folder_exists = False
        for item  in os.listdir(self.get_path()):
            if os.path.isdir(self.get_path() + item):
                if item == folder_name:
                    folder_exists = True
                    break
        
        if not folder_exists:
            os.mkdir(self.get_path() + folder_name)
    
    
    def get_dict(self):
        return self.__dict
     
    
    def set_path(self, path):
        self.__path = path
    
        
    def get_path(self):
        return self.__path
    
    # Function to show all the items in the directory.
    def show_items(self):
        
        for item in os.listdir(self.get_path()):
            print item
    
    # Function to arrange items.
    def arrange_items(self):
        
        try:
            for item in os.listdir(self.get_path()):
                extension_found = False
                if os.path.isfile(self.get_path() + item):
                    item_full_path = self.get_path() + item
                    ext = os.path.splitext(item)[1]
                    for key, val in self.get_dict().items():
                         
                        if ext in val:
                            shutil.move(item_full_path, self.get_path() + key )
                            extension_found = True
                            break
                    if not extension_found:
                        shutil.move(item_full_path, self.get_path() + 'others')
        
        except Exception as err:
            print 'Error occured during moving the file. ', err.message
            raise Exception
                
path = 'D://'
if os.path.isdir(path):
    print 'yes'
    ob = File_organizer(path)
    #ob.arrange_items()
    ob.add_extension_type('Codes', '.py')
    print ob.get_dict()
    ob.add_extension_type('Faltu', '.cfg')
    print ob.get_dict()