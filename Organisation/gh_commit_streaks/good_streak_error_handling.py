# Importing necessary modules
import os
import logging
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
    filename : str
        The name of the file to which the day is written.

    Methods
    -------
    simulate_commits():
        Simulates the commits for the specified number of days. Returns None.
    """

    def __init__(
        self, total_days: int, max_commits_per_day: int, filename: str = "file.txt"
    ):
        """
        Constructs all the necessary attributes for the GitCommitSimulator object.

        Parameters
        ----------
            total_days : int
                The total number of days for which commits are to be simulated.
            max_commits_per_day : int
                The maximum number of commits that can be simulated in a day.
            filename : str, optional
                The name of the file to which the day is written (default is 'file.txt').

        Returns
        -------
        None
        """

        self.total_days = total_days
        self.max_commits_per_day = max_commits_per_day
        self.filename = filename

    def simulate_commits(self) -> None:
        """
        Simulates the commits for the specified number of days.

        Returns
        -------
        None
        """

        try:
            for day in range(1, self.total_days + 1):
                for commit in range(0, randint(1, self.max_commits_per_day)):
                    self._write_day_to_file(day)
                    self._make_git_commit(day)

            self._push_commits_to_repository()
            logging.info("Successfully simulated git commits.")
        except Exception as e:
            logging.error(f"An error occurred while simulating git commits: {e}")

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

        try:
            with open(self.filename, "a") as file:
                file.write(f"{day} days ago\n")
            logging.info(f"Successfully wrote day {day} to file.")
        except Exception as e:
            logging.error(f"An error occurred while writing to file: {e}")

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

        try:
            os.system("git add .")
            os.system(
                f'git commit --date="{day} days ago" -m "commit {randint(1,99999)}"'  # This file name or whatever it is.
            )
            logging.info(f"Successfully made git commit for day {day}.")
        except Exception as e:
            logging.error(f"An error occurred while making git commit: {e}")

    def _push_commits_to_repository(self) -> None:
        """
        Pushes the commits to the main branch of the origin remote.

        Returns
        -------
        None
        """

        try:
            os.system("git push -u origin main")
            logging.info("Successfully pushed git commits to repository.")
        except Exception as e:
            logging.error(
                f"An error occurred while pushing git commits to repository: {e}"
            )


# Usage
logging.basicConfig(level=logging.INFO)
commit_simulator = GitCommitSimulator(total_days=365 * 2, max_commits_per_day=10)
commit_simulator.simulate_commits()


# Want rand num of commits per day? or fixed?
# let the user choose.
