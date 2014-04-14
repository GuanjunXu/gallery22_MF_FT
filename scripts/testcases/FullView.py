#!/usr/bin/env python
import unittest
import string,random,commands
import libs.datahelper
import gallery22_RHB_FT.cases.util
import commands
import time

PACKAGE_NAME = 'com.intel.android.gallery3d'
ACTIVITY_NAME = PACKAGE_NAME + '.app.Gallery'
SCREEN_ANY_POINT = (640,990)
PULLUP_CARD_POP_MENU_POINT = (290,96)
SHARE_ICON_IN_FULL_VIEW = (446,100)
PLAY_VIDEO_ICON_POINT = (360,666)

class FullViewTest(unittest.TestCase):
    def setUp(self):
        super(FullViewTest,self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        self.util = gallery22_RHB_FT.cases.util.Util()
        self.util._confirmResourceExists()
    
    def _launchGallery(self):
        """
        method: launchgallery app.
        """
        self.launch(component=self.runComponent)\
        .expect('0_launchgallery_checkpoint.png')


    def testSlidePictures(self):
        self._launchGallery()
        self.util._enterSingleView()
        for i in range (1,5):
            commands.getoutput('adb shell input swipe 648 288 59 288')
        self.expect('1_slide_from_R_to_L.png')
        for i in range (1,4):
            commands.getoutput('adb shell input swipe 59 288 648 288')
        self.expect('2_slide_from_L_to_R.png')

    def testCheckShareListIcons(self):
        self.util._clearCache()
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.expect('3_share_list.png')
    
    def testSharePictureToBlueTooth(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_bluetooth.png')
        if self.exists('4_turnon.png'):
            self.touch('4_turnon.png')
        self.expect('5_bluetooth_screen.png')
        
    def testSharePictureToPicasa(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_picasa.png',waittime=5)
        self.expect('4_picasa_screen.png')
        
        
    def testSharePictureToMessaging(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_messaging.png')
        self.expect('4_message_screen.png')
        self._discardMessage()
        
    def testSharePictureToOrkut(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_orkut.png',waittime=8)
        self.expect('4_orkut_screen.png')
    
    def testSharePictureTowifidirect(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_wifidirect.png')
        self.expect('4_wifidirect_screen.png')
    
    def testSharePictureToGooglePlus(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_googleplus.png')
        
    def testSharePictureToIntelConnectCenter(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_intel_connectcenter.png',waittime=8)
        self.expect('4_intel_connnectcenter_screen.png')
        
    def testSharePictureToGmail(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_gmail.png',waittime=8)
        self.expect('4_gmail_screen.png')
        self._discardGmail()
        
    def testSharePictureToDrive(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_driver.png',waittime=8)
        if self.exists('4_accept.png'):
            self.touch('4_accept.png')
        self.expect('5_driver_screen.png')
        
    def testSharePictureToFacebook(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        commands.getoutput('adb shell input swipe 590 1086 590 680')
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
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_youktube.png',waittime=8)
        self.expect('4_youktube_screen.png')
    
    def testSharePictureToBlueToothCheckLastIcon(self):
        self.util._clearCache()
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_bluetooth.png')
        if self.exists('4_turnon.png'):
            self.touch('4_turnon.png')
        self.expect('5_bluetooth_screen.png')
        self.press('back')
        self._touchShareIcon()
        self.expect('6_bt_first.png')
        
    def testSharePictureToPicasaCheckLastIcon(self):
        self.util._clearCache()
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_picasa.png',waittime=5)
        self.expect('4_picasa_screen.png')
        self.press('back')
        self._touchShareIcon()
        self.expect('5_picasa_first.png')
        
    def testPlayVideo(self):
        self.util._prepareVideo()
        self._launchGallery()
        self.util._enterSingleView()
        time.sleep(2)
        self.expect('1_play_icon.png')
        self.touch('1_play_icon.png')
        
        if self.exists('2_choose_action_using.png'):
            self.touch('3_socialgallery_icon.png',waittime=1)
            self.touch('4_always.png')
        self.sleep(15)
        self.touch(PLAY_VIDEO_ICON_POINT)
        self.touch(PLAY_VIDEO_ICON_POINT)
        self.expect('5_share_icon.png')
    
       
    def testSharePictureToMessagingCheckLastIcon(self):
        self.util._clearCache()
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_messaging.png')
        self.expect('4_message_screen.png')
        self._discardMessage()
        self._touchShareIcon()
        self.expect('5_message_first.png')
        
    def testSharePictureToOrkutCheckLastIcon(self):
        self.util._clearCache()
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_orkut.png',waittime=8)
        self.expect('4_orkut_screen.png')
        self.press('back')
        self._touchShareIcon()
        self.expect('5_orkut_first.png')
    
    def testSharePictureToWifidirectCheckLastIcon(self):
        self.util._clearCache()
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_wifidirect.png')
        self.expect('4_wifidirect_screen.png')
        self.press('back')
        self._touchShareIcon()
        self.expect('5_wifidirect_first.png')
    
    def testSharePictureToGooglePlusCheckLastIcon(self):
        self.util._clearCache()
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_googleplus.png',waittime=10)
        #self.sleep(10)
        #self.expect('4_googleplus_screen.png')
        #self.press('back,back')
        #self._touchShareIcon()
        #self.expect('5_googleplus_first.png')
        
    def testSharePictureToIntelConnectCenterCheckLastIcon(self):
        self.util._clearCache()
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_intel_connectcenter.png',waittime=8)
        self.expect('4_intel_connnectcenter_screen.png')
        self.press('back')
        self._touchShareIcon()
        self.expect('5_intel.png')
        
    def testSharePictureToGmailCheckLastIcon(self):
        self.util._clearCache()
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_gmail.png',waittime=8)
        if self.exists('4_syncnow.png'):
            self.logger.info('Gmail syncing now!!!')
        else:
            self.expect('4_gmail_screen.png')
            self._discardGmail()
            self._touchShareIcon()
            self.expect('5_gmail.png')
        
    def testSharePictureToDriveCheckLastIcon(self):
        self.util._clearCache()
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_driver.png',waittime=8)
        if self.exists('4_accept.png'):
            self.touch('4_accept.png')
        self.expect('5_driver_screen.png')
        #self.press('back,back')
        self.press('back')
        self._showUpOperations()
        self._touchShareIcon()
        self.expect('5_driver.png')

    def testShareVideoToYouTubeCheckLastIcon(self):
        self.util._clearCache()
        self.util._prepareVideo()
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        self.touch('3_youktube.png',waittime=8)
        self.expect('4_youktube_screen.png')     
        self.press('back')
        self._touchShareIcon()
        self.expect('5_youtube.png')

    def testDeleteSingle(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        #self.touch('1_extrasmenu.png')
        #self.touch((664,100),waittime=3)
        beforeNo = self.util._getPictureNumber()
        self.touch('delete_icon.png')
        self.touch('delete_confirm.png')
        afterNo = self.util._getPictureNumber()
        self.failIf(string.atoi(beforeNo)-string.atoi(afterNo) != 1,'Delete single picture in single view failed !!!')
        
    def testCancelDelete(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        #self.touch('1_extrasmenu.png')
        #self.touch((664,100),waittime=3)
        self.touch('delete_icon.png')
        beforeNo = self.util._getPictureNumber()
        self.touch('3_delete_CANCEL.png')
        afterNo = self.util._getPictureNumber()
        self.failIf(beforeNo != afterNo,'Cancel delete single picture in single view failed !!!')
        
    def testCheckSlideshowOptions(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        #self.touch('1_extrasmenu.png')
        #self.touch((664,100),waittime=3)
        self._pressMenu()
        self.touch('2_slideshow_option.png')
        self.touch('3_slideshow_list.png')
    
    def testSlideshowWithCineEffect(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        #self.touch('1_extrasmenu.png')
        #self.touch((664,100),waittime=3)
        self._pressMenu()
        self.touch('2_slideshow_option.png')
        self.touch('3_slideshow_list.png')
        self.touch((420,200+100*(1-1)))
        #slide show time 10s
        self.sleep(5)
        #touch screen any point
        self.touch(SCREEN_ANY_POINT,waittime=2)
        self._showUpOperations()
        self.expect('4_share_icon.png')
    
    def testSlideshowWithDissolve(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        #self.touch('1_extrasmenu.png')
        #self.touch((664,100),waittime=3)
        self._pressMenu()
        self.touch('2_slideshow_option.png')
        self.touch('3_slideshow_list.png')
        self.touch((420,200+100*(2-1)))
        #slide show time 10s
        self.sleep(5)
        #touch screen any point
        self.touch(SCREEN_ANY_POINT,waittime=2)
        self._showUpOperations()
        self.expect('4_share_icon.png')
        
    def testSlideshowWithFlash(self):
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        #self.touch('1_extrasmenu.png')
        #self.touch((664,100),waittime=3)
        self._pressMenu()
        self.touch('2_slideshow_option.png')
        self.touch('3_slideshow_list.png')
        self.touch((420,200+100*(3-1)))
        #slide show time 10s
        self.sleep(5)
        #touch screen any point
        self.touch(SCREEN_ANY_POINT,waittime=2)
        self._showUpOperations()
        self.expect('4_share_icon.png')
    
    def testSharePictureToFacebookCheckLastIcon(self):
        self.util._clearCache()
        self._launchGallery()
        self.util._enterSingleView()
        self._showUpOperations()
        self._touchShareIcon()
        self.touch('2_seeall.png')
        commands.getoutput('adb shell input swipe 562 1127 562 850')
        self.touch('3_facebook.png',waittime=8)
        if self.exists('4_loading_icon.png'):
            self.logger.debug('Cannot enter into facebook screen!!!')
        elif self.exists('4_facebook_screen.png'):
            self.logger.debug('Enter into facebook screen successful!!!')
        else :
            self.fail()
        self.press('back')
        self._touchShareIcon()
        self.expect('5_facebook.png')
    
    def testPlayVideoBackground(self):
        self.util._prepareVideo()
        self._launchGallery()
        self.util._enterSingleView()
        time.sleep(2)
        self.expect('1_play_icon.png')
        self.touch('1_play_icon.png')
        
        if self.exists('2_choose_action_using.png'):
            self.touch('3_socialgallery_icon.png',waittime=1)
            self.touch('4_always.png')
        time.sleep(5)
        self.touch((540,650))
        self.touch((565,58))
        self.expect('5_background.png')
        time.sleep(90)


    def _touchShareIcon(self):
        self.touch(SHARE_ICON_IN_FULL_VIEW,waittime=3) 
    
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
    
    def tearDown(self):
        self.press('back,back,back,back')
        super(FullViewTest,self).tearDown()
