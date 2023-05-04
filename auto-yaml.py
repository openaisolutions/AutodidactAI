import os
import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def save_yaml(file_path, data):
    with open(file_path, 'w') as f:
        yaml.dump(data, f)

def add_item(yaml_file, item):
    file_structure = load_yaml(yaml_file)
    file_structure.update(item)
    save_yaml(yaml_file, file_structure)

def remove_item(yaml_file, item_name):
    file_structure = load_yaml(yaml_file)
    if item_name in file_structure:
        del file_structure[item_name]
    save_yaml(yaml_file, file_structure)

def edit_item(yaml_file, old_item_name, new_item):
    file_structure = load_yaml(yaml_file)
    if old_item_name in file_structure:
        file_structure.pop(old_item_name)
        file_structure.update(new_item)
    save_yaml(yaml_file, file_structure)

def improve_structure(yaml_file):
    file_structure = load_yaml(yaml_file)

    def sort_structure(structure):
        sorted_folders = sorted((k, v) for k, v in structure.items() if isinstance(v, dict))
        sorted_files = sorted((k, v) for k, v in structure.items() if isinstance(v, list))

        sorted_structure = {}
        for folder, contents in sorted_folders:
            sorted_structure[folder] = sort_structure(contents)
        for file, contents in sorted_files:
            sorted_contents = sorted(x for x in contents if isinstance(x, str))
            sorted_contents.extend(sorted((k, sort_structure(v)) for k, v in (x.items() for x in contents if isinstance(x, dict))))
            sorted_structure[file] = sorted_contents

        return sorted_structure

    improved_structure = sort_structure(file_structure)
    save_yaml(yaml_file, improved_structure)

# Example usage:
yaml_file = 'files.yaml'

# Add an item
add_item(yaml_file, {'new_folder': ['new_file.txt']})

# Remove an item
remove_item(yaml_file, 'folder_to_remove')

# Edit an item
edit_item(yaml_file, 'folder_to_edit', {'folder_to_edit': ['new_file.txt']})

# Improve the YAML file structure
improve_structure(yaml_file)
