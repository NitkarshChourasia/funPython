# def myFunc(x):
#     a = lambda b: x * b
#     return a
#
#
# myDoubler = myFunc(2)
# myTripler = myFunc(3)
# myQuad = myFunc(4)
#
# print(myDoubler(10))
# print(myTripler(10))
# print(myQuad(10))


# rangeRevenge = [x for x in range(1, 10 + 1)]


# even1 = list(filter(lambda x: x % 2 == 0, rangeRevenge))
#
# odd1 = list(filter(lambda x: x % 2 != 0, rangeRevenge))
#
# print(even1)
# print(odd1)
#
# import datetime
#
# now = datetime.datetime.now()
# print(now.time())
#
# print(f"The year is: {now.year}")
# print(f"The month is: {now.month}")
# print(f"The day is: {now.day}")
#
# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# time = lambda x: x.time()
#
# print(year(now))
# print(month(now))
# print(day(now))
# print(time(now))
# # print(datetime.datetime.now.time())
# print(now.time())
#
# string1 = "123123123"
# string2 = "123123abc"
#
# isNumber = lambda x: str((abs(int(x.replace(".", "", 1))))).isnumeric() if "." in x else str((abs(int(x)))).isnumeric()
#
# print(isNumber(string1))
# print(isNumber(string2))
# print(isNumber("-12313123"))
# print(isNumber("-131.1321313"))
#
#
# def longestCommonPrefix(strs):
#     first = strs[0]
#     last = strs[-1]
#     i = 0
#     while i < len(first) and i < len(last) and first[i] == last[i]:
#         i += 1
#     if i > 0:
#         return strs[0][:i]
#     else:
#         return ""
#
#
# print(longestCommonPrefix(["flower", "flow", "flinge"]))
# list2 = ["aaa", "aa", "aaa"]
# print(list2)
# list2.sort()
# print(list2)

# import requests
#
# username = input("Enter the github username:")
# request = requests.get('https://api.github.com/users/' + username + '/repos')
# json = request.json()
# for i in range(0, len(json)):
#     print("Project Number:", i + 1)
#     print("Project Name:", json[i]['name'])
#     print("Project URL:", json[i]['svn_url'], "\n")


import requests

username = "NitkarshChourasia"
response = requests.get(f"https://api.github.com/users/{username}/repos?sort=updated&per_page=100&page=1")
repositories = response.json()

# Check if there are more pages and retrieve repositories from additional pages
page = 2
while "next" in response.links:
    response = requests.get(response.links["next"]["url"])
    repositories.extend(response.json())
    page += 1

# Prepare the list of repository names
repository_list = [repo["name"] for repo in repositories]

# Write the repository list to a text file
with open("repository_lst_final.txt", "w") as file:
    file.write("\n".join(repository_list))

print("Repository list saved to repository_list.txt")

for i in range(0, len(repositories)):
    print("Project Number:", i + 1)
    print("Project Name:", repositories[i]['name'])
    print("Project URL:", repositories[i]['svn_url'], "\n")
#### Categorise according to the repository type.
#### Want to add, Repository type.
#### Print that type, too.
#### Output with much more detail. To the text file.

# Functionalities it should have is load all the repo.
# Make it listed and detailed.
# Make it export file.
