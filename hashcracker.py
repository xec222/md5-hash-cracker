import hashlib

user_input = input('Enter md5 hash : ')
pass_list = input('Enter Path TO PASSWD list')

def file_open(pass_list):
    global
    try:
        password_doc = open(pass_list, "r")
    except:
        print("Thew is nO Files My Man")
        quit()
file_open(pass_list)

for word in password_doc:
    print("Trying: " + word.strip("/n"))
    encoded = word.encode('utf-8')
    md5_hash = hashlib.md5(encoded.strip().hexdigest())

    if md5_hash == user_input:
        print("Passwd Found : " + word)
        exit(0)
print("Passwd not in L sowwy")

