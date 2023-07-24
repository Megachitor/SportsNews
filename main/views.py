from django.shortcuts import render
import requests
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView
from datetime import date as dt
import datetime
from datetime import timezone, timedelta
# from .api import *

# Create your views here.

def home(request):

    matchq = Match.objects.all().order_by('date')[:5]
    table = Standings.objects.all().order_by('rank')
    news = News.objects.all().order_by('date')[:4]
    match_new = Match.objects.all().order_by('date')[:1]
    random_players = Player.objects.all().order_by('?')[:4]
    matchito = Match.objects.all().order_by('date')[:10]



    # Updating Standings Table which updates every hour
    #####################################################################################
    headers = {
        "X-Apisports-Key": "56afa8bb967f6e0ea1f68cfc0ac59c8d",
    }

    url = 'https://v3.football.api-sports.io/standings?league=39&season=2023'

    get_time = LastUpdated.objects.get(name="Matchs") # Lastupdate is a model which help to check and compare the dates
    now = datetime.datetime.now(tz=timezone(timedelta(hours=0)))

    if now < get_time.time: # if now is less than given time it wioll not update
        pass

    elif get_time.time < now:

        standings =  requests.get(url, headers=headers).json()['response'][0]['league']['standings'] # getting standings from api
        standings = standings[0]

        for stand in standings:
            # filtering the data and giving them values
            rank = stand['rank']
            name = stand['team']['name']
            played = stand['all']['played']
            won = stand['all']['win']
            lost = stand['all']['lose']

            trem = Club.objects.get(name = name)

            teem = Standings.objects.get(team=trem)

            # to check does the position of the team has changed or not

            if teem.rank == rank and teem.played == played and teem.won == won and teem.lost == lost:

                continue
            
            # if it has changed so we update it

            else:
                team = Club.objects.get(name=name)

                Standings.objects.filter(team=team).update(
                    rank = rank,
                    team = team,
                    played = played,
                    won = won,
                    lost = lost
                )



        url2 = 'https://v3.football.api-sports.io//fixtures?league=39&season=2023&status=NS'

        fixtures =  requests.get(url2, headers=headers).json()['response'] # All fixtures

        # Getting info from json api

        for match in fixtures:
            home = match['teams']['home']['name']
            away = match['teams']['away']['name']
            index = match['fixture']['id']
            datestr = match['fixture']['date']
            datestr = str(datestr)



            # Getting date from api and trasnforming it to datetime
            year = int(datestr[:4])
            month = int(datestr[5:7])
            day = int(datestr[8:10])
            hour = int(datestr[11:13])
            minute = int(datestr[14:16])

            date1 = datetime.datetime(year, month, day, hour, minute,tzinfo=timezone(timedelta(hours=0)))

            matchss = Match.objects.all()

            check = 1
            for match2 in matchss:  # it checkes whether the match is existing or not
                if match2.index == index:
                    check = 0
                    break

                else:
                    check = 1
            

            if check == 0 and date1 < now: # If there is A match with outdated game it will be deleted

                Match.objects.filter(index=index).delete()

            elif check == 1: # If there is no such a match with the fixture id it will be created

                team1 = Club.objects.get(name = home)
                team2 = Club.objects.get(name = away)


                obj = Match.objects.create(
                    home = team1,
                    away = team2,
                    date = date1,
                    index = index
                )

                obj.save()
    
        datess = get_time.time + timedelta(hours=1)

        LastUpdated.objects.filter(name="Matchs").update(time = datess)

    contect = {
        'matches':matchq,
        'table':table,
        'news':news,
        'new_match':match_new,
        'rand': random_players,"matchito":matchito
    }

    return render(request, 'index.html', context=contect)

def about(request):

    matchito = Match.objects.all().order_by('date')[:10]


    

    return render(request, 'about.html',{'matchito':matchito})

def news(request):
    matchito = Match.objects.all().order_by('date')[:10]

    today = dt.today()
    today = str(today)
    num = int(today[8:10])
    num = num - 1
    k = today[:8]
    today = ''
    today = str(k)+str(num)
    
    url = f'https://newsdata.io/api/1/news?apikey=pub_26571ed02f5bf509ef5a95f45c5b20d48cb3d&q=football&language=en'

    response = requests.get(url).json()

    article = response['results'][0]

    art2 = News.objects.all().order_by('-date')

    check = 1

    for info in art2:
        # print('1a')

        if info.source == article['link']:
            check = 0
            # print('aaaa')
            break
        else:
            # print('2a')
            check = 1

    if check == 1:
        name = article['title']
        description = article['description']
        url = article['link']
        image = article['image_url']
        content = article['content']
        datestr = article['pubDate']

        year = int(datestr[:4])
        month = int(datestr[5:7])
        day = int(datestr[8:10])
        hour = int(datestr[11:13])
        minute = int(datestr[14:16])

        date = datetime.datetime(year, month, day, hour, minute)

        obj = News.objects.create(
            name = name,
            description = description,
            source = url,
            image_url = image,
            content = content,
            date = date,
        )
        print(obj)
        obj.save()

    content = {
        'news' : art2,'matchito':matchito
    }

    return render(request, 'news.html', context=content)

