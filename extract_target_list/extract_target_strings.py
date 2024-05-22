import json
import os

# Load the JSON data
file_path = 'targets.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Function to recursively extract keys with up to three levels of depth
def extract_three_level_keys(d, prefix='', depth=1):
    keys = []
    if isinstance(d, dict):
        for k, v in d.items():
            new_prefix = f"{prefix}.{k}" if prefix else k
            if depth < 3:
                keys.extend(extract_three_level_keys(v, new_prefix, depth + 1))
            elif depth == 3:
                keys.append(new_prefix)
    return keys

# Extract the keys up to three levels
three_level_keys_no_overlay = extract_three_level_keys(data)

# Function to print keys with file check
def print_keys_with_file_check(keys):
    parent_folder = '../'
    for key in keys:
        # Check for the existence of files with different extensions
        file_exists = any(os.path.exists(os.path.join(parent_folder, f"{key}{ext}")) for ext in ['.jpg', '.png', '.jpeg'])
        if file_exists:
            print(f' - [x] `{key}`')
        else:
            print(f' - [ ] `{key}`')

# Print the keys with the file check
print_keys_with_file_check(three_level_keys_no_overlay)
