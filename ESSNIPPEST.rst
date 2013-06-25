===============
Elastic Search things we've learned
===============


----------------------------------
Python Modules and the API
----------------------------------

pyelasticsearch appears to be the best python module for interface to
elasticsearch, mostly because it lets you do nearly raw queries. This
is what we should use for any interface layer to our logstash.

By default API calls return 10 results with cursor position 0. If you
search all indexes you may very well only see one listed in the
results because there are probably 10 hits in a single index.

By default there is no sorting in API returned results. Unlike with
SQL there is no natural search order here.

----------------------------------
LogStash Structure
----------------------------------

Elastic Search is a document based model based on Lucene. Logstash's
primary use case is syslog, or other log files that are really
streams, so it creates one document per line (or logical line in the
event of a trace) of log file. While useful in a production
environment, this actually ends up being a little weird for us as
getting back a timeslice is going to require range queries.

----------------------------------
Sample Code / Queries
----------------------------------

The minimalist elastic search code needed is as follows:

.. code:: python

   from pyelasticsearch import ElasticSearch

   ES_URL = "http://logstash.openstack.org/elasticsearch"
   es = ElasticSearch(ES_URL)
   result = es.search(query)

Some useful query containers we've figured out so far

.. code:: python

   all_the_jobs = {
    "query": {
        "query_string": {
            "query": ('@tags:"console.html" AND ( @message:'
                      '"Finished: SUCCESS" OR @message:"Finished: FAILURE" )')
            }
        }
    }

    tempest_failure_line = {
    "query": {
        "match": {
            "@message": {
                "query": "FAILED SKIP failures",
                "operator": "and"
                }
            }
        }
    }
