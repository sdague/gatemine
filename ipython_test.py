from pyelasticsearch import ElasticSearch
from gatemine import results

ES_URL = "http://logstash.openstack.org/elasticsearch"

es = ElasticSearch(ES_URL)

tempest_failed_jobs = {
    "query": {
        "query_string": {
            "query": ('@tags:"console.html" AND ( @message:'
                      '"Finished: SUCCESS" OR @message:"Finished: FAILURE" )')
            }
        }
    }

a = es.search(tempest_failed_jobs)
