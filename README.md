# selenium_web_scrape

## Catch Marketplace Black Friday Sale Product Analysis

This project aims to analyze products listed on **Catch's Black Friday Sale**. The data for the products was fetched using a **Selenium Chromium WebDriver** and cleaned using **BeautifulSoup**. The analysis focuses on various product metrics, including prices, brands, discounts, and ratings. We visualize the findings using **Plotly**.

## Getting Started

These instructions will guide you on setting up the project on your local machine for development and analysis.

### Prerequisites

- Python 3.x
- Libraries: `pandas`, `numpy`, `beautifulsoup4`, `plotly`, `selenium`, and `requests`.

You can install the necessary libraries using `pip`:

```bash
pip install pandas numpy beautifulsoup4 plotly selenium requests
```

Additionally, you will need to install the **Chrome WebDriver** for Selenium. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

### Web Scraping and Data Collection

To fetch the product details from the Black Friday sale page, we use **Selenium** with a Chrome WebDriver. The script simulates scrolling through the page to load more products, then collects product details like:

- **Product ID**
- **Name**
- **Brand**
- **Price**
- **RRP (Recommended Retail Price)**
- **Discount Labels**
- **Product URLs**
- **Image URLs**
- **Ratings**

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

s = Service("C:/path/to/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.catch.com.au/event/black-friday-sale-185091/')

# Code to scroll and fetch product details...
```

The products are saved as an HTML file (`catch-black-friday.html`) for further analysis.

### Data Cleanup and Analysis

After fetching the HTML, the data is parsed using **BeautifulSoup** and stored in a pandas DataFrame. The following columns are extracted:

- **Product_Id**
- **Name**
- **Brand**
- **Price**
- **RRP**
- **Discount_Label**
- **Product_URL**
- **Image_URL**
- **Stars**
- **Rating**

#### Price Column Cleanup

The `Price` column is cleaned to remove any non-numeric characters, and the column is converted to a float type for further analysis:

```python
df['Price'] = df['Price'].str.replace(r'[^\d.]', '', regex=True).astype(float)
```

#### RRP Column Cleanup

For the `RRP` (Recommended Retail Price) column, a custom function is applied to handle various formats such as "Save $X". This ensures the RRP column reflects accurate values:

```python
def update_rrp(row):
    if 'Save' in row['RRP']:
        numeric_part = float(re.sub(r'[^\d.]', '', row['RRP'].replace('Save $', '').strip()))
        return row['Price'] + numeric_part
    else:
        return pd.to_numeric(re.sub(r'[^\d.]', '', row['RRP']), errors='coerce')

df['RRP'] = df.apply(update_rrp, axis=1)
```

#### Discount Calculation

The `discount` column is calculated as the difference between `RRP` and `Price`, and the `discount_percentage` is computed based on these values:

```python
df['discount'] =  df['RRP'] - df['Price']
df['discount_percentage'] = df['discount'] / df['RRP'] * 100
```

### Data Analysis and Visualization

We perform a few analyses, such as identifying the brands with the most products on sale, and displaying the results in a bar plot using **Plotly**:

```python
df_brands = df.groupby('Brand')['Product_Id'].count().sort_values(ascending=False).head(10)
px.bar(df_brands)
```

The top products with the highest discount percentages are also sorted and displayed:

```python
df.sort_values(by='discount_percentage', ascending=False).head(20)
```

## Usage

1. **Scrape the data**: Run the Selenium script to fetch product data.
2. **Clean and analyze the data**: Use the pandas code to process the HTML data and perform analysis.
3. **Visualize the results**: Use Plotly for interactive graphs.

## Future Improvements

- Automate the scraping and analysis process with scheduled runs.
- Expand the analysis to other sales events or marketplaces.
- Implement more advanced visualizations and insights (e.g., time series analysis of price trends).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
