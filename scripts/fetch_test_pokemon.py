''' here we will fetch the test pokemon from the data test_photo inside we have the photos
of the pokemon that we want to test and on the basisi of which we are going to checkt he accuracy of the model
 '''

# Get the List of Pokémon Used for Training

import os

train_dir = r"../data/processed/pokemon_images_255_class"
train_species = set(os.listdir(train_dir))
print(f"Number of training species: {len(train_species)}")

# ilter Folders in the Test Set
test_root = r"../data/Test_photos/Pokemon Images DB"
filtered_species = [species for species in os.listdir(test_root) if species in train_species]
print(f"Number of matching species in test set: {len(filtered_species)}")
print(filtered_species)