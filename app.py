
import requests
from datetime import date, timedelta   
from pprint import pprint
from prettytable import PrettyTable

sender_email = "xyz@abc.com"
receiver_email = "opq@abc.com"
subject = "An email with Pull request detail"

print('From','-',sender_email)
print('To','-',receiver_email)
print('Subject','-',subject)

table = PrettyTable()
table.field_names = ["PR Title", "PR Number", "Created Date", "State"]

url = "https://api.github.com/repos/newren/git-filter-repo/pulls"
params = {
    "state": "all",
    "per_page": "100",
    "page": 1,
}
res=requests.get(url, params=params)
repos=res.json()
while 'next' in res.links.keys():
  res=requests.get(res.links['next']['url'])
  repos.extend(res.json())

#timestamp
today = date.today()
week_prior =  today - timedelta(weeks=1)
week_prior= week_prior.strftime("%Y-%m-%dT%H:%M:%SZ")

for repo in repos:
    table.add_row([repo["title"], repo["number"], repo["created_at"], repo["state"]])
print(table)

