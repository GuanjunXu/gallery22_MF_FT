#!/usr/bin/env python
import unittest,string
import gallery22_MF_FT.cases.util
import time

PACKAGE_NAME = 'com.intel.android.gallery3d'
ACTIVITY_NAME = PACKAGE_NAME + '.app.Gallery'

#SETTING_BAR = (500,1100)
PULLUP_CARD_POP_MENU_POINT = (290,96)
SETTING_BAR = (363,1045)
EVENT = (400,700)
VENUE = (400,760)

class FullViewMenuTest(unittest.TestCase):

    def setUp(self):
        super(FullViewMenuTest,self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        self.util = gallery22_RHB_FT.cases.util.Util()
        self.util._confirmResourceExists()
        
    def _launchGallery(self):
        """
        method: launchgallery app.
        """
        self.launch(component=self.runComponent)
        self.expect('0_launchgallery_checkpoint.png',interval=2,timeout=4)

    def testRotateLeft(self):
        """
        Summary:Rotate left in setting menu
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch Rotate left
              4.Repeat 2-3 steps 4 times
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        
        #Step 3-4
        for i in range (1,4):
            self.press('menu')
            self.touch('1_rotate_left.png')

    def testRotateRight(self):
        """
        Summary:Rotate left in setting menu
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch Rotate right
              4.Repeat 2-3 steps 4 times
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        
        #Step 3-4
        for i in range (1,4):
            self.press('menu')
            self.touch('1_rotate_right.png')

    def testCropPicture(self):
        """
         Summary:Crop the photo
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Click crop 
              4.Click crop
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self.press('menu')
        self.touch('1_crop.png')
        
        beforePicNo = self.util._getPictureNumber()
        self.touch('2_CROP_OK.png')
        
        afterPicNo = self.util._getPictureNumber()
	time.sleep(2)
        self.failIf(string.atoi(beforePicNo) != string.atoi(afterPicNo)-1,'Crop single in fullview failed!!!')  

    def testCropCancel(self):
        """
         Summary:Crop the photo
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Click crop 
              4.Click crop
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self.press('menu')
        self.touch('1_crop.png')
        
        beforePicNo = self.util._getPictureNumber()
        self.touch('2_CROP_CANCEL.png')
        
        afterPicNo = self.util._getPictureNumber()
        self.failIf(beforePicNo != afterPicNo,'CANCEL Crop single in fullview failed!!!')     

    def testSetPicAsContact(self):
        """
        Summary:Set picture as contact photo
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Click Set picture as 
              4.Click Contact photo
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self.press('menu')
        self.touch('1_set_pic_as.png')
        self.expect('2_set_as_dialog.png')
        self.touch('3_contact_icon.png')
        self.expect('4_contact_screen.png')

    def testSetPicAsWallpaper(self):
        """
        Summary:Set picture as wallpaper
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Click Set picture as 
              4.Click Wallpaper
              5.Click corp
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self.press('menu')
        self.touch('1_set_pic_as.png')
        self.expect('2_set_as_dialog.png')
	self.touch('3_wallpaper_icon.png')
	if self.exists("always.png"):
	    self.touch('gallery.png')
	    time.sleep(1)
	    self.touch('OK_Always.png')       
        if self.exists("crop_picture.png",timeout=5):
            self.touch("crop_picture.png")\
            .touch("just_once.png")
        self.touch('4_CROP_OK.png')
        
    def testSetPicAsWallpaperCancel(self):
        """
        Summary:Cancel Set picture as wallpaper
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Click Set picture as 
              4.Click Wallpaper
              5.Click cancel
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self.press('menu')
        self.touch('1_set_pic_as.png')
        self.expect('2_set_as_dialog.png')
        self.touch('3_wallpaper_icon.png')
	if self.exists("always.png"):
	    self.touch('gallery.png')
	    time.sleep(1)
	    self.touch('OK_Always.png')
        if self.exists("crop_picture.png",timeout=5):
            self.touch("crop_picture.png")\
            .touch("just_once.png")
        self.touch('4_CROP_CANCEL.png')

    def testCheckDetail(self):
        """
        Summary:Check picture details
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Click Details Item
              4.Click close
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self.touch(PULLUP_CARD_POP_MENU_POINT)
        self.touch(PULLUP_CARD_POP_MENU_POINT)
        self.touch(SETTING_BAR,waittime=5)
        self.drag((600,1130),(600,400),2,5)
        self.sleep(2)
        
        if not self.exists('2_check_details.png'):
            self.fail("Check details failed!!!")
            
    def testAddKeyWords(self):
        """
        Summary:Add key words for picture
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Click Details Item
              4.Click close
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self.touch(PULLUP_CARD_POP_MENU_POINT)
        self.touch(PULLUP_CARD_POP_MENU_POINT)
        self.touch(SETTING_BAR,waittime=5)
        self.drag((600,1030),(600,400),2,5)
        self.sleep(2)
        
        self.touch('2_add_keywords_icon.png',waittime=2)\
        .input('keyword')\
        .touch('keyboard_done.png')\
        .expect('3_add_successful.png')
        
        self.touch('delete_keyword.png')
        
    def testAddEvent(self):
        """
        Summary:Add event for picture
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Click Details Item
              4.Click close
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self.sleep(3)
        #self.touch(SETTING_BAR)\
        self.touch(PULLUP_CARD_POP_MENU_POINT)
        self.touch(PULLUP_CARD_POP_MENU_POINT)
        self.touch(SETTING_BAR)\
        .sleep(1)\
        .touch(EVENT)\
        .sleep(3)\
        .input('event')\
        .touch('2_keyboard_done.png')\
        .expect('3_add_event_successful.png')
        
    def testAddVenue(self):
        """
        Summary:Add event for picture
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Click Details Item
              4.Click close
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self.touch(PULLUP_CARD_POP_MENU_POINT)
        self.touch(PULLUP_CARD_POP_MENU_POINT)
        self.touch(SETTING_BAR)\
        .sleep(1)\
        .touch(VENUE)\
        .sleep(3)\
        .input('venue')\
        .touch('2_keyboard_done.png')\
        .expect('3_add_venue_successful.png')
    
    def tearDown(self):
        self.press('back,back,back,back,home')
        super(FullViewMenuTest,self).tearDown()
