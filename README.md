# PhonePe Transaction insight Dashboard
An interactive Streamlit-based analytical dashboard that explores and visualizes trends from the PhonePe Pulse dataset. This project is built to empower users, analysts, and business stakeholders with insights on digital payment transactions, user engagement, and insurance adoption patterns across Indian states, districts, and pin codes.
``
## 📌 Project Overview
With the digital payments space booming in India, PhonePe Pulse offers a treasure trove of granular insights. This dashboard extracts, organizes, and visualizes that data to help answer business-critical questions like:

🏆 Which states dominate digital transactions?
📲 What devices are users using most to access PhonePe?
🏥 Which districts have the highest insurance engagement?
📈 How does user engagement vary quarterly across India?

It connects to a PostgreSQL database, uses SQLAlchemy for data querying, and offers visually rich analytics via Streamlit and Plotly.

📹Watch demo video live: http://localhost:8501/
``
## 🎯 Objectives
♦To analyze transaction behavior across states, districts, and pincodes.

♦To monitor user engagement using app opens, registrations, and device brand data.

♦To discover high-performing regions and under-utilized markets.

♦To visualize actionable insights using a dynamic and user-friendly dashboard.

♦To support PhonePe's strategic decisions in marketing, expansion, and product optimization
`` 
### ▶️ How to Run the PhonePe Transaction Insight Dashboard
### 1️⃣ Clone the Repository
Download the project to your local system:
bash
git clone https://github.com/yourusername/phonepe-pulse-project.git
cd phonepe-pulse-project

### 2️⃣ (Optional) Create a Virtual Environment
Helps isolate your project dependencies:
bash
### Create virtual environment
python -m venv venv
Activate it
### For Windows:
venv\Scripts\activate
### For macOS/Linux:
source venv/bin/activate

### 3️⃣ Install Required Dependencies
Install all necessary libraries listed in requirements.txt:
bash
pip install -r requirements.txt

### 4️⃣ Set Up PostgreSQL Database
Ensure PostgreSQL is installed, running, and a database named phonepedb is created.
You can load your data in two ways:

### ✅ Option A: Load via SQL Scripts
bash
psql -U postgres -d phonepedb -f scripts/create_tables.sql
psql -U postgres -d phonepedb -f scripts/load_data.sql

### ✅ Option B: Load Using Python + Pandas
If you're working with JSON files locally, your dashboard code will automatically load the data into tables using pandas.

### 5️⃣ Database Connection
Your code uses SQLAlchemy to connect to the database like this:
engine = create_engine("postgresql://postgres:MALATHI28@localhost:5432/phonepedb")
✅ Note: You can optionally manage your credentials using a .env file for better security.

### 6️⃣ Launch the Streamlit Dashboard
Run the app using:
bash
streamlit run streamlit_app/dashboard.py
🌐 Open your browser and go to: http://localhost:8501
``
## 🗂️ Dataset Details
The project uses a cleaned and structured version of PhonePe’s pulse data across three major categories:

### Aggregated Tables
1. `agg_trans_table` – Transaction data aggregated by state, year, quarter, transaction type.
2. `agg_user_table` – User device brand share data by state, year, quarter.
3. `agg_ins_table` – Insurance-related transactions aggregated by state, year, quarter.

### Map Tables
4. `map_trans_table` – District-level transaction amount and count data.
5. `map_user_table` – District-level registered users and app opens.
6. `map_ins_table` – District-level insurance transaction performance.

### Top Tables
7. `top_trans_table` – Top 10 pincodes for transactions.
8. `top_user_table` – Top pincodes by user registrations.
9. `top_ins_table` – Top pincodes in insurance activity.

### Hover Table
10. `map_ins1_table` – Insurance map hover-level data (optional visual enhancement).
``
## 📁 Folder Structure
```text
📦phonepe-pulse-project
 ┣ 📁data
 ┃ ┣ 📁aggregated
 ┃ ┃ ┣ 📁transaction
 ┃ ┃ ┣ 📁user
 ┃ ┃ ┗ 📁insurance
 ┃ ┣ 📁map
 ┃ ┣ 📁top
 ┃ ┗ 📄 raw_jsons
 ┣ 📄 phonepe_project.ipynb (data extraction, data preprocessing, data pushed into SQL)
 ┣ 📁streamlit_app
 ┃ ┗ 📄 phonepe.py (Streamlit dashboard with full logic and visuals)
 ┣ 📄 db_connection.py (Postgres export logic)
 ┣ 📄 insights_queries.sql (All SQL queries)
 ┣ 📄 requirements.txt (Python package dependencies)
 ┣ 📄 README.md (Project documentation)
```

