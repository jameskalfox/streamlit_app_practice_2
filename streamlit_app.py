import streamlit
import snowflake.connector
import pandas

my_cnx = snowflake.connector.connect(**streamlit.secrets['snowflake'])
my_cur = my_cnx.cursor()

my_cur.execute('select color_or_style from catalog_for_website')
my_catalog = my_cur.fetchall()

df = pandas.DataFrame(my_catalog)
streamlit.write(df)

streamlit.header('Zena\'s Amazing Athleisure Catalog')

streamlit.selectbox('Pick a sweatsuit colour or style:', list(df))
