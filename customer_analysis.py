## Customer analysis

from cleaning_data import load_clean_data

def customer_analysis(customer_df):
    total_customers=customer_df['customer_id'].nunique()
    gender_count=customer_df['gender'].value_counts()
    city=[]

    
    for address in customer_df['Address']:
       city.append(address.split(' , ')[-1].strip())
    customer_df['city']=city
    city_count=customer_df['city'].value_counts()


    return{'Total_customers':total_customers,
           'Gender count':gender_count,
           'city_count':city_count}

customer_df=load_clean_data()['Customers']
print(customer_analysis(customer_df))



