#!/usr/bin/env python

#Copyright 2015 RAPP

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

    #http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.


PKG='rapp_cognitive_exercise'

import sys
import unittest
import rospy
import roslib

from rapp_platform_ros_communications.srv import (
  recordUserCognitiveTestPerformanceSrv,
  recordUserCognitiveTestPerformanceSrvRequest,
  recordUserCognitiveTestPerformanceSrvResponse,
  testSelectorSrv,
  testSelectorSrvRequest,
  testSelectorSrvResponse,
  cognitiveTestCreatorSrv,
  cognitiveTestCreatorSrvRequest,
  cognitiveTestCreatorSrvResponse,
  userScoresForAllCategoriesSrv,
  userScoresForAllCategoriesSrvRequest,
  userScoresForAllCategoriesSrvResponse,
  userScoreHistoryForAllCategoriesSrv,
  userScoreHistoryForAllCategoriesSrvRequest,
  userScoreHistoryForAllCategoriesSrvResponse,
  createNewPlatformUserSrv,
  createNewPlatformUserSrvResponse,
  createNewPlatformUserSrvRequest,
  removePlatformUserSrv,
  removePlatformUserSrvRequest,
  removePlatformUserSrvResponse,
  retractUserOntologyAliasSrv,
  retractUserOntologyAliasSrvRequest,
  retractUserOntologyAliasSrvResponse,
  getUserOntologyAliasSrv,
  getUserOntologyAliasSrvRequest,
  getUserOntologyAliasSrvResponse,
  returnTestsOfTypeSubtypeDifficultySrv,
  returnTestsOfTypeSubtypeDifficultySrvResponse,
  returnTestsOfTypeSubtypeDifficultySrvRequest
  )

