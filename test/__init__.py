from rdflib import plugin
from rdflib import store

import sys # sop to Hudson
sys.path.insert(0, '/var/lib/tomcat6/webapps/hudson/jobs/rdfextras')

plugin.register(
        'SPARQLStore', store.Store,
        'rdflib_sparqlstore.SPARQLStore', 'SPARQLStore')

