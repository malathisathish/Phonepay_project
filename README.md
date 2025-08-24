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

**Definition**:
Transaction dynamics refer to the changing behaviors, trends, and patterns in financial transactions over time.

**Who is transacting?** Users across different age groups, using different devices, from different regions
Example: A 25-year-old in Delhi using Android for UPI transfers vs a senior citizen in Kerala using PhonePe for utility bills

**What are they transacting for?** Recharge, bills, shopping, travel
Example: A user pays for a Swiggy order or recharges their mobile through PhonePe

**Where are they transacting?** Urban vs rural areas, state-wise analysis
Example: Users in Tier 3 towns increasingly using PhonePe for electricity payments

**When are they transacting?** Based on seasons, sales events, or peak hours
Example: Huge transaction spikes during Diwali or at the beginning of the month

**How are they transacting?** Mobile apps, QR codes, UPI, cards, wallets
Example: Paying via QR at a local store using PhonePe UPI

### Key Components:

**Volume and Value of Transactions**:
**Volume** = Number of transactions
**Value** = Total money transacted
📊 Insight: High volume + low value = daily retail use; Low volume + high value = rent/insurance/business payments

**Transaction Types**:

Peer-to-peer transfers (P2P) – e.g., sending money to friends

Merchant payments (P2M) – e.g., shopping, food orders

Bill payments, recharges, subscriptions – e.g., DTH recharge, electricity bill

Government & financial services – e.g., tax payments, subsidies

Insurance-related payments – e.g., health policy premiums via PhonePe

**Geographic Trends**:

Urban vs rural adoption

Growth in Tier 2 & Tier 3 cities

Top states/districts driving transactions

**Time-Based Trends**:

Seasonal spikes (e.g., Diwali, New Year sales)

Quarterly & yearly growth patterns

Weekday vs weekend usage

**Device/Platform Usage**:

Android vs iOS dominance

Brand-wise user base (e.g., Xiaomi, Samsung)

App vs web usage

**User Demographics**:

Age group & gender-based usage

First-time vs returning users

State-wise new user registrations

**Failure & Security Metrics**:

Transaction failure/drop rates

Secure UPI practices (e.g., PIN, OTP protection)

## 📌 2. User Engagement

**Definition**:
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

**Definition**:
Insurance penetration through apps like PhonePe marks a key move toward financial awareness and safety.

### Key Metrics:

Policy Purchase Trends – Region-wise uptake of insurance categories (life, health, vehicle)
Example: Spike in health insurance purchases post-pandemic

User Demographics – Which age groups or regions are buying insurance?

District/State Analysis – Mapping financial awareness and insurance activity across India

### ✅ Outcomes & Impact – From Section A

**For PhonePe & Fintech Companies**:
Identify user behavior clusters and adapt features to improve conversion and engagement
Spot emerging regions with low digital adoption and target them with campaigns

**For Policymakers**:
Understand regional inequalities in financial access and digital usage
Design strategic plans to improve inclusion and literacy

**For Data Analysts & Researchers**:
Case study on large-scale fintech analytics
Hypothesis building, behavioral modeling, forecasting

**For Educators & Students**:
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
**For PhonePe & Businesses**:
Identify high-potential regions for service expansion
Launch targeted marketing campaigns and boost user engagement

**For Policymakers**:
Detect gaps in digital payment access and adoption
Focus financial inclusion programs on underserved districts

**For Data Analysts & Educators**:
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

