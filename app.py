import streamlit as st
import pickle
import pandas as pd
import numpy as np



pipe = pickle.load(open('final-true-bht.pkl','rb'))
st.title('True BHT Predictor')


depth = st.number_input('depth')
stemp = st.number_input('stemp')
clay_present = st.number_input('clay present')
clay_type = st.number_input('clay type')
wa_or_nwa = st.number_input('wa or nwa')
clay_content = st.number_input('clay content')
corr_bht = st.number_input('corr bht')
alpha = st.number_input('alpha')
beta = st.number_input('beta')


# 'pH(CaCl2)':[pH(CaCl2)],'pH(H2O)':[pH(H2O)],
if st.button('Predict'):
      input=pd.DataFrame({'depth':[depth],'surface temp':[stemp],'clay_present':[clay_present],'clay_type':[clay_type],'water active ?':[wa_or_nwa],'clay_content':[clay_content],'corr_bht':[corr_bht],'alpha':[alpha],'beta':[beta]})
      result = pipe.predict(input)
      st.success('THE TRUE BHT FOR GIVEN DATA WILL BE {}'.format(result))
# st.header(result)
