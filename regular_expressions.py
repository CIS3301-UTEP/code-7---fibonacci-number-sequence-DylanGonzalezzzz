import re

file_object = open("social_media_users.csv")

print(file_object)

text_from_file = file_object.read()

emails = re.findall('[a-z]+@[a-z]+\.com',text_from_file)
print(emails)

are_emails = re.search('[a-z+@gmail]')