``
## 📂 Project Structure – Luxury Housing Sales Analysis
Luxury_Housing_Sales_Analysis/
│
├── data/  
│   ├── uncleaned_data.csv         # Raw housing dataset (before preprocessing)  
│   ├── cleaned_data.csv           # Processed dataset after cleaning  
│
├── main_files/  
│   ├── cleaning.py                # Data cleaning scripts (handle NaN, outliers, duplicates)  
│   ├── dataloader.py              # Load data from CSV into pandas or SQL DB  
│   ├── dboperation.py             # Database connection and CRUD operations  
│   ├── eda.py                     # Exploratory Data Analysis (univariate, bivariate, multivariate)  
│   ├── feature_engineering.py     # Feature creation, encoding, scaling  
│   ├── main.py                    # Main execution file to run complete pipeline  
│   ├── utils.py                   # Utility/helper functions (logging, configs, etc.)  
│
├── notebooks/  
│   └── luxury_housing_sales.ipynb # Jupyter notebook for step-by-step analysis and visualization  
│
├── power_bi/  
│   ├── dax_measures.pbix          # Power BI DAX calculations file  
│   ├── report.pbix                # Final Power BI dashboard/report file  
│
├── sql/  
│   ├── create_schema.py           # SQLAlchemy / SQL script to create project schema  
│
├── assets/  
│   ├── dashboard_page1.png        # Screenshot of dashboard (page 1)  
│   ├── dashboard_page2.png        # Screenshot of dashboard (page 2)  
│   ├── insights_summary.png       # Screenshot of summary insights  
│
├── README.md                      # Project documentation (problem, solution, structure, usage)  
├── requirements.txt               # Python dependencies (pandas, numpy, matplotlib, SQLAlchemy, etc.)  

## LUXURY HOUSING MARKET INSIGHTS – BENGALURU
Executive Summary | Based on 100,000+ Sales Records

📊 1. Market Trends
Line Chart: Bookings by Quarter & Micro-Market

🔍 Key Insights:
Whitefield leads in bookings with over 1,200 bookings in Q3 2024 — the highest among all micro-markets.
Sarjapur Road shows steady growth — bookings increased from ~380 in Q1 2023 to ~520 in Q3 2024, indicating rising demand.
Indiranagar has seasonal spikes — peak in Q4 2023 (~480 bookings), likely due to year-end property launches.
💡 Whitefield and Sarjapur Road are the most dynamic markets for luxury housing. 

📊 2. Builder Performance
Bar Chart: Revenue vs. Avg Ticket Size by Builder

🔍 Key Insights:
Total Environment leads in total revenue with ₹1.89 Cr from 1,200+ sales — highest in the dataset.
Prestige has the highest average ticket price at ₹14.9 Cr (e.g., PROP004042, PROP090609), indicating premium positioning.
Brigade has high volume but lower average price (₹12.2 Cr) — focuses on volume over premium pricing.
💡 Total Environment dominates volume; Prestige leads in premium pricing. 

📊 3. Amenity Impact
Scatter Plot: Amenity Score vs. Booking Conversion Rate

🔍 Key Insights:
Projects with Amenity Score >8.0 (e.g., PROP090609: 8.54) have 72–78% booking conversion — 2.3x higher than low-amenity projects.
Low-amenity projects (Score <6.0) like PROP001033 (5.82) have <30% conversion — poor amenities hurt sales.
PROP036652 (Bellary Road) has Amenity Score of 6.79 and 100% booking rate — outlier due to "Connectivity is poor" (low competition?).
💡 High amenity score = high conversion. Developers should invest in gyms, pools, and security. 

📊 4. Booking Conversion
Stacked Column: % Booking Status by Micro-Market

🔍 Key Insights:
Whitefield has 72% booking rate — highest in Bengaluru (e.g., PROP071376, PROP034916)
Domlur has only 48% booking rate — despite high inquiries, conversion is low (e.g., PROP029742)
Hennur Road shows 68% conversion — strong interest but needs better follow-up to close more deals.
💡 Whitefield converts best; Domlur needs better sales execution. 

📊 5. Configuration Demand
Donut Chart: Most In-Demand Housing Configurations

🔍 Key Insights:
5BHK+ units account for 38% of all bookings — most in-demand configuration (e.g., PROP032301, PROP001060)
3BHK units make up 32% — popular among NRI and HNI buyers (e.g., PROP053700, PROP076808)
4BHK units at 30% — slightly less popular, but still strong demand in Sarjapur Road and Hebbal.
💡 Buyers prefer larger homes — developers should launch more 5BHK+ units. 

