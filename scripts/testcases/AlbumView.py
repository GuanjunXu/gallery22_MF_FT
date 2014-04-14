#!/usr/bin/env python
import unittest
import string
import gallery22_MF_FT.cases.util

PACKAGE_NAME = 'com.intel.android.gallery3d'
ACTIVITY_NAME = PACKAGE_NAME + '.app.Gallery'

#POINT
ALBUM_FILTER_POINT = (205,105)
SELECT_ONE_ALBUM_POINT = (373,698)
SELECT_ITEM_POINT = (200,100)
UPDATE_NOTIFICATION_POINT = (537,254)

class AlbumViewTest(unittest.TestCase):
    def setUp(self):
        super(AlbumViewTest,self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        self.util = gallery22_MF_FT.cases.util.Util()
        self.util._confirmResourceExists()
        
    def _launchGallery(self):
        """
        method: launchgallery app.
        """
        self.launch(component=self.runComponent)\
        .expect('0_launchgallery_checkpoint.png')
    
    def testSwitchToCamera(self):
        """
        Summary:testSwitchToCamera: Launch Social Gallery and switch to intel camera
        Initialization: Make sure not less than 1 pictures in sdcard,if less than 1 picture in it, push resources(20)
        Steps:  1.Launch Social Gallery app
                2.Check launch successfully
                3.Touch camera key to switch camera
                4.Check camera launch
        """
        self._launchGallery()
        self.touch('1_camera_icon.png')
        if self.exists('2_complete_action_using.png'):
            self.touch('3_camera2.png',waittime=2)
            #self.touch('4_always.png',waittime=3)
        self.expect('5_launchcamera_checkpoint.png')
    
    def testSwitchAlbumToEvents(self):
        """
        Initialization: Make sure not less than 1 pictures in sdcard
        Steps: 1.Launch Social Gallery app 
               2.Check launch successfully 
               3.Touch album filter
               4.Select events option
               5.Exit Gallery app
        """
        self._launchGallery()
        self.touch(ALBUM_FILTER_POINT)
        self.expect('1_album_filter_list.png')
        self.touch('2_event.png',waittime=3)
        self.expect('3_event_in_title.png')
    
    def testSwitchAlbumToPlaces(self):
        """
        Initialization: Make sure not less than 1 pictures in sdcard
        Steps: 1.Launch Social Gallery app 
               2.Check launch successfully 
               3.Touch album filter
               4.Select events option
               5.Exit Gallery app
        """
        self._launchGallery()
        self.touch(ALBUM_FILTER_POINT)
        self.expect('1_album_filter_list.png')
        self.touch('2_places.png',waittime=3)
        self.expect('3_places_in_title.png')     
    
    def testSwitchAlbumToDates(self):
        """
        Initialization: Make sure not less than 1 pictures in sdcard
        Steps: 1.Launch Social Gallery app 
               2.Check launch successfully 
               3.Touch album filter
               4.Select dates option
               5.Exit Gallery app
        """
        self._launchGallery()
        self.touch(ALBUM_FILTER_POINT)
        self.expect('1_album_filter_list.png')
        self.touch('2_dates.png',waittime=3)
        self.expect('3_dates_in_title.png')
        
    def testSwitchAlbumToPeople(self):
        """
        Initialization: Make sure not less than 1 pictures in sdcard
        Steps: 1.Launch Social Gallery app 
               2.Check launch successfully 
               3.Touch album filter
               4.Select people option
               5.Exit Gallery app
        """
        self._launchGallery()
        self.touch(ALBUM_FILTER_POINT)
        self.expect('1_album_filter_list.png')
        self.touch('2_people.png',waittime=3)
        self.expect('3_people_in_title.png')
    
    def testSwitchOtherFilterToAlbums(self):
        """
        Initialization: Make sure not less than 1 pictures in sdcard
        Steps: 1.Launch Social Gallery app 
               2.Check launch successfully 
               3.Touch album filter
               4.Select people option
               5.Exit Gallery app
        """
        self._launchGallery()
        self.touch(ALBUM_FILTER_POINT)
        self.expect('1_album_filter_list.png')
        self.touch('2_people.png',waittime=3)
        self.expect('3_people_in_title.png')
        
        self.touch(ALBUM_FILTER_POINT)
        self.touch('4_album.png',waittime=2)
        self.expect('5_album_in_title.png')

    def testCheckAlbumInfo(self):
        self._launchGallery()
        self.expect('1_album_info.png')
    
    def testSelectDeselectAllByMenu(self):
        self._launchGallery()
        #self.touch('1_extras_menu.png',waittime=2)
        self._pressMenu()
        self.sleep(10)
        self.touch('2_select_album.png',waittime=2)
        self.expect('3_0selected.png')
        self.touch(SELECT_ITEM_POINT,waittime=2)
        self.touch('4_selectall.png')
        self.touch(SELECT_ITEM_POINT,waittime=2)
        self.touch('5_deselectall.png')
        self.expect('0_launchgallery_checkpoint.png')
        
    def testMakeAvailableOffline(self):
        self._launchGallery()
        #self.touch('1_extras_menu.png',waittime=2)
        self._pressMenu()
        self.touch('2_make_available_offline.png',waittime=2)
        self.expect('3_makeavailableoffline_checkpoint.png')
    
    def testRefresh(self):
        self._launchGallery()
        #self.touch('1_extras_menu.png',waittime=2)
        self._pressMenu()
        self.touch('2_refresh.png')
        self.expect('0_launchgallery_checkpoint.png')
    
    def testEnterSettingsScreen(self):
        self._launchGallery()
        #self.touch('1_extras_menu.png')
        self._pressMenu()
        self.touch('2_settings.png')
        self.expect('3_settings_screen.png')
    
    def testTurnOffOnUpdateNotification(self):
        self._launchGallery()
        #self.touch('1_extras_menu.png')
        self._pressMenu()
        self.touch('2_settings.png')
        
        if self.exists('3_settings_screen.png'):
            self.touch(UPDATE_NOTIFICATION_POINT,waittime=2)
            self.expect('4_turnoff_notification.png')
            self.touch(UPDATE_NOTIFICATION_POINT,waittime=2)
            self.expect('3_settings_screen.png')
        elif self.exists('4_turnoff_notification.png'):
            self.touch(UPDATE_NOTIFICATION_POINT,waittime=2)
            self.expect('3_settings_screen.png')
            self.touch(UPDATE_NOTIFICATION_POINT,waittime=2)
            self.expect('4_turnoff_notification.png')
        else: 
            self.fail()
        
    def testSortByNameZA(self):
        self._launchGallery()
        #self.touch('1_extras_menu.png')
        self._pressMenu()
        self.touch('2_sortbynameZA.png')
        #self.expect('1_extras_menu.png')
        self.expect('0_launchgallery_checkpoint.png')
    
    def testSortByNameAZ(self):
        self._launchGallery()
        #self.touch('1_extras_menu.png')
        self._pressMenu()
        self.touch('2_sortbynameAZ.png')
        #self.expect('1_extras_menu.png')
        self.expect('0_launchgallery_checkpoint.png')
    
    def testSortByRecentDescending(self):
        self._launchGallery()
        #self.touch('1_extras_menu.png')
        self._pressMenu()
        self.touch('2_sortbyrecentdescending.png')
        #self.expect('1_extras_menu.png')
        self.expect('0_launchgallery_checkpoint.png')
    
    def testSortByRecentAscending(self):
        self._launchGallery()
        #self.touch('1_extras_menu.png')
        self._pressMenu()
        self.touch('2_sortbyrecebtascending.png')
        #self.expect('1_extras_menu.png')
        self.expect('0_launchgallery_checkpoint.png')
    
    
    def testSocialSyncIcon(self):
        self._launchGallery()
        #self.touch('1_extras_menu.png',waittime=2)
        self._pressMenu()
        self.touch('1_socialsync.png')
        self.expect('0_launchgallery_checkpoint.png')
    
    def testSearchAlbum(self):
        """
        Initialization: Make sure 1 album with keywords
        Steps:1.Launch Social Gallery app
              2.Check launch successfully
              3.Touch 'Search' button
              4.Type the content you want to search(Input Test)
              5.Touch 'Search' button
              6.View the searched picture
              7.Touch 'Menu'
              8.Touch 'select item'
              9.Touch selected icon
              10.Touch select all
              11.Touch Delete icon
              12.Exit Gallery app 
        """
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        self.touch('1_extras_menu.png',waittime=2)
        self.touch('2_add_keywords.png',waittime=2)
        self.input('addalbumkeywords')
        self.expect('3_input_tag_checkpoint.png')
        self.touch('3_keyboard_done.png',waittime=5)
        self.touch('5_search_icon.png')
        self.input('addalbumkeywords')
        self.sleep(2)
        self.touch('6_searach_result.png')
        #self.touch('7_extras_menu.png')
        #self._pressMenu()
        self.longtouch((150,280))
        self.touch('8_select_item_option.png')
        #self.touch(SELECT_ITEM_POINT,waittime=2)
        self.touch('9_selectall.png')
        self.touch('10_delete_icon.png')
        self.touch('11_delete_OK.png',waittime=10)
    
    def testAddkeywordsToAlbum(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        self.touch('1_extras_menu.png',waittime=2)
        self.touch('2_add_keywords.png',waittime=2)
        self.input('addalbumkeywords')
        self.expect('3_input_tag_checkpoint.png')
        self.touch('3_keyboard_done.png',waittime=5)
        self.touch('5_search_icon.png')
        self.input('addalbumkeywords')
        self.sleep(2)
        self.touch('6_searach_result.png')
        #self.touch('7_extras_menu.png')
        #self._pressMenu()
        self.longtouch((150,280))
        self.touch('8_select_item_option.png')
        #self.touch(SELECT_ITEM_POINT,waittime=2)
        self.touch('9_selectall.png')
        self.touch('10_delete_icon.png')
        self.touch('11_delete_OK.png',waittime=10)
    
    def testCheckAlbumDetail(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        self.touch('1_extras_menu.png')
        self.touch('2_detail.png') 
        self.expect('3_detail_screen.png')
    
    def testCheckNoDetailOption(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        self.expect('1_1selected.png')
        self.touch(SELECT_ITEM_POINT)
        self.touch('2_selectall.png')
        self.touch('3_extras_menu.png')
        self.failIf(self.exists('4_detail.png'),'Exists detail option when select all albums!!!')
    
    def testShareAlbumToBluetooth(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_bluetooth.png')
        
        if self.exists('4_turnon.png'):
            self.touch('4_turnon.png')
        self.expect('5_bluetooth_screen.png')
    
    def testShareAlbumToPicasa(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_picasa.png',waittime=5)
        self.expect('4_picasa_screen.png')
        
    def testShareAlbumToMessaging(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_messaging.png')
        self.expect('4_message_screen.png')
        self._discardMessage()
    
    def testShareAlbumToGooglePlus(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_googleplus.png')
        if self.exists('Choose_account.png'):
            self.touch('Account_Icon.png')
        self.expect('4_googleplus_screen.png')
        self.press('back')
        self.touch('5_ConfirmCancel.png')
    
    def testSharePictureToIntelConnectCenter(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_intel_connectcenter.png',waittime=8)
        self.expect('4_intel_connnectcenter_screen.png')
    
    def testShareAlbumToGmail(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_gmail.png',waittime=8)
        self.expect('4_gmail_screen.png')
        self._discardGmail()
        
    def testShareAlbumToDrive(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_driver.png',waittime=8)
        if self.exists('4_accept.png'):
            self.touch('4_accept.png')
        self.expect('4_driver_screen.png')
    
    def testShareAlbumToFacebook(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_facebook.png',waittime=8)
        '''
        self.press('back')
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_facebook.png',waittime=8)
	'''
        if self.exists('4_loading_icon.png'):
            self.logger.debug('Cannot enter into facebook screen!!!')
        elif self.exists('4_facebook_screen.png'):
            self.logger.debug('Enter into facebook screen successful!!!')
	    self.press('back')
            self.sleep(1)
            self.touch('5_ConfirmCancel.png')
        else :
            self.fail()

        
    def testShareAlbumToOrkut(self):
        self.util._push1Picture()
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_orkut.png',waittime=8)
        self.expect('4_orkut_screen.png')
    
    def testShareAlbumToYoutube(self):
        self.util._prepareVideo()
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        self.touch('1_share_icon.png')
        self.touch('2_seeall.png')
        self.touch('3_youktube.png',waittime=8)
        self.expect('4_youktube_screen.png')
    
    def testDeleteOneAlbum(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        self.touch('1_delete_icon.png')
        beforeNo = self.util._getPictureNumber()
        self.touch('2_delete_OK.png')
        afterNo = self.util._getPictureNumber()
        self.failIf(string.atoi(beforeNo)-string.atoi(afterNo) !=  20,'Delete one album failed !!')
        
    def testDeleteAllAlbums(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        self.touch(SELECT_ITEM_POINT)
        self.touch('1_selectall.png')
        self.touch('2_delete_icon.png')
        self.touch('3_delete_OK.png',waittime=15)
        afterNo = self.util._getPictureNumber()
        self.failIf(string.atoi(afterNo) != 0,'Delete all album failed !!')
    
    def testCancelDeleteAlbum(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        self.touch('1_delete_icon.png')
        beforeNo = self.util._getPictureNumber()
        self.touch('2_delete_CANCEL.png')
        afterNo = self.util._getPictureNumber()
        self.failIf(beforeNo != afterNo,'Cancel delete one album failed !!')
    
    def testSelectDeselectAllByLongTouch(self):
        self._launchGallery()
        self.drag(SELECT_ONE_ALBUM_POINT,SELECT_ONE_ALBUM_POINT,3,6)
        self.expect('1_1selected.png')
        self.touch(SELECT_ITEM_POINT,waittime=2)
        self.touch('2_selectall.png')
        self.touch(SELECT_ITEM_POINT,waittime=2)
        self.touch('3_deselectall.png')
        self.expect('0_launchgallery_checkpoint.png')
        
    def _discardMessage(self):
        #self.touch('mss0_extras_menu.png',waittime=2)
        self.sleep(1)
        self._pressMenu()
        self.sleep(1)
        self.touch('mss1_discard.png',waittime=2)
    
    def _pressMenu(self):
        self.press('menu')
        self.sleep(2)

    def _discardGmail(self):
        #self.touch('gmail_extrasmenu.png')
        self._pressMenu()
        self.touch('gmail_discard.png')
        self.touch('gmail_discard_OK.png')
        
    
    def tearDown(self):
        self.press('back,back,back,back')
        super(AlbumViewTest,self).tearDown()

