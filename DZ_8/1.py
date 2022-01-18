import re


def email_parse(email):
    check = re.match(r'\w+\@\w+\.\w+', email)
    if check:
        pars = re.split(r'@', email)
        print({'username': pars[0], 'domain': pars[1]})
    else:
        raise ValueError(f'wrong email:{email}')


email_parse('someone21@geekbrains.ru')
