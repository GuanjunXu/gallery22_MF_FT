#!/usr/bin/env python
import unittest
import string,random,commands
import libs.datahelper
import gallery22_MF_FT.cases.util
import time

PACKAGE_NAME = 'com.intel.android.gallery3d'
ACTIVITY_NAME = PACKAGE_NAME + '.app.Gallery'

PACKAGE_NAME1 = 'com.intel.camera22'
ACTIVITY_NAME1 = PACKAGE_NAME1 + '.Camera'

#POINT
SELECT_ONE_ALBUM_POINT = (373,698)
SCREEN_ANY_POINT = (640,990)
ONE_PICTURE_IN_GRIDVIEW_POINT = (120,267)
SELECT_ITEM_POINT = (200,100)
ONE_PIC_IN_SEARCH_RESULT = (373,666)
PULLUP_CARD_POP_MENU_POINT = (290,96)
SINGLE_PIC_BOTTOM_POINT = (590,1078)
EDIT_VINTAGE_EFFECT_POINT = (376,580)
CAMERA_GEOTAG_ON_OFF = "adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_camera_geo_location_key"
GEO_TAG_POINT_IN_SETTING = (60,60)
GEP_TAG_IMAG = (290,170)
GEO_TAG_ON_POINT_IN_SETTING = (176,290)
GEO_TAG_OFF_POINT_IN_SETTING = (60,290)

