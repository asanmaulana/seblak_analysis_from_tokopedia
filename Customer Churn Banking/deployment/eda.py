import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():

    #Membuat Title
    st.title('Churn Prediction Model')

 
    # create the opening

    st.write ('Churn rate is a factor that must be maintained by the company to ensure the business continues to run well. When the churn rate is low, it indicates that the company has succeeded in retaining the majority of its customers.')
    
    st.write('This model will predict the activities or status of the customer, including basic information about their activities, credit card ownership, and other important information, which can serve as parameters to determine whether a person will stay or churn.')

    st.write ("Before we proceed, let's take a look at a sample of the dataset used to train this model.")

    # Memuat dan menampilkan file CSV
    csv_file = 'dataset_churn.csv'  # Ganti dengan path ke file CSV yang sesuai
    df = pd.read_csv(csv_file)
    st.dataframe(df)

    # create pie chart about churn rate
    churn = df['Exited'].value_counts()
    fig = px.pie(
        values=churn.values, 
        names=churn.index, 
        title='Percentage of Churn vs No-Churn',
        color_discrete_sequence=['CadetBlue', 'SkyBlue'], 
        hole=.3,
        labels={'index': 'Churn Status', 'values': 'Count'},
        opacity=0.8,
        width=600, 
        height=400
    )
    fig.update_traces(textinfo='percent+label', pull=[0, 0.1])
    st.plotly_chart(fig)

    st.write('According to the dataset, 20 percent of the customers are predicted to churn. To better understand this trend, we need to investigate the geographic distribution of these customers. Do they predominantly come from Germany, Spain, or France? Let us delve into this analysis.')

     # Memfilter pelanggan yang churn
    churned_customers = df[df['Exited'] == 1]

    # Menghitung jumlah churn per negara
    churn_per_country = churned_customers['Geography'].value_counts().reset_index()
    churn_per_country.columns = ['Geography', 'Count']

    # Membuat bar plot menggunakan Plotly
    fig = px.bar(churn_per_country, x='Geography', y='Count',
                 title="Total Churned Customers per Country",
                 labels={'Count': 'Number of Churned Customers', 'Geography': 'Country'},
                 color='Geography',  # Memberikan warna berbeda berdasarkan negara
                 height=400)
    
    # Menampilkan plot di Streamlit
    st.plotly_chart(fig)


    st.write('It turns out that many of the customers who churn are from France and Germany. Let us take another look to see whether they are active or not.')
    # Membuat count plot dengan Plotly
    fig = px.histogram(df, x='IsActiveMember', color='Exited',
                       barmode='group',
                       labels={'IsActiveMember': 'Member Status', 'Exited': 'Churn Status'},
                       title='Total Active Members Grouped by Churn Status',
                       color_discrete_map={0: 'red', 1: 'blue'})  # Atur warna

    # Mengganti nilai x axis labels
    fig.update_xaxes(tickvals=[0, 1], ticktext=['Passive Member', 'Active Member'])
    
    # Menambahkan label pada bar
    fig.update_traces(texttemplate='%{y}', textposition='outside')

    # Menampilkan legenda dengan nama yang lebih deskriptif
    fig.update_layout(legend_title='Churn Status', legend=dict(
        traceorder='reversed',
        title_font_family='Arial',
        itemsizing='constant',
        tracegroupgap=0,
        y=1.02, yanchor="auto",
    ))
    
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))

     # Tampilkan plot di Streamlit
    st.plotly_chart(fig)

    st.write('Inactive customers tend to exited more rather than active customer. Do churned customers have higher balance?')

    # Membuat bins dan label untuk segmentasi saldo
    bins = [0, 1, 25000, 50000, 75000, 100000, 125000, 150000, float('inf')]
    labels = ['0', '1-25K', '25-50K', '50-75K', '75-100K', '100-125K', '125-150K', '150K+']
    
    # Menggunakan pd.cut untuk membuat kolom baru
    df['BalanceGroup'] = pd.cut(df['Balance'], bins=bins, labels=labels, right=False)

    # Membuat bar plot dengan Plotly
    fig = px.histogram(df, x='BalanceGroup', color='Exited', barmode='group',
                       title='Customer Exit Status by Balance Group',
                       labels={'Exited': 'Churn Status'},
                       category_orders={"BalanceGroup": labels},  # Urutkan x-axis sesuai dengan urutan bins
                       color_discrete_map={'1': 'Green', '0': 'Blue'})  # Customize warna jika diperlukan

    # Tambahkan label pada bar
    fig.update_traces(texttemplate='%{y}', textposition='outside')

    # Tampilkan plot di Streamlit
    st.plotly_chart(fig)

    st.write("It appears that customers with high balances, as well as those with zero balances, are more likely to churn. However, there is a possibility that the zero balance could be automatically adjusted by the system. For this analysis, we define a 'high balance' as any balance over 100K. With that in mind, which country has the highest average customer balance?")

    # Menghitung rata-rata saldo per negara
    plote = df.groupby(['Geography'])['Balance'].mean()

    # Membuat bar plot dengan Matplotlib
    fig, ax = plt.subplots()
    plote.plot(kind='bar', color='blue', ax=ax)
    ax.set_title('Average Balance by Country')
    ax.set_ylabel('Average Balance')
    ax.set_xlabel('Country')

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

    st.write("In summary, we now have a clearer profile of customers with the highest likelihood of churn. They are likely from Germany, have a high balance, and may be inactive members. Of course, this conclusion is neither 100 percent accurate nor entirely false, as the data is vast and complex, making it difficult to definitively determine the exact profile of churned customers.This is why we need a machine learning model—to make more accurate predictions rather than relying on guesswork")

    st.write ('You can proceed to the next page for accessing the prediction model and exploring its deployment.')



if __name__ == '__main__':
    run()