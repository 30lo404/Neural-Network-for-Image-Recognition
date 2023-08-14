import os
import random
import shutil

def split_and_move_images(source_folder, training_folder, testing_folder,num_to_select):
    subjects = [f"s{i}" for i in range(1, 41)]  # s1 to s10
    
    #loop through S1 to S10
    for subject in subjects:
        #reconstruct S1 to S10 in trianing and testing folder
        source_subject_folder = os.path.join(source_folder, subject)
        training_subject_folder = os.path.join(training_folder, subject)
        testing_subject_folder = os.path.join(testing_folder, subject)
        
        #create a directory 
        os.makedirs(training_subject_folder, exist_ok=True)
        os.makedirs(testing_subject_folder, exist_ok=True)
        
        all_images = os.listdir(source_subject_folder) #get a list of all images
        selected_images = random.sample(all_images, num_to_select) #get 8 random num

        for image in all_images:
            source_path = os.path.join(source_subject_folder, image) #join source path and current image name
            if image in selected_images:
                destination_folder = training_subject_folder
            else:
                destination_folder = testing_subject_folder #put non-selected to testing folder
            destination_path = os.path.join(destination_folder, image) #complete image destination path

            shutil.copy(source_path, destination_path) #copy image

source_folder = "img/faces"
training_folder = "img/faces-training"
testing_folder = "img/faces-testing"


# Call the function to split and move the images
split_and_move_images(source_folder, training_folder, testing_folder, 8)