class GridViewTest(unittest.TestCase):
    def setUp(self):
        super(GridViewTest,self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        self.runComponent1 = PACKAGE_NAME1 + '/' + ACTIVITY_NAME1
        self.util = gallery22_MF_FT.cases.util.Util()
        self.util._confirmResourceExists()
    
    def _launchCamera(self):
        """
        method: launch Camera app
        """
        self.launch(component=self.runComponent1)
        self.expect('0_launchCamera_checkpoint.png')
    
    def _launchGallery(self):
        """
        method: launchgallery app.
        """
        self.launch(component=self.runComponent)\
        .expect('0_launchgallery_checkpoint.png')
    
    def testUpnavigation(self):
        self._launchGallery()
        self.util._enterGridView()
        self.touch('1_upnavigation.png')
        self.expect('2_album_view_checkpoint.png')

    def testSlideShowWithCinEffect(self):
        self._launchGallery()
        self.util._enterGridView()
        #self.touch(SELECT_ONE_ALBUM_POINT,waittime=2)
        self.touch('1_option.png')
        self.touch('1_slideshow_icon.png')
        self.expect('2_slideshow_list.png')
        self.touch('3_cine_effect.png')
        #slide show time 10s
        self.sleep(10)
        #touch screen any point
        self.touch(SCREEN_ANY_POINT,waittime=2)
        self.expect('0_launchgallery_checkpoint.png')
    
    def testSlideShowWithDissolve(self):
        self._launchGallery()
        self.util._enterGridView()
        #self.touch(SELECT_ONE_ALBUM_POINT,waittime=2)
        self.touch('1_option.png')
        self.touch('1_slideshow_icon.png')
        self.expect('2_slideshow_list.png')
        self.touch('3_dissolve.png')
        #slide show time 10s
        self.sleep(10)
        #touch screen any point
        self.touch(SCREEN_ANY_POINT,waittime=2)
        self.expect('0_launchgallery_checkpoint.png')
        
    def testSlideShowWithFlash(self):
        self._launchGallery()
        self.util._enterGridView()
        #self.touch(SELECT_ONE_ALBUM_POINT,waittime=2)
        self.touch('1_option.png')
        self.touch('1_slideshow_icon.png')
        self.expect('2_slideshow_list.png')
        self.touch('3_flash.png')
        #slide show time 10s
        self.sleep(10)
        #touch screen any point
        self.touch(SCREEN_ANY_POINT,waittime=2)
        self.expect('0_launchgallery_checkpoint.png')
        
    def testSocialSyncIcon(self):
        self._launchGallery()
        self.util._enterGridView()
        #self.touch('1_extrasmenu_icon.png')
        self.touch('1_option.png')
        self.touch('1_socialsync_option.png')
        self.expect('0_launchgallery_checkpoint.png')
    
    def testSelectItem(self):
        self._launchGallery()
        self.util._enterGridView()
        #self.touch('1_extrasmenu_icon.png')
        #self._pressMenu()
        self.longtouch((150,300))
        self.expect('1_one_pic_selected.png')
        self.touch('2_select_item.png')
        #self.touch(SELECT_ITEM_POINT,waittime=2)
        self.touch('3_selectall.png')
        self.expect('3_all_pic_selected.png')
        self.touch('2_select_item.png')
        self.touch('4_deselectall.png')
        self.expect('0_launchgallery_checkpoint.png')
    
    def testCheckShareListIcons(self):
        self.util._clearCache()
        self._launchGallery()
        self.util._enterGridView()
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.expect('3_share_list.png')
        
    def testSharePictureToBlueTooth(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_bluetooth.png')
        if self.exists('4_turnon.png'):
            self.touch('4_turnon.png')
        self.expect('5_bluetooth_screen.png',timeout=10)
    
    def testSharePictureToPicasa(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_picasa.png',waittime=5)
        self.expect('4_picasa_screen.png')
    
    def testSharePictureToMessaging(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_messaging.png')
        self.expect('4_message_screen.png')
        self._discardMessage()
    
    def testSharePictureToOrkut(self):
        self.util._push1Picture()
        self._launchGallery()
        self.util._enterGridView()
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_orkut.png',waittime=8)
        self.expect('4_orkut_screen.png')
    
    def testSharePictureToGooglePlus(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_googleplus.png')
        #self.expect('4_googleplus_screen.png')
        
    def testSharePictureToIntelConnectCenter(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_intel_connectcenter.png',waittime=8)
        self.expect('4_intel_connnectcenter_screen.png')
        
    def testSharePictureToGmail(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        if self.exists('3_gmail.png',similarity=1):
            self.touch('3_gmail.png',waittime=8)
        else :
            self.drag((600,900),(600,500),4,6)
            self.touch('3_gmail.png',waittime=8)
        self.expect('4_gmail_screen.png')
        self._discardGmail()
    
    def testSharePictureToDrive(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_driver.png',waittime=8)
        if self.exists('4_accept.png'):
            self.touch('4_accept.png')
        self.expect('5_driver_screen.png')
        
    def testSharePictureToFacebook(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        if not self.exists('3_facebook.png'):
            self.drag((500,1000),(500,200),4,6)
        else:
            pass
        self.touch('3_facebook.png',waittime=8)
        if self.exists('4_loading_icon.png'):
            self.logger.debug('Cannot enter into facebook screen!!!')
        elif self.exists('4_facebook_screen.png'):
            self.logger.debug('Enter into facebook screen successful!!!')
        else :
            self.fail()
        
        
    def testShareVideoToYouTube(self):
        self.util._prepareVideo()
        self._launchGallery()
        self.util._enterGridView()
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_youktube.png',waittime=8)
        self.expect('4_youktube_screen.png')
    
    def testShareVideoToYouTubeAndCheckLastIcon(self):
        self.util._clearCache()
        self.util._prepareVideo()
        self._launchGallery()
        self.util._enterGridView()
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_youktube.png',waittime=8)
        self.expect('4_youktube_screen.png')
        self.press('back')
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.expect('5_first_shareicon_youtube.png')
        
    def testCheckSharelistStatusAfterSharePicToBT(self):
        self.util._clearCache()
        self._launchGallery()
        self.util._enterGridView()
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_bluetooth.png')
        if self.exists('4_turnon.png'):
            self.touch('4_turnon.png')
        self.expect('5_bluetooth_screen.png')
        self.press('back')
        self.drag((360,650),(360,650),4,6)
        self.touch('1_share_icon.png')
        self.expect('6_first_shareicon_bluetooth.png')
    
    
    def testDeleteSelectedOnePhoto(self):
        self._launchGallery()
        #self.touch(SELECT_ONE_ALBUM_POINT,waittime=2)
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch('1_delete_icon.png')
        beforeNo = self.util._getPictureNumber()
        self.touch('2_delete_OK.png',waittime=2)
        afterNo = self.util._getPictureNumber()
        self.failIf(string.atoi(beforeNo)-string.atoi(afterNo) !=  1,'Delete 1 picture failed !!')
    
    
    def testDeleteSelectedMultiPhotos(self):
        self._launchGallery()
        #self.touch(SELECT_ONE_ALBUM_POINT,waittime=2)
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch((383,284),waittime=2)
        self.touch((397,551),waittime=2)
        
        self.touch('1_delete_icon.png')
        beforeNo = self.util._getPictureNumber()
        self.touch('2_delete_OK.png',waittime=5)
        afterNo = self.util._getPictureNumber()
        self.failIf(string.atoi(beforeNo)-string.atoi(afterNo) !=  3,'Delete 3 picture failed !!')
           
    def testSelectDeselectAll(self):
        self._launchGallery()
        #self.touch(SELECT_ONE_ALBUM_POINT,waittime=2)
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch(SELECT_ITEM_POINT,waittime=2)
        self.touch('1_selectall.png')
        self.touch(SELECT_ITEM_POINT,waittime=2)
        self.touch('2_deselectall.png')
    
    def testRotatePhotoLeft(self):
        self._launchGallery()
        #self.touch(SELECT_ONE_ALBUM_POINT,waittime=2)
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch(SELECT_ITEM_POINT)
        self.touch('1_selectall.png',waittime=3)
        self.touch('2_extrasmenu.png',waittime=2)
        self.touch('3_rotateleft.png')
        self.sleep(10)
        self.expect('0_launchgallery_checkpoint.png')
    
    def testRotatePhotoRight(self):
        self._launchGallery()
        #self.touch(SELECT_ONE_ALBUM_POINT,waittime=2)
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch(SELECT_ITEM_POINT)
        self.touch('1_selectall.png',waittime=3)
        self.touch('2_extrasmenu.png',waittime=2)
        self.touch('3_rotateright.png')
        self.sleep(10)
        self.expect('0_launchgallery_checkpoint.png')
    
    def testCropPhoto(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch('1_extrasmenu.png',waittime=2)
        self.touch('2_crop_option.png')
        if self.exists('3_complete_action_using.png'):
            self.touch('4_socialgallery.png')
            self.touch('5_always.png')
        beforeNo = self.util._getPictureNumber()
        self.touch('6_CROP.png')
        afterNo = self.util._getPictureNumber()
        self.failIf(string.atoi(afterNo)-string.atoi(beforeNo) != 1,'Crop picture failed!!!')
    
    def testSetPictureAs(self):
        self.da = libs.datahelper.DataHelper()
        self.da.clearup('contacts')
        self.da.insertContact('contact0', '10010', '1')
        
        self._launchGallery()
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch('1_extrasmenu.png',waittime=2)
        self.touch('2_set_pic_as_option.png')
        self.expect('3_setas_dialog.png')
        a = random.randint(1,2)
        if a == 1:
            self.touch('4_contact.png',waittime=2)
            self.expect('5_contact_screen.png')
        else :
            self.touch('6_socialgallery.png',waittime=2)
            if self.exists('7_complete_action_using.png'):
                self.touch('8_socialgallery_icon.png',waittime=2)
                self.touch('9_always.png',waittime=2)
            self.touch('10_crop.png', waittime=5)
            self.expect('0_launchgallery_checkpoint.png')
    
    def testCheckPhotoDetail(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch('1_extrasmenu.png',waittime=2)
        self.touch('2_details.png')
        time.sleep(1)
        commands.getoutput('adb shell input swipe 600 900 600 300')
        self.expect('3_detail_dialog.png')
        
    def testSlideshow(self):
        self._launchGallery()
        self.util._enterGridView()
        #self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch('1_extrasmenu.png',waittime=2)
        self.touch('2_slideshow.png')
        
        a = random.randint(1,3)
        self.touch((420,200+100*(a-1)))
        #slide show time 10s
        self.sleep(10)
        #touch screen any point
        self.touch(SCREEN_ANY_POINT,waittime=2)
        self.expect('0_launchgallery_checkpoint.png')
    
    def testConvertPhotos(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch((383,284),waittime=2)
        self.touch((397,551),waittime=2)
        self.touch('1_extrasmenu.png',waittime=2)
        self.touch('2_convert_option.png',waittime=3)
        
        a = random.randint(1,3)
        self.touch((200,350+100*(a-1)),waittime=3)
        
        self.touch('3_convert.png',waittime=20)
        
        beforeNo = self._getConvertFileNum()
        self.expect('4_save_icon.png')
        self.touch('4_save_icon.png',waittime=3)
        
        afterNo = self._getConvertFileNum()
        self.util._deleteConvertFile()
    
    def testAddKeywordsToPhoto(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch('1_extrasmenu.png',waittime=2)
        self.touch('2_add_keywords.png')
        self.input('addkeywords')
        self.touch('3_DONE.png')
        self.touch('5_search_icon.png')
        self.input('addkeywords')
        self.sleep(5)
        self.touch('6_search_result.png',similarity=0.6)
        #self.touch('7_extras_menu.png')
        #self._pressMenu()
        self.longtouch((300,650))
        self.touch(SELECT_ITEM_POINT,waittime=2)
        if self.exists('9_selectall.png',similarity=0.95):
            self.touch('9_selectall.png')
        else:
            self.press('back')
        self.touch('10_delete_icon.png')
        self.touch('11_delete_OK.png',waittime=10)
        self.expect('0_launchgallery_checkpoint.png')
        
    def testSelectAllToShare(self):
        self.util._clearCache()
        self.util._confirmResourceExists()
        #Step 1
        self._launchGallery()
        
        #Step 2
        self.util._enterGridView()
        
        #Step 3
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch(SELECT_ITEM_POINT)
        self.touch('1_selectall.png')
        a = random.choice(['Bluetooth','Picasa','Messaging','Google+','Gmail','Drive','Facebook','Photos'])
        self.touch('2_share_icon.png',waittime=3)
        self.touch('3_seeall.png')
        
        if a == 'Bluetooth':
            self.touch('4_bluetooth.png')
            if self.exists('5_turnon.png'):
                self.touch('5_turnon.png')
                self.expect('6_bluetooth_screen.png')
        elif a == 'Picasa':
            self.touch('7_picasa.png',waittime=5)
            self.expect('8_picasa_screen.png')
        elif a == 'Messaging':
            self.touch('9_messaging.png')
            self.expect('10_message_screen.png')
            self._discardMessage()
        elif a == 'orkut':
            self.touch('11_orkut.png',waittime=8)
            self.expect('12_orkut_screen.png')
        elif a == 'Google+':
            self.touch('13_googleplus.png')
            #self.expect('14_googleplus_screen.png')
        elif a == 'wifidirect':
            self.touch('15_wifidirect.png')
            self.expect('16_wifidirect_screen.png')
        elif a == 'intel':
            self.touch('17_intel_connectcenter.png',waittime=8)
            self.expect('18_intel_connnectcenter_screen.png')
        elif a == 'Gmail':
            self.touch('19_gmail.png',waittime=8)
            self.expect('20_gmail_screen.png')
            self._discardGmail()
        elif a == 'Drive':
            self.touch('21_driver.png',waittime=8)
            if self.exists('22_accept.png'):
                self.touch('22_accept.png')
            self.expect('23_driver_screen.png')
        elif a == 'Facebook':
            self.touch('24_facebook.png',waittime=8)
            #if self.exists('25_loading_icon.png'):
            #    self.logger.debug('Cannot enter into facebook screen!!!')
            #elif self.exists('26_facebook_screen.png'):
            #    self.logger.debug('Enter into facebook screen successful!!!')
            #else :
            #    self.fail()
        elif a == 'Photos':
            self.touch('25_photos.png',waittime=8)
            self.expect('26_photos_screen.png')
    
    def testSelectAllRotate(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch(SELECT_ITEM_POINT)
        self.touch('1_selectall.png',waittime=3)
        self.touch('2_extrasmenu.png',waittime=2)
        a = random.randint(1,2)
        if a == 1:
            self.touch('3_rotateleft.png')
        else :
            self.touch('4_rotateright.png')
        self.sleep(10)
        self.expect('0_launchgallery_checkpoint.png')
    
    def testSelectAllToAddKeywords(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch(SELECT_ITEM_POINT)
        self.touch('1_selectall.png',waittime=3)
        self.touch('2_extrasmenu.png',waittime=2)
        self.touch('3_addkeywords.png')
        self.input('addkeywords')
        self.touch('4_DONE.png',waittime=20)
        self.touch('5_search_icon.png')
        self.input('addkeywords')
        self.touch('6_search_result.png',similarity=0.6)
        #self.touch(ONE_PIC_IN_SEARCH_RESULT,waittime=3)
        self.expect('7_addedkeywords_pics.png')
        #self.touch('8_extrasmenu.png')    
        #self._pressMenu()
        #self.touch('9_selectitem.png') 
        self.longtouch((300,650))
        self.touch(SELECT_ITEM_POINT)
        self.touch('1_selectall.png',waittime=3)      
        self.touch('10_delete_icon.png')
        self.touch('11_delete_OK.png',waittime=10)
    
    def testSelectAllSlideshow(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch(SELECT_ITEM_POINT)
        self.touch('1_selectall.png',waittime=3)
        self.touch('2_extrasmenu.png',waittime=2)
        self.touch('3_slideshow_option.png')
        self.expect('4_slideshow_list.png')
        a = random.randint(1,3)
        self.touch((420,200+100*(a-1)))
        #slide show time 10s
        self.sleep(10)
        #touch screen any point
        self.touch(SCREEN_ANY_POINT,waittime=2)
        self.expect('0_launchgallery_checkpoint.png')
    
    
    def testSelectAllConvert(self):
        self._launchGallery()
        self.util._enterGridView()
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        self.touch(SELECT_ITEM_POINT)
        self.touch('1_selectall.png',waittime=3)
        self.touch('2_extrasmenu.png',waittime=2)
        self.touch('3_convert_option.png',waittime=3)
        a = random.randint(1,3)
        self.touch((200,300+100*(a-1)),waittime=3)
        beforeNo = self._getConvertFileNum()
        self.touch('4_convert.png',waittime=20)
        self.touch('5_save_icon.png',waittime=3)
        
        afterNo = self._getConvertFileNum()
        self.util._deleteConvertFile()
    
    def testShowOnMap(self):
        self.util._clearAllResource()
        
        #launch map and locate current address
        self.launch(component='com.google.android.apps.maps/com.google.android.maps.MapsActivity')
        if self.exists('Welcome_Gmap.png'):
            self.touch('Welcome_Accept.png')
        self.expect('1_map_icon.png')
        self.touch('1_map_icon.png',waittime=5)
        self.press('back,back,back')
        #take a geotag pic
        self._launchCamera()
        if self.exists('launch_camera_OK.png'):
            self.touch('launch_camera_OK.png')
        self._setGeotagOnOff('on')
        self._capturePicAndCheck()
        self.press('back,back,back')
        
        #Step 1
        self._launchGallery()
        
        #Step 2
        self.util._enterGridView()
        
        self.drag((356,666),(356,666),4,6)
        self.touch('2_extra_menu.png')
        self.touch('3_show_on_map.png',waittime=5)
        self.expect('4_show_on_suc.png')
        self.util._clearAllResource()
    
    def testEditSelectedPhoto(self):
        """
        Initial:1.One or more pics  stored in the device
        Steps:1.Launch gallery activity 
              2.Enter Grid view
              3.Long touch a pic to select
              4.Tap Extra Menu
              5.Tap Edit option
              6. Random choose the options and tap SAVE icon
        """
        self.util._confirmResourceExists()
        #Step 1
        self._launchGallery()
        beforePicNo = self.util._getPictureNumber()
        
        #Step 2
        self.util._enterGridView()
        #Step 3
        self.drag(ONE_PICTURE_IN_GRIDVIEW_POINT,ONE_PICTURE_IN_GRIDVIEW_POINT,3,6)
        
        self.touch('2_extrasmenu.png',waittime=2)
        self.touch('3_edit_option.png',waittime=2)
        
        if self.exists('4_choose_an_action.png'):
            self.touch('5_socialgallery_icon.png',waittime=2)
        self.sleep(5)    
        a = random.randint(1,4)
        
        self.logger.debug('a = radom.randint(1,4) , a = '+str(a))
        self.touch((240+150*(a-1),1080),waittime=2)
        self.touch('6_save_icon.png',waittime=2)        
        afterPicNo = self.util._getPictureNumber()
        self.failIf(string.atoi(beforePicNo) != string.atoi(afterPicNo)-1,'Edit album failed!!!')
    
    
    def _capturePicAndCheck(self):
        self.touch((360,1095),waittime=5)
        
    def _setGeotagOnOff(self,tag):
        """
        set geotag is on or off
        tag is on or off
        """
        self.logger.debug('Set Geo tag is ************'+str(tag))
        value = commands.getoutput(CAMERA_GEOTAG_ON_OFF)
        self.logger.debug('NOW value is *********************'+value)
        if tag == 'on':
            mValue = value.find('off')
            if mValue != -1:
                #self.press('menu')
                self.touch((360,10))
                self.drag((360,5),(360,300),5,5)
                self.touch(GEO_TAG_POINT_IN_SETTING,waittime=2)
                self.touch(GEP_TAG_IMAG,waittime=2)
                self.touch(GEO_TAG_ON_POINT_IN_SETTING,waittime=4)
                value1 = commands.getoutput(CAMERA_GEOTAG_ON_OFF)
                mValue1= value1.find('off')
                if mValue1 != -1:
                    self.logger.debug('set geotag is on failed !!!')
                    self.assertTrue(False)
                    
        elif tag == 'off':
            mValue = value.find('on')
        
            if mValue == -1:
                #self.press('menu')
                self.touch((360,10))
                self.drag((360,5),(360,300),5,5)
                self.touch(GEO_TAG_POINT_IN_SETTING,waittime=2)
                self.touch(GEP_TAG_IMAG,waittime=2)
                self.touch(GEO_TAG_OFF_POINT_IN_SETTING,waittime=4)
                value1 = commands.getoutput(CAMERA_GEOTAG_ON_OFF)
                mValue1= value1.find('on')
                if mValue1 == -1 :
                    self.logger.debug('set geotag is off failed !!!')           
                    self.assertTrue(False)
    
    def _pressMenu(self):
        self.press('menu')
        self.sleep(2)
    
    def _discardMessage(self):
        #self.touch('mss0_extras_menu.png',waittime=2)
        self._pressMenu()
        self.touch('mss1_discard.png',waittime=2)
    
    def _discardGmail(self):
        #self.touch('gmail_extrasmenu.png')
        self._pressMenu()
        self.touch('gmail_discard.png')
        self.touch('gmail_discard_OK.png')
    
    def _showUpOperations(self):
        self.touch(PULLUP_CARD_POP_MENU_POINT)
        self.touch(PULLUP_CARD_POP_MENU_POINT)
        self.touch(PULLUP_CARD_POP_MENU_POINT)
    
    def _getConvertFileNum(self):
        """
        Get convert file number
        """
        result = commands.getoutput('adb shell ls /sdcard/Sharing/| wc -l')
        self.logger.debug('Now the convert file number is :' + result)
        return result 
    
    def tearDown(self):
        self.press('back,back,back,back')
        super(GridViewTest,self).tearDown()
