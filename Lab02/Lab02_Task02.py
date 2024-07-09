import matplotlib.pyplot as plt

class SmartphoneInventoryManager:
    def __init__(self, average_price, critical_stock_level, discount_threshold, order_quantity, minimum_order):
        # Initialize with parameters
        self.average_price = average_price
        self.critical_stock_level = critical_stock_level
        self.discount_threshold = discount_threshold
        self.order_quantity = order_quantity
        self.minimum_order = minimum_order
        
        # Initialize current state variables
        self.stock_level = 0
        self.current_price = 0
        
        # Initialize history to track changes over time
        self.history = {'price': [], 'stock': []}

    def update_price(self, price):
        # Update current price and add to history
        self.current_price = price
        self.history['price'].append(price)

    def update_stock(self, quantity):
        # Update current stock level and add to history
        self.stock_level = quantity
        self.history['stock'].append(quantity)

    def decide_order(self):
        # Determine the quantity to order based on current conditions
        tobuy = 0
        discount_price = self.average_price * (1 - self.discount_threshold)
        
        if self.current_price < discount_price:
            if self.stock_level < self.critical_stock_level:
                tobuy = self.minimum_order  # Place minimum order if below critical stock
            else:
                tobuy = self.order_quantity  # Place regular order if not below critical stock
        elif self.stock_level < self.critical_stock_level:
            tobuy = self.minimum_order  # Place minimum order if price not discounted but below critical stock

        return tobuy

    def plot_history(self):
        # Plot price and stock level history over time
        plt.figure(figsize=(10, 5))
        plt.plot(self.history['price'], label='Price')
        plt.plot(self.history['stock'], label='Stock Level')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Smartphone Price and Stock Level Over Time')
        plt.legend()
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define initial parameters
    average_price = 600
    critical_stock_level = 10
    discount_threshold = 0.2
    order_quantity = 15
    minimum_order = 10

    # Create an instance of SmartphoneInventoryManager
    manager = SmartphoneInventoryManager(average_price, critical_stock_level, discount_threshold, order_quantity, minimum_order)
    
    # Simulate updates over time
    prices = [620, 580, 540, 500, 560]
    stocks = [25, 20, 15, 10, 5]
    
    for price, stock in zip(prices, stocks):
        # Update price and stock level
        manager.update_price(price)
        manager.update_stock(stock)
        
        # Determine order quantity based on current conditions
        order = manager.decide_order()
        
        # Print current state and decision
        print(f"Current Price: {price}, Current Stock: {stock}, Order: {order}")
        
    # Plot the history of price and stock level changes
    manager.plot_history()
