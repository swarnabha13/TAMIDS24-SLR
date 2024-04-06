# Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.

# ~~~~~~~~~~~~~~~~~~~~~ Importing required packages -

import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import webbrowser

# ~~~~~~~~~~~~~~~~~~~~~ Different User pages and respective functions -

# ~~~~~~~~~~ Home Page -

def home_page():
    # Setting the title -
    #st.title("TAMIDS Data Science Competition 2024")

    # Desription -
    st.markdown("""
                <p style='text-align: justify;'>
                The 2024 TAMIDS Data Science Competition is about finding the
                impact of Sea Level Rise.
                </p>
                """, unsafe_allow_html=True)

    # Problem Statement -
    st.write("""
             ## Problem Statement
             """)
    st.markdown("""
                <p style='text-align: justify;'>
            Will the sea level rise in the future? If so, by how much?</p>
                
            <p style='text-align: justify;'>Rising sea levels due to climate change pose a severe threat to coastal regions around the United States and globally. As global temperatures increase, glaciers and ice sheets are melting at an accelerated rate, adding vast amounts of water to the world's oceans. This melting of land-based ice is the primary driver of sea level rise, along with the thermal expansion of warming ocean waters.</p>
            <p style='text-align: justify;'>The cumulative loss of mass from glaciers worldwide is projected to continue increasing over time, as shown by the equation:</p>
            <p>
                Cumulative Loss of Mass (Gigatonnes) = 
                <span style="white-space: nowrap;">-8.73y<sup>2</sup> + 3.5×10<sup>4</sup>y - 3.46×10<sup>7</sup></span>
            </p>
            <p style='text-align: justify;'>    Where y is the number of years since 2000. This ongoing ice melt will cause sea levels to rise at varying rates in different U.S. coastal regions based on factors like ocean circulation patterns, land movement, and proximity to melting glaciers.<p>
            <p style='text-align: justify;'>    Projected sea level rise equations for 2024 estimate:<p>
                <ul>
                <li> North Atlantic: 6.38 meter rise
                <li> North Pacific: 7.40 meter rise
                <li> Gulf of Mexico: 9.78 meter rise
                </ul>
                <p style='text-align: justify;'>The impacts of this sea level rise include permanent inundation of low-lying areas, more frequent coastal flooding from high tides and storm surges, erosion of beaches and cliffs, saltwater intrusion into freshwater supplies, and damage to critical infrastructure like roads, utilities, and residential/commercial property.</p>
                <p style='text-align: justify;'>Hundreds of millions of people living in U.S. coastal cities and communities face displacement, along with profound economic disruptions across sectors like tourism, agriculture, fishing, and trade. Coastal ecosystems like wetlands and estuaries that provide storm protection and marine habitats are also at high risk.</p>
                <p style='text-align: justify;'>Mitigating the current and future impacts of sea level rise requires a multi-faceted approach of reducing global greenhouse gas emissions to limit temperature rise, implementing coastal adaptation measures, developing policies for managed retreat from high-risk areas, and investing in resilient infrastructure to protect coastal communities and economies.
             </p>
                """, unsafe_allow_html=True)
    
    image = Image.open('Images/Picture1.png')
    #image = Image.open('Images/rohit img/Beaumont Research_Stephenvile Research.png')
    #Setting the image width
    # Dividing screen into 3 parts -
    col1, col2, col3 = st.columns((0.25,1,0.25))
    col2.image(image, use_column_width = True)

    # Data Collection and Pre-processing -
    st.write("""
             ## Data Collection and Pre-processing
             """)
    st.markdown("""
                <p style='text-align: justify;'>
                    <span style="font-style: italic;">Absolute Dynamic Topography (ADT)</span> is a record of US east coast sea surface height measurements, acquired via satellites from 1993 to 2023. The measurements are detailed, with a fine spatial resolution of 0.25 degrees for both latitude and longitude. It is instrumental for probing the intricate patterns of ocean circulation, as it captures the dynamic activity of the sea. This activity is depicted through fluctuations in ADT, which are indicative of oceanic currents and swirls. Higher ADT values generally signify warmer ocean currents, while lower values are characteristic of cooler currents.
                </p>
                """, unsafe_allow_html=True)
    
    #get_formula()
    
    st.markdown("""
            <p style='text-align: justify;'>
             <span style="font-style: italic;">Global Mean Sea Level (GMSL)</span> is the area-weighted average of sea surface height anomalies from a 10-day cycle of satellite measurements. It's akin to the 'eustatic sea level,' reflecting a hypothetical uniform sea level in a singular global ocean basin, unaffected by local land movements. GMSL changes are attributed to variations in ocean water mass, basin size, and water density, mainly due to thermal expansion and land ice melt. The trend in GMSL data since 1992 shows a predominantly linear increase, especially after accounting for instrument biases and geological impacts.
             </p>
                """, unsafe_allow_html=True)
    #st.markdown("""
    #            <p style='text-align: justify;'>
    #         In order to have a better understanding of these metrics, a graphical representation per department was plotted which 
    #         has been included in our website and a few of these plots have been shown below.
    #         </p>
    #            """, unsafe_allow_html=True)

    
    # Overview -
    st.write("""
             ## Methodology
             """)
    st.markdown("""
                <p style='text-align: justify;'>

                * **Spatial and Temporal Analysis:** The Copernicus dataset consists of the ADT data along both temporal and spatial axes. To decouple the changes of ADT in different dates and positions, average ADT along latitude and longitude are calculated. Differences of ADT between different years are compared as well.

                * **Raw time-series analysis:** We do the analysis for the TOPEX, Jason and Sentinel-6 missions dataset from the aggregated dataset by the researchers from Colorado. We also use datasets from the National Tidal Centre (Bureau of Meteorology, Australia), NASA/JPL – satellite altimeter data, particularly TOPEX/Poseidon to do the time series data analysis. These provide sea level rise data from 1992 to 2022 for various latitudes and longitudes.</p>
                
                <p>
                In the Copernicus dataset, we analyze the ADT time-series with a granularity of latitude and longitude. Statistical metrics such as mean and standard deviation are computed to obtain the overall picture.

                * **Pre-processing, box-plot analysis, and time-series clustering:** We apply a 30-filter window and a 3-degree polynomial Savitzky-Golay [1] filter to each time-series in the Copernicus dataset. Next, a statistical analysis using box-plots is performed over the filtered dataset. More specifically, we use monthly information from the dataset to draw a box-plot series. Then, the filtered dataset is used to run clustering analysis over the time-series. For the time-series clustering, we run principal components analysis (PCA) [2] embedding on each time-series to extract meaningful features. Then, the embedded dataset is used to perform clustering analysis using KMeans algorithm.

                * **Quantitative Analysis and Geospatial Visualization:**  The analysis of the Ramsar wetlands dataset focused on determining the average elevation (ELEV_AVG) distribution across various sites to identify elevation ranges critical for assessing submergence risks. This evaluation of elevation quantiles set the stage for further gradient analysis, which ranked the submergence risk based on proximity to sea level and extent of forest cover. By correlating these gradients with the dataset's percentage risk factors, a comprehensive submersion score was developed, reflective of each area's vulnerability to sea level rise. This approach provided a nuanced understanding of which wetlands are at higher risk and offered a robust framework for predicting the impact of rising sea levels on these ecosystems.
             </p>
                """, unsafe_allow_html=True)

    # Navigation -
    st.write("")
    st.info("Please navigate using the select box in the sidebar on the left.")
    

