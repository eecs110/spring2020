
# # ----------------------------------------------------------------
# # Course: EECS 110, Northwestern University
# # Term: Winter 2019
# # Autogenerated from: "../lectures/lecture_15/answers/Jupyter Yelp Practice.ipynb"
# # 
# # Note: Each example is commented out. To uncomment, highlight
# # the area you want to uncomment and type "cmd /" (which both adds
# # and removes comments).
# # ----------------------------------------------------------------

# from apis import yelp
# from apis import utilities
# from pprint import pprint
# help(yelp)
# help(utilities)
# businesses = yelp.get_businesses('Evanston, IL')
# pprint(businesses)
# df = utilities.get_dataframe(businesses)
# df
# df[['name', 'categories', 'display_address']]
# reviews = yelp.get_reviews(businesses[0]['id'])
# reviews
# df = utilities.get_dataframe(reviews)
# df