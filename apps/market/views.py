from django.shortcuts import render
from utils.fcoin3 import Fcoin
from utils.coineal import Coineal
# Create your views here.
def index():
    pass

def customer(request):
    customers = []
    return render(request, 'market/customer.html',{'customer_list': customers})

def dashboard(request):
    return render(request,'market/dashboard.html')

def market_depth(request):
    site = request.GET.get('site')
    first_coin = request.GET.get('first')
    second_coin = request.GET.get('second')
    if site != None:
        request.session['site'] = site
    else:
        site = request.session.get('site',None)
    if first_coin != None:
        request.session['first'] = first_coin
    else:
        first_coin = request.session.get('first',None)
    if second_coin != None:
        request.session['second'] = second_coin
    else:
        second_coin = request.session.get('second', None)
    if first_coin is None or second_coin is None:
        return render(request, 'market/error.html',{'error_msg':'不合法的币种对'})
    if site == 'fcoin':
        fcoin = Fcoin()
        rjson = fcoin.get_market_depth("L20", first_coin+second_coin)
        if rjson is None:
            return render(request, 'market/error.html', {'error_msg': '不合法的币种对'})
        bids = rjson['data']['bids']
        asks = rjson['data']['asks']
    elif site == 'coineal':
        coineal = Coineal()
        rjson = coineal.get_market_depth("step0", "btcusdt")
        bids = rjson['data']['tick']['bids']
        asks = rjson['data']['tick']['asks']
    elif site == None:
        bids = []
        asks = []
    bid_pairs = []
    ask_pairs = []
    for i in range(int(len(bids)/2)):
        bid_pairs.append([bids[2*i], bids[2*i + 1]])
    for i in range(int(len(asks)/2)):
        ask_pairs.append([asks[2*i], asks[2*i + 1]])

    return render(request, 'market/market_depth.html', {'bid_pairs': bid_pairs, 'ask_pairs': ask_pairs})
