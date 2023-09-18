import os
import shutil
import argparse

trashDirectory = "~/.trash_can"


def createTrashCan():
    trashDirectory = os.path.expanduser(trashDirectory)
    os.makedirs(trashDirectory, exist_ok=True)


def moveToTrash(filePath):
    filename = os.path.basename(filePath)
    trashDirectory = os.path.expanduser(trashDirectory)
    trashPath = os.path.join(trashDirectory, filename)
    shutil.move(filePath, trashPath)
    print(f"Moved '{filename}' to trash can.")


def emptyTrashCan():
    trashDirectory = os.path.expanduser(trashDirectory)
    shutil.rmtree(trashDirectory)
    print("Trash can emptied.")


def main():
    parser = argparse.ArgumentParser(description="CLI Trash Can")
    parser.add_argument("action", choices=["delete", "empty"], help="Action to perform: 'delete' or 'empty'")
    parser.add_argument("filePath", nargs="?", default=None, help="Path of the file to delete")

    args = parser.parse_args()

    if args.action == "delete":
        if args.filePath is None:
            print("Error: Please provide a file path.")
        else:
            moveToTrash(args.filePath)
    elif args.action == "empty":
        emptyTrashCan()


if __name__ == "__main__":
    createTrashCan()
    main()

# Let me iterate then I will update it.
