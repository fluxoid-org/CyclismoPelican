from pelican import signals
from . import jinja_filters

def add_filter(pelican):
    pelican.env.filters.update({'by_tag': jinja_filters.by_tag})

def register():
    signals.generator_init.connect(add_filter)
