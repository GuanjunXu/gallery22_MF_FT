#!/usr/bin/env python
import unittest,string
import commands
import sys
import time
import libs.datahelper
import gallery22_MF_FT.cases.util

PACKAGE_NAME = 'com.intel.android.gallery3d'
ACTIVITY_NAME = PACKAGE_NAME + '.app.Gallery'

FDFR = "adb shell cat /data/data/com.intel.android.gallery3d/shared_prefs/SocialGallery2.0_Pref.xml | grep fdfr_mode"
PULLUP_CARD_POP_MENU_POINT = (290,950)
class FullViewFRTest(unittest.TestCase):

    def setUp(self):
        super(FullViewFRTest,self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        self.da = libs.datahelper.DataHelper()
        self.util = gallery22_MF_FT.cases.util.Util()
        self.util._clearAllResource()
        self.util._push1Picture()
        self.da.clearup('contacts')
        self.util._clearCache()
        
    def _launchGallery(self):
        """
        method: launchgallery app.
        """
        self.launch(component=self.runComponent)\
        .expect('0_launchgallery_checkpoint.png',interval=2,timeout=4)
    
    def testFaceRecognized(self):
        """
        Summary:Test face recognized
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1. Launch gallery and open a picture has unrecognized face
              2. Tap on the face into contact list
              3. Create a new contact and input name, click done
              4. When into crop picture interface, tap on crop
        """
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchFace()
        #self.touch((235,500))
        self.touch('1_new_contact.png')
        if self.exists('2_OK.png'):
            self.touch('2_OK.png')
        self.input('contact1')

        self.touch('3_DONE.png',waittime=2)
        self.touch('4_CROP.png')

    def testTurnFDFROnOff(self):
        """
        Summary:Test turn on/off FD/FR icon
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1. Launch gallery and open a picture
              2. Turn on/off FD/FR icon
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        
        self._turnOnOffFDFR('false')
        self._turnOnOffFDFR('true')
    
            
    def testChangeIdentityAndRemove(self):
        """
        Summary:Test change identity
        Initial:Make sure there are not less than 1 photo(with face) in gallery
        Steps:1. Launch gallery and open a picture has recognized face
              2. Tap on the face menu icon and select change identity
              3. Select an exist contact
        """
        self.da.insertContact('contact0', '10010', '1')
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
	self._showUpOperations()
        self._touchFace()
        #self.touch((200,507))
        
        if self.exists('1_new_contact',similarity=0.6):
            self.touch('1_new_contact.png')
            if self.exists('2_OK.png'):
                self.touch('2_OK.png')
            self.input('contact01')
            self.touch('3_DONE.png',waittime=3)
            if self.exists('4_CROP.png'):
                self.touch('4_CROP.png',waittime=3)
            self._touchFace()
        self.touch('5_edit_menu_icon.png')
        self.touch('6_change_identity_option.png')
        #self.touch((226,491))
        
        self.touch('7_contact01.png',waittime=2)
        
        
        #remove identity 
        self._touchFace()
        self.touch('5_edit_menu_icon.png')
        
        self.touch('8_remove_identity_option.png')
        self.touch('9_remove_identity_OK.png')
        
        
    def testChangeContactPhoto(self):
        """
        Summary:Test change contact photo
        Initial:Make sure there are not less than 1 photo(with face) in gallery
        Steps:1. Launch gallery and open a picture has recognized face
              2. Tap on the face menu icon and select change contact photo
              3. Click crop
        """
        self.da.insertContact('contact0', '10010', '1')
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #self._turnOnOffFDFR('true')
	self._showUpOperations()
        self._touchFace()
        self.touch('1_new_contact.png')
        if self.exists('3_OK.png'):
            self.touch('3_OK.png')
        self.input('contacttest1')

        self.touch('3_DONE.png',waittime=2)
        self.touch('4_CROP.png')
	time.sleep(3)
	self._touchFace()
        self.touch('5_edit_menu_icon.png',waittime=2)
	self.touch('change_contact_photo.png',waittime=2)
	self.touch('crop.png',waittime=3)
       
        
        #remove identity 
        self._touchFace()
        self.touch('5_edit_menu_icon.png')
        self.touch('7_remove_identity_option.png')
        self.touch('8_remove_identity_OK.png')
        
    def testEditContactInfo(self):
        """
        Summary:Test change contact info
        Initial:Make sure there are not less than 1 photo(with face) in gallery
        Steps:1. Launch gallery and open a picture has recognized face
              2. Tap on the face menu icon and select edit contact info
              3. Change contact name and click done
        """
        self.da.insertContact('contact0', '10010', '1')
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #self._turnOnOffFDFR('true')
	self._showUpOperations()
        self._touchFace()
        #self.touch((226,489))
        if self.exists('1_new_contact'):
            self.touch('2_contact01',waittime=2)
            if self.exists('3_OK.png'):
                self.touch('3_OK.png')
            self._touchFace()
            
        self.touch('5_edit_menu_icon.png')
        self.touch('6_edit_contact_info.png')
        self.touch((265,320),waittime=2)
        
        for i in range(0,5):
            self.touch('7_delete_icon.png')
            
        self.input('abc')
        self.touch('8_DONE.png',waittime=3)
        #remove identity 
        self._touchFace()
        self.touch('5_edit_menu_icon.png')
        self.touch('9_remove_identity_option.png')
        self.touch('10_remove_identity_OK.png')
        
    def testFindOtherPhoto(self):
        """
        Summary:Test find other photo
        Initial:Make sure there are not less than 1 photo(with face) in gallery
        Steps:1. Launch gallery and open a picture has recognized face
              2. Tap on the face menu icon and select find other photo
        """
        self.da.insertContact('contact0', '10010', '1')
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #self._turnOnOffFDFR('true')
	self._showUpOperations()
        self._touchFace()
        #self.touch((300,510))
        if self.exists('1_new_contact'):
            self.touch('2_contact01',waittime=2)
            if self.exists('3_OK.png'):
                self.touch('3_OK.png')
            self._touchFace()
            
        self.touch('5_edit_menu_icon.png')
        self.touch('6_find_other_photo.png')
        self.expect('camera.png')
    
    def _showUpOperations(self):
        commands.getoutput('adb shell input tap 621 550')#self.touch((360,640))
	time.sleep(2)

        #self.touch(PULLUP_CARD_POP_MENU_POINT)
        #self.touch(PULLUP_CARD_POP_MENU_POINT)
        #self.touch(PULLUP_CARD_POP_MENU_POINT)
    
    def _touchFace(self):
        """
        touch face
        """
        commands.getoutput('adb shell input tap 360 640')#self.touch((346,640))
	time.sleep(3)

    def _turnOnOffFDFR(self,status):
        """
        Turn on or turn off FDFR 
        """      
        self._showUpOperations()
        #self.touch('setting.png',waittime=2)
        #self.touch('fdfr.png',waittime=2)
        result1 = commands.getoutput(FDFR)
        if status == 'true':
            self.logger.debug('1111111111111111111111111')
            a1 = result1.find('true')
            if a1 == -1:
                #touch thumbnail
                self.logger.debug('22222222222222222222222222222222')
                self.touch('setting.png',waittime=2)
                self.touch('fdfr.png',waittime=3)
                self.failIf(commands.getoutput(FDFR).find('true') == -1,'failed to turn FDFR on    !!!')
		self._showUpOperations()
		time.sleep(3)

        elif status == 'false':
            self.logger.debug('33333333333333333333333333333333')
            aa1 = result1.find('false')
            if aa1 == -1:
                self.logger.debug('44444444444444444444444444')
                self.touch('setting.png',waittime=2)
                self.touch('fdfr.png',waittime=3)
                self.failIf(commands.getoutput(FDFR).find('false') == -1,'failed to turn FDFR off    !!!')
		self._showUpOperations()
		time.sleep(3)

    
    def _touchIdentityIcon(self):
        self.touch((440,100))


        
    def tearDown(self):
        self.press('back,back,back,back,back')
        super(FullViewFRTest,self).tearDown()