📊 6. Sales Channel Efficiency
100% Stacked Column: Sales Channel vs. Booking Status

🔍 Key Insights:
NRI Desk has 72% booking conversion — highest of all channels (e.g., PROP053700, PROP034916)
Broker channel converts at only 54% — high inquiries but poor follow-up (e.g., PROP001085)
Online channel has 63% conversion — effective for tech-savvy buyers (e.g., PROP034917, PROP079158)
💡 NRI Desk is the most efficient — recommend scaling this channel. 

📊 7. Quarterly Builder Contribution
Matrix: Builders by Quarter & Revenue

🔍 Key Insights:
Total Environment dominated Q2 2024 with ₹68.2 Cr in revenue — highest quarterly contribution.
Puravankara surged in Q3 2024 with ₹54.7 Cr — aggressive launches in Whitefield and Hebbal.
Brigade declined in Q4 2024 — revenue dropped from ₹48 Cr to ₹32 Cr — possible lack of new projects.
💡 Total Environment is consistent; Puravankara is rising; Brigade needs new launches. 

📊 8. Possession Status Analysis
Clustered Column: Possession Status vs. Booking Status by Buyer_Type

🔍 Key Insights:
NRIs book 78% of "Under Construction" homes — investment-driven (e.g., PROP053701, PROP034917)
HNI/CXO buyers prefer "Ready To Move" (72% of bookings) — want immediate occupancy (e.g., PROP005045, PROP066652)
"Launch" projects have 68% inquiry-to-booking ratio — strong early interest, especially from Startup Founders.
💡 NRIs invest in future; HNIs want now. Developers should tailor messaging. 

📊 9. Geographical Insights
Map: Project Concentration in Bengaluru

🔍 Key Insights:
Whitefield has 28% of all luxury projects — highest density (e.g., PROP034916, PROP071376)
Sarjapur Road and Hebbal follow with 22% and 18% respectively — emerging hubs
Domlur and Yelahanka have low project count but high buyer comments — untapped potential
💡 Whitefield is the epicenter; Sarjapur Road is the next big thing. 

📊 10. Top Performers
KPI Cards: Top 5 Builders by Revenue & Booking Success

🔍 Key Insights:
Total Environment is #1 builder with ₹1.89 Cr total revenue and 1,200+ bookings
Prestige has highest avg price (₹14.9 Cr) and 68% conversion — premium leader
Sobha has 70% conversion rate — best sales execution despite lower revenue
💡 Total Environment = volume king; Prestige = premium leader; Sobha = sales efficiency. 

📌 Final Summary: Top 3 Pain Points from Buyer Comments
"Connectivity is poor" → 2,800+ mentions (e.g., PROP001061, PROP006588)
"Too far from my office" → 940+ mentions (e.g., PROP009319)
"Agent was not responsive" → 680+ mentions — a red flag for sales teams
💡 Location and service matter as much as price and amenities. 



## 🔍 Sample Insights
📍🇮🇳 Maharashtra and Karnataka are the most active transaction states

📱 Users on Xiaomi and Samsung devices show higher app open rates

🌟 Top-performing districts: Bangalore Urban, Pune, Hyderabad

⛨️ Insurance adoption is still <30% in northern and north-eastern states

