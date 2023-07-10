import yaml
import os
import argparse





# print(folder_structure)

def create_folder_structure(folder_structure, parent_path=''):
    for key, value in folder_structure.items():
        if isinstance(value, dict):
            path = os.path.join(parent_path, key)
            if isinstance(value, dict):
                if value["type"] == 'folder':
                    os.makedirs(path, exist_ok=True)
                    create_folder_structure(value, path)
                else:
                    f=open(path,'a')
                    if value.get("content",False):
                        f.write(value.get("content"))
                    f.close()



parser = argparse.ArgumentParser(description='Generate the scaffolding for the project')
parser.add_argument('-p', '--path', help='Path to generate the scaffolding at')
parser.add_argument("-n",'--name',help="Name of the project")
parser.add_argument("-c","--config",help="Configuration File in YAML")
args = vars(parser.parse_args())
path=''
config_path="./scaffolding.yml"
if args['path'] is not None:
    path = args['path']
if args['config'] is not None:
    config_path=args['config']
if args['name'] is not None:
    print(f"Creating Project Directory - {args['name']} at Path - {path}")
    path = os.path.join(path, args['name'])
    os.makedirs(path, exist_ok=True)

with open(config_path, 'r') as file:
    folder_structure = yaml.safe_load(file)
create_folder_structure(folder_structure,path)