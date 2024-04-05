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
    
    image = Image.open('Images\Picture1.png')
    #Setting the image width
    st.image(image, use_column_width = True)

    # Data Collection and Pre-processing -
    st.write("""
             ## Data Collection and Pre-processing
             """)
    st.markdown("""
                <p style='text-align: justify;'>
                 The analysis has been made on two groups of data: Grants and Publications. We created a dataset with
                 different publication data including abstract, departments, research institutions and citation data.
                 Before diving deep into the analysis, we tried to estimate the impact of research using four 
                 main-terms per abstract word that have been defined per department.                
                 <ul>
                 <li> Publication score:
                 <li> Citation score
                 <li> Normalized funding
                 <li> Impact score </ul>
                 Impact Score =  Normalized(Funding(Topic for dept)) x 
                 [no of publication (for topic in dept) x Total citation 
                 for topic]/Total citation for dept
                 </p>
                """, unsafe_allow_html=True)
    
    get_formula()
    
    st.markdown("""
                <p style='text-align: justify;'>
             The abstract keywords per department were calculated by using NLP algorithms on the dataset containing the 
             abstracts of the publications using unigram, bigram and trigram to find the most frequently occurring sequential tokens. 
             From the sequential tokens, the generic words were removed to formulate a clean corpus which was used to compute the four 
             types of scores defined above.
             </p>
                """, unsafe_allow_html=True)
    st.markdown("""
                <p style='text-align: justify;'>
             In order to have a better understanding of these metrics, a graphical representation per department was plotted which 
             has been included in our website and a few of these plots have been shown below.
             </p>
                """, unsafe_allow_html=True)

    
    # Overview -
    st.write("""
             ## Methodology
             """)
    st.markdown("""
                <p style='text-align: justify;'>

                * **Feature Engineering:** Data normalization explained
                * **Unsupervised Learning:** Clustering based on different features of the data. Rather, with the mapper package, we see a better picture of our clusters which brings us to the visualizations.
                * **Dynamic Visualization:** About TDA and other visualization. Therefore, the website we have designed is very dynamic and suitable for everyone.
             </p>
                """, unsafe_allow_html=True)

    # Navigation -
    st.write("")
    st.info("Please navigate using the select box in the sidebar on the left.")
    
