# Mod Runner
### © Heights studios© all rights reserved
https://github.com/redbuttontheare/modruner

#### How to create and read cookies?

from Creator.Create import create_cookie as cookie
from Creator.Mod import writer as wr

with open("test_cookie.data", "r+") as f:
    data = f.readlines()

wr(f"your last cokie: {data}")
wr("insert a text please")
cook = "test_cookie"
text = input()

cookie(cook, text)
