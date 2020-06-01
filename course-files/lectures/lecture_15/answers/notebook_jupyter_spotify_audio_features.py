
# # ----------------------------------------------------------------
# # Course: EECS 110, Northwestern University
# # Term: Winter 2019
# # Autogenerated from: "../lectures/lecture_15/answers/Jupyter Spotify Audio Features.ipynb"
# # 
# # Note: Each example is commented out. To uncomment, highlight
# # the area you want to uncomment and type "cmd /" (which both adds
# # and removes comments).
# # ----------------------------------------------------------------




# # --------------------------------------------------------------------------------
# # # Spotify: Working with Audio Analysis
# # --------------------------------------------------------------------------------

# # import dependencies:
# from apis import spotify
# from pprint import pprint
# import pandas as pd
# from IPython.display import HTML
# 
# from IPython.core.display import HTML
# 
# # some formatting:
# HTML(spotify.get_jupyter_styling())
# # Let's understand our options by using the help function:
# # help(spotify)



# # --------------------------------------------------------------------------------
# # ## 1. Get tracks by search term
# # --------------------------------------------------------------------------------

# # search_term = input('What song do you want to listen to? ')
# search_term = 'blowin in the wind'
# tracks = spotify.get_tracks(search_term)
# 
# # 1. Uncomment below to see the returned data:
# #    pprint(tracks)
# 
# # 2. pandas doesn't gracefully handle heirarchal data (uncomment below to see what I mean)
# # df = pd.DataFrame(tracks)
# # df.head(3)
# 
# # 3. Format data and display in Pandas:
# tracks = spotify.flatten_for_pandas(tracks)
# df = pd.DataFrame(tracks).set_index('num')
# df[['artist_name', 'name', 'album_name', 'album_image_url']].head(8)



# # --------------------------------------------------------------------------------
# # ## 2. Analyze a track
# # --------------------------------------------------------------------------------

# #track_num = input('What track would you like to listen to (1-10)? ')
# #track_num = int(track_num) - 1
# track_num = 1
# 
# analysis = spotify.get_audio_features_by_track(tracks[track_num]['id'])
# # pprint(analysis)
# for key in analysis:
#     print('{key:>16}: {val}'.format(key=key, val=analysis[key]))



# # --------------------------------------------------------------------------------
# # ## 3. Get similar tracks
# # --------------------------------------------------------------------------------

# # play the whole album:
# track_id = tracks[track_num]['id']
# artist_id = tracks[track_num]['artist_id']
# tracks = spotify.get_similar_tracks(track_ids=[track_id], artist_ids=[artist_id], simplify=True)
# # pprint(tracks, depth=3)
# 
# tracks = spotify.flatten_for_pandas(tracks)
# df = pd.DataFrame(tracks).set_index('num')
# df[['artist_name', 'name', 'album_name', 'album_image_url']].head(8)



# # --------------------------------------------------------------------------------
# # ## 4. Display all album covers
# # --------------------------------------------------------------------------------

# # display all of the album covers:
# html = ''
# for track in tracks[0:8]:
#     html += spotify.get_image_html(track['album_image_url'])
# display(HTML(
#     html
# ))