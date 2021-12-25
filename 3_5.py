from  random import  randrange
def get_jokes(n):
    joke_list=[]
    for _ in range(n):
        joke =' '.join([nouns[randrange(len(nouns))],adv[randrange(len(adv))],adj[randrange(len(adj))]])
        joke_list.append(joke)
    print(joke_list)
nouns=["автомобиль","лес","огонь","город","дом","столб","монитор"]
adv=["сегодня","вчера","завтра","позавчера","ночью","днём","послезавтра"]
adj=["веселый","яркий","зелёный","утопичный","мягкий","красный","грустный"]
get_jokes(10)