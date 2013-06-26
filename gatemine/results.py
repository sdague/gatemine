# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


DEFAULT_PAGE_SIZE = 100


class ESQuery(object):
    """An encapsulation of an elastic search query"""
    query = ""
    pagesize = DEFAULT_PAGE_SIZE
    page = 0

    def __init__(self, query, size=DEFAULT_PAGE_SIZE):
        self.query = query
        self.pagesize = size


class ResultSet(object):
    """A container for results"""
    results = []
    pagesize = DEFAULT_PAGE_SIZE
    page = 0
    took = 0
    timed_out = False
    size = 0

    def __init__(self, data):
        self.results = []
        self._parse(data)

    def _parse(self, data):
        self.took = data['took']
        self.timed_out = data['timed_out']
        self.size = data['hits']['total']
        for r in data['hits']['hits']:
            self.results.append(Result(r))

    def next(self, pagesize=None):
        """Eventually used to load the next page of results"""
        pass

    def __iter__(self):
        return iter(self.results)


class Result(object):
    """A single log stash result"""

    def __init__(self, data):
        self._data = data

    def __str__(self):
        return str(self._data)
