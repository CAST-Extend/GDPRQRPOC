'''
Created on sep 5, 2018

@author: NNA
'''

from cast.application import ApplicationLevelExtension, ReferenceFinder,create_link
import logging
import csv                 # @UnusedImport
import os, re
from docutils.nodes import row
import cast.analysers
from cast.analysers import Bookmark

class ExtensionApplication(ApplicationLevelExtension):

    def end_application(self, application):
        logging.info("GDPR Running code at the end of an Application")
        application.declare_property_ownership('GDPRViolation_CustomMetrics.GDPRJAVAViolation',['JV_FILE'])
        str_FindList =[]
        filename = self.find_csv_fullpath(application)
        #logging.info("Filename-->  " + str(filename))
        with self.my_open_source_file(filename) as csvfile: 
            index = filename.rfind('\\')
            self.name = filename[index+1:]
            mydictreader = csv.reader(csvfile)       # wo fieldnames : line #1 i used to get the column names
            for row in mydictreader:
                if row[0] not in str_FindList:
                    str_FindList.append(row[0])
                    
        files = application.get_files(['JV_FILE'])
        rfCall = ReferenceFinder()
        for strval in str_FindList:
            rfCall.add_pattern(strval, before="", element= strval , after="")
            
            
        #references = []
        gjvf = list(application.search_objects(category='JV_FILE', load_properties= True))
        #logging.info("file JVF from search--" + str(gjvf))
        #jvFile_list = list(application.search_objects(category='JV_FILE', load_properties= True))
        #print("Lenght of jvlist %s" + str(gjvf))
        for fle in files:
            #logging.info("file value--" + str(fle.name))
            if (fle.get_path().endswith('.java')):
                
                references = [reference for reference in rfCall.find_references_in_file(fle)]  
                
                for reference in references:
                    sfpath=fle.name
                    #print("file path%s" + str(sfpath))
                    jvf=filter(lambda x: (x.name == sfpath), gjvf)
                    #print("Lenght of jvlist %s" + str(jvf))
                    try:
                        if jvf !=None:
                            for j in jvf:
                                #print("Lenght of jvlist---" + str(j.name))
                                print("references.bookmark---" + str(reference.bookmark))
                                #j.save_violation('GDPR_CustomMetrics.GDPR_violation', reference.bookmark)
                                j.save_violation('GDPRViolation_CustomMetrics.GDPRJAVAViolation', reference.bookmark)
                                logging.info("Violation saved for file --" + str(j.name))
                                break
                    except Exception as e:
                        print("Error in violation---" +  str(e) + '------' + str(j.name)) 
                   
        
        
    def find_csv_fullpath(self,application):
        # TODO : find the file *.csv (or or *.cvm.csv) in CVM_CSV package folder 
        _filename = None
        _filename = 'C:\Oxygenworkspacegdprjava\com.castsoftware.labs.javagdpr\Inbox.csv'
        logging.info("CSV file found!!!")
        
        return _filename
 
       
            
    
    def my_open_source_file(self,path):     # copied from C:\ProgramData\CAST\CAST\Extensions\com.castsoftware.sqlscript.1.2.0-alpha1\analyser.py
        """
        Uses chardet to autodetect encoding and open the file in the correct encoding.
        """
        from chardet.universaldetector import UniversalDetector
        #logging.info("Path-->" + str(path))
        
        detector = UniversalDetector()
        with open(path, 'rb') as f:
            for line in f:
                #logging.info("Line No" + str(line))
                detector.feed(line)
                if detector.done: break
        detector.close()
        
        result = open(path, 'r', encoding=detector.result['encoding'])
        #print (encoding=detector.result['encoding'])
        return result