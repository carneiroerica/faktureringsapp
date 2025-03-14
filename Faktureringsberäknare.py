import streamlit as st
import pandas as pd

# Sidrubrik
st.title("Faktureringsberäknare - GWR")

# Create the data
data = {
    'dp': ['DP1', 'DP2','DP4','DP5','DP10'],  # Character values
    'no': [40, 24, 7, 11, 4]             # Numeric values
}

# Create the DataFrame
df = pd.DataFrame(data)

# Create a dropdown based on the 'dp' column
selected_dp = st.selectbox('Välj detaljplan:', df['dp'])
#selected_no = df[selected_dp,'no']
# Extract the corresponding 'total_gwr' value
total_gwr_value = df.loc[df['dp'] == selected_dp, 'no'].iloc[0]


# Användaren matar in ett fakturabelopp
belopp = st.number_input("Ange fakturans totalbelopp:", min_value=0.0, step=100.0)

# Calculate the ratio
ratio = total_gwr_value / df['no'].sum()
belopp_t = belopp*ratio
# Beräkning och visning av resultat
if belopp_t > 0:
    tpab = belopp_t * 0.82
    täby_kommun = belopp_t * 0.09
    riksbyggen = belopp_t * 0.06
    wallenstam = belopp_t * 0.03

    st.write(f"### Uppdelning av beloppet:")
    st.write(f"**TPAB:** {tpab:.2f} kr")
    st.write(f"**Täby Kommun:** {täby_kommun:.2f} kr")
    st.write(f"**Riksbyggen:** {riksbyggen:.2f} kr")
    st.write(f"**Wallenstam:** {wallenstam:.2f} kr")


