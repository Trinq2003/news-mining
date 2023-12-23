import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from worldcloud import WordCloud, STOPWORDS

# Category visualization
def top_categories_of_news_articles(news_df, top_no:int = 10, chart_type:list = None):
    """
    This function returns the top 10 categories of news articles.
    """
    cat_df = pd.DataFrame(news_df['category'].value_counts()).reset_index()
    cat_df.rename(columns={'index':'news_classes','category':'numcat'}, inplace=True)
    if chart_type is not None:
        if 'bar' in chart_type:
            plt.figure(figsize=(top_no,10))
            ax = sns.barplot(np.array(cat_df.news_classes)[:top_no], np.array(cat_df.numcat)[:top_no])
            for p in ax.patches:
                ax.annotate(p.get_height(), (p.get_x()+0.01, p.get_height() + 50))
            plt.title(f"TOP {top_no} Categories of News articles", size=15)
            plt.xlabel("Categories of articles", size=14)
            plt.xticks(rotation=45)
            plt.ylabel("Number of articles", size=14)
            plt.show()
        if 'pie' in chart_type:
            fig = plt.figure(figsize=(12,12))
            A = plt.pie(cat_df['numcat'][:top_no],
                        labels=cat_df['news_classes'][:top_no],
                        autopct='%1.1f%%',
                        startangle=90,
                        labeldistance=1.08,
                        pctdistance=1.03,
                        rotatelabels=45
                        )

            plt.title(f"Pie Chart of TOP {top_no} categories of news articles", size=20, weight='bold')
            plt.show()

# Wordclouds of categories
def categories_wordclouds_visualization(news_df):


    # create new dataframe of category and length of each news articles in that categories
    ndf = final_df.copy()
    ndf.drop('len_news', inplace=True, axis=1)

    # list of top 10  categories in out dataset
    categories = cat_df['news_classes'][:10].to_list()

    # list of news articles of each top 10 categories list
    articles_list = []

    for i in categories:
        cat_ndf = ndf[ndf['category'] == i]
        cat_array = cat_ndf['length_of_news'].values  # array of news articles text in each category
        articles_list.append(cat_array)
        
    # create a wordcloud instance
    wc1 = WordCloud(max_words=1000, 
                min_font_size=10,
                height=600,
                width=1600,
                background_color='black',
                contour_color='black',
                colormap='plasma',
                repeat=True,
                stopwords=STOPWORDS)

    # plot the figure of 10 wordcloud from out dataset
    plt.figure(figsize=(15,15))

    for idx, j in enumerate(categories):
        plt.subplot(5,2,idx+1)
        cloud = wc1.generate(' '.join(articles_list[idx]))
        plt.imshow(cloud, interpolation= "bilinear")
        plt.title(f"Wordcloud for news topic {j}")
        plt.axis('off')








