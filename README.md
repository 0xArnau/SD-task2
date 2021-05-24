## Task 2: Big Data challenge

#### Requirements:
- python3 -m pip install -U [awscli](https://github.com/aws/aws-cli) --user
- python3 -m pip install -U [ibm-cos-sdk](https://ibm.github.io/ibm-cos-sdk-python/) --user
- python3 -m pip install -U [lithops](https://lithops-cloud.github.io/getting-started/) --user

[This task](https://github.com/a-ppi/SD-task2/blob/master/pdf/hackathon.pdf) is related to the European Research project [CloudButon.eu](http://cloudbuton.eu/). The project is developing novel Cloud technologies aiming to democratize Big Data applications in the Cloud. The CloudButton project has created the lithops.cloud toolkit that will be used to implement the Big Data challenge.

 The challenge consists of developing the entire life cycle of a Big Data application including data acquisition and storage, data preprocessing and indexing, and data queries and visualization.

Students are free to select the topic and data selected for their challenge, but we encourage students to select data in the catalan and/or spanish language.

In groups of 2 or three persons, you will create a distributed system using Cloud technologies with three main functionalities: (i) create a new text dataset extracting information from the Web (Web crawler, Twitter crawler, …) and store it in Cloud Object Storage, and (ïi) preprocess the text dataset to build structured data (csv) that can be queried and analyzed later on. And (iii) create Python notebooks to demonstrate date related queries, basic visualization, and sentiment analysis techniques over the data.

To build the system, you will leverage the Lithops.cloud toolkit developed in CloudButton. This toolkit enables to launch processes in the Cloud over Cloud Functions, and to store data in Cloud Object Storage. We will provide training and examples of how to use this toolkit.

Stage 1: Data crawler. Massively parallel functions crawling data and storing it in Cloud Object Storage. Obtain information from web pages or tweets and create a dataset of text data. Use FaaS backend in lithops to launch crawling process over serverless functions.

Stage 2: Data preprocessing stage to produce structured data in csv format also stored in Cloud Object Storage. As columns in the csv file we suggest date, geographic location, url, and sentiment analysis.

This stage should ensure the consistency of data accessed and updated to csv files.  Note that Object Storage does not provide consistent modification of objects in buckets. You need an addressable, consistent, and fault-tolerant stateful entity to access the structured data for modification, or query purposes.

Propose a distributed architecture guaranteeing scaling transparency, location transparency, failure transparency, and concurrency transparency.

Stage 3: Python notebook: Demonstrate simple queries in Python notebooks over your data. In particular, apply sentiment analysis to data in different dates and periods and generate simple plots. Enable search queries over the data.

**Example projects:**

Students can propose their own ideas for data acquisition and analysis, but they should align with Open Data inititiatives like [Open Data Lab](http://iniciativabarcelonaopendata.cat/es/open-data-lab/) (http://iniciativabarcelonaopendata.cat/es/open-data-lab/) and [Tarragona Open Data Lab](http://opendatalabtgn.cat/ca/el-projecte/) (http://opendatalabtgn.cat/ca/el-projecte/). These inciatives are these days interested in datasets helping to understand the social and economic impact of the COVID pandemic in Tarragona/Catalonia.**
**

Some potential ideas could be:

\1.    Crawl text from social networks in Spain/Catalonia with the goal of analyzing sentiment analysis during the past three years to understand the impact of the COVID pandemic.

\2.    Crawl text from news web sites from Spain with the goal of analyzing sentiment analysis during the past three years to understand the impact of the COVID pandemic.

\3.    Crawl text in the Catalan language from web sites and social networks to create a big Catalan dataset. Create a sample search engine for Catalan content.

\4. Crawl comments from touristic locations in Catalonia (airbnb, hotels) to analyze the impact of the pandemic in the following months as the pandemic improves.

\5.    Create a Tarragona/Catalonia dataset with text content from web sites and twitter. Create a sample search engine for content related to Tarragona or Catalonia. Enable geographical and time-based queries over data.

 

You can also include in your challenge available open data sets with different data formats.

https://analisi.transparenciacatalunya.cat/ca/

https://seu-e.cat/ca/web/tarragona/dades-obertes

https://opendata.reus.cat/

https://lionbridge.ai/datasets/22-best-spanish-language-datasets-for-machine-learning/

https://www.cs.upc.edu/~nlp/wikicorpus/

 

The professors will provide training in Lithops, Cloud technologies, sentiment analysis, python plotting, and geospatial map generation.

Hackathon: In June, as final evaluation of this course, we will organize a two days hackathon sponsored by IBM and RedHat to present your solutions. The committee will include IBM and RedHat engineers, and several prizes for the three top solutions.

The code and data of selected projects will be hosted by the CloudLab group in a public OpenHub repository.

**Final requirements**

All groups must prepare a github repository with enough documentation to reproduce the experiments.

You must provide a 5 minutes video with a presentation of your solution. To pass the distributed system course, the video can be produced in catalan, spanish, or english.

Nevertheless, only videos in english will be considered by the CloudButton committee and may receive a prize.

- Deadline to deliver the task: June 12th
- Evaluation and interviews: June 14-18
- Final score: June 18
