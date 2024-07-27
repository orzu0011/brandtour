from tour.models import Tour, IncludeExclude, Country, Destination
from post.models import Post
from modeltranslation.translator import TranslationOptions, register

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ['title', 'body']


@register(Tour)
class TourTranslationOptions(TranslationOptions):
    fields = ['title', 'duration', 'overview', 'itinerary']


@register(IncludeExclude)
class IncludeExcludeTranslationOptions(TranslationOptions):
    fields = ['name']


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ['name']


@register(Destination)
class DestinationTranslationOptions(TranslationOptions):
    fields = ['city', 'about']