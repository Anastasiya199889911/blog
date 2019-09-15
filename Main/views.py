from django.shortcuts import render
from . import models

# Create your views here.
def Main(request):
    news1 = models.News.objects.all()
    news = []
    ch = False;
    for i in news1:
        new = []
        new.append(i.text)
        new.append(i.name)
        new.append(i.img_path)
        if (ch == False):
            new.append('active')
            ch = True
        else:
            new.append('')

        news.append(new)
    # print(news)
    news_slide = []
    cnt = len(news1)
    ch1 = False
    # print(cnt)
    i = 0
    while i < cnt:
        news_slide1 = []
        news_slide1.append(i)
        if ch1 == False:
            news_slide1.append('active')
        else:
            news_slide1.append('')
        news_slide.append(news_slide1)
        i = i + 1
    return render(request, 'Main.html', locals())