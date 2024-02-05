import os

pathName = "/Eeja"

def listDirectory(path, depth=0):
    if os.path.exists(path):
        if os.listdir(path):
            print(f"{'  ' * depth}> {os.path.basename(path)}")
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isfile(item_path):
                    print(f"{'  ' * (depth + 1)}> {os.path.basename(item_path)}")
                elif os.path.isdir(item_path):
                    listDirectory(item_path, depth + 1)
        else:
            print(f"{'  ' * depth}> {os.path.basename(path)}")
    else:
        print(f"Direktori Tidak Ditemukan")

listDirectory(pathName)
