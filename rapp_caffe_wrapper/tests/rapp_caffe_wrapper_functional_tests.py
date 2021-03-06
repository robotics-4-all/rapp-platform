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

# Author: Athanassios Kintsakis
# contact: akintsakis@issel.ee.auth.gr

PKG='test_rapp_mysql_wrapper'
import sys
import unittest
import rospy
from os.path import expanduser

from rapp_platform_ros_communications.srv import (
  imageClassificationSrv,
  imageClassificationSrvRequest,
  imageClassificationSrvResponse,
  ontologyClassBridgeSrv,
  ontologyClassBridgeSrvRequest,
  ontologyClassBridgeSrvResponse  
  )


## @class TestCaffeWrapper 
# Inherits the unittest.TestCase class in order to offer functional tests functionality 
class TestCaffeWrapper(unittest.TestCase):

  def test_image_classification_valid(self):
    ros_service = rospy.get_param(\
            "rapp_caffe_wrapper_image_classification")
    rospy.wait_for_service(ros_service)
    
    test_service = rospy.ServiceProxy(\
            ros_service, imageClassificationSrv)

    req = imageClassificationSrvRequest()
    req.objectFileUrl= expanduser("~")+"/rapp_platform_files/image_processing/example_images/toilet.jpg"
    req.registerToOntology=False
    response = test_service(req)     
    self.assertEqual(response.success, True) 
    self.assertEqual(response.objectClass, "toilet seat") 

  def test_caffe_ontology_class_bridge_valid(self):
    ros_service = rospy.get_param(\
            "rapp_caffe_wrapper_get_ontology_class_equivalent")
    rospy.wait_for_service(ros_service)
    
    test_service = rospy.ServiceProxy(\
            ros_service, ontologyClassBridgeSrv)

    req = ontologyClassBridgeSrvRequest()
    req.caffeClass = "refrigerator, icebox"
    response = test_service(req)     
    self.assertEqual(response.success, True) 
    self.assertEqual(response.ontologyClass, "Refrigerator")     

  def test_image_classification_with_registration(self):
    ros_service = rospy.get_param(\
            "rapp_caffe_wrapper_image_classification")
    rospy.wait_for_service(ros_service)
    
    test_service = rospy.ServiceProxy(\
            ros_service, imageClassificationSrv)

    req = imageClassificationSrvRequest()
    req.objectFileUrl= expanduser("~")+"/rapp_platform_files/image_processing/example_images/refrigerator.jpg"
    req.registerToOntology=True
    req.username="rapp"
    response = test_service(req)     
    self.assertEqual(response.error, "")
    self.assertEqual(response.success, True) 
    self.assertEqual(response.objectClass, "refrigerator, icebox")    
    self.assertTrue("Refrigerator" in response.ontologyNameOfImage) 
    
## The main function. Initializes the Rapp caffe wrapper functional tests
if __name__ == '__main__':
  import rosunit
  rosunit.unitrun(PKG, 'TestCaffeWrapper', TestCaffeWrapper)
