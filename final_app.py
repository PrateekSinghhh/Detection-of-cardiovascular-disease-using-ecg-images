import streamlit as st
from ecg import  ECG
ecg = ECG()

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  """#### **UPLOADED IMAGE**"""
  # call the getimage method
  ecg_user_image_read = ecg.getImage(uploaded_file)
  #show the image
  st.image(ecg_user_image_read)

  """#### **GRAY SCALE IMAGE**"""
  #call the convert Grayscale image method
  ecg_user_gray_image_read = ecg.GrayImgae(ecg_user_image_read)
  
  #create Streamlit Expander for Gray Scale
  my_expander = st.expander(label='Gray SCALE IMAGE')
  with my_expander: 
    st.image(ecg_user_gray_image_read)
  
  """#### **DIVIDING LEADS**"""
   #call the Divide leads method
  dividing_leads=ecg.DividingLeads(ecg_user_image_read)

  #streamlit expander for dividing leads
  my_expander1 = st.expander(label='DIVIDING LEAD')
  with my_expander1:
    st.image('Leads_1-12_figure.png')
    st.image('Long_Lead_13_figure.png')
  
  """#### **PREPROCESSED LEADS**"""
  #call the preprocessed leads method
  ecg_preprocessed_leads = ecg.PreprocessingLeads(dividing_leads)

  #streamlit expander for preprocessed leads
  my_expander2 = st.expander(label='PREPROCESSED LEAD')
  with my_expander2:
    st.image('Preprossed_Leads_1-12_figure.png')
    st.image('Preprossed_Leads_13_figure.png')
