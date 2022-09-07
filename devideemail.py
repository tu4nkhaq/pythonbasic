def email(emails):
    email_username=emails[0:emails.index("@")]
    email_domain=emails[emails.index("@")+1:]
    return(email_username,email_domain)
def printemail(email_username,email_domain):
    print(f"User name is {email_username}, email domain is {email_domain}")
def main():
    emails = input("Nhap email:").strip()
    email_username,email_domain=email(emails)
    printemail(email_username,email_domain)
if __name__ == "__main__":
    main()

