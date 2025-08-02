"""
PhonePe Pulse Insights Queries Module
Contains all predefined analytical queries for comprehensive data insights
"""

from sqlalchemy import create_engine, text
import pandas as pd
import streamlit as st

# Database connection
engine = create_engine("postgresql://postgres:MALATHI28@localhost:5432/phonepedb")

def execute_query(query):
    """Execute SQL query and return DataFrame"""
    try:
        with engine.connect() as connection:
            df = pd.read_sql(text(query), connection)
        return df
    except Exception as e:
        st.error(f"Database query failed: {e}")
        return pd.DataFrame()

# ========================= TRANSACTION ANALYSIS QUERIES =========================

def get_top_states_by_transaction_amount():
    """1.1 Top States by Total Transaction Amount"""
    query = """
    SELECT "State", 
    sum("Transaction_amount") as Total_transaction_amount
    FROM agg_trans_table
    GROUP BY "State"
    ORDER BY Total_transaction_amount desc;
    """
    return execute_query(query)

def get_quarterly_growth_by_state():
    """1.2 Quarterly Growth of Transactions in Each State"""
    query = """
    SELECT "State",
    "Year","Quarter",
    sum("Transaction_amount") as Total_transaction_amount
    FROM agg_trans_table
    GROUP BY "State", "Year", "Quarter";
    """
    return execute_query(query)

def get_popular_transaction_types():
    """1.3 Most Popular Transaction Type Nationally"""
    query = """
    SELECT "Transaction_type",
    sum("Transaction_count") as Total_transaction_count
    FROM agg_trans_table
    GROUP BY "Transaction_type"
    ORDER BY Total_transaction_count DESC
    """
    return execute_query(query)

def get_declining_transaction_regions():
    """1.4 States, Districts, and Quarters with Decline in Transactions"""
    query = """
    SELECT 
        t1."State",
        t1."District",
        t1."Year",
        t1."Quarter" AS From_Quarter,
        t2."Quarter" AS To_Quarter,
        t1."Transaction_count" AS From_Count,
        t2."Transaction_count" AS To_Count
    FROM map_trans_table t1
    JOIN map_trans_table t2
      ON t1."State" = t2."State"
     AND t1."District" = t2."District"
     AND t1."Year" = t2."Year"
     AND t2."Quarter" = t1."Quarter" + 1
    WHERE t2."Transaction_count" < t1."Transaction_count"
    ORDER BY t1."State", t1."District", t1."Year", t1."Quarter";
    """
    return execute_query(query)

def get_declining_activity_patterns():
    """1.5 Find patterns of declining user activity across quarters by district and state"""
    query = """
    WITH Quarter_Comparisons AS (
      SELECT 
        t1."State",
        t1."District",
        t1."Year",
        t1."Quarter" AS From_Quarter,
        t2."Quarter" AS To_Quarter,
        t1."Transaction_count" AS From_Count,
        t2."Transaction_count" AS To_Count
      FROM map_trans_table t1
      JOIN map_trans_table t2
        ON t1."State" = t2."State"
       AND t1."District" = t2."District"
       AND t1."Year" = t2."Year"
       AND t2."Quarter" = t1."Quarter" + 1
      WHERE t2."Transaction_count" < t1."Transaction_count"
    )
    SELECT 
      "State",
      "District",
      "Year",
      COUNT(*) AS Decline_Streaks
    FROM Quarter_Comparisons
    GROUP BY "State", "District", "Year"
    HAVING COUNT(*) >= 2
    ORDER BY Decline_Streaks DESC;
    """
    return execute_query(query)

# ========================= USER BEHAVIOR QUERIES =========================

def get_top_device_brands():
    """2.1 Top Device Brands by Total Users"""
    query = """
    SELECT "Device_Brand", SUM("Transaction_count") AS Total_Users
    FROM agg_user_table
    GROUP BY "Device_Brand"
    ORDER BY Total_Users DESC;
    """
    return execute_query(query)

def get_high_app_opens_low_registrations():
    """2.2 High App Opens but Low Registrations"""
    query = """
    SELECT "State", "District", "RegisteredUsers", "AppOpens"
    FROM map_user_table
    WHERE "RegisteredUsers" < 1000 AND "AppOpens" > 5000
    ORDER BY "AppOpens" DESC;
    """
    return execute_query(query)

def get_device_brand_decline():
    """2.3 Device Brands with Possible Decline"""
    query = """
    SELECT "Device_Brand","Year", "Quarter", 
    SUM("Transaction_count") AS Total_Users
    FROM agg_user_table
    GROUP BY "Device_Brand", "Year", "Quarter"
    ORDER BY Total_Users DESC;
    """
    return execute_query(query)

