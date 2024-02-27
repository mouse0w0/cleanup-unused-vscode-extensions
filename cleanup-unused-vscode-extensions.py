import os
import os.path as path
import json
import shutil

print("WARNING: This script will delete unused extension directories. Press enter to continue.")
input()

extensionsDir = path.join(path.expanduser("~"), ".vscode", "extensions")

if not path.exists(extensionsDir):
    print("VSCode extensions directory not exists")
    exit(0)

extensionsFile = path.join(extensionsDir, "extensions.json")

with open(extensionsFile, "r") as file:
    extensions = json.load(file)

ignoreExtensionRelativePaths = set()

for extension in extensions:
    ignoreExtensionRelativePaths.add(extension["relativeLocation"])

for relativePath in os.listdir(extensionsDir):
    absolutePath = path.join(extensionsDir, relativePath)
    if path.isdir(absolutePath) and not ignoreExtensionRelativePaths.__contains__(relativePath):
        print("Delete unused extension directory: " + absolutePath)
        shutil.rmtree(absolutePath)

print("Done")