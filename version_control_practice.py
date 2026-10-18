"""Module 6: Individual Git and GitHub Practice.

Run this starter program, complete the TODO tasks, and commit your changes.
No outside packages are required.
"""


def show_project_info():
    """Display basic information about this version-control exercise."""
    project_name = "Module 6 Activity"
    version = "1.1"
    print(f"Project: {project_name}")
    print(f"Version: {version}")
    print("Git helps track changes in a software project.")


def show_git_workflow():
    """Print the basic sequence used in this exercise."""
    steps = [
        "1. Edit and save your Python file.",
        "2. Stage your changes with git add.",
        "3. Record a local commit with git commit.",
        "4. Upload your commit to GitHub with git push.",
    ]
    for step in steps:
        print(step)


def main():
    show_project_info()
    print()
    show_git_workflow()
    print()

    # TODO: Add a print() statement below that explains, in your own words
    print("Git helps track changes so developers can review their work and restore earlier versions.")
    # TODO 3: Add another print() statement describing one difference
    #         between git commit and git push.
    print("git commit saves changes locally, while git push uploads it to github.")    


if __name__ == "__main__":
    main()