def team(request):
    matchito = Match.objects.all().order_by('date')[:10]
    


    # Taking from api and saving to the models
    # ALERT: USE IT IF U NEED TO REFRESH "Club" AND "Players" MODELS
    ####################################################################
    # headers = {
    #     "X-Apisports-Key": "56afa8bb967f6e0ea1f68cfc0ac59c8d",
    # }
    # url1 = f'https://v3.football.api-sports.io/teams?league=39&season=2023'

    # teams = requests.get(url1, headers=headers).json()['response']
    # print(teams)
    # for id in range(len(teams)):
    #     name1 = teams[id]['team']['name']
    #     code1 = teams[id]['team']['code']
    #     id1 = int(teams[id]['team']['id'])
    #     logo_url = teams[id]['team']['logo']

    #     obj = Club.objects.create(
    #         name=name1,
    #         code=code1,
    #         index=id1,
    #         image=logo_url
    #     )
    #     obj.save()

    #     url2 = f'https://v3.football.api-sports.io//players/squads?team={id1}'

    #     players = requests.get(url2, headers=headers).json()['response'][0]['players']
    #     club1 = Club.objects.get(index = id1)

    #     for player in players:
    #         index1 = player['id']
    #         name = player['name']
    #         age = player['age']
    #         number = player['number']
    #         position = player['position']
    #         image = player['photo']

    #         obj2 = Player.objects.create(
    #             name = name,
    #             age = age,
    #             number = number,
    #             position = position,
    #             index = index1,
    #             club = club1,
    #             image = image
    #         )
    #         obj2.save()


    # print(teams)

    # /players/squads?team=33


    teams = Club.objects.all()



    content = {
        'teams':teams,
        'matchito':matchito
    }

    return render(request, 'team.html', context=content)

def blog(request):
    matchito = Match.objects.all().order_by('date')[:10]
    matchq = Match.objects.all().order_by('date')[:5]
    table = Standings.objects.all().order_by('rank')

    posts = Post.objects.all

    content = {
        # 'page': page,
        'posts': posts,'matchito':matchito, 'table':table, 'matches':matchq
    }

    return render(request, 'blog.html', context=content)

def contact(request):
    matchito = Match.objects.all().order_by('date')[:10]

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()


    else:

        form = ContactForm()


    return render(request, 'contact.html', {'form':form,'matchito':matchito})

def single(request, id):
    matchito = Match.objects.all().order_by('date')[:10]

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()

    else:

        form = CommentForm()

    post=Post.objects.get(id=id)
    comment = Comment.objects.filter(post = post.id)
    user = request.user
    # print(user.pk)

    content = {
        'post':post,
        'comments':comment,
        'form':form,
        'user':user
    }


    return render(request, 'single.html', context=content)

def login(request):

    matchito = Match.objects.all().order_by('date')[:10]


    return render(request, 'registration/login.html',{'matchito':matchito})


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    print(form_class)   


def base(request):

    matchito = Match.objects.all().order_by('date')[:10]

    user = User.objects.all()
    context = {
        'user':user,
        'matches':matchito
    }

    return render(request, 'base.html',context=context)


def command(request, id):
    matchito = Match.objects.all().order_by('date')[:10]

    ckub = Club.objects.get(index = id)
    players = Player.objects.filter(club = ckub)


    content = {
        'players':players,
        'club':ckub,
        'matchito':matchito
    }

    return render(request, 'command.html', context=content)


# def player(request, id):

#     url = f'https://apiv2.allsportsapi.com/football/?&met=Players&playerId={id}&APIkey=c8d88be05f7272c3fe4f8cf199e313f35c47b513b0ce13a1152b1903c2953cec'
#     player = requests.get(url).json()['result'][1]



#     return render(request, 'player.html', {'player':player,'matchito':matchito})


def article(request, id):
    matchito = Match.objects.all().order_by('date')[:10]

    article = News.objects.get(id =id)

    content = {
        'article': article,
        'matchito':matchito
    }

    return render(request, 'article.html', context=content)
    