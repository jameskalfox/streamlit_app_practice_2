import streamlit
import snowflake.connector
import pandas

my_cnx = snowflake.connector.connect(**streamlit.secrets['snowflake'])
my_cur = my_cnx.cursor()

my_cur.execute('select color_or_style from catalog_for_website')
my_catalog = my_cur.fetchall()

df = pandas.DataFrame(my_catalog)
colour_list = df[0].values.tolist()

streamlit.header('Zena\'s Amazing Athleisure Catalog')

option = streamlit.selectbox('Pick a sweatsuit colour or style:', colour_list)

streamlit.image
streamlit.write('Our ' + option + ' sweatsuit')

my_cur.execute(
    'select direct_url from catalog_for_website where color_or_style = \'' + option + '\'')
df2 = my_cur.fetchone()

streamlit.image(df2[0], width=400)
