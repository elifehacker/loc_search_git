
black_list = ['@2x', 'png', 'jpg', 'wixpress', 'template', 'md.x', 'sentry','jpeg','@sm.x','-only', 'lodash','core-js-bundle','polyfill','yourdomain','react','wixofday','layout','accor','requirejs','test','example']
def find_word(email, black_list):
    if email[-2]=='.':
        return True
    for word in black_list:
        if word in email:
            return True
    return False
exist = set()
folders = ['18122020203137_sydn1_email','18122020205341_sydn2_email','18122020205428_sydn3_email','18122020210945_sydn4_email']
for f in folders:
    with open(f+"/emails.txt", "r") as file:
        for email in file:
            email = email.rstrip("\n")
            print(email)
            if email in exist:
                continue
            exist.add(email)
            if not find_word(email, black_list):
                with open("emails_filtered.txt", "a") as f:
                    f.write(email+'\n')
