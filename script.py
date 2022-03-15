import os
import argparse


def create_paths():
    return [f"{os.path.abspath('.')}/{i}" for i in os.listdir() if "." not in i]


def rename_all():
    files_vanilla = [i for i in os.listdir() if i[0] != "."]
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
        os.rename(files_vanilla[i], files_new[i])


def recursion(
    path: str,
    recursive: bool,
):
    os.chdir(path)
    rename_all()
    if recursive:
        paths = create_paths()
        for p in paths:
            os.chdir(p)
            recursion(p, recursive)


def main():
    parser = argparse.ArgumentParser(
        description="Remove all spaces from the directory names and their child directories",
        allow_abbrev=False,
    )
    parser.add_argument(
        "-p", "--path", type=str, help="The path of the parent directory", required=True
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Specifies if child directories should also be renamed. Default is false",
    )
    args = parser.parse_args()
    print(args.path)

    recursion(args.path, args.recursive)


if __name__ == "__main__":
    main()
