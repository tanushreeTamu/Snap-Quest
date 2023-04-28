import Img_TFIDF
import nltk
import math
#nltk.download('all')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

#pre-processing for query
def pre_process_query(query):
    processed_query = []
    for data in query.split():
        low_val = data.lower()
        lemm_query = WordNetLemmatizer().lemmatize(low_val)
        processed_query.append(lemm_query)
    return processed_query

def calc_Denom1_img(tfIdf):
    val=0
    denominator_doc = 0
    for term,value in tfIdf.items():
        val += math.pow(value, 2)
        denominator_doc = math.sqrt(val)
    return denominator_doc

# cosine similarity b/w query and image
def queryImg_cosine(img_TFIDF,query):
    denom2_query = math.sqrt(len(query))
    query_img_score={}
    for doc, tfIdf in img_TFIDF.items():
        denom1_doc = calc_Denom1_img(tfIdf)
        score = 0
        score_final = 0
        for term in query:
            if term in tfIdf:
                score += (tfIdf[term])
        score_final= (score)/ (denom2_query * denom1_doc)
        query_img_score[doc] = score_final
    sorted_query_img_score = dict(sorted(query_img_score.items(), key=lambda item: item[1], reverse = True))
    return sorted_query_img_score

def print_top10_results(results):
    count =1
    for score,image in results.items():
        print(count,"\t",score, "\t", image)
        count+=1
        if(count >=11):
            break

#adding test function here for github push
def Image_list(image_doc_with_score):
    img_list = []
    for key,val in image_doc_with_score.items():
        if val != 0:
            img_list.append(key)
    return img_list

def Image_search(query):
    query_processed = pre_process_query(query)
    img_query_cosine_simil = queryImg_cosine(Img_TFIDF.img_desc_TFIDF, query_processed)
    print_top10_results(img_query_cosine_simil)

'''

if __name__ == "__main__":
    query = "water body"
    query_processed = pre_process_query(query)
    img_query_cosine_simil = queryImg_cosine(Img_TFIDF.img_desc_TFIDF, query_processed)
    print_top10_results(img_query_cosine_simil)

'''