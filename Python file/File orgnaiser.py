

import os 
import shutil 

    
    


def category_decider (full_path):
   if full_path.endswith(".png"):
      return "Images"
   elif full_path.endswith(".py"):
      return "Python file"
   elif full_path.endswith(".pdf"):
      return "PDF file"
   else:
      return "Other"
   
 

def folder_creator (category):
  if not os.path.exists(category):
    os.mkdir(category)



def file_transfer (full_path, category, item):
 destination = os.path.join(category, item) 
 shutil.move (full_path, destination)



def creating_list_of_files():
 folder_path = "."
 items = os.listdir(folder_path)

 for item in items :
   full_path = os.path.join(folder_path, item)
   
   if os.path.isfile(full_path):
    category = category_decider(full_path)
    folder_creator(category)
    file_transfer (full_path, category, item)

    print (f'moved {item} to {category}')



def main () :
 creating_list_of_files()



if __name__ == "__main__":
    main ()


