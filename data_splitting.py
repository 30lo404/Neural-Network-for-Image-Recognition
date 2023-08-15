import os
import random
import shutil

def split_and_move_images(source_folder, training_folder, testing_folder,num_to_select):
    #subjects = [f"s{i}" for i in range(1, 41)]  # s1 to s40
    subjects = os.listdir(source_folder) # get folder names

    #loop through S1 to S40
    for subject in subjects:
        #reconstruct S1 to S40 in trianing and testing folder
        source_subject_folder = os.path.join(source_folder, subject)
        if os.path.isdir(source_subject_folder):
            training_subject_folder = os.path.join(training_folder, subject)
            testing_subject_folder = os.path.join(testing_folder, subject)

            #remove the folder if it already exists
            if os.path.exists(training_subject_folder):
                shutil.rmtree(training_subject_folder)
            if os.path.exists(testing_subject_folder):
                shutil.rmtree(testing_subject_folder)
            #create a directory
            os.makedirs(training_subject_folder, exist_ok=False)
            os.makedirs(testing_subject_folder, exist_ok=False)
        
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