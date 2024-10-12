import  streamlit as st

gelir = st.number_input("Brüt gelir giriniz")
gelir = int(gelir)
if gelir <= 110000:
    gelir = gelir * 0.15
    st.write(gelir)
elif gelir <= 230000:
    gelir = 16500 + (gelir - 110000) * 0.20
    st.write(gelir)
elif gelir <= 870000:
    gelir = 40500 + (gelir - 230000) * 0.27
    st.write(gelir)
elif gelir <= 3000000:
    gelir = 213300 + (gelir - 870000) * 0.35
    st.write(gelir)
else:
    gelir = 958800 + (gelir - 3000000) * 0.40
    st.write(gelir)
st.write('işte kazancınız')