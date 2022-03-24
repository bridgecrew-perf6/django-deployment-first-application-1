from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'NewsApp/index.html')
def indianews (request):
    dict1={'mainmsg':'India News Page',
           'submsg1':'100+ crores vaccines successfully done!!!',
           'submsg2':'India is super-power in the world',
           'submsg3':'Agni-5 long-range missile(20000kms) successfully tested!!!',
           'photo':'images/image1.jpg'};
    return render(request,'NewsApp/news.html',context=dict1);

def sportsnews (request):
    dict1={'mainmsg':'Sports News Page',
           'submsg1':'India won By Cricket World Cup 2023',
           'submsg2':'World Olmpic India Gold Count 500(Tops-List)',
           'submsg3':'India to host next Olymoics for 5-times',
           'photo':'images/image2.jpg'};
    return render(request,'NewsApp/news.html',context=dict1);

def technews (request):
    dict1={'mainmsg':'Technology News Page',
           'submsg1':'Apple to release Apple-14 in 4-models(mini,basic,pro,pro-max)',
           'submsg2':'India Starts Semi-Conductor chips to world Smartphones',
           'submsg3':'Tech-jobs more in India than elsewhere in the world',
           'photo':'images/image3.jpg'};
    return render(request,'NewsApp/news.html',context=dict1);