def get_formula():
    #Getting the graph
    HtmlFile = open(f"formula.html",'r',encoding = 'utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2,height = 200)


def get_topics():
    #Getting the graph
    HtmlFile = open(f"Publication_data/topics.html",'r',encoding = 'utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2,height = 500)
    
def get_dept_collab_graph(dept_1):
    #Getting the graph
    HtmlFile = open(f"Images/Dept_collab/dept_collab_{dept_1}.html",'r',encoding = 'utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2,height = 500)

#------------------ Publication Analysis----------------
def publication_analysis():
    # Setting the title
    st.title('Publication Analysis and NLP')

    #description
    st.markdown("""
                <p style='text-align: justify;'>
                The key aspect of the project was to do Natural Language
                processing on the bibliometric data and find meaningful insights.
                Different keywords are related to different professors and departments
                with a possibility or existence of collaboration.
                """,unsafe_allow_html = True)
    st.write("")

    #Getting the intial Image
    col1, col2, col3 = st.columns((1,2.5,1))

    get_topics()
    
    st.markdown("""<p style='text-align: justify;'>
                Initially we started exploration of the corpus with capping the word 
                limit of sentences of abstract to 10000. The ideas was to find the 
                frequency of words in abstracts with either high altimetric score 
                or citation or public responses in different media channels. Then 
                correlating those words for grant received for the 
                research/publications. Hence we did the analysis and formed 
                15 topics with associated keywords where these word occurances 
                fetched great funds and associated with publications with high 
                predefined metrics.
                </p>""", unsafe_allow_html = True)
    st.write("")

    col1, col2 = st.columns((1,1))
    dept_lst = [' Aerospace Engineering',' Biochemistry and Biophysics',
    ' Biological and Agricultural Engineering', ' Biomedical Engineering',
    ' Chemical Engineering', ' Computer Science and Engineering',
    ' Learning and Culture', ' Materials Science and Engineering',
    ' Ocean Engineering', ' Park and Tourism Sciences',
    ' Veterinary Integrative Biosciences', 'Animal Science',
    'Biological and Agricultural Engineering', 'Chemistry',
    'Civil Engineering', 'Electrical and Computer Engineering',
    'Mechanical Engineering', 'Molecular and Cellular Medicine',
    'Recreation', 'Teaching', 'Veterinary Physiology and Pharmacology']
    #Getting dept_1 from user
    dept_1 = col1.selectbox("Select department",dept_lst)
  

    #Getting the graph
    get_dept_collab_graph(dept_1)
    
    st.markdown("""
                <p style ='text-align: justify;'>
                This graph represents the existing collaboration between departments
                along with the insight related to the similarity between them based on 
                the publication data obtained from altmetric website. 
                x represents other departments with collaborations (some) and y represents
                the number of publications they have together.
                We can select a department and look at the common publications
                they have with some other departments. The departments are sampled based 
                on high publication counts and non zero collaboration.
                </p>
                """,unsafe_allow_html = True)
    st.write("")

    #Dept_collab interactive analysis
    st.markdown("""
                <p style='text-align: justify;'>
                The following interactive graph is about the departments with different publications
                for different years, with a possibility at looking at multiple departments.
                </p>
                """, unsafe_allow_html = True)
    st.write(" ")
    st.write("""
            We can go to the department collaboration page by clicking on the
            link. Below is a snapshot of the dept collaboration network analysis.
            """)
    # To access the network analysis, press the button below -
    st.write("")
    col1, col2, col3 = st.columns((1,1,1))
    link = '[Go to Department Network Analysis](https://pandey-tushar.github.io/TAMIDS-22/)'
    col2.markdown(link, unsafe_allow_html=True)

    st.write(" ")
    #Setting the Image
    image = Image.open('Images/dept_collab.jpg')

    #Setting the image width
    st.image(image, use_column_width = True)

    st.write(" ")


    #Univ_collab interactive analysis
    st.markdown("""
                <p style='text-align: justify;'>
                The following interactive graph is about the collaboration
                between different universities, which can be further filtered to
                different departments.</p>
                """,unsafe_allow_html=True)
    st.write(" ")
    st.write("""
            You can go to the University collaboration page by clicking on the
            link. Below is a snapshot of the university collaboration network analysis.
            """)
    # To access the network analysis, press the button below -
    st.write("")
    col1, col2, col3 = st.columns((1,1,1))
    link = '[Go to University Network Analysis](https://pandey-tushar.github.io/Datathon-21/)'
    col2.markdown(link, unsafe_allow_html=True)

    st.write(" ")
    #Setting the Image
    image = Image.open('Images/univ_collab.jpg')

    #Setting the image width
    st.image(image, use_column_width = True)

    st.write(" ")


    
    
#-------------------- Potential Collab -----------------    
def get_dept_similar_graph(dept):
    #Setting the Image
    image = Image.open('Images/rohit img/{dept}.png')

    #Setting the image width
    st.image(image, use_column_width = True)
    
def collaboration_plot():
    #Setting the title
    st.title("Similar research areas for different departments")

    #Description
    st.markdown("""
                <p style='text-align: justify;'>
                 A similarity score is generated for every combination of the
                 department and in this case, we use the cosine similarity. 
                 Higher the cosine similarity score between two departments, 
                 higher is their potential to work together on various subdisciplines.
                </p>""",unsafe_allow_html = True)
    st.write("")

    #Getting the initial image
    col1, col2, col3 = st.columns((1,2.5,1))

    col1,col2 = st.columns((1,1))
    dept_opt = ['Amarillo Research_Lubbock Research','Beaumont Research_Ecology and Conservation biology',
                'Beaumont Research_Lubbock Research', 'Beaumont Research_Stephenvile Research',
                'Biochemistry_Epigenetics',
                'Biochemistry_Medical Physiology',
                'Center for Microencapsule and Drug Delivery_Irma Lerma Rangel College of Pharmacy',
                'Chemical Engineering_Industrial Engineering',
                'Corpus Christi Entomology_Lubbock Entomology',
                'Ecology_Lubbock Research',
                'Epigenetics_Pharmaceuticals',
                'Geography_Ocena Engineering',
                'Marketing_Multiresolution Modelling',
                'Veterinary Physiology_Medical Physiology']
    
    #Geting dept from user
    dept = col1.selectbox("Select department",dept_opt)    
    if dept == 'Amarillo Research_Lubbock Research':
        #Setting the Image
        image = Image.open('Images/rohit img/Amarillo Research_Lubbock Research.png')
    elif dept == 'Beaumont Research_Ecology and Conservation biology':
        #Setting the Image
        image = Image.open('Images/rohit img/Beaumont Research_Ecology and Conservation biology.png')
    elif dept == 'Beaumont Research_Lubbock Research':
        #Setting the Image
        image = Image.open('Images/rohit img/Beaumont Research_Lubbock Research.png')
    elif dept == 'Beaumont Research_Stephenvile Research':
        #Setting the Image
        image = Image.open('Images/rohit img/Beaumont Research_Stephenvile Research.png')
    elif dept == 'Biochemistry_Epigenetics':
        #Setting the Image
        image = Image.open('Images/rohit img/Biochemistry_Epigenetics.png')
    elif dept == 'Center for Microencapsule and Drug Delivery_Irma Lerma Rangel College of Pharmacy':
        #Setting the Image
        image = Image.open('Images/rohit img/Center for Microencapsule and Drug Delivery_Irma Lerma Rangel College of Pharmacy.png')
    elif dept == 'Chemical Engineering_Industrial Engineering':
        #Setting the Image
        image = Image.open('Images/rohit img/Chemical Engineering_Industrial Engineering.png')
    elif dept == 'Corpus Christi Entomology_Lubbock Entomology':
        #Setting the Image
        image = Image.open('Images/rohit img/Corpus Christi Entomology_Lubbock Entomology.png')
    elif dept == 'Ecology_Lubbock Research':
        #Setting the Image
        image = Image.open('Images/rohit img/Ecology_Lubbock Research.png')
    elif dept == 'Geography_Ocena Engineering':
        #Setting the Image
        image = Image.open('Images/rohit img/Geography_Ocena Engineering.png')
    elif dept == 'Marketing_Multiresolution Modelling':
        #Setting the Image
        image = Image.open('Images/rohit img/Marketing_Multiresolution Modelling.png')
    elif dept == 'Veterinary Physiology_Medical Physiology':
        #Setting the Image
        image = Image.open('Images/rohit img/Veterinary Physiology_Medical Physiology.png')
    elif dept == 'Epigenetics_Pharmaceuticals':
        #Setting the Image
        image = Image.open('Images/rohit img/Epigenetics_Pharmaceuticals.png')
    elif dept == 'Biochemistry_Medical Physiology':
        #Setting the Image
        image = Image.open('Images/rohit img/Biochemistry_Medical Physiology.png')
    #Setting the image width
    st.image(image, use_column_width = True)
    
    st.markdown("""
                <p style='text-align: justify;'>
                 A total of 83028 (408C2) comparisons were made and we could see that various 
                 departments were exclusively working on similar subdisciplines. We could thus 
                 make recommendations to these departments to collaborate if they don’t already. 
                 The following plots show the departments that have high potential of 
                 collaboration, the plots also show the subdisciplines in which the departments 
                 should be collaborating. We visually analyze the graphs to analyze which is a 
                 better approach for the subdiscipline representation.
                </p>""",unsafe_allow_html = True)
    st.write("")
    
    
    
    
    
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
               * **LinkedIn:** [linkedin.com/in/swarnabha7/]https://www.linkedin.com/in/swarnabha7/)
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
 'Publication Analysis','Collaboration potential', 'Grant Analysis',
 'Impact score', 'About the Authors'))

# Displaying pages according to the selection -

# Home page -
if navigation_tab == 'Home-Page':
    home_page()

# First page -
elif navigation_tab == 'Publication Analysis':
    publication_analysis()


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
