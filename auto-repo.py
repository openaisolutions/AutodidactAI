import os
import yaml

def create_file_structure(file_structure, root_dir):
    """
    Creates the file and folder structure based on the YAML file.
    """
    for item in file_structure:
        if isinstance(item, str):
            file_path = os.path.join(root_dir, item)
            if not os.path.exists(file_path):
                open(file_path, 'w').close()
            continue
        for folder, contents in item.items():
            folder_path = os.path.join(root_dir, folder)
            if os.path.exists(folder_path):
                if os.path.isfile(folder_path):
                    # Skip if the path exists and is a file
                    continue
            else:
                # Create the directory if it does not exist
                os.makedirs(folder_path, exist_ok=True)

            if isinstance(contents, dict):
                create_file_structure([contents], folder_path)
            else:
                for file in contents:
                    if isinstance(file, str):
                        file_path = os.path.join(folder_path, file)
                        # Create the file if it does not exist
                        if not os.path.exists(file_path):
                            open(file_path, 'w').close()
                    else:
                        new_func(folder_path, file)

def new_func(folder_path, file):
    create_file_structure([file], folder_path)

if __name__ == '__main__':
    with open('files.yaml') as f:
        file_structure = yaml.load(f, Loader=yaml.FullLoader)

    create_file_structure(file_structure, os.getcwd())