def get_device_brand_trends():
    """2.4 Device Brand Trends Over Quarters"""
    query = """
    SELECT "Device_Brand", "Year", "Quarter",
    SUM("Transaction_count") AS Total_Users
    FROM agg_user_table
    GROUP BY "Device_Brand", "Year", "Quarter"
    ORDER BY "Device_Brand", "Year", "Quarter";
    """
    return execute_query(query)

def get_engagement_vs_registration():
    """2.5 Compare Engagement vs Registration"""
    query = """
    SELECT "State", 
    sum("RegisteredUsers") AS Total_Registered_Users,
    sum("AppOpens") AS Total_App_Opens
    FROM map_user_table
    GROUP BY "State"
    ORDER BY Total_App_Opens DESC;
    """
    return execute_query(query)

def get_user_growth_trends():
    """2.6 Overall User Growth Trends"""
    query = """
    SELECT "State", "Year", "Quarter",
    SUM("RegisteredUsers") AS Total_Registered_Users
    FROM map_user_table
    GROUP BY "State", "Year", "Quarter"
    ORDER BY "State", "Year", "Quarter";
    """
    return execute_query(query)

# ========================= INSURANCE ANALYTICS QUERIES =========================

def get_low_insurance_adoption():
    """3.1 States with Low Insurance Adoption (untapped potential)"""
    query = """
    SELECT "State", SUM("Transaction_count") AS Total_Insurance_Count
    FROM agg_ins_table
    GROUP BY "State"
    ORDER BY Total_Insurance_Count ASC;
    """
    return execute_query(query)

def get_top_insurance_states():
    """3.2 Top States by Number of Insurance Transactions"""
    query = """
    SELECT "State", SUM("Transaction_count") AS Total_Insurance_Transactions
    FROM agg_ins_table
    GROUP BY "State"
    ORDER BY Total_Insurance_Transactions DESC;
    """
    return execute_query(query)

def get_insurance_growth_rate():
    """3.3 State-District Quarterly Insurance Growth Rate"""
    query = """
    WITH previous_quarter AS (
        SELECT 
            "State", 
            "District", 
            CAST("Year" AS INT) AS "Year", 
            "Quarter", 
            "Transaction_count" AS prev_count
        FROM map_ins_table
    ),
    current_quarter AS (
        SELECT 
            "State", 
            "District", 
            CAST("Year" AS INT) AS "Year", 
            "Quarter", 
            "Transaction_count" AS curr_count
        FROM map_ins_table
    )
    SELECT 
        curr."State",
        curr."District",
        curr."Year",
        curr."Quarter",
        prev.prev_count,
        curr.curr_count,
        ROUND(((curr.curr_count - prev.prev_count) * 100.0) / NULLIF(prev.prev_count, 0), 2) AS Growth_Percentage
    FROM current_quarter curr
    JOIN previous_quarter prev
      ON curr."State" = prev."State"
      AND curr."District" = prev."District"
      AND curr."Year" = prev."Year"
      AND curr."Quarter" = prev."Quarter" + 1
    WHERE curr."Year" >= 2022
    ORDER BY Growth_Percentage DESC
    LIMIT 20;
    """
    return execute_query(query)

def get_insurance_growth_trajectory():
    """3.4 State, district, quarter wise insurance growth trajectory"""
    query = """
    SELECT 
        curr."State",
        curr."District",
        curr."Year",
        curr."Quarter",
        curr."Transaction_count" AS Current_Transaction_Count,
        prev."Transaction_count" AS Previous_Transaction_Count,
        ROUND(
            ((curr."Transaction_count" - prev."Transaction_count") * 100.0) / NULLIF(prev."Transaction_count", 0), 2
        ) AS Growth_Percentage
    FROM map_ins_table curr
    JOIN map_ins_table prev
      ON curr."State" = prev."State"
     AND curr."District" = prev."District"
     AND curr."Year" = prev."Year"
     AND curr."Quarter" = prev."Quarter" + 1
    ORDER BY Growth_Percentage DESC;
    """
    return execute_query(query)

def get_high_priority_insurance_regions():
    """3.5 High-Priority Regions for Insurance Growth"""
    query = """
    SELECT 
        "State", 
        "District",
        SUM("Transaction_count") AS Total_Insurance_Transactions,
        COUNT(DISTINCT CONCAT("Year", '-', "Quarter")) AS Active_Quarters,
        ROUND(SUM("Transaction_count") * 1.0 / COUNT(DISTINCT CONCAT("Year", '-', "Quarter")), 2) AS Avg_Transactions_Per_Quarter
    FROM map_ins_table
    GROUP BY "State", "District"
    HAVING SUM("Transaction_count") > 10000  
    ORDER BY Avg_Transactions_Per_Quarter DESC
    LIMIT 15;
    """
    return execute_query(query)

