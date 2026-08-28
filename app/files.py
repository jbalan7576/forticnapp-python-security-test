import os


BASE_DIRECTORY = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "test-files"
)


def read_file(filename):
    # INTENTIONALLY VULNERABLE: CWE-22 Path Traversal
    filepath = os.path.join(BASE_DIRECTORY, filename)

    with open(filepath, "r") as file:
        return file.read()