## @class CognitiveExerciseFunc 
# Inherits the unittest.TestCase class in order to offer functional tests functionality 
class CognitiveExerciseFunc(unittest.TestCase):

    ## Tests the cognitive exercise test chooser service when selection parameters are provided
    def test_chooser_parameters_provided(self):
        ros_service = rospy.get_param(\
                "rapp_cognitive_exercise_chooser_topic")
        rospy.wait_for_service(ros_service)
        
        test_service = rospy.ServiceProxy(\
                ros_service, testSelectorSrv)

        req = testSelectorSrvRequest()
        req.username="rapp"        
        req.testType="ArithmeticCts"
        req.testSubType="BasicArithmeticCts"
        req.testDifficulty="1"
        req.testIndex="1" 
        response = test_service(req)     
        self.assertEqual(response.success, True) 
        self.assertEqual(len(response.questions)>=1, True) 
        self.assertEqual(response.test,"ArithmeticCts_bneXbLGX")

    ## Tests the cognitive exercise test chooser service with only testType parameter
    def test_chooser_basic(self):
        ros_service = rospy.get_param(\
                "rapp_cognitive_exercise_chooser_topic")
        rospy.wait_for_service(ros_service)
        
        test_service = rospy.ServiceProxy(\
                ros_service, testSelectorSrv)

        req = testSelectorSrvRequest()
        req.username="rapp"        
        req.testType="ArithmeticCts"
        response = test_service(req)     
        self.assertEqual(response.success, True) 
        self.assertEqual(len(response.questions)>=1, True)     
    
    ## Tests the cognitive exercise test chooser service with testType and testSubType parameters    
    def test_chooser_subtype(self):
        ros_service = rospy.get_param(\
                "rapp_cognitive_exercise_chooser_topic")
        rospy.wait_for_service(ros_service)
        
        test_service = rospy.ServiceProxy(\
                ros_service, testSelectorSrv)

        req = testSelectorSrvRequest()
        req.username="rapp"        
        req.testType="ArithmeticCts"
        req.testSubType="BasicArithmeticCts"
        response = test_service(req)     
        self.assertEqual(response.success, True) 
        self.assertEqual(len(response.questions)>=1, True) 
        self.assertEqual(response.testSubType, "BasicArithmeticCts")
        
    ## Tests the cognitive exercise test chooser service when test type is not provided  
    def test_chooser_no_type(self):
        ros_service = rospy.get_param(\
                "rapp_cognitive_exercise_chooser_topic")
        rospy.wait_for_service(ros_service)
        
        test_service = rospy.ServiceProxy(\
                ros_service, testSelectorSrv)
    
        req = testSelectorSrvRequest()
        req.username="rapp"       
        req.testType=""
        response = test_service(req)     
        self.assertEqual(response.success, True)    
              
    ## Tests the record user cognitive exercise test performance service  
    def test_record_user_performance_basic(self):
        ros_service = rospy.get_param(\
                "rapp_cognitive_exercise_record_user_cognitive_test_performance_topic")
        rospy.wait_for_service(ros_service)
        
        test_service = rospy.ServiceProxy(\
                ros_service, recordUserCognitiveTestPerformanceSrv)

        req = recordUserCognitiveTestPerformanceSrvRequest()
        req.username="rapp"       
        req.test="ArithmeticCts_bneXbLGX"
        req.score=10
        response = test_service(req)     
        self.assertEqual(response.success, True)  
        
    ## Tests the cognitive exercise test creation service when invalid path is used
    def test_cognitive_test_creat_of_invalid_path(self):
        ros_service = rospy.get_param(\
                "rapp_cognitive_test_creator_topic")
        rospy.wait_for_service(ros_service)
        
        test_service = rospy.ServiceProxy(\
                ros_service, cognitiveTestCreatorSrv)

        req = cognitiveTestCreatorSrvRequest()
        req.inputFile="someInvalidPath"
        response = test_service(req)     
        self.assertEqual(response.success, False)  
        self.assertEqual(response.error, "Test description file does not exist")
        
    ## Tests the cognitive exercise return user scores service for valid input
    def test_user_scores_for_all_categories_valid_input(self):
        ros_service = rospy.get_param(\
                "rapp_cognitive_exercise_user_all_categories_score_topic")
        rospy.wait_for_service(ros_service)
        
        test_service = rospy.ServiceProxy(\
                ros_service, userScoresForAllCategoriesSrv)

        req = userScoresForAllCategoriesSrvRequest()
        req.username="rapp"
        req.upToTime=10000000000000
        response = test_service(req)     
        self.assertEqual(response.success, True)          
        self.assertEqual("ArithmeticCts" and "ReasoningCts" and "AwarenessCts" in response.testCategories, True)
        self.assertEqual(len(response.testScores)>=0, True)

    ## Tests the cognitive exercise return user history service for valid input
    def test_user_score_history_for_all_categories_valid_input_basic(self):
        ros_service = rospy.get_param(\
                "rapp_cognitive_exercise_user_all_categories_history_topic")
        rospy.wait_for_service(ros_service)
        
        test_service = rospy.ServiceProxy(\
                ros_service, userScoreHistoryForAllCategoriesSrv)

        req = userScoreHistoryForAllCategoriesSrvRequest()
        req.username="rapp"
        req.toTime=0
        req.fromTime=0
        response = test_service(req)     
        self.assertEqual(response.success, True)          
        self.assertEqual(len(response.recordsPerTestType)>0,True)

    ## Tests the cognitive exercise return tests of type for various parameter selection combinations
    def test_return_tests_of_type_subtype_difficulty_combinations(self):
        ros_service = rospy.get_param(\
                "rapp_cognitive_exercise_return_tests_of_type_subtype_difficulty_topic")
        rospy.wait_for_service(ros_service)
        
        test_service = rospy.ServiceProxy(\
                ros_service, returnTestsOfTypeSubtypeDifficultySrv)
        req = returnTestsOfTypeSubtypeDifficultySrvRequest()
        
        req.testType="ArithmeticCts"
        req.testSubType="BasicArithmeticCts"
        req.difficulty="1"
        req.language="el"
        response = test_service(req)     
        self.assertEqual(response.success, True)  
        self.assertTrue(response.totalNumberOfTestsReturned>1)    
        self.assertEqual(len(response.cognitiveExercises),response.totalNumberOfTestsReturned)   

        req.testType="ArithmeticCts"
        req.testSubType="BasicArithmeticCts"
        req.difficulty="1"
        req.language=""
        response = test_service(req)     
        self.assertEqual(response.success, True)  
        self.assertTrue(response.totalNumberOfTestsReturned>1)    
        self.assertEqual(len(response.cognitiveExercises),response.totalNumberOfTestsReturned) 

        req.testType="ArithmeticCts"
        req.testSubType="BasicArithmeticCts"
        req.difficulty=""
        req.language=""
        response = test_service(req)     
        self.assertEqual(response.success, True)  
        self.assertTrue(response.totalNumberOfTestsReturned>1)    
        self.assertEqual(len(response.cognitiveExercises),response.totalNumberOfTestsReturned) 
        
        req.testType="ArithmeticCts"
        req.testSubType=""
        req.difficulty=""
        req.language=""
        response = test_service(req)     
        self.assertEqual(response.success, True)  
        self.assertTrue(response.totalNumberOfTestsReturned>1)    
        self.assertEqual(len(response.cognitiveExercises),response.totalNumberOfTestsReturned) 
        
    ## Tests the creation of a new platform user and selection of a cognitive test and cleans up afterwards
    def test_create_new_platform_user_and_request_cognitive_test_then_cleanup(self):
        #create user
        ros_service = rospy.get_param("rapp_mysql_wrapper_create_new_platform_user_service_topic")
        rospy.wait_for_service(ros_service)    
        test_service = rospy.ServiceProxy(ros_service, createNewPlatformUserSrv)
        req = createNewPlatformUserSrvRequest()
        req.username="temp_to_delete"
        req.password="temp_to_delete"
        req.language="el"
        req.creator_username="rapp"              
        response = test_service(req)     
        self.assertTrue(response.success) 
        
        #request test
        ros_service = rospy.get_param("rapp_cognitive_exercise_chooser_topic")
        rospy.wait_for_service(ros_service)
        
        test_service = rospy.ServiceProxy(\
                ros_service, testSelectorSrv)

        req = testSelectorSrvRequest()
        req.username="temp_to_delete"        
        req.testType="ArithmeticCts"
        response = test_service(req)     
        self.assertEqual(response.success, True)     
        self.assertEqual(len(response.questions)>=1, True)   
        
        #get user's ontology alias
        ros_service = rospy.get_param("rapp_mysql_wrapper_get_user_ontology_alias_service_topic")
        rospy.wait_for_service(ros_service)
        
        test_service = rospy.ServiceProxy(\
                ros_service, getUserOntologyAliasSrv)

        req = getUserOntologyAliasSrvRequest()
        req.username="temp_to_delete"
        response = test_service(req)     
        self.assertEqual(response.success, True)  
        ontology_alias=response.ontology_alias
        
        #retract user's ontology alias
        ros_service = rospy.get_param("rapp_knowrob_wrapper_retract_user_ontology_alias")
        rospy.wait_for_service(ros_service)
        
        test_service = rospy.ServiceProxy(\
                ros_service, retractUserOntologyAliasSrv)

        req = retractUserOntologyAliasSrvRequest()
        req.ontology_alias=ontology_alias
        response = test_service(req)     
        self.assertEqual(response.success, True) 
        
        #remove user        
        ros_service = rospy.get_param("rapp_mysql_wrapper_remove_platform_user_service_topic")
        rospy.wait_for_service(ros_service)    
        test_service = rospy.ServiceProxy(ros_service, removePlatformUserSrv)
        req = removePlatformUserSrvRequest()
        req.username="temp_to_delete"             
        response = test_service(req)     
        self.assertTrue(response.success) 
        
        
        
## The main function. Initializes the Cognitive Exercise System functional tests
if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(PKG, 'CognitiveExerciseFunc', CognitiveExerciseFunc)














