import unittest

from kidash import ElasticSearch

def test_elasticsearch_version(self):
        version = '6.6.1'
        TEST_ES_VER = 6
        TEST_ES_VER_MID = 6
        ES_VER, ES_VER_MID = kidash.find_elasticsearch_version("./data/elastic.json")

        self.assertEqual(TEST_ES_VER, ES_VER)
        self.assertEqual(TEST_ES_VER_MID, ES_VER_MID)