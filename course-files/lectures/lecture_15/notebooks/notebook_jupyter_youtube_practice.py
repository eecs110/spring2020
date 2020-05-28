
# # ----------------------------------------------------------------
# # Course: EECS 110, Northwestern University
# # Term: Winter 2019
# # Autogenerated from: "../lectures/lecture_15/notebooks/Jupyter YouTube Practice.ipynb"
# # 
# # Note: Each example is commented out. To uncomment, highlight
# # the area you want to uncomment and type "cmd /" (which both adds
# # and removes comments).
# # ----------------------------------------------------------------




# # --------------------------------------------------------------------------------
# # # Exercise 1: In Class Activity
# # 1. Figure out how to query for a video
# # 2. Figure out how to display a list of videos using Pandas (hint: use one of the utilties functions)
# # 3. Figure out how to embed the first video returned from your search results in the notebook

# # --------------------------------------------------------------------------------

# from apis import youtube
# from apis import utilities
# from pprint import pprint
# from IPython.core.display import HTML
# 
# # some formatting:
# HTML(utilities.get_jupyter_styling())
# help(youtube)
# help(utilities)
# # Just a little syntax help...
# # video_player = youtube.get_video_player_html('https://www.youtube.com/embed/4sEV1lMn64k')
# # display(HTML(video_player))
