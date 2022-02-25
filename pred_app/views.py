from django.shortcuts import render, redirect
from pred_app.lstm_prediction import *
from django.contrib import messages

# pk_e4c317db75c8461fb6c92a1ea3c0e496
# Browser request for home page, pass in dict


def baseN(request):
    import requests
    import json
    
    if request.method == 'POST':
        ticker = request.POST['ticker'] 
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_e4c317db75c8461fb6c92a1ea3c0e496")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'pred_app/homeN.html', {'api' : api}) 
    
    else:
        return render(request, 'pred_app/homeN.html', {'ticker' : "Enter a Stock Ticker Above, to get a quote."})

def news(request):
    import requests 
    import json
    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=7fbe44ccbd564351af262ff843fdb6d5")
    api=json.loads(news_api_request.content)
    return render(request,'pred_app/news.html',{'api':api})


# --------------- MAIN WEB PAGES -----------------------------


def redirect_root(request):
    return redirect('/pred_app/Home')

def Home(request):
    return render(request, 'pred_app/home.html')

def about(request):
    return render(request, 'pred_app/about.html')

def index(request):
	return render(request, 'pred_app/index.html') 

def pred(request):
    return render(request, 'pred_app/prediction.html')


def search(request, se, stock_symbol):
	import json
	predicted_result_df = lstm_prediction(se, stock_symbol)
	return render(request, 'pred_app/search.html', {"predicted_result_df": predicted_result_df})
# -----------------------------------------------------------