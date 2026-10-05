# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
artist_fav= {
    "ArtistName" : "Karan Aujla",
    "CommonColab" : ["Ikky", "Mxrci"]
    "Albums" : {"P-Pop Culture": 2025, "Making Memories": 2025, "Only Love Gets Reply": 2024, "Street Dreams": 2024 }

}
print(artist_fav.keys())
print(artist_fav.values())
# Pretty-print the data structure
pprint(artist_fav)
# Display details of one album recorded by a specific artist
print(artist_fav(Albums))