import streamlit as st
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Deutsche_Telekom_2022.svg/1024px-Deutsche_Telekom_2022.svg.png", width =100)

st.title('ONE Script')
#new_title = '<p style="font-family:ariel; color:Black; font-size: 54px;font-weight: 900;">ONE Script</p>'
#st.markdown(new_title, unsafe_allow_html=True)

st.header("One stop ETL")
#new_heading = '<p style="font-family:verdana; color:black; font-size: 42px;">One stop ETL</p>'
#st.markdown(new_heading, unsafe_allow_html=True)
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.telekom.com/resource/image/479398/landscape_ratio2x1/1296/648/a9ca660537f7304e9f8e86d41d636fc8/FD94178AECF373783ACB36331F0AEA9E/bi-icss-en-b.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

col1, col2, col3 ,col4 = st.columns(4)

with col1:
   #new_col1 = '<p style="font-family:arial; color:Black; font-size: 32px;font-weight: 900;">Global Variables</p>'
   #st.markdown(new_col1, unsafe_allow_html=True)
   st.header('Global Prameters')
   INPOOL_DIR=st.text_input("inpool")
   STAGING_DIR=st.text_input("staging")
   SOURCE_DIR=st.text_input("source")
   FTP_DIR=st.text_input("ftp")
   

with col2:
   #new_col2 = '<p style="font-family:arial; color:Black; font-size: 32px;font-weight: 900;">Lexographical parameter</p>'
   #st.markdown(new_col2, unsafe_allow_html=True)
   st.header("Lex params")
   parameter=st.text_input("enter params")
   dext=st.text_input("d extension")
   cext=st.text_input("c extension")
   #SRC_DIR_LEX=st.text_input("source directory of lex")
   #DEST_DIR_LEX=st.text_input("dest directory of lex")



with col3:
   #new_col2 = '<p style="font-family:arial; color:Black; font-size: 32px;font-weight: 900;">Control File</p>'
   #st.markdown(new_col2, unsafe_allow_html=True)
   st.header("Control file")
   cext_mf=st.text_input("c extension mf")
   dext_mf=st.text_input("d extension mf")
   header =st.selectbox(
    'Header',
    ('y', 'n'))
   footer= st.selectbox(
    'Footer',
    ('y', 'n'))
   #SRC_DIR_CF=st.text_input("src dir")
   #DEST_DIR_CF=st.text_input("dest dir")
   delim=st.text_input("delimiter")
   r_pos=st.text_input("r_pos")
   b_pos=st.text_input("b_pos")
   
   
with col4:
   #new_col2 = '<p style="font-family:arial; color:Black; font-size: 32px;font-weight: 900;">Control File</p>'
   #st.markdown(new_col2, unsafe_allow_html=True)
   st.header("SFTP pull")
   remote_host_src=st.text_input("remote host")
   remote_user_src=st.text_input("remote user")
   remote_path_src=st.text_input("remote path")
   local_path=st.text_input("local path")
   last_date_file=st.text_input("last date file")
   keyfile_src=st.text_input("key file source")
   PORT_SRC=st.text_input("port")
   DEST_DIR_SFTP_PULL=st.text_input("destination dir")
   SRC_DIR_SFTP_PULL=st.text_input("source dir")
   date_pattern_src=st.text_input("edate pattern")
   remote_server_clean= st.selectbox(
    'clean remote server',
    ('y', 'n'))
   
   
   
   

download=st.button("Download properties file")
if download:
    print("it is going to write file")
    with open('generic.properties', 'w') as f:
        f.write('INPOOL_DIR = "' + str(INPOOL_DIR) + '"\n')  
        f.write('STAGING_DIR = "' + str(STAGING_DIR) + '"\n')
        f.write('SOURCE_DIR = "' + str(SOURCE_DIR) + '"\n')
        f.write('FTP_DIR = "' + str(FTP_DIR) + '"\n')
    















