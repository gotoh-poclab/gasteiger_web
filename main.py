import streamlit as st

from common.multiapp import MultiApp

from main_pages.GasteigerCharge import rdkit_charge_analysis


st.set_page_config(page_title="chemoinfomaticstool")
st.title('Chemoinfomatics Tool')

main = MultiApp()


main.add_app("🔋ChargeAnalysis", rdkit_charge_analysis)

main.run()