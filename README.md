# PhonePe Transaction insight Dashboard
An interactive Streamlit-based analytical dashboard that explores and visualizes trends from the PhonePe Pulse dataset. This project is built to empower users, analysts, and business stakeholders with insights on digital payment transactions, user engagement, and insurance adoption patterns across Indian states, districts, and pin codes.
``
# 🧠 Problem Statement

## 📝 Note:

In my perspective, clearly understanding the problem statement is the most critical step in grasping the true purpose of why this dashboard was created. Since this is an analytical project aimed at solving real-world challenges faced by PhonePe, a well-defined problem statement becomes the foundation for meaningful insights.

Interestingly, there’s often a hidden logic within problems — the solution usually lies within the problem itself. With that in mind, I have chosen to present the problem statement in two structured sections:

 ### ⚠️ The Problem – Highlighting the real-world challenges and gaps
 ### 🎯💡The Aim (as the Solution) – Defining how we intend to solve these challenges through data analysis and visualization

This approach offers a clear and focused understanding of the problem's nature and the strategic direction of the solution. It will greatly enhance how you explore and interpret the dashboard's purpose and insights.

# 🔴 SECTION A: Problem – The Need to Decode Digital Financial Patterns in India

With the increasing reliance on digital payment systems like PhonePe, understanding the dynamics of transactions, user engagement, and insurance-related data is crucial for improving services and targeting users effectively.

## 📌 1. Transaction Dynamics

Definition:
Transaction dynamics refer to the changing behaviors, trends, and patterns in financial transactions over time.

Who is transacting? Users across different age groups, using different devices, from different regions
Example: A 25-year-old in Delhi using Android for UPI transfers vs a senior citizen in Kerala using PhonePe for utility bills

What are they transacting for? Recharge, bills, shopping, travel
Example: A user pays for a Swiggy order or recharges their mobile through PhonePe

Where are they transacting? Urban vs rural areas, state-wise analysis
Example: Users in Tier 3 towns increasingly using PhonePe for electricity payments

When are they transacting? Based on seasons, sales events, or peak hours
Example: Huge transaction spikes during Diwali or at the beginning of the month

How are they transacting? Mobile apps, QR codes, UPI, cards, wallets
Example: Paying via QR at a local store using PhonePe UPI

### Key Components:

Volume and Value of Transactions:
Volume = Number of transactions
Value = Total money transacted
📊 Insight: High volume + low value = daily retail use; Low volume + high value = rent/insurance/business payments

Transaction Types:

Peer-to-peer transfers (P2P) – e.g., sending money to friends

Merchant payments (P2M) – e.g., shopping, food orders

Bill payments, recharges, subscriptions – e.g., DTH recharge, electricity bill

Government & financial services – e.g., tax payments, subsidies

Insurance-related payments – e.g., health policy premiums via PhonePe

Geographic Trends:

Urban vs rural adoption

Growth in Tier 2 & Tier 3 cities

Top states/districts driving transactions

Time-Based Trends:

Seasonal spikes (e.g., Diwali, New Year sales)

Quarterly & yearly growth patterns

Weekday vs weekend usage

Device/Platform Usage:

Android vs iOS dominance

Brand-wise user base (e.g., Xiaomi, Samsung)

App vs web usage

User Demographics:

Age group & gender-based usage

First-time vs returning users

State-wise new user registrations

Failure & Security Metrics:

Transaction failure/drop rates

Secure UPI practices (e.g., PIN, OTP protection)

## 📌 2. User Engagement

Definition:
User engagement refers to how frequently, consistently, and effectively users interact with the app.

### Key Metrics:

App Opens (from map_user_table) – Indicates daily/weekly active usage
Example: Frequent app opens during sale seasons or after salary credits

Brand Penetration (from agg_user_table) – Popularity of mobile brands among PhonePe users
Example: Samsung dominating app usage in Maharashtra, Redmi in Uttar Pradesh

User Retention – Are users returning and completing transactions?
Example: Consistent use of PhonePe for all monthly bills

Growth of New Users – How many new users joined during a quarter or year?

Engagement Funnel:
Registration → App Usage → First Transaction → Repeat Use

## 📌 3. Insurance Insights via Digital Platforms

Definition:
Insurance penetration through apps like PhonePe marks a key move toward financial awareness and safety.

### Key Metrics:

Policy Purchase Trends – Region-wise uptake of insurance categories (life, health, vehicle)
Example: Spike in health insurance purchases post-pandemic

User Demographics – Which age groups or regions are buying insurance?

District/State Analysis – Mapping financial awareness and insurance activity across India

### ✅ Outcomes & Impact – From Section A

For PhonePe & Fintech Companies:

Identify user behavior clusters and adapt features to improve conversion and engagement
Spot emerging regions with low digital adoption and target them with campaigns
For Policymakers:

Understand regional inequalities in financial access and digital usage
Design strategic plans to improve inclusion and literacy
For Data Analysts & Researchers:

Case study on large-scale fintech analytics
Hypothesis building, behavioral modeling, forecasting
For Educators & Students:

Real-world application of analytics in digital payments
Teach SQL, EDA, dashboards using actual fintech datasets

# 🟢 SECTION B: Aim – A Smart Dashboard to Decode Digital Behaviour

This project aims to analyze and visualize aggregated values of payment categories, create maps for total values at state and district levels, and identify top-performing states, districts, and pin codes.

To solve the challenges highlighted in Section A, this project delivers an interactive analytical dashboard powered by real-time PhonePe Pulse data. The goal is to translate raw numbers into powerful insights using PostgreSQL, Python, and Streamlit.

### This dashboard is structured to explore three core dimensions:

## 1.🧾 Aggregated Analysis of Payment Categories

Analyze total transaction count and amount across categories like recharges, P2P transfers, and merchant payments
Study yearly and quarterly trends to track shifts in user spending behavior
Example: Discover which category saw the highest spike in Q4 during Diwali season

## 2.🗺️ Map Visualizations at State & District Levels

Use interactive choropleth maps to show transaction count and value for each state and district
Dynamically update maps based on year and quarter selections
Example: Identify underperforming regions with low transaction penetration

## 3.🏆 Identifying Top Performing Regions (States, Districts, Pin Codes)

Rank top states, districts, and pin codes based on user registrations and transaction volume
View dynamic leaderboards filtered by time period
Example: Spot the top 5 pin codes in Tamil Nadu with the highest digital payments
What This Dashboard Offers:

📊 Interactive Charts – Filter by year, quarter, and payment category
🗺️ 2D Map Visualizations – Visualize regional performance on choropleth maps
🏆 Top Performer Leaderboards – Easily identify high-performing regions
🔍 Quick Comparisons – Compare data across multiple timeframes and locations

### 💡 Outcomes & Impact – From Section B
For PhonePe & Businesses:
Identify high-potential regions for service expansion
Launch targeted marketing campaigns and boost user engagement
For Policymakers:

Detect gaps in digital payment access and adoption
Focus financial inclusion programs on underserved districts
For Data Analysts & Educators:

Showcase end-to-end skills in SQL, data cleaning, and dashboarding
Use real fintech data for storytelling and decision-making demonstrations
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