def get_dept_collab_graph(dept_1):
    #Getting the graph
    HtmlFile = open(f"Images/Dept_collab/dept_collab_{dept_1}.html",'r',encoding = 'utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2,height = 500)


#_______________________US regional Sea level Trend_______________________
def us_sea_level_trend():
    # Setting the title
    st.title('US Regional Sea Level Trend')

    # Description
    st.markdown("""
                <p style='text-align: justify;'>
                While global average sea level rise projections provide an overall estimate, the actual impacts on specific U.S. coastal regions will vary substantially based on regional factors. Along the densely populated U.S. East and Gulf Coasts, sea levels are projected to rise 10-14 inches (0.25-0.36 meters) on average over the next 30 years, and as much as 4.9 feet (1.5 meters) by 2100 under higher emissions scenarios. This puts millions of residents and critical infrastructure at increasing risk of flooding from high tides, storm surges, and permanent inundation of low-lying areas
                </p>""",unsafe_allow_html = True)
    st.write("")

    # Getting the initial image
    col1, col2, col3 = st.columns((1,2.5,1))

    # Getting the graph
    HtmlFile = open("Images/Swarnabha/3d_plot_with_regions.html", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=700)

    st.markdown("""
                <p style='text-align: justify;'>
                To better capture the periodicity and the overall trend of the ADT series, a customized mathematical model is proposed to fit the historical ADT data. In the model, the linearity and the periodicity are represented by the linear and sinusoidal part, respectively.
                </p>
                """, unsafe_allow_html=True)
    st.write("")

    col1,col2 = st.columns((1,1))
    sea_opt = ['North Atlantic','North Pacific','Gulf of Mexico']
    #Geting dept from user
    sea = col1.selectbox("Select the sea region around US",sea_opt)    
    if sea == 'North Atlantic':
        #Setting the Image
        get_sea_data('NA')
    elif sea == 'North Pacific':
        #Setting the Image
        get_sea_data('NP')
    elif sea == 'Gulf of Mexico':
        #Setting the Image
        get_sea_data('GOM')

    sea_level_trend(sea)

    st.markdown("""
                <p style='text-align: justify;'>
                Our model's projections underscore a continuous uptrend in sea levels, leading to growing concerns about coastal inundation, impacts on marine ecosystems, and implications for climate-related resettlement and adaptation strategies. 
                The persistent increase aligns with scientific consensus on climate change, suggesting that rising sea levels pose significant challenges in the decades to come.
                </p>

                <p style='text-align: justify;'>
                We started the projection of sea level using Long Short-Term Memory (LSTM) networks [3]. LSTMs are a type of recurrent neural network that is particularly designed to remember long-term dependencies, making them suitable for modeling sequences of data over time. 
                Figure below shows a series of ADT for the U.S. East and Gulf Coasts, with the blue solid curve representing the historical ADT, and the red dashed line representing the prediction. 
                We can observe that the LSTM model does not accurately capture and predict the seasonality and the rising trend of ADT. 
                </p>
                """, unsafe_allow_html=True)
    st.write("")

    # Dividing screen into 3 parts -
    col1, col2, col3 = st.columns((0.25,1,0.25))

    image = Image.open('Images/Swarnabha/ADT_LSTM.png')

    #Setting the image width
    col2.image(image, use_column_width = True)

def sea_level_trend(sea):
    if sea == 'North Atlantic':
        #Setting the Image
         st.markdown("""
        <p>North Atlantic: Estimated Sea Level<sub>NA</sub> = -49.34 sin(6.27×year+2.5) + 3.25×year - 6504</p>
                     """, unsafe_allow_html=True)
        
    elif sea == 'North Pacific':
        #Setting the Image
         st.markdown("""
        <p>North Pacific: Estimated Sea Level<sub>NP</sub> = -55.56 sin(6.27×year+2.5) + 3.78×year - 7550</p>
                     """, unsafe_allow_html=True)
        
    elif sea == 'Gulf of Mexico':
        #Setting the Image
         st.markdown("""
        <p>Gulf of Mexico: Estimated Sea Level<sub>GM</sub> = -40.98 sin(6.27×year+2.5) + 4.96×year - 9935</p>
                        """, unsafe_allow_html=True)
    
    st.markdown("""
    <p>Where year is the number of years since 2000.</p>
                """, unsafe_allow_html=True)
    st.write("")
        
def get_sea_data(sea):
    #Getting the graph
    HtmlFile = open(f"Images/Swarnabha/{sea}_regions1.html",'r',encoding = 'utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2,height = 400)

    st.markdown("""
                <p style='text-align: justify;'>
                Historical measurements are traced using blue lines, revealing a notable ascending trajectory punctuated by regular fluctuations. A polynomial regression model, shown in Orange, adeptly captures this upward pattern and the inherent periodicity. 
                Red lines extend this model into the future, projecting a persistent rise in sea levels.
                </p>
                """, unsafe_allow_html=True)
    st.write("")

    HtmlFile = open(f"Images/Swarnabha/{sea}_regions2.html",'r',encoding = 'utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2,height = 400)



#_______________________Impacts of Glacier Melting_______________________
def get_glacier_impact():
    # Setting the title
    st.title("Impacts of Glacier Melting")

    # Description
    st.markdown("""
                <p style='text-align: justify;'>
                The cumulative loss of mass from glaciers worldwide is projected to continue increasing over time, as shown by the equation:
                </p>
                <p>
                Cumulative Loss of Mass (Gigatonnes) = -8.73y<sup>2</sup> + 3.5×10<sup>4</sup>y - 3.46×10<sup>7</sup>
                </p>
                <p style='text-align: justify;'>
                Where y is the number of years since 2000. This ongoing ice melt will cause sea levels to rise at varying rates in different U.S. coastal regions based on factors like ocean circulation patterns, land movement, and proximity to melting glaciers.
                </p>
                <p style='text-align: justify;'>
                Projected sea level rise equations for 2024 estimate:
                </p>
                <ul>
                <li> North Atlantic: 6.38 meter rise
                <li> North Pacific: 7.40 meter rise
                <li> Gulf of Mexico: 9.78 meter rise
                </ul>
                <p style='text-align: justify;'>
                The impacts of this sea level rise include permanent inundation of low-lying areas, more frequent coastal flooding from high tides and storm surges, erosion of beaches and cliffs, saltwater intrusion into freshwater supplies, and damage to critical infrastructure like roads, utilities, and residential/commercial property.
                </p>
                <p style='text-align: justify;'>
                Hundreds of millions of people living in U.S. coastal cities and communities face displacement, along with profound economic disruptions across sectors like tourism, agriculture, fishing, and trade. Coastal ecosystems like wetlands and estuaries that provide storm protection and marine habitats are also at high risk.
                </p>
                <p style='text-align: justify;'>
                Mitigating the current and future impacts of sea level rise requires a multi-faceted approach of reducing global greenhouse gas emissions to limit temperature rise, implementing coastal adaptation measures, developing policies for managed retreat from high-risk areas, and investing in resilient infrastructure to protect coastal communities and economies.
                </p>
                """, unsafe_allow_html=True)
    st.write("")

    

    # Dividing screen into 3 parts -
    col1, col2, col3 = st.columns((0.5,1,0.5))

    # Setting the image -
    image = Image.open('Images/Swarnabha/Glacier_melt.png')

    # Setting the image width -
    col2.image(image, use_column_width=True)

#------------------ Grant Analysis -------------------------
def get_grant_graph(dept, year):
    # Getting the Graph -
    if year == '2020 - Current':
        year = '2020'
    elif year == '2010 - 2019':
        year = '2010'
    elif year == '2000 - 2009':
        year = '2000'
    elif year == 'Before 1999':
        year = '0'
    HtmlFile = open(f"Images/Grant_collab/grant_dept_{dept}_{year}.html", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=500)

def get_grant_analysis():
    #Setting the title
    st.title("Grant Analysis and Natural Language processing")

    #Description
    st.markdown("""
                <p style='text-align: justify;'>
                The data related to funding has information about the topic for
                which the funding was provided and the departments which are
                involved. In addition to the amount, it also has the duration
                of the funding.
                </p>""",unsafe_allow_html = True)
    st.write("")

    #Getting the initial image
    col1, col2, col3 = st.columns((1,2.5,1))



    col1,col2 = st.columns((1,1))
    depts = ['Math', 'Physics',
    'Chemistry', 'Earth Science', 'Environmental', 'Biology',
    'Agricultural and Veterinary Sciences', 'Computer Science',
    'Engineering', 'Technology', 'Medical and Health Sciences',
    'Environment and Design', 'Education', 'Economics',
    'Commerce, Management, Tourism and Services', 'Human Society',
    'Psychology and Cognitive Sciences', 'Law',
    'Language, Communication and Culture', 'History and Archaeology',
    'Philosophy and Religious Studies']

    #Geting dept from user
    dept = col1.selectbox("Select department",depts)

    #Getting year info from user
    year = col2.selectbox("Select year range",['All','2020 - Current',
    '2010 - 2019', '2000 - 2009', 'Before 1999'])

    get_grant_graph(dept, year)
    
    
    st.markdown("""
                <p  style = 'text-align: justify;'>
                This graph describes the funding received by different
                departments over the years. The plot contains information
                about the amount of funding received per year, the total
                amount of funding received for every department.
                There are various trends which can be observed here, the trivial
                one being a constant increase in the funding throughout the 
                years for most of the departments.
                </p> """,unsafe_allow_html = True)
    st.write(" ")


    #Grant_collab interactive analysis
    st.markdown("""<p style= 'text-align : justify;'>
                The following interactive graph is about the clustering of
                different departments accoring the connectivity with
                other departments. One can look up multiple departments in
                the searchbox to see the joint grant awards.
                </p>""",unsafe_allow_html = True)
    st.write(" ")

    st.write("""
            We can go to the grant network analysis page by clicking
            on the link. Below is a snapshot of the department-wise Grant
            network analysis""")

    #To access the network analysis, press the button below.

    st.write("")
    col1, col2, col3 = st.columns((1,1,1))
    link = '[Go to dept_wise grant analysis](https://pandey-tushar.github.io/intro_to_TDA/)'
    col2.markdown(link, unsafe_allow_html=True)

    st.write(" ")
    #Setting the Image
    image = Image.open('Images/grant_dept_collab.jpg')

    #Setting the image width
    st.image(image, use_column_width = True)

    st.write(" ")

#------------------ Impact score -----------------------------

def get_impact_dept(dept):
    #Getting the graph
    HtmlFile = open(f"Images/Impact/{dept}.html",'r',encoding = 'utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2,height = 500)    

    
def impact_score():
    #Setting the title
    st.title("Metric to calculate Impact of research")

    #Description
    st.markdown("""
                <p style='text-align: justify;'>
                The analysis related to funding/grant, publication and citations led 
                us to create a powerful metric to determine the significance of specific
                topics within a department that could enhance the chances of receiving 
                grants and influencing the work in the academics as well as industry.
                </p>""",unsafe_allow_html = True)
    st.write("")
    
    get_formula()
    #st.markdown("""
    #            <p style='text-align: justify;'>                
    #            Impact Score = \hat{F}[(Topics) * || C(Topic) ||_1 * ||P(Topic)||_0] / || C(Dept)||_1
    #            </p>""",unsafe_allow_html = True)
    #st.write("")
    #Getting the initial image
    col1, col2, col3 = st.columns((1,2.5,1))

    #Showing intial analysis
    st.markdown("""
                <p style ='text-align: justify;'>
                The following plot describes the impact score for different departments.
                Some interesting observations are, that neither of the factors alone is 
                sufficient to determine the impact, thereby implying that our approach 
                might be an efficient perspective to look from. 
                </p>""",unsafe_allow_html = True)
    st.write(" ")
    
    col1,col2 = st.columns((1,1))
    depts = ['Mathematics', 'Physics',
    'Chemistry', 'Biology and Genetics',
    'Agriculture and Crop Sciences', 
    'Engineering', 'History and Archaeology',
    'Geology and Geophysics']

    #Geting dept from user
    dept = col1.selectbox("Select department",depts)

    get_impact_dept(dept)
    
    #Another graph
    st.markdown("""
                <p style = 'text-align: justify;'>
                It's a 3D scatter plot, which beautifully describes the 
                effects of funding, citation and publication on impact
                score, for different buzzwords within different departments.
                </p>""",unsafe_allow_html=True)
    st.write(" ")
    
    st.markdown("""
                <p style = 'text-align: justify;'>
                The graph is interactive, where we can rotate it to look at
                the points in 3-Dimensions from different angles.
                </p>""",unsafe_allow_html=True)
    st.write(" ")
    
    
    st.markdown("""
                <p style = 'text-align: justify;'>
                The motivation for impact score was paved through the following pipeline
                
                Publication data Collection and cleaning ->
                Natural Language Processing on data related to publications ->
                Data analysis using similarity metrics and network analysis using TDA ->
                Grant data collection and preprocessing -> 
                Natural Language Processing on Grant data ->
                Network Analysis using TDA and grant trends ->
                Merge the two dataset using common keywords ->
                Frequent words used in grants associates to higher citations and higher publications ->
                "Canonical choice of metric - Impact Score based on normalized values"
                </p>""",unsafe_allow_html=True)
    st.write(" ")
    
    

#------------------ About the Authors -------------------------
def authors():
    # Setting the title -
    st.title("About the Authors")
    st.write(" ")


    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75,0.1,2))

    # Setting the image -
    image = Image.open('Images/Hailiang_2023_CS.jpg')

    # Setting the image width -
    col1.write("")
    col1.image(image, use_column_width=True)

    # Hailiang Hu -
    col3.write("## Hailiang Hu")

    # About section -
    col3.write("""
               Research Area: Placement Optimization on FPGAs, Machine Learning in EDA

               * **Department:** Electrical and Computer Engineering
               * **Degree:** PhD Student 
               * **Email:** hailiang@tamu.edu
               * **LinkedIn:** [linkedin.com/in/hailiang-hu-282b90ba/](https://www.linkedin.com/in/hailiang-hu-282b90ba/)
               * **Website:** [hailiangh.github.io/](https://hailiangh.github.io/)
               """)
    st.write("")

    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75,0.1,2))

    # Setting the image -
    image = Image.open('Images/cristhian.jpg')

    # Setting the image width -
    col1.write("")
    col1.write("")
    col1.image(image, use_column_width=True)

    # Ritesh Singh Suhag -
    col3.write("## Cristhian Roman Vicharra")

    # About section -
    col3.write("""
               Research Area: Machine learning, quantum computing and molecular modelling.

               * **Department:** Electrical and Computer Engineering
               * **Degree:** PhD Student 
               * **Email:** cristhianroman@tamu.edu
               * **LinkedIn:** [www.linkedin.com/in/cristhianromanv/](https://www.linkedin.com/in/cristhianromanv/)
               """)
    st.write("")

    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75,0.1,2))

    # Setting the image -
    image = Image.open('Images/souryendu.jpg')

    # Setting the image width -
    col1.write("")
    col1.write("")
    col1.image(image, use_column_width=True)

    # Abhijit Mahapatra -
    col3.write("## Souryendu Das")

    # About section -
    col3.write("""
               Research Area: Computer Networking

               * **Department:** Department of Electrical and Computer Engineering
               * **Degree:** PhD student
               * **Email:** bubunda@tamu.edu 
               * **LinkedIn:** [linkedin.com/in/souryendu-das/](https://www.linkedin.com/in/souryendu-das/)
               """)
    st.write("")
    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75,0.1,2))

    # Setting the image -
    image = Image.open('Images/swarnabha.jpg')

    # Setting the image width -
    col1.write("")
    col1.write("")
    col1.image(image, use_column_width=True)

    # Swarnabha -
    col3.write("## Swarnabha Roy")

    # About section -
    col3.write("""
               Research Area: Modular Robotics and Virtual Reality.

               * **Department:** Department of Electrical and Computer Engineering
               * **Degree:** PhD Student 
               * **Email:** swarnabha7@tamu.edu
               * **LinkedIn:** [linkedin.com/in/swarnabha7/](https://www.linkedin.com/in/swarnabha7/)
               * **Github:** [github.com/swarnabha13](https://github.com/swarnabha13)
               """)
    st.write("")

