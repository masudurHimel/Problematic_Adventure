from bdshare import *
from datetime import datetime, timedelta
import sys


def get_stock_floor_price(stock_name=None, count=5):
    if not stock_name:
        return False
    end = datetime.now().date() - timedelta(days=1)
    start = end - timedelta(days=15)
    df = get_hist_data(start, end, stock_name)
    result = 0
    for close_price in df['close'][:5]:
        result += float(close_price)
    result = result / count
    return "{:.2f}".format(result)


if __name__ == "__main__":
    floor_price = get_stock_floor_price(stock_name=sys.argv)
    if floor_price:
        print(floor_price)
    else:
        print("Validation Error!")
