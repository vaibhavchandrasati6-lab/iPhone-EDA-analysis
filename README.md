📱 iPhone Products Data Analysis (EDA)

A complete Exploratory Data Analysis (EDA) project on the iPhone products dataset to uncover pricing trends, rating patterns, discount impact, and product popularity.

This project demonstrates practical use of Pandas, NumPy, Matplotlib, and Seaborn for real-world product data analysis.

📌 Objective

The objective of this project is to analyze iPhone product data and extract meaningful insights such as:

1.Identifying top-rated iPhones

2.Understanding pricing distribution

3.Finding most & least expensive models

4.Analyzing relationship between ratings and price

5.Studying the impact of discounts on product popularity

📂 Project Structure
iPhone-EDA-analysis/
│
├── apple_products.csv
├── iphone_analysis.py
├── images/
├── requirements.txt
└── README.md

🛠 Technologies Used

Python 3.x

NumPy

Pandas

Matplotlib

Seaborn

🧹 Data Cleaning Performed

1.Cleaned RAM column (e.g., "8 GB" → 8)

2.Converted RAM column to integer datatype

3.Checked data types and null values

4.Sorted products based on ratings

5.Identified extreme values using idxmax() and idxmin()

📊 Business Questions Answered

1️⃣ Which are the top 10 highest-rated iPhones?

2️⃣ Which iPhone is the most expensive?

3️⃣ Which iPhone is the least expensive?

4️⃣ Is there a relationship between number of ratings and sale price?

5️⃣ Does discount percentage influence product popularity?

📈 Analysis & Visualizations

1.Top 10 highest-rated iPhones (Sorting & Filtering)

2.Scatter Plot: Number of Ratings vs Sale Price

3.Scatter Plot: Discount Percentage vs Number of Ratings

4.Identification of most & least expensive products

5.Popularity analysis using rating counts

🔎 Key Insights

1.Highly rated iPhones are not always the most expensive ones.

2.Discount percentage may influence the number of ratings.

3.Some models receive significantly more customer engagement.

4.Pricing and popularity show observable trends.

▶ How to Run This Project
1️⃣ Clone the repository
git clone https://github.com/vaibhavchandrasati6-lab/iPhone-EDA-Project.git

2️⃣ Navigate to project folder
cd iPhone-EDA-Project

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the script
python iphone_analysis.py

🚀 Future Improvements

1.Add correlation heatmap

2.Perform feature comparison (RAM vs Price)

3.Create interactive dashboard (Streamlit)

4.Build price prediction model using ML

👨‍💻 Author

Vaibhav Chandra Sati

Aspiring Data Scientist | Python | Pandas | Data Visualization
