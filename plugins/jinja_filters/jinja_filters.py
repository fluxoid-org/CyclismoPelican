def by_tag(articles_by_tag, tag):
    """ Filter a list of (tag, articles) to list of articles by tag"""
    for a in articles_by_tag:
        if a[0].slug == tag:
            return a[1]
