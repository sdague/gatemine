#!/usr/bin/python

from pyelasticsearch import ElasticSearch

ES_URL = "http://logstash.openstack.org/elasticsearch"

es = ElasticSearch(ES_URL)

# '{"query": { "match": {"@message": {"query": "FAILED SKIP failures", "operator": "and"}}

tempest_failed_log = {
    "query": {
        "match": {
            "@message": {
                "query": "FAILED SKIP failures",
                "operator": "and"
                }
            }
        }
    }


print es.search(tempest_failed_log)
