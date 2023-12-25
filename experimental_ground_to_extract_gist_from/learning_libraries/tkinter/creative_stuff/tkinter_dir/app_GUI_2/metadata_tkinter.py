# Always check the metadata before applying.
class Metadata:
    def __init__(self):
        # Author Information
        self.author_name = "Nitkarsh Chourasia"
        self.author_email = "playnitkarsh@gmail.com"
        self.gh_profile_url = "https://github.com/NitkarshChourasia"
        self.gh_username = "NitkarshChourasia"

        # Project Information
        self.project_name = "Simple Calculator"
        self.project_description = (
            "A simple calculator app made using Python and Tkinter."
        )
        self.project_creation_date = "30-09-2023"
        self.project_version = "1.0.0"

        # Edits
        self.original_author = "Nitkarsh Chourasia"
        self.original_author_email = "playnitkarsh@gmail.com"
        self.last_edit_date = "30-09-2023"
        self.last_edit_author = "Nitkarsh Chourasia"
        self.last_edit_author_email = "playnitkarsh@gmail.com"
        self.last_edit_author_gh_profile_url = "https://github.com/NitkarshChourasia"
        self.last_edit_author_gh_username = "NitkarshChourasia"

    def display_author_info(self):
        """Display author information."""
        print(f"Author Name: {self.author_name}")
        print(f"Author Email: {self.author_email}")
        print(f"GitHub Profile URL: {self.gh_profile_url}")
        print(f"GitHub Username: {self.gh_username}")

    def display_project_info(self):
        """Display project information."""
        print(f"Project Name: {self.project_name}")
        print(f"Project Description: {self.project_description}")
        print(f"Project Creation Date: {self.project_creation_date}")
        print(f"Project Version: {self.project_version}")

    def display_edit_info(self):
        """Display edit information."""
        print(f"Original Author: {self.original_author}")
        print(f"Original Author Email: {self.original_author_email}")
        print(f"Last Edit Date: {self.last_edit_date}")
        print(f"Last Edit Author: {self.last_edit_author}")
        print(f"Last Edit Author Email: {self.last_edit_author_email}")
        print(
            f"Last Edit Author GitHub Profile URL: {self.last_edit_author_gh_profile_url}"
        )
        print(f"Last Edit Author GitHub Username: {self.last_edit_author_gh_username}")

    def open_github_profile(self):
        """Open GitHub Profile."""
        import webbrowser

        webbrowser.open(self.gh_profile_url)

    def open_github_profile(self) -> None:
        """Open the author's GitHub profile in a new tab."""
        import webbrowser

        return webbrowser.open_new_tab(self.gh_profile_url)


# Example usage:
metadata = Metadata()

# Display author information
metadata.display_author_info()

# Display project information
metadata.display_project_info()

# Display edit information
metadata.display_edit_info()
