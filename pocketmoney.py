import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set the pocket money for every month
pocket_money_per_month = 2000

# Customized spending categories and percentages
spending_categories = ['Shopping', 'Movies', 'Food', 'Technology', 'Charitable Contributions', 'Miscellaneous']
spending_percentages = [0.11, 0.05, 0.10, 0.45, 0.10, 0.19]  # Ensure the percentages sum to 1

# Generating amounts for each category based on percentages
amounts = np.round(pocket_money_per_month * np.array(spending_percentages))

# Generating repeated months for 12 months
months = np.tile(
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
     'December'], 2)[:len(amounts)]

# Create the structured array
pocket_money_data = np.array(list(zip(amounts, spending_categories, months)),
                             dtype=[('amount', float), ('category', 'U25'), ('month', 'U10')])

# Aggregation by category
category_sums = {category: np.sum(pocket_money_data['amount'][pocket_money_data['category'] == category]) for category
                 in np.unique(pocket_money_data['category'])}


# Function to update the plot during animation
def update(frame):
    plt.clf()

    # Pie chart with thickness and "glassy" effect
    plt.pie(category_sums.values(), labels=category_sums.keys(), autopct='%1.1f%%', startangle=frame,
            wedgeprops=dict(width=0.3, edgecolor='black', linewidth=1.5), colors=plt.cm.Paired.colors)

    plt.title('Pocket Money Spendings')
    plt.annotate('@Sudheer Debbati', xy=(0.5, 0.5), xytext=(0, 0), ha='center', va='center', fontsize=12, color='black',
                 fontweight='bold')


# Create the animation
animation = FuncAnimation(plt.figure(figsize=(8, 8)), update, frames=np.arange(0, 360, 5), interval=500)

plt.show()






