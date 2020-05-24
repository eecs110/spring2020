template = '{name:<30}{rating:>10}{review_count:>20}'

print('-' * 60)
print(template.format(name='NAME', rating='RATING', review_count='REVIEW COUNT'))
print('-' * 60)
print(template.format(name='Giordannos Pizza', rating=3.5, review_count=280))
print(template.format(name='Lou Malnati\'s Pizza', rating=3.7, review_count=190))
print('-' * 60)

from apis import yelp
businesses = yelp.get_businesses()
print(businesses)
yelp.print_formatted_businesses_table(businesses)


# from apis import spotify

# # help(spotify)
# artists = spotify.get_artists('Beyonce')
# # print(artists)

# # template = '{name:<30}{id:<25}{genres:<35}'

# # print('-' * 90)
# # print(template.format(name='NAME', id='ID', genres='GENRES'))
# # print('-' * 90)
# # print(template.format(name='Beyoncé', id='6vWDO969PvNqNYHIOW5v0m', genres='dance pop, pop, r&b'))
# # print(template.format(name='Beyonce as Shine', id='3mjguRNN96bC8zvaTwHoqE', genres=''))
# # print('-' * 90)

# recommendations = spotify.get_similar_tracks(artist_ids=['6vWDO969PvNqNYHIOW5v0m'])
# spotify.print_formatted_tracklist_table(recommendations)