# ========================= GROWTH PATTERNS QUERIES =========================

def get_fastest_growth_states():
    """4.1 States with Fastest Quarterly Growth in Transactions"""
    query = """
    WITH curr AS (
      SELECT "State", CAST("Year" AS INT) AS Year, "Quarter", SUM("Transaction_count") AS curr_count
      FROM agg_trans_table
      GROUP BY "State", "Year", "Quarter"
    ),
    prev AS (
      SELECT "State", CAST("Year" AS INT) AS Year, "Quarter", SUM("Transaction_count") AS prev_count
      FROM agg_trans_table
      GROUP BY "State", "Year", "Quarter"
    )
    SELECT 
      c."State", c.Year, c."Quarter",
      ROUND(((c.curr_count - p.prev_count) * 100.0) / NULLIF(p.prev_count, 0), 2) AS Growth_Percentage
    FROM curr c
    JOIN prev p 
      ON c."State" = p."State" 
      AND c.Year = p.Year 
      AND c."Quarter" = p."Quarter" + 1
    WHERE c.Year = 2023
    ORDER BY Growth_Percentage DESC
    LIMIT 10;
    """
    return execute_query(query)

def get_fastest_growing_states_qoq():
    """4.2 Fastest Growing States by Quarter-over-Quarter Growth"""
    query = """
    SELECT 
        curr."State",
        curr."Year",
        curr."Quarter",
        prev."Transaction_amount" AS Previous_Amount,
        curr."Transaction_amount" AS Current_Amount,
        ROUND(
            (
                (curr."Transaction_amount" - prev."Transaction_amount") * 100.0 / 
                NULLIF(prev."Transaction_amount", 0)
            )::numeric,
            2
        ) AS Growth_Percentage
    FROM agg_trans_table curr
    JOIN agg_trans_table prev
      ON curr."State" = prev."State"
      AND curr."Year" = prev."Year"
      AND curr."Quarter" = prev."Quarter" + 1
    ORDER BY Growth_Percentage DESC
    LIMIT 10;
    """
    return execute_query(query)

def get_underperforming_states():
    """4.3 Underperforming States with Low Transaction Totals"""
    query = """
    SELECT "State", 
    SUM("Transaction_amount") AS Total_Transaction_Amount
    FROM agg_trans_table
    GROUP BY "State"
    ORDER BY Total_Transaction_Amount ASC;
    """
    return execute_query(query)

def get_low_value_states():
    """4.4 States with High Transaction Counts but Low Amounts"""
    query = """
    SELECT 
        "State",
        SUM("Transaction_count") AS total_transactions,
        SUM("Transaction_amount") AS total_amount,
        ROUND(SUM("Transaction_amount")::numeric / NULLIF(SUM("Transaction_count"), 0), 2) AS avg_transaction_value
    FROM agg_trans_table
    GROUP BY "State"
    ORDER BY avg_transaction_value ASC;
    """
    return execute_query(query)

def get_geo_expansion_potential():
    """4.5 Geographic Expansion Potential (Based on Map Data)"""
    query = """
    SELECT "State", "Year", "Quarter", 
    SUM("Transaction_amount") AS Geo_Transaction_Amount
    FROM map_trans_table
    GROUP BY "State", "Year", "Quarter"
    ORDER BY Geo_Transaction_Amount DESC;
    """
    return execute_query(query)

# ========================= ENGAGEMENT METRICS QUERIES =========================

def get_top_engagement_states():
    """5.1 Top States by Engagement Rate"""
    query = """
    SELECT 
        "State", "Year", "Quarter",
        ROUND(SUM("AppOpens")::numeric / NULLIF(SUM("RegisteredUsers"), 0), 2) AS Engagement_Rate
    FROM map_user_table
    GROUP BY "State", "Year", "Quarter"
    ORDER BY Engagement_Rate DESC
    LIMIT 10;
    """
    return execute_query(query)

def get_state_brand_dominance():
    """5.2 State-wise Brand Dominance"""
    query = """
    SELECT 
        "State", "Device_Brand",
        ROUND(AVG("Percentage"):: numeric, 2) AS Avg_Brand_Share
    FROM agg_user_table
    GROUP BY "State", "Device_Brand"
    ORDER BY Avg_Brand_Share DESC
    LIMIT 15;
    """
    return execute_query(query)

