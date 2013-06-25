#!/usr/bin/python

from pyelasticsearch import ElasticSearch

ES_URL = "http://logstash.openstack.org/elasticsearch"

es = ElasticSearch(ES_URL)

# '{"query": { "match": {"@message": {"query": "FAILED SKIP failures", "operator": "and"}}

tempest_failed_jobs = {
    "query": {
        "query_string": {
            "query": ('@tags:"console.html" AND ( @message:'
                      '"Finished: SUCCESS" OR @message:"Finished: FAILURE" )')
            }
        }
    }

    #     "match": {
    #         "@fields.build_status": {
    #             "query": "FAILURE"
    #             },
    #         "@message": "Finished: FAILURE"{
    #             "query": "Finished: FAILURE",
    #             }
    #         }
    #     }
    # }


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
