from yelpapi import YelpAPI
import pandas as pd

api_key ='t1UBjaDqxUy0NtNRU8QEKgCz2cqCSgB0p8pnYPKfSYSzgZIlcOT_0ii0GJVLASlbwzkcdqFsPVlIkpQdNCMgoT__Kz0nXaxtupK8l6gtaqA_zfbfQBxOiJ3o-NA0ZHYx'

yelp_api = YelpAPI(api_key)

#search_query
search_term = "Burgers"
search_location ="El paso, Tx"
search_sort_by = "rating" # best_match, rating, review_count, distance
search_limit = 50

search_results = yelp_api.search_query(term = search_term, location = search_location,sorting = search_sort_by, limit = search_limit)


#['id', 'alias', 'name', 'image_url', 'is_closed', 'url', 'review_count', 'categories', 'rating', 'coordinates', 'transactions', 'price', 'location', 'phone', 'display_phone', 'distance']

results_df = pd.DataFrame.from_dict(search_results['businesses'])
print(results_df)

results_df.to_csv('yelp_API_burgers.csv')

while True:
    id_for_reviews = input("Enter the business ID to retrieve reviews (or type 'exit' to quit): ")
    
    if id_for_reviews.lower() == 'exit':
        break
    
    review_results = yelp_api.reviews_query(id=id_for_reviews)
    review_df = pd.DataFrame.from_dict(review_results['reviews'])

    filename = 'reviews_' + id_for_reviews + '.txt'

    with open(filename, 'w') as f:
        f.write('\n\n'.join(review_df['text'].tolist()))
