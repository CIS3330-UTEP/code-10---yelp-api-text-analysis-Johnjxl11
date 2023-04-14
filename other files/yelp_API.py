from yelpapi import YelpAPI
import pandas as pd

api_key ='t1UBjaDqxUy0NtNRU8QEKgCz2cqCSgB0p8pnYPKfSYSzgZIlcOT_0ii0GJVLASlbwzkcdqFsPVlIkpQdNCMgoT__Kz0nXaxtupK8l6gtaqA_zfbfQBxOiJ3o-NA0ZHYx'

yelp_api = YelpAPI(api_key)

#search_query
search_term = "pizza"
search_location ="Chicago, IL"
search_sort_by = "rating" # best_match, rating, review_count, distance
search_limit = 20

search_results = yelp_api.search_query(term = search_term, location = search_location,sorting = search_sort_by, limit = search_limit)

print (search_results)

for business in search_results ['businesses']:
    print(business["name"])
    print(business['alias'])
    print("\n")


results_df = pd.DataFrame.from_dict(search_results['businesses'])
print(results_df)
#results_df.to_csv('yelp_API.csv')
id_for_reviews = "montis-chicago"

#review_query
review_results =yelp_api.reviews_query(id= id_for_reviews)
print (review_results)

#for review in review_results['reviews']:
   # print(review)
    #print("\n\n")
review_df = pd.DataFrame.from_dict(review_results['reviews'])
print(review_df['text'])
review_df.to_csv(f"{id_for_reviews}_reviews_for_yelp_API")



