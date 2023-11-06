from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSiteView(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', "disclaimer", "kcet-cutoff", "college-cutoff", "seat-analyser", "jee-orcr"]

    def location(self, item):
        return reverse(item)