#* **Github:** [github.com/swarnabha13](https://github.com/swarnabha13)






#--------------------------- Main Application page----------------

st.set_page_config(layout='wide', page_title = 'Imapct of Sea Level Rise', page_icon="chart_with_upwards_trend")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Setting the image - 
image = Image.open('Images/MainPage.png')

# Setting the image width -
st.image(image, use_column_width=True)

# Sidebar navigation for users -
st.sidebar.header('Navigation tab')
navigation_tab = st.sidebar.selectbox('Choose a tab', ('Home-Page',
 'US regional Sea level Trend', 'Impacts of Glacier Melting','About the Authors'))

# Displaying pages according to the selection -

# Home page -
if navigation_tab == 'Home-Page':
    home_page()

# First page -
elif navigation_tab == 'US regional Sea level Trend':
    us_sea_level_trend()

# Second page -
elif navigation_tab == 'Impacts of Glacier Melting':
    get_glacier_impact()


# Second Page -
elif navigation_tab == 'Collaboration potential':
    collaboration_plot()

# Third Page -
elif navigation_tab == 'Grant Analysis':
    get_grant_analysis()

# Fourth Page -
elif navigation_tab == 'Impact score':
    impact_score()
    



# About Page -
elif navigation_tab == 'About the Authors':
    authors()
