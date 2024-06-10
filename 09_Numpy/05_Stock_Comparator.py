import yfinance as yf
import matplotlib.pyplot as plt

class StockComparator:

    #Constructor to initialize the StockComparator object.
    def __init__(self, tickers : list[str], 
                 start_date : str, 
                 end_date : str):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date

        #download from yahoo finance
        self.data = yf.download(self.tickers, self.start_date, 
                                self.end_date)["Adj Close"]
    
    def plot_stock_comparison(self):
        
        #set the canvas
        plt.figure(figsize=(14, 7))

        #iterate through the downloaded data and plot chart
        for ticker in self.tickers:
            plt.plot( self.data[ticker], label=ticker)
        
        #Define the chart title
        plt.title(f"Stock prices of : {self.tickers} between {self.start_date} and {self.end_date}")
        #Define the X axis label
        plt.xlabel("Date")
        #Define the Y Label
        plt.ylabel("Closing price")
        plt.legend()
        #Display grid lines.
        plt.grid(True)
        plt.show()

def test_classes():
    stock_list = []
    flag = True

    while(flag):
        stock_to_be_compared = input("Please enter the stock symbol : ")
        #add to stock list
        stock_list.append(stock_to_be_compared)
        #seek user input to check if he want to add more
        to_continue = input("Do you want to add more (y/n) : ")
        if (to_continue == "n"):
            break

    #seek start date
    start_date = input("enter start date in yyyy-mm-dd : ")
    #seek end date
    end_date = input("enter end date in yyyy-mm-dd : ")

    #Initialize StockComparator object
    stock_comparator = StockComparator(stock_list, start_date, end_date)

    #Plot the graph
    stock_comparator.plot_stock_comparison()

if __name__ == "__main__":
    test_classes()