```
## 📚 Full project analytical report tab:

🧩 Problem Statement

🔍 Exploratory Data Analysis (EDA)

🛠️ Identified Issues

🎯 Proposed Solutions

## 📊 Analytical Report Summary

### 🔍 Problem Statement

Digital payments adoption is uneven across India with disparities in user registrations, transaction volume, device usage, and insurance penetration.

## 🏡 Luxury Housing Sales Analysis – EDA Summary
📊 1. Dataset Overview

🗂️ Rows/Columns: ~15,000 × 19 features

🎯 Target: Booking_Flag (1=Booked ✅, 0=Not Booked ❌)

🔢 Features: Numerical (💰 Price, 📐 Sqft, 🏗️ Infra Score, 🚦 Traffic) + Categorical (📍 Location, 🏠 Configuration, 👤 Buyer Type, 🏢 Developer, 🏗️ Possession Status)

🧹 2. Data Quality

✅ Missing values <2% → filled with median/mode or “Unknown”

🚫 Outliers in Price & Price_per_Sqft capped (99th percentile)

🔁 Duplicates removed

📈 3. Univariate Insights

📊 Booking Rate: 43.1% overall

🏠 Configuration: 3BHK (39.3%) > 2BHK (30.1%) > 4BHK+ (16.4%) > 1BHK (14.2%)

💰 Price: Avg 3.24 Cr, mostly 2–4 Cr (52.6%)

👥 Buyer Type: End-user (59.6%) > Investor (40.4%)

🌍 NRI Buyers: 25.2%, avg price 4.12 Cr

🏗️ Infrastructure Score: Avg 6.8/10, higher score = higher bookings 📈

🚦 Traffic: Avg 28.5 min, lower = higher bookings

🔗 4. Bivariate Insights

🏠 Config vs Booking: 4BHK+ (52.3%) > 1BHK (35.2%)

👥 Buyer Type: End-user 45.6% > Investor 39.8%

🌍 NRI vs Domestic: NRI higher booking (46.2%) & price

🏗️ Possession: Ready-to-move (47.8%) > Under-construction (38.9%)

🏗️+🚦 Infra + Traffic: High Infra + Low Traffic = 62.4% bookings

🧩 5. Multivariate Insights

⭐ Top Segment: NRI End-user + 4BHK+ + High Infra + Ready → 67.8% booking

🏢 Developers: Prestige & Brigade outperform consistently

💰 Price/Sqft: Smaller units > higher psf premium

📍 Micro-markets: Indiranagar, Koramangala, Whitefield lead in bookings

⏳ 6. Time Series Insights

📈 Bookings rising 2020 (41.2%) → 2024 (51.2%)

🗓️ Seasonal: Q4 peak, Q2 lowest

🌍 NRI buyers show Q4 seasonality

💡 7. Business Insights

⭐ High Performing: NRI + Premium Configurations + Ready-to-Move

⚠️ Underperforming: Domestic Investors, 1BHK, Low Infra, UC projects

💰 Revenue Drivers: NRI End-users = ~30% revenue

🚀 Opportunities: Q2 activation, investor-focused products, new micro-markets

✅ 8. Recommendations

👤 Buyer Focus: Target NRI + End-users, ready-to-move & premium units

🏠 Config Strategy: Grow 3BHK/4BHK+, price 2BHK competitively

📍 Location: Prioritize High-Infra (>7) + Low Traffic (<25 min) zones

🏢 Developers: Leverage top brands (Prestige, Brigade)

🗂️ Portfolio Mix: 3BHK (35–40%) | 2BHK (25–30%) | 4BHK+ (20–25%) | 1BHK (10–15%)

📆 Timing: Align launches with Q4 peak

🎯 Key Takeaway

Luxury housing bookings depend on:
👤 Buyer Type | 🏠 Configuration | 🏗️ Project Status | 📍 Location Infra | 🚦 Traffic

👉 Optimizing these drives higher bookings, better pricing & revenue 🚀

## ❗ Key Problems Identified

🏚️📉 Low Conversion in Under-Construction Projects
📌 Issue: Buyers hesitate to book under-construction projects.
📡 Cause: Possession risk, trust issues with developers, and project delays.

💰⚖️ High Price Sensitivity in Luxury Housing
📌 Issue: Premium projects show lower booking rates than mid-segment.
📡 Cause: Affordability gap, preference for value-for-money homes.

📍🏞️ Location-Based Demand Disparities
📌 Issue: Certain micro-markets show high supply but weak demand.
📡 Cause: Poor infrastructure, lack of connectivity, or oversupply.

🛠️❌ Mismatch Between Amenities and Buyer Priorities
📌 Issue: Projects with high amenity scores don’t always attract bookings.
📡 Cause: Amenities offered don’t align with buyer expectations (e.g., prefer affordability over luxury add-ons).

👥🔀 Investor vs. End-User Demand Gap
📌 Issue: Different expectations affect booking trends.
📡 Cause: Investors focus on ROI, while end-users focus on timely possession and affordability.

📊⏳ Seasonal Sales Fluctuations
📌 Issue: Bookings peak during festive/financial year-end but remain low otherwise.
📡 Cause: Seasonal buying behavior, discounts, and cultural factors.
``
## 💡 Proposed Solutions

🏙️ Target Affordable & Mid-Premium Segments
✔️ Alongside luxury housing, launch mid-premium and “affordable luxury” units.
✔️ Attracts aspirational middle-income buyers and ensures steady absorption rates.
✔️ Balances exclusivity with wider market reach.

📢 Strengthen Marketing & Awareness Strategy
✔️ Mix digital campaigns, property portals, and targeted ads for NRI + domestic buyers.
✔️ Use VR/AR virtual tours and 360° walkthroughs for immersive buyer experience.
✔️ Collaborate with real estate influencers, YouTubers, and property fairs.

🛣️ Boost Location Value & Accessibility
✔️ Work with civic authorities to improve last-mile connectivity.
✔️ Highlight proximity to IT hubs, schools, healthcare, and malls in sales pitches.
✔️ Develop projects in emerging micro-markets for early advantage.

💰 Flexible Financing & Buyer-Friendly Schemes
✔️ Tie up with banks for attractive EMI and low-interest home loan packages.
✔️ Offer staggered payment plans, festive discounts, and referral bonuses.
✔️ Introduce rent-to-own or part-ownership models for young buyers.

🏗️ Sustainable & Smart Housing Features
✔️ Incorporate solar panels, rainwater harvesting, and green building materials.
✔️ Offer IoT-enabled smart homes (remote security, energy-efficient appliances).
✔️ Aligns with eco-conscious buyers and long-term cost savings.

🤝 Enhance Buyer Trust & Transparency
✔️ Maintain RERA compliance and provide timely project updates.
✔️ Share construction progress videos/photos for transparency.
✔️ Offer escrow-linked payment models to boost buyer confidence.

🧑‍🤝‍🧑 Community-Centric Amenities
✔️ Focus on co-working spaces, daycare centers, fitness hubs, and wellness zones.
✔️ Create gated communities with sports, culture, and social engagement facilities.
✔️ Appeals to families and long-term residents, not just investors.

📊 Data-Driven Market Intelligence
✔️ Track buyer demographics, conversion ratios, and amenity preferences.
✔️ Use predictive analytics to design customized offers for different buyer clusters.
✔️ Benchmark performance against competitors to stay ahead.
``
## 🏡✨ Features of the Housing Project

🔑 Comprehensive Sales Analysis
Analyzes property sales across multiple dimensions such as location, possession status, amenities, and buyer profiles.

📊 Interactive Visualizations
Charts, slicers, and filters in Power BI for dynamic insights into housing trends.

🏢 Possession Status Insights
Tracks the impact of under-construction vs. ready-to-move properties on booking decisions.

🛠️ Amenity Impact Evaluation
Measures how amenities like gym, pool, parking, etc. influence booking conversion rates.

👥 Buyer Segmentation
Identifies preferences of different buyer types (end-users vs. investors).

🌍 Location-Based Trends
Compares micro-markets, cities, and regions to highlight high-demand zones.

📈 Price & Size Analysis
Correlates ticket size, unit area, and price per sqft with booking success.

🕒 Time-Based Performance
Evaluates booking patterns by quarter/year to identify seasonal demand spikes.

📌 Market Competitiveness
Benchmarks project performance against competitors to identify positioning gaps.

💡 Decision Support
Provides actionable insights for developers, investors, and buyers for better housing decisions.
``
## 📌 Key Takeaways

🏙️📍 Bangalore, Mumbai & Delhi NCR Lead in Luxury Housing Demand
These metro cities dominate both sales volume and ticket price, making them prime hubs for premium real estate development.

💰📈 Amenities Strongly Influence Booking Decisions
Projects with higher amenity scores (swimming pools, gyms, clubhouses) show significantly higher booking conversion rates.

📅🏡 Possession Status Impacts Buyer Behavior
Ready-to-move-in projects attract end-users, while under-construction properties see higher investor interest.

👥📊 Buyer Type Segmentation Highlights Distinct Patterns
NRIs prefer premium projects in metro cities, while local buyers focus more on affordability and possession timelines.

📐💡 Unit Size Drives Price Per Sq. Ft. Variations
Smaller units tend to command higher per sq. ft. prices, while larger luxury villas offer better overall value.

📍🚉 Proximity to Metro & IT Hubs Boosts Bookings
Housing projects closer to IT corridors, airports, and metro lines have higher demand and quicker sales cycles.

🌳🏗️ Green & Sustainable Projects Show Rising Interest
Eco-friendly housing with green certifications (LEED, IGBC) is increasingly appealing to urban buyers.

📊📆 Quarterly Trends Show Seasonal Spikes in Sales
Festive seasons (Q3–Q4) consistently drive higher bookings, making them crucial for targeted marketing campaigns.

📌🔍 Micro-Market Analysis Reveals Hidden Growth Pockets
Emerging suburban areas show faster appreciation rates than saturated metro zones, signaling new investment opportunities.

🏢📉 Unsold Inventory Remains a Challenge in Certain Segments
Ultra-luxury apartments above ₹5 Cr face slower absorption, requiring innovative pricing and marketing strategies.
``
## 🛠️ Tech Stack

**Frontend / Visualization**:

Power BI → Interactive dashboards, slicers & rich visualizations

Excel → Data preprocessing, pivot tables & quick checks

**Backend / Processing**:

Python → Data cleaning, preprocessing & analysis

Pandas / NumPy → Data wrangling & numerical computations

Matplotlib / Seaborn → Exploratory data analysis & charts

**Database / Storage**:

CSV / Excel Files → Raw housing data storage

**Development Environment**:

Visual Studio Code (VS Code) → Development & coding

Jupyter Notebook → Analysis, EDA & reporting

## 🔮 Future Enhancements
🗺️ Add real-time interactive geographic map plots.  

☁️ Migrate backend to AWS RDS or Snowflake for scalability.  

📉 Introduce predictive models to forecast user growth.  

🧠 Add ML-based anomaly detection on transaction patterns.  

🧾 Auto-generate PDF/Excel reports for business teams.  

## 🙏 Acknowledgments

📂 Dataset Providers – for making real estate data accessible for research and analysis.

🧮 PostgreSQL – for efficient relational storage and SQL querying.

📊 Power BI – for insightful and interactive business dashboards.

🐍 Python, Pandas & Matplotlib – for robust data cleaning, processing, and visualization.

🧑‍🏫 GUVI Data Science Program Mentors (Especially my mentors Mr. Santhosh Nagaraj sir and Ms. Shadiya mam) – for their constant guidance, support, and encouragement in completing this project successfully and building my confidence throughout the learning journey.

👨‍👩‍👧‍👦 My Family & Friends – for their unwavering encouragement, motivation, and support that kept me focused and inspired during this project.

## ✅ Conclusion

The Luxury Housing Sales Analysis Project transformed raw data into valuable insights on buyer behavior, pricing trends, amenities, and possession status. Using Python, SQL, and Power BI, the project highlighted how amenities and timely possession play a major role in driving booking decisions.
Overall, this project shows the power of data-driven decision-making in real estate and provides stakeholders with actionable insights to improve sales strategies, buyer engagement, and future planning.

## 🙏 Thank You!

✨ "Housing is not just about buildings; it is about dreams, lifestyles, and aspirations."

🚀 Thank you for exploring the Luxury Housing Sales Analysis Project.
📊 Whether your interest was in data, insights, or decisions, we hope this project offered both clarity and inspiration.

💡 Keep analyzing, keep innovating, and let data shape better choices.

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

![Uploading image.png…]()
