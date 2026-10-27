import streamlit as st
from cleaning_data import load_clean_data
from customer_analysis import customer_analysis
from orders_analysis import analyze_order,monthly_orders
from delivery_analysis import analyze_delivery,delivery_status
import os

st.set_page_config(page_title="Food Delivery Analysis", layout="wide")

st.title("Food Delivery Analysis App")

try:
    data=load_clean_data()
    customer=data['Customers']
    orders=data['Orders']
    menu=data['Menu']
    rest=data['rest']
    delivery=data['Delivery']
    print("All Table Loaded")
except:
    print("Database connection Failed")

CA,OA,DA=st.tabs(['Customer Analysis','Orders Analysis','Delivery Analysis'])

with CA:
    st.header("Customer Analysis Report")
    col1,col2,col3=st.columns(3)
    customer_analysis_data=customer_analysis(customer,orders)

    col1.header("Total Customers")
    col1.subheader(customer_analysis_data['Total_customers'])

    col2.header("Repeted Customers")
    col2.subheader(customer_analysis_data['repeted_customers'])

    col3.header("New Customers")
    col3.subheader(customer_analysis_data['new customers'])

    st.header("Gender Analysis")
    st.bar_chart(customer_analysis_data['Gender count'])

    st.header("Area Analysis")
    st.bar_chart(customer_analysis_data['city_count'])


with OA:
    st.header("Orders Analysis Report")
    orders_analysis_data=analyze_order(orders)
    col1,col2,col3=st.columns(3)

    col1.header("Total Revenue")
    col1.subheader(orders_analysis_data['Revenue'])

    col2.header("Total Orders")
    col2.subheader(orders_analysis_data['Total_Orders'])    

    col3.header("Average Order Value")
    col3.subheader(orders_analysis_data['Average_Order_Value'])

    st.divider()

    monthly_orders_data=monthly_orders(orders)

    st.header("Monthly Orders Analysis")

    st.divider()
    
    st.line_chart(monthly_orders_data)





with DA:
    st.header("Delivery Analysis Report")
