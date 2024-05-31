import os
import shutil
import random
from sklearn.model_selection import train_test_split

def make_directory(path):
    '''
    If the path does not exist, create it
    '''
    if not os.path.exists(path):
        os.makedirs(path)

def split_data(source_dir, train_dir, test_dir, test_size=0.2):
    '''
    Split data into training and testing sets
    '''
    # Create train and test directories
    make_directory(train_dir)
    make_directory(test_dir)

    # Iterate through each category directory
    categories = [d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d))]
    for category in categories:
        category_path = os.path.join(source_dir, category)
        images = [f for f in os.listdir(category_path) if os.path.isfile(os.path.join(category_path, f))]

        # Split images into training and testing sets
        train_images, test_images = train_test_split(images, test_size=test_size, random_state=42)

        # Create category directories in train and test directories
        train_category_dir = os.path.join(train_dir, category)
        test_category_dir = os.path.join(test_dir, category)
        make_directory(train_category_dir)
        make_directory(test_category_dir)

        # Copy images to respective directories
        for image in train_images:
            shutil.copy(os.path.join(category_path, image), os.path.join(train_category_dir, image))
        for image in test_images:
            shutil.copy(os.path.join(category_path, image), os.path.join(test_category_dir, image))

if __name__ == "__main__":
    source_directory = '../datasets/archive/PokemonData'
    train_directory = '../datasets/archive/PokemonDataTrain'
    test_directory = '../datasets/archive/PokemonDataTest'

    split_data(source_directory, train_directory, test_directory)