def get_low_engagement_districts():
    """5.3 Districts with High Users but Low Engagement"""
    query = """
    SELECT 
        "State", "District", "Year", "Quarter",
        SUM("RegisteredUsers") AS Total_Users,
        SUM("AppOpens") AS Total_App_Opens,
        ROUND(SUM("AppOpens")::numeric / NULLIF(SUM("RegisteredUsers"), 0), 2) AS Engagement_Rate
    FROM map_user_table
    GROUP BY "State", "District", "Year", "Quarter"
    HAVING SUM("RegisteredUsers") > 1000 AND ROUND(SUM("AppOpens")::numeric / NULLIF(SUM("RegisteredUsers"), 0), 2) < 1
    ORDER BY Engagement_Rate ASC;
    """
    return execute_query(query)

def get_fastest_growth_registrations():
    """5.4 States with Fastest Growth in Registrations (Quarter-over-Quarter)"""
    query = """
    WITH prev_quarter AS (
        SELECT "State", "Year", "Quarter", SUM("RegisteredUsers") AS reg_prev
        FROM map_user_table
        GROUP BY "State", "Year", "Quarter"
    ),
    curr_quarter AS (
        SELECT "State", "Year", "Quarter", SUM("RegisteredUsers") AS reg_curr
        FROM map_user_table
        GROUP BY "State", "Year", "Quarter"
    )
    SELECT 
        curr."State",
        curr."Year",
        curr."Quarter",
        ROUND(
            ((curr.reg_curr - prev.reg_prev)::numeric / NULLIF(prev.reg_prev, 0)) * 100, 2
        ) AS Growth_Percentage
    FROM curr_quarter curr
    JOIN prev_quarter prev
      ON curr."State" = prev."State"
      AND curr."Year" = prev."Year"
      AND curr."Quarter" = prev."Quarter" + 1
    ORDER BY Growth_Percentage DESC
    LIMIT 10;
    """
    return execute_query(query)

def get_popular_device_brands():
    """5.5 Most Popular Device Brands (All India)"""
    query = """
    SELECT 
        "Device_Brand",
        SUM("Transaction_count") AS Total_Users,
        ROUND(AVG("Percentage"):: numeric, 2) AS Avg_Usage_Share
    FROM agg_user_table
    GROUP BY "Device_Brand"
    ORDER BY Total_Users DESC
    LIMIT 10;
    """
    return execute_query(query)

def get_high_engagement_states():
    """5.6 Top 10 States with High User Engagement (App Opens per Registered User)"""
    query = """
    SELECT 
        "State",
        SUM("RegisteredUsers") AS Total_Registered_Users,
        SUM("AppOpens") AS Total_App_Opens,
        ROUND(SUM("AppOpens")::numeric / NULLIF(SUM("RegisteredUsers"), 0), 2) AS App_Open_Rate
    FROM map_user_table
    GROUP BY "State"
    HAVING SUM("RegisteredUsers") > 100000
    ORDER BY App_Open_Rate DESC
    LIMIT 10;
    """
    return execute_query(query)

# ========================= QUERY MAPPING =========================

QUERY_MAPPING = {
    "Transaction Analysis": {
        "Top States by Transaction Amount": get_top_states_by_transaction_amount,
        "Quarterly Growth by State": get_quarterly_growth_by_state,
        "Popular Transaction Types": get_popular_transaction_types,
        "Declining Transaction Regions": get_declining_transaction_regions,
        "Declining Activity Patterns": get_declining_activity_patterns
    },
    "User Behavior": {
        "Top Device Brands": get_top_device_brands,
        "High App Opens, Low Registrations": get_high_app_opens_low_registrations,
        "Device Brand Decline": get_device_brand_decline,
        "Device Brand Trends": get_device_brand_trends,
        "Engagement vs Registration": get_engagement_vs_registration,
        "User Growth Trends": get_user_growth_trends
    },
    "Insurance Analytics": {
        "Low Insurance Adoption": get_low_insurance_adoption,
        "Top Insurance States": get_top_insurance_states,
        "Insurance Growth Rate": get_insurance_growth_rate,
        "Insurance Growth Trajectory": get_insurance_growth_trajectory,
        "High Priority Insurance Regions": get_high_priority_insurance_regions
    },
    "Growth Patterns": {
        "Fastest Growth States": get_fastest_growth_states,
        "Fastest Growing States QoQ": get_fastest_growing_states_qoq,
        "Underperforming States": get_underperforming_states,
        "Low Value States": get_low_value_states,
        "Geographic Expansion Potential": get_geo_expansion_potential
    },
    "Engagement Metrics": {
        "Top Engagement States": get_top_engagement_states,
        "State Brand Dominance": get_state_brand_dominance,
        "Low Engagement Districts": get_low_engagement_districts,
        "Fastest Growth Registrations": get_fastest_growth_registrations,
        "Popular Device Brands": get_popular_device_brands,
        "High Engagement States": get_high_engagement_states
    }
}