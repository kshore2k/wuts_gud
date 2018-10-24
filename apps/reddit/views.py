from django.shortcuts import render, HttpResponse, redirect

import praw


mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]


mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]


def mobileBrowser(request):
    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
 
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True
 
    return mobile_browser



def index(request):
    if mobileBrowser(request):
        temp = 'reddit/m_index.html'
    else:
        temp = 'reddit/index.html'
    return render(request,temp)

def news(request):
    reddit = praw.Reddit(client_id = 'yCZy9qTv6HOciw', client_secret = 'Mq7dRceUdWpeLUigbX7U_Wedk44', username = 'deadbeat253' , password = 'Billionaire710', user_agent = 'prawtest')

    subreddit = reddit.subreddit('UpliftingNews')

    hot_news = subreddit.hot(limit=50)

    for submission in hot_news:
        if not submission.stickied:
                context = {
                    'hot_news' : hot_news,
                }

                return render(request,"reddit/news.html", context)

def tech(request):
    reddit = praw.Reddit(client_id = 'yCZy9qTv6HOciw', client_secret = 'Mq7dRceUdWpeLUigbX7U_Wedk44', username = 'deadbeat253' , password = 'Billionaire710', user_agent = 'prawtest')

    subreddit = reddit.subreddit('AmazingTechnology')

    hot_news = subreddit.hot(limit=50)

    for submission in hot_news:
        if not submission.stickied:
                context = {
                    'hot_news' : hot_news,
                }

                return render(request,"reddit/tech.html", context)

def habits(request):
    reddit = praw.Reddit(client_id = 'yCZy9qTv6HOciw', client_secret = 'Mq7dRceUdWpeLUigbX7U_Wedk44', username = 'deadbeat253' , password = 'Billionaire710', user_agent = 'prawtest')

    subreddit = reddit.subreddit('GetMotivated')

    hot_news = subreddit.hot(limit=50)

    for submission in hot_news:
        if not submission.stickied:
                context = {
                    'hot_news' : hot_news,
                }

                return render(request,"reddit/habits.html", context)

def quotes(request):
    reddit = praw.Reddit(client_id = 'yCZy9qTv6HOciw', client_secret = 'Mq7dRceUdWpeLUigbX7U_Wedk44', username = 'deadbeat253' , password = 'Billionaire710', user_agent = 'prawtest')

    subreddit = reddit.subreddit('quotesporn')

    hot_news = subreddit.hot(limit=50)

    for submission in hot_news:
        if not submission.stickied:
                context = {
                    'hot_news' : hot_news,
                }

                return render(request,"reddit/quotes.html", context)






