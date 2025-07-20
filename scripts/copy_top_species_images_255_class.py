import os
import shutil

src_root = "data/raw/Pokemon Dataset"
dst_root = "data/processed/pokemon_images_40_class"

os.makedirs(dst_root, exist_ok=True)

for species in os.listdir(src_root):
    species_dir = os.path.join(src_root, species)
    if not os.path.isdir(species_dir):
        continue

    # Count images recursively
    image_paths = []
    for dirpath, _, filenames in os.walk(species_dir):
        for fname in filenames:
            if fname.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_paths.append(os.path.join(dirpath, fname))

    if len(image_paths) > 40:
        species_dst = os.path.join(dst_root, species)
        os.makedirs(species_dst, exist_ok=True)
        for img_path in image_paths:
            # Get the relative path from the species folder
            rel_path = os.path.relpath(img_path, species_dir)
            # Replace os separators with underscores for the new filename
            rel_path_flat = rel_path.replace(os.sep, "_")
            # Prepend the species name
            dst_file = os.path.join(species_dst, f"{species}_{rel_path_flat}")
            # Copy the file
            shutil.copy2(img_path, dst_file)
        print(f"Copied and flattened {species} with {len(image_paths)} images.")

print("Flattening complete! All species with >40 images are now in data/processed/pokemon_images_40_class_flattened/<species>/ with metadata in filenames.") 