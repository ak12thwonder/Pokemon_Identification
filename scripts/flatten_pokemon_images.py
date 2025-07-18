import os
import shutil

# Source: deeply nested Pokémon images
src_root = "data/raw/Pokemon Dataset"
# Destination: flattened structure in processed folder
dst_root = "data/processed/pokemon_images_train"

os.makedirs(dst_root, exist_ok=True)

for pokemon in os.listdir(src_root):
    pokemon_src = os.path.join(src_root, pokemon)
    if not os.path.isdir(pokemon_src):
        continue
    pokemon_dst = os.path.join(dst_root, pokemon)
    os.makedirs(pokemon_dst, exist_ok=True)
    for dirpath, _, filenames in os.walk(pokemon_src):
        for fname in filenames:
            if fname.lower().endswith((".png", ".jpg", ".jpeg")):
                src_file = os.path.join(dirpath, fname)
                dst_file = os.path.join(pokemon_dst, fname)
                base, ext = os.path.splitext(dst_file)
                counter = 1
                while os.path.exists(dst_file):
                    dst_file = f"{base}_{counter}{ext}"
                    counter += 1
                shutil.copy2(src_file, dst_file)

print("Flattening complete! All images are now in data/processed/pokemon_images_train/<pokemon>/")
