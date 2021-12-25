def thesaurus(*args):
    namelist=list(map(str,args))
    dict_names={}
    for name in namelist:
        first_letter=name[0]
        dict_names[first_letter]=dict_names.get(first_letter,[])+[name]
    return print(dict_names)
thesaurus("Артур","Артём","Иван","Мария","Петр","Илья","Михаил","Григорий","георгий")