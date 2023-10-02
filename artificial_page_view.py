import urllib.request
import time

def visit_link(url, count):
    for _ in range(count):
        print(_)
        time.sleep(1)
        urllib.request.urlopen(url)

# Example usage
link = "https://github.com/maityamit"  # Replace with your desired link
visit_count = 1000  # Replace with the desired number of visits

visit_link(link, visit_count)


# Will develop it further to make it more robust and useful