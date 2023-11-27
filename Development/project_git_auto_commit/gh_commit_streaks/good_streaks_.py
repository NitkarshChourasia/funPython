# Importing necessary modules
import os
from random import randint


class GitCommitSimulator:
    """
    A class used to simulate git commits.

    ...

    Attributes
    ----------
    total_days : int
        The total number of days for which commits are to be simulated.
    max_commits_per_day : int
        The maximum number of commits that can be simulated in a day.

    Methods
    -------
    simulate_commits():
        Simulates the commits for the specified number of days. Returns None.
    """

    def __init__(self, total_days: int, max_commits_per_day: int):
        """
        Constructs all the necessary attributes for the GitCommitSimulator object.

        Parameters
        ----------
            total_days : int
                The total number of days for which commits are to be simulated.
            max_commits_per_day : int
                The maximum number of commits that can be simulated in a day.

        Returns
        -------
        None
        """

        self.total_days = total_days
        self.max_commits_per_day = max_commits_per_day

    def simulate_commits(self) -> None:
        """
        Simulates the commits for the specified number of days.

        Returns
        -------
        None
        """

        for day in range(1, self.total_days + 1):
            for commit in range(0, randint(1, self.max_commits_per_day)):
                self._write_day_to_file(day)
                self._make_git_commit(day)
        self._push_commits_to_repository()

    def _write_day_to_file(self, day: int) -> None:
        """
        Writes the day to the file.

        Parameters
        ----------
            day : int
                The current day.

        Returns
        -------
        None
        """

        with open("file.txt", "a") as file:  # What does this a do?
            file.write(f"{day} days ago\n")

    def _make_git_commit(self, day: int) -> None:
        """
        Adds the changes and commits them with a random message.

        Parameters
        ----------
            day : int
                The current day.

        Returns
        -------
        None
        """

        os.system("git add .")
        os.system(f'git commit --date="{day} days ago" -m "commit {randint(1,99999)}"')

    def _push_commits_to_repository(self) -> None:
        """
        Pushes the commits to the main branch of the origin remote.

        Returns
        -------
        None
        """

        os.system("git push -u origin main")


# Usage
# commit_simulator = GitCommitSimulator(total_days=365 * 2, max_commits_per_day=10000)
# commit_simulator.simulate_commits()
# TODO: Take days and per day commits as input from user.
