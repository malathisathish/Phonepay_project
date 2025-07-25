
# PhonePe Transaction insight Dashboard

## 📌 Project Overview
This project is an end-to-end data analysis and visualization solution built on the PhonePe Pulse datasets. It offers comprehensive insights into digital transactions, user registrations, app engagement, and device brand distribution across India at both state and district levels.

The project extracts structured JSON data, transforms it into tabular formats, performs in-depth SQL-based analysis, and visualizes the results through an interactive Streamlit dashboard.

## 🎯 Objectives
♦To analyze transaction behavior across states, districts, and pincodes.

♦To monitor user engagement using app opens, registrations, and device brand data.

♦To discover high-performing regions and under-utilized markets.

♦To visualize actionable insights using a dynamic and user-friendly dashboard.

♦To support PhonePe's strategic decisions in marketing, expansion, and product optimization

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

## 📊 Analysis Scenarios & Key Insights
Scenario-wise Key Insights:

♥Transaction Trends: Analyzed top-performing states and districts based on transaction volume and value, including quarter-wise growth trends.

♥Underperforming Regions: Identified states with high transaction counts but low transaction amounts, highlighting regions with low-ticket size usage.

♥Geographic Expansion: Discovered regions with increasing user engagement but relatively low market penetration, indicating potential areas for expansion.

♥User Engagement: Examined the gap between registered users and app opens to understand user retention, engagement, and activity levels.

♥Device Analytics: Explored brand-wise device usage trends, helping optimize the app experience and ensure better device compatibility.

## 📌 Key Takeaways
♣States like Maharashtra, Karnataka, and Tamil Nadu dominate transaction value and user base.

♣Certain districts show high app activity but low average transaction value, indicating marketing opportunities.

♣Device brands vary significantly by state, influencing UI/UX strategies.

♣App opens per registered user is a strong metric for evaluating engagement.

## 🛠️ Tech Stack
- **Frontend**: Streamlit(Dashboard creation and interactivity)
- **Backend**: Python, Pandas, SQAlchemy(Data processing,Data wrangling,SQL querying via sqlalchemy)
- **Database**: PostgreSQL(Data querying and aggregation)
- **IDE**: Visual Studio Code(development environment)

## 📈 Dashboard Features (Built with Streamlit)
🔎 Filter by State, Year, and Quarter  
📍 District-wise and Pincode-level Metrics  
💰 Top Transaction States & Growth Patterns  
📲 User Registrations vs App Opens  
📱 Device Brand Usage by Region  
💼 Insurance Trends Visualization  
📈 Dynamic Charts: Bar, Line, and Pie Graphs  
🔁 Real-Time Query Display & Updates  

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

## 📁 Folder Structure
```
📦phonepe-pulse-project
 ┣ 📁data
 ┃ ┣ 📁aggregated
 ┃ ┃ ┣ 📁transaction
 ┃ ┃ ┣ 📁user
 ┃ ┃ ┗ 📁insurance
 ┃ ┣ 📁map
 ┃ ┣ 📁top
 ┃ ┗ 📄 raw_jsons
 ┣ 📁scripts
 ┃ ┗ 📄 data_extraction.py
 ┣ 📁streamlit_app
 ┃ ┗ 📄app.py
 ┣ 📄 db_connection.py(or postgres export)
 ┣ 📄 queries.sql
 ┣ 📄 requirements.txt
 ┣ 📄 README.md
```

## ▶️ How to Run

1. Clone the Repository  
```bash
git clone https://github.com/yourusername/phonepe-pulse-project.git
cd phonepe-pulse-project
```

2. Install Dependencies  
```bash
pip install -r requirements.txt
```

3. Set Up Database  
Run SQL scripts to create and load tables (or use pandas to load from JSONs).  
Ensure PostgreSQL is running and connected properly via SQLAlchemy.

4. Launch Dashboard  
```bash
streamlit run streamlit_app/dashboard.py
```

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

## ✅ Conclusion
This project bridges the gap between raw JSON data and strategic insights through structured SQL queries, engaging dashboards, and effective storytelling. It allows businesses, analysts, and policymakers to explore the digital economy across India and identify impactful opportunities for growth, engagement, and financial inclusion.

## 👤 Author
** Malathi y**  
Data Science Enthusiast | Staff Nurse turned Analyst  
📧 Email: malathisathish2228@gmail.com  
🔗 LinkedIn: [https://www.linkedin.com/in/malathi-sathish-016a03354/](https://www.linkedin.com/in/malathi-sathish-016a03354/
📂 GitHub: [github.com/malathisathish](https://github.com/malathisathish)
