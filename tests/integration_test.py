import unittest
from cast.application.test import run
from cast.application import create_postgres_engine
import logging

logging.root.setLevel(logging.DEBUG)

class TestIntegration(unittest.TestCase):

    def test1(self):
        
         #run(kb_name='jslink_local', application_name='gdp', engine=create_postgres_engine())
         run(kb_name='jeegdpr_local', application_name='jeegdp', engine=create_postgres_engine())
        
         
if __name__ == "__main__":
    unittest.main()
