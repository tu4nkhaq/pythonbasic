from devideemail import email,printemail
def main():
    emails=["fdf@gaidsanf.com","kjdkfhds@gmail.com","dkfdksfj@gmail.com","fidfi@akfdif","dkfjdfi@kdnfkdsjf","fjdsifjewi@9492"]
    for t in emails:
        email_username,email_domain=email(t)
        printemail(email_username,email_domain)
if __name__=="__main__":
    main()