## 📊 Analysis Scenarios & Key Insights
Scenario-wise Key Insights:

♥Transaction Trends: Analyzed top-performing states and districts based on transaction volume and value, including quarter-wise growth trends.

♥Underperforming Regions: Identified states with high transaction counts but low transaction amounts, highlighting regions with low-ticket size usage.

♥Geographic Expansion: Discovered regions with increasing user engagement but relatively low market penetration, indicating potential areas for expansion.

♥User Engagement: Examined the gap between registered users and app opens to understand user retention, engagement, and activity levels.

♥Device Analytics: Explored brand-wise device usage trends, helping optimize the app experience and ensure better device compatibility.

## 🔍 Sample Insights
📍🇮🇳 Maharashtra and Karnataka are the most active transaction states

📱 Users on Xiaomi and Samsung devices show higher app open rates

🌟 Top-performing districts: Bangalore Urban, Pune, Hyderabad

⛨️ Insurance adoption is still <30% in northern and north-eastern states

 ## 💡 Example Queries Used

### 1. Top States by Total Transaction Amount
```sql
SELECT "State", SUM("Transaction_amount") AS Total_transaction_amount
FROM agg_trans_table
GROUP BY "State"
ORDER BY Total_transaction_amount DESC;
```

### 2. Device Brands with Possible Decline
```sql
SELECT "Device_Brand", "Year", "Quarter", SUM("Device_Count") AS Total_Users
FROM agg_user_table
GROUP BY "Device_Brand", "Year", "Quarter"
ORDER BY Total_Users DESC;
```

### 3. States with Low Insurance Adoption (Untapped Potential)
```sql
SELECT "State", SUM("Total_count") AS Total_Insurance_Count
FROM agg_ins_table
GROUP BY "State"
ORDER BY Total_Insurance_Count ASC;
```
## 📚 Full project analytical report tab:

🧩 Problem Statement

🔍 Exploratory Data Analysis (EDA)

🛠️ Identified Issues

🎯 Proposed Solutions

## 📊 Analytical Report Summary

### 🔍 Problem Statement

Digital payments adoption is uneven across India with disparities in user registrations, transaction volume, device usage, and insurance penetration.

### 📊 Exploratory Data Analysis (EDA)
🧑‍🤝‍🧑📱 Correlation Between Population Density and App Opens
Analyzed how user density in various districts influences the number of app opens, highlighting the role of regional engagement and accessibility.

📈🗓️ Time-Series Analysis of Transaction Counts by State and Quarter
Tracked transaction trends over time across all states and quarters to uncover seasonal patterns, usage peaks, and digital adoption growth.

📱⚙️ Device Brand Analysis vs User Engagement
Explored how different smartphone brands impact user interaction levels, revealing engagement gaps between premium and budget devices.

🗺️🔥 Insurance Usage Heatmaps by District
Visualized insurance activity intensity across districts to identify awareness and adoption gaps geographically, especially in low-performing regions.
``
### ❗ Key Problems Identified
📉🏞️ Low User Registrations in Rural Pin Codes
📌 Issue: Poor digital access, awareness, and onboarding in rural regions.
📡 Cause: Limited internet access, low smartphone usage, and digital illiteracy.

🧠❌ Insurance Awareness Lacking in Northern Regions
🗺️ Issue: Minimal digital insurance transactions in northern states.
🧾 Cause: Lack of awareness, trust, and financial literacy regarding digital insurance.

📱⚖️ Disparity in Engagement Based on Device Brand
📊 Issue: Uneven engagement patterns across phone brands.
📉 Cause: Budget phones struggle with app performance and feature access.

🌐⚠️💥 Uneven Infrastructure Distribution Causing Transaction Overload
🖥️ Issue: High transaction volumes causing server slowdowns and failures.
📍 Cause: Infrastructure concentrated in metro areas; rural clusters under-supported.
``
### 💡 Proposed Solutions
🧾🏕️ Rural Outreach Through Incentives
🎁 Solution: Offer region-specific bonuses, referrals, and scratch card rewards.
🗣️ Tactic: Community outreach via local influencers and multilingual support.

🗺️📣 Localized Awareness Campaigns for Insurance
📢 Solution: Run insurance awareness programs via vernacular media and street campaigns.
📺 Tactic: Use short videos, banners, and local events to build understanding and trust.

⚙️📱 App Optimization for Low-Performance Brands
📦 Solution: Create a lightweight version of the app for low-end phones.
🔧 Tactic: Reduce app size, improve battery usage, and test on budget devices.

🧭🔌 Infrastructure Scaling in High-Load Districts
🚀 Solution: Upgrade cloud/server capacity and introduce load balancing.
🧠 Tactic: Predict traffic spikes using ML models and dynamically scale infrastructure.
``
## ✨ Features

🌐 Interactive 2D Choropleth Map using PyDeck

📊 Plotly visualizations (Bar, Pie, Line)

🔍 Filters by State, Year, Quarter

🔹 Drill-down to districts and pincode-level insights

👥 Device brand usage and engagement breakdown

🛡️ Insurance penetration analytics
``
## 📌 Key Takeaways 
🏆📍 Maharashtra, Karnataka & Tamil Nadu Dominate Transactions
These states consistently lead in total transaction volume and value, marking them as strongholds of digital financial adoption.

📱💸 Some Districts Show High App Opens but Low Transaction Value
Frequent usage doesn’t always translate to high-value transactions. These regions present strong marketing and product education opportunities.

📲⚙️ Device Brand Usage Impacts Engagement
Brand-based differences in app performance show that device optimization (especially for low-end models) is crucial to retain users.

👥📈 App Opens per Registered User Is a Key Engagement Indicator
A higher ratio indicates better app stickiness and user satisfaction. This metric is essential for tracking user lifecycle quality.

🧠📉 Northern States Show Low Insurance Adoption
Insurance transaction heatmaps reveal that northern states have lower usage, calling for targeted awareness campaigns in these regions.

🌐🔌 Infrastructure Bottlenecks in High-Load Urban Clusters
Peak usage districts show signs of transaction overload, pointing to the need for scalable backend systems and network optimization.

🗓️📊 Quarterly Trends Reveal Seasonal Spikes
Time-series analysis shows that certain quarters (e.g., Q4 during festive seasons) consistently bring usage surges — useful for campaign planning.

📍🧾 Rural PIN Codes Are Underrepresented in New Registrations
Despite high population density in some rural districts, registration rates are low, hinting at digital access or literacy barriers.

🔍💡 District-Level Heatmaps Uncover Hidden High-Performers
Some smaller districts outperform metro areas in engagement per capita — suggesting these could be future growth hubs.
``
## 🛠️ Tech Stack
- **Frontend**: Streamlit(Dashboard creation and interactivity,),plotly(Data Visualization),pydeck(Map Creation),HTML(Icon And Font Styling) 
- **Backend**: Python(Data processing),Pandas(Data wrangling),SQLAlchemy(SQL querying via sqlalchemy)
- **Database**: PostgreSQL(Data querying and aggregation)
- **IDE**: Visual Studio Code(development environment)

## 🔮 Future Enhancements
🗺️ Add real-time interactive geographic map plots.  

☁️ Migrate backend to AWS RDS or Snowflake for scalability.  

📉 Introduce predictive models to forecast user growth.  

🧠 Add ML-based anomaly detection on transaction patterns.  

🧾 Auto-generate PDF/Excel reports for business teams.  

## 🙏 Acknowledgments
📡 PhonePe Pulse – for open access data.  

🧮 PostgreSQL – for efficient relational storage and querying.  

📊 Streamlit – for elegant and interactive dashboards.  

🐍 Python & Pandas – for powerful data processing.

🧑‍🏫 GUVI Data Science Program Mentors 

## ✅ Conclusion
This project bridges the gap between raw JSON data and strategic insights through structured SQL queries, engaging dashboards, and effective storytelling. It allows businesses, analysts, and policymakers to explore the digital economy across India and identify impactful opportunities for growth, engagement, and financial inclusion.

## 🙏 Thank You!
✨ "Data is a precious thing and will last longer than the systems themselves."
— Tim Berners-Lee, Inventor of the World Wide Web

🚀 Your time exploring the PhonePe Transaction Insight Dashboard is deeply appreciated!
📊 Whether you came for data, design, or direction — we hope you found insight and inspiration.

💡 Keep decoding, keep questioning, and let data guide the way.

## 👩‍💻 Author
Malathi Y
Data Science Enthusiast | Former Staff Nurse turned Aspiring Data Analyst

💬 Feedback? Questions? Contributions?
We’d love to hear from you!

📧 Email: malathisathish2228@gmail.com

🔗 LinkedIn: linkedin.com/in/malathi-sathish-016a03354

💻 GitHub: github.com/malathisathish

💡 “Transforming clinical experience into data-driven insights — where empathy meets analytics.”

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/ff8b9029-e9a5-4245-ba52-652877da2d39" />

