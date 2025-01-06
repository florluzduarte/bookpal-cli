def get_genres():
    return ["drama", "fiction", "non-fiction", "poetry"]


def get_subgenres(genre):
    subgenres = {
        "drama": ["comedy", "tragedy"],
        "fiction": ["fantasy", "folklore", "historical", "mystery", "realistic fiction", "romance", "science fiction", "thriller", "horror"],
        "non-fiction": ["biography and memoires", "technical", "textbook", "science", "history and politics", "philosophy", "self-help and wellness", "arts and crafts", "business", "spirituality", "humor"],
        "poetry": ["lyric", "narrative", "dramatic"]
    }
    if genre not in subgenres.keys():
        raise KeyError(f"{genre} is invalid. Valid genres are: drama, fiction, non-fiction or poetry")
    return subgenres[genre]