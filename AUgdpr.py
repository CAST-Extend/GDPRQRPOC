'''
Created on sep 5, 2018

@author: NNA
'''

import cast.analysers.jee
import cast.application
import cast.analysers.log as LOG





class sactivator(cast.analysers.jee.Extension):
    def __init__(self):
        self.fielPath = ""
        
               
    def start_analysis(self,options):
        LOG.info('Successfully GDPR analyzer Started')
       
           
    
    def end_analysis(self):
        LOG.info("Java GDPR  Analyzer  Ended")
        
   