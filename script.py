import os
import sys


def create_paths() -> list[str]:
    return [f"{os.path.abspath('.')}/{i}" for i in os.listdir() if "." not in i]


def rename_all():
    files_vanilla = [i for i in os.listdir() if i[0] != "."]
    print(files_vanilla)

    files_new = [
        i.replace(" ", "_")
        .replace("-", "")
        .replace("___", "-")
        .replace("__", "_")
        .lstrip()
        for i in os.listdir()
        if i[0] != "."
    ]
    for i, v in enumerate(files_vanilla):
        # print(files_vanilla[i], files_new[i])
        os.rename(files_vanilla[i], files_new[i])


def recursion():
    rename_all()
    paths = create_paths()
    for path in paths:
        os.chdir(path)
        recursion()


# rename_all()
def main():
    recursion()


if __name__ == "__main__":
    main()
