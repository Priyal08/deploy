import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelBinarizer



model = pickle.load(open('C:/Users/hp/Desktop/web app/deploy.pkl', 'rb'))


def main():
        st.title("Loan Grade prediction using Machine Learning")
        st.sidebar.header('User Input Features')

         #funded ammount inv
        funded_amt_inv = st.sidebar.number_input("Funded amount($)",0.00,10**6.00)
  
        #interest rate
        interest_r = st.sidebar.slider("Interest Rate",5.30,31.1)
    
        #employment length
        emp_len = st.sidebar.selectbox("Employment Length",[0,1,2,3,4,5,6,7,8,9,10])
    
        #annual income
        annual_inc = st.sidebar.number_input("Annual Income",0.00,10**7.00)
    
        #payment plan
        pymt_plan = st.sidebar.selectbox("Payment Plan",['Yes','No'])
    
        #debt_to_income ratio
        dti_r = st.sidebar.number_input("Debt-to-Income Ratio",0.00,1000.00)
    
        #deling_2yr
        deling_2 = st.sidebar.number_input("Delinquencies in last 2 years",0,90)
    
        #fico_range_lowe
        fico_range_lower = st.sidebar.number_input("FICO Score [low]",0.00,1000.00)
    
        #inquiry_last_6
        inq_last_6 = st.sidebar.number_input("Inquiries [last 6 months]",0,20)
    
        #open_acc
        open_acct = st.sidebar.number_input("No. of open accounts",0,200)
    
        #public records
        pub_recs = st.sidebar.number_input("No. of derogatory public records",0,100)
    
        #revolving balance
        revo_bal = st.sidebar.number_input("Revolving Balance",0.00,10**9.00)
    
        #revolving utilisation
        revo_util = st.sidebar.number_input("Revolving Line Utilization Rate",0.0,1000.0)
    
        #total accounts
        total_acct = st.sidebar.number_input("Total Accounts",0,200)
    
        #initial list status
        initial_list_st = st.sidebar.selectbox("Initial List Status",['Whole','Fractional Market'])
    
        #total recording late fee
        total_rec_late_fe = st.sidebar.number_input("Total Recording Late Fee",0.00,5000.00)

        #last payment amount
        last_pymt_amt = st.sidebar.number_input("Last Payment Amount",0.00,10**6.00)
    
        # last fico_range high
        last_fico_range_hi = st.sidebar.number_input("Last FICO Score [High]",0.0,1000.0)
    
        #fico_range_lowe
        last_fico_range_lower = st.sidebar.number_input("Last FICO Score [low]",0.0,1000.0)
    
        # collections ex med
        collections_ex_med = st.sidebar.number_input("Collections [Ex-med for past 12 months]",0.0,50.0)

        #policy code
        pol_options = [1.0]
        pol_code = st.sidebar.selectbox("Gender",pol_options)

        #application type
        app_options= ['Individual','Joint App']
        app_type = st.sidebar.selectbox("Application Type", app_options)

         #account now dealing
        acc_dealing_now = st.sidebar.number_input("No.of Accounts Now Dealing",0,20)
    
        #total collecion amount
        total_col_amt = st.sidebar.number_input("Total Collection Amount",0.00,10**7.00)
    
        #total current balance
        total_cur_bal = st.sidebar.number_input("Total Current Balance",0.00,10**7.00)
    
        #total balance available
        total_avail_bal = st.sidebar.number_input("Total Available Balance",0.00,2*10**6.00)
    
        #maximum balance 
        max_balance_bc = st.sidebar.number_input("Maximum Current Balance",0.00,2*10**6.00)
    
        #Issue date month
        #issue_d_month = st.sidebar.date_input('Issue date',datetime.date.today())
        #issue_options = ['January','February','March','April','May','June','July','August',
                    # 'September','October','November','December']
        issue= st.sidebar.date_input("Issue Date")
    
        #earliest credit line date
        ecl= st.sidebar.date_input("Earliest Credit Line")
    
                                         
        #last payment date
        lpm= st.sidebar.date_input("Last Payment Date")
    
        #last credit pull date
        lcp= st.sidebar.date_input("Last Credit Pull Date")
    
        
        df = pd.DataFrame({'funded_amnt_inv':funded_amt_inv ,
    'int_rate':interest_r ,
    'emp_length':emp_len,
    'annual_inc':annual_inc,
    'pymnt_plan':pymt_plan,
    'dti':dti_r,
    'deling_2yrs':deling_2,
    'fico_range_low':fico_range_lower,
    'ing_last_6mths':inq_last_6 ,
    'open_acc':open_acct ,
    'pub_rec':pub_recs ,
    'revol_bal':revo_bal ,
    'revol_util':revo_util,
    'total_acc':total_acct,
    'initial_list_status':initial_list_st,
    'total_rec_late_fee':total_rec_late_fe,
    'last_pymnt_amnt':last_pymt_amt,
    'last_fico_range_high':last_fico_range_hi,
    'last_fico_range_low':last_fico_range_lower,
    'collections_12_mths_ex_med':collections_ex_med,
    'policy_code':pol_code ,
    'application_type':app_type,
    'acc_now_dealing':acc_dealing_now ,
    'tot_coll_amt':total_col_amt,
    'tot_cur_bal':total_cur_bal,
    'total_bal_il':total_avail_bal ,
    'max_bal_bc':max_balance_bc,
    'issue_d':issue ,
    'earliest_cr_line':ecl,
    'last_pymnt_d':lpm,
    'last_credit_pull_d':lcp},index=[0],
    columns=['funded_amnt_inv',
     'int_rate',
     'emp_length',
     'annual_inc',
     'pymnt_plan',
     'dti',
     'deling_2yrs',
     'fico_range_low',
     'ing_last_6mths',
     'open_acc',
     'pub_rec',
     'revol_bal',
     'revol_util',
     'total_acc',
     'initial_list_status',
     'total_rec_late_fee',
     'last_pymnt_amnt',
     'last_fico_range_high',
     'last_fico_range_low',
     'collections_12_mths_ex_med',
     'policy_code',
     'application_type',
     'acc_now_dealing',
     'tot_coll_amt',
     'tot_cur_bal',
     'total_bal_il',
     'max_bal_bc','issue_d','earliest_cr_line','last_pymnt_d','last_credit_pull_d'])
        for col in ['issue_d','earliest_cr_line','last_pymnt_d','last_credit_pull_d']:
                    date = pd.to_datetime(df[col],format='%Y/%m/%d')
                    df[col+'_year'] = date.dt.year
                    df[col+'_month'] = date.dt.month 
        label_binary_columns = ['pymnt_plan','initial_list_status','application_type']

        labelb = LabelBinarizer()
        for col in label_binary_columns:
            df[col] = labelb.fit_transform(df[col])
       
       
        features = ['funded_amnt_inv',
     'int_rate',
     'emp_length',
     'annual_inc',
     'pymnt_plan',
     'dti',
     'deling_2yrs',
     'fico_range_low',
     'ing_last_6mths',
     'open_acc',
     'pub_rec',
     'revol_bal',
     'revol_util',
     'total_acc',
     'initial_list_status',
     'total_rec_late_fee',
     'last_pymnt_amnt',
     'last_fico_range_high',
     'last_fico_range_low',
     'collections_12_mths_ex_med',
     'policy_code',
     'application_type',
     'acc_now_dealing',
     'tot_coll_amt',
     'tot_cur_bal',
     'total_bal_il',
     'max_bal_bc',
     'issue_d_month',
     'earliest_cr_line_month',
     'earliest_cr_line_year',
     'last_pymnt_d_month',
     'last_credit_pull_d_month',
     'last_credit_pull_d_year']
        
        input_features = df[features]
        if st.button('Predict'):
              result = model.predict(input_features)
              st.success('The Predicted Grade is: ')
              st.write(result)
        prediction_proba=model.predict_proba(input_features)
        st.subheader('Prediction Probability')
        st.write(prediction_proba) 

if __name__ == '__main__':
    main()
    

