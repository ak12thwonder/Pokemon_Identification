import os
import shutil

# Paths
train_dir = r"data/processed/pokemon_images_255_class"
test_root = r"data/Test_photos/Pokemon Images DB"
dst_root = r"data/processed/pokemon_images_255_test"

# Get set of species used for training
train_species = set(os.listdir(train_dir))

# Make destination directory
os.makedirs(dst_root, exist_ok=True)

# Copy only matching species folders from test to processed test folder
count=0
for species in os.listdir(test_root):
    if species in train_species:
        src_folder = os.path.join(test_root, species)
        dst_folder = os.path.join(dst_root, species)
        if not os.path.exists(dst_folder):
            shutil.copytree(src_folder, dst_folder)
            print(f"Copied {species}")
            count=count+1

print("Copying complete! Only matching species are now in data/processed/pokemon_images_255_test/") 
print(f"Number of matching species: {count}")