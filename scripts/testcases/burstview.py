#!/usr/bin/env python
import unittest, string
import random
import commands
import sys
import gallery22_MF_FT.cases.util
import time

"""
@author: Huang Rui
@contact: rui.huang@borqs.com 

@note: FT test cases for Intel Gallery
"""

SOCIAL_GALLERY_PACKAGE_NAME = 'com.intel.android.gallery3d'
SOCIAL_GALLERY_ACTIVITY_NAME = SOCIAL_GALLERY_PACKAGE_NAME + '.app.Gallery'

SDCARD_PATH = '/sdcard/DCIM/'
FOLDER_NAME = '100ANDRO'

WAIT_SLIDE_SHOW_TIME = 5
SLIDE_ICON_SHOW_POINT = (100, 100)
SMALL_PLAY_BURST_ICON_POINT = (550, 90)
EDIT_BUST_ICON_POINT = (550, 100)
TRASH_ICON_POINT = (440, 103)
THUMBNAIL_IN_FULLVIEW = (360, 1180)
EXTRA_MENU = (660,100)
SETTING_BAR = (500,1146)
EVENT = (400,700)
VENUE = (400,760)
PULLUP_CARD_POP_MENU_POINT = (324,100)
MEDIA_MOUNTED_SCAN_COMMAND = 'am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///mnt/sdcard'
PLAY_BURST_ICON_POINT = (360,666)


class GalleryBurstViewTest(unittest.TestCase):

    def setUp(self):
        super(GalleryBurstViewTest, self).setUp()
        self.runSocialGalleryComponent = SOCIAL_GALLERY_PACKAGE_NAME + '/' + SOCIAL_GALLERY_ACTIVITY_NAME
        self.util = gallery22_RHB_FT.cases.util.Util()
    
    def testSmallPlayBurstIconOfDissolve(self):
        """
        Summary:This case test play burst with Dissolve mode in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap small play burst icon -> Dissolve, wait some seconds to check if stopped the playing
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        #Tap small play burst icon twice,the fist tap try to activity the tool bar due to it is disappeared
        self._showUpOperations()
        self.touch(EXTRA_MENU)
        self.touch((500,390))\
        .sleep(WAIT_SLIDE_SHOW_TIME)\
        .expect('2_enter_burst_view_successful_checkpoing')

    def testSmallPlayBurstIconOfFlash(self):
        """
        Summary:This case test play burst with Flash mode in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap small play burst icon -> Flash, wait some seconds to check if stopped the playing
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        #Tap small play burst icon twice,the fist tap try to activity the tool bar due to it is disappeared
        self._showUpOperations()
        self.touch(EXTRA_MENU)
        self.touch((500,390))\
        .sleep(WAIT_SLIDE_SHOW_TIME)
        self.touch('3_Flash_item.png')\
        .sleep(WAIT_SLIDE_SHOW_TIME)\
        .expect('2_enter_burst_view_successful_checkpoing')
    
    def testSmallPlayBurstIconOfPageflip(self):
        """
        Summary:This case test play burst with Page flip mode in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap small play burst icon -> Page flip, wait some seconds to check if stopped the playing
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        #Tap small play burst icon twice,the fist tap try to activity the tool bar due to it is disappeared
        self._showUpOperations()
        self.touch(EXTRA_MENU)
        self.touch((500,390))\
        .sleep(WAIT_SLIDE_SHOW_TIME)
        self.touch('3_Page_flip_item.png')\
        .sleep(WAIT_SLIDE_SHOW_TIME)\
        .expect('2_enter_burst_view_successful_checkpoing')

    def testDeleteBurstPics(self):
        """
        Summary:This case test delete burst pictures in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap trash icon -> delete,wait some seconds
          3. Get current burst picture count
          4. Verify if delete successful
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        #Tap trash icon twice,the fist tap try to activity the tool bar due to it is disappeared
        self._showUpOperations()
        self.touch(EXTRA_MENU)
        self.touch('3_delete_item.png', waittime=2)\
        .touch('4_delete_item_delete.png', waittime=2)
        #Step 3
        afterDeleteCount = self._getCount(fileType='burst')
        self.logger.debug("Before export burt pics to gallery, the count is : %s " % str(afterDeleteCount))
        #Step 4
        self.failUnless(afterDeleteCount == 0, 'Delete burst pics failed...')
    
    def _touchEgeInSingleView(self):
        self.touch((330, 90))
        self.touch((330, 90))
    def _touchThumbnailInMid(self):
        self.touch(EXTRA_MENU)
        self.touch(EXTRA_MENU)

    def testMenuKeyOfSync(self):
        """
        Summary:This case test rotate left burst pictures by menu key in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> Rotate left,check Rotate left progress pops up.
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        self._showUpOperations()
        self.press('menu')
        self.touch('3_social_sync_item.png')
        self.expect('2_enter_burst_view_successful_checkpoing')

    def testMenuKeyOfRotateLeft(self):
        """
        Summary:This case test rotate left burst pictures by menu key in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> Rotate left,check Rotate left progress pops up.
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        self.press('menu')\
        .touch('3_rotate_left_item.png')
        #.expect('4_rotate_left_process_dialog.png',interval=0.2,timeout=3)
        self.expect('2_enter_burst_view_successful_checkpoing')
    
    def testMenuKeyOfRotateRight(self):
        """
        Summary:This case test rotate right burst pictures by menu key in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> Rotate right,check Rotate right progress pops up.
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        self.press('menu')\
        .touch('3_rotate_right_item.png')
        self.expect('2_enter_burst_view_successful_checkpoing')
        #.expect('4_rotate_right_process_dialog.png',interval=0.2,timeout=3)
    
    def testMenuKeyOfTagSelected(self):
        """
        Summary:This case test Tag selected burst pictures by menu key in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> Tag selected -> Save,check Tagging picture progress pops up.
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        self.press('menu')\
        .touch('3_tag_selected_item.png')\
        .expect('4_tag_photo_screen.png', interval=1)\
        .touch('5_save_button.png')
        #.expect('6_togging_picture_precess.png',interval=0.2,timeout=3)
        
    def testMenuKeyOfConvert(self):
        """
        Summary:This case test rotate left burst pictures by menu key in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> convert -> animated - > convert -> save,check Rotate left progress pops up.
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        self.press('menu')\
        .touch('3_convert_item.png')\
        .touch('4_animated_item.png')\
        .touch('5_convert_button.png')\
        .sleep(20)\
        .touch('6_save_button.png')\
        .expect('2_enter_burst_view_successful_checkpoing')
        
    def testAddVenue(self):
        """
        Summary:This case test rotate left burst pictures by menu key in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> setting bar
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        self._showUpOperations()
	time.sleep(1)
        self.touch(SETTING_BAR)\
	.sleep(1)\
        .touch(SETTING_BAR)\
        .sleep(1)\
        .touch(VENUE)\
        .sleep(3)\
        .input('venue')\
        .touch('3_keyboard_done.png')\
        .expect('4_add_venue_successful.png')
        
    def testAddEvent(self):
        """
        Summary:This case test rotate left burst pictures by menu key in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> setting bar
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        self._showUpOperations()
        self.touch(SETTING_BAR)\
        .touch(SETTING_BAR)\
        .sleep(1)\
        .touch(EVENT)\
        .sleep(3)\
        .input('event')\
        .touch('3_keyboard_done.png')\
        .expect('4_add_event_successful.png')

    def testAddKeyword(self):
        """
        Summary:This case test rotate left burst pictures by menu key in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> setting bar -> add keyword
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        self._showUpOperations()
	time.sleep(1)
        self.touch(SETTING_BAR)\
	.sleep(1)\
        .touch(SETTING_BAR)
        
        self.drag((600,1130),(600,400),2,5)
        
        self.touch('3_add_keywords_icon.png')\
        .input('keyword')\
        .touch('3_keyboard_done.png')\
        .expect('4_add_successful.png')
        
        self.touch('delete_keyword.png')

    def testCheckDetails(self):
        """
        Summary:This case test rotate left burst pictures by menu key in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> setting bar -> add keyword
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        self._showUpOperations()
        self._showUpOperations()
        self.touch(SETTING_BAR)
        
        self.drag((600,1130),(600,400),2,5)
        self.sleep(2)
        
        if not self.exists('3_check_details.png'):
            self.fail("Check details failed!!!")

    def testSmallPlayBurstIconOfDissolveInEditView(self):
        """
        Summary:This case test paly burst pictures with Dissolve in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon -> Select all -> play burst icon -> Dissolve,wait some seconds.(Can not check during playing)
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        self._enterEditScreen()
        self.touch('4_selected_drop_down_menu.png')\
        .touch('5_selected_all_item.png')\
        .expect('6_selected_all_successful_checkpoing.png')\
        .touch('7_small_play_burst_icon.png')\
        .touch('8_dissolve_item.png')\
        .sleep(5)
    
    def testSmallPlayBurstIconOfFlashInEditView(self):
        """
        Summary:This case test paly burst pictures with Flash in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon -> Select all -> play burst icon -> Flash,wait some seconds.(Can not check during playing)
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        #Tap edit burst icon twice,the fist tap try to activity the tool bar due to it is disappeared
        self._enterEditScreen()
        self.touch('4_selected_drop_down_menu.png')\
        .touch('5_selected_all_item.png')\
        .expect('6_selected_all_successful_checkpoing.png')\
        .touch('7_small_play_burst_icon.png')\
        .touch('8_flash_item.png')\
        .sleep(5)
    
    def testSmallPlayBurstIconOfPageflipInEditView(self):
        """
        Summary:This case test paly burst pictures with Page flip in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon -> Select all -> play burst icon -> Page flip,wait some seconds.(Can not check during playing)
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        #Tap edit burst icon twice,the fist tap try to activity the tool bar due to it is disappeared
        self._enterEditScreen()
        self.touch('4_selected_drop_down_menu.png')\
        .touch('5_selected_all_item.png')\
        .expect('6_selected_all_successful_checkpoing.png')\
        .touch('7_small_play_burst_icon.png')\
        .touch('8_page_flip_item.png')\
        .sleep(20)

    def testRandomSelBusrtPicsExportToGalleryInEditView(self):
        """
        Summary:This case test random select some burst pictures export to gallery in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon twice to enter burst edit view
          3. Get random generated a number and related (x,y) coordinate
          4. Choose the selected pictures -> extra menu icon -> Export to gallery
          5. Check if export to gallery successful
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        #Tap edit burst icon twice,the fist tap try to activity the tool bar due to it is disappeared
        self._enterEditScreen()
        #.touch(EDIT_BUST_ICON_POINT)\
        self.expect('3_enter_burst_edit_view_checkpoint.png')
        #Step 3
        selected_pics_count, touch_points = self._getRandomSlectedPicsPoint()
        #Step 4
        for i in range(len(touch_points)):
            self.touch(touch_points[i])
        self.touch('4_extra_menu_icon.png')\
        .touch('5_export_to_gallery.png')\
        .sleep(3)
        #Step 5
        afterExportCount = self._getCount(fileType='other')
        self.logger.debug("Before export burt pics to gallery, the count is : %s " % str(afterExportCount))
        self.failUnless(afterExportCount == selected_pics_count, 'Export to gallery failed...')

    def testSelectAllBusrtPicsExportToGalleryInEditView(self):
        """
        Summary:This case test select all burst pictures export to gallery in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Get the burst picture count before export to gallery
          2. Launch Intel gallery and enter to burst view
          3. Tap edit burst icon twice to enter burst edit view, then select all -> extra menu icon -> Export to gallery, wait some seconds
          4. Get the NOT burt picture count after export to gallery
          5. Check if export to gallery successful
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        beforeExportCount = self._getCount(fileType='burst')
        self.logger.debug("Before export burt pics to gallery, the count is : %s " % str(beforeExportCount))
        #Step 2
        self._enterBurstView()
        #Step 3
        self._enterEditScreen()
        self.touch('3_selected_drop_down_menu.png')\
        .touch('4_selected_all_item.png')\
        .touch('5_extra_menu_icon.png')\
        .touch('6_export_to_gallery.png')\
        .sleep(3)
        #Step 4
        afterExportCount = self._getCount(fileType='other')
        self.logger.debug("After export burt pics to gallery, the count is : %s " % str(afterExportCount))
        #Step 5
        self.failUnless(afterExportCount == beforeExportCount, 'Export to gallery failed...')

    def testRandomSelBusrtPicsDeleteMarkedInEditView(self):
        """
        Summary:This case test random select some burst pictures delete marked in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Get the burst picture count before delete marked
          2. Launch Intel gallery and enter to burst view
          3. Tap edit burst icon twice to enter burst edit view
          4. Get random generated a number and related (x,y) coordinate
          5. Choose the selected pictures -> extra menu icon -> delete marked 
          6. Check if delete marked successful
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        beforeDelMarkedCount = self._getCount(fileType='burst')
        self.logger.debug("Before delete marked pics to gallery, the count is : %s " % str(beforeDelMarkedCount))
        #Step 2
        self._enterBurstView()
        #Step 3
        self._enterEditScreen()
        self.expect('3_enter_burst_edit_view_checkpoint.png')
        #Step 4
        selected_pics_count, touch_points = self._getRandomSlectedPicsPoint()
        #Step 5
        for i in range(len(touch_points)):
            self.touch(touch_points[i])
        self.touch('4_extra_menu_icon.png')\
        .touch('5_delete_marked_item.png')\
        .sleep(3)
        #Step 6
        afterDelMarkedCount = self._getCount(fileType='burst')
        self.logger.debug("After delete marked pics to gallery, the count is : %s " % str(afterDelMarkedCount))
        if (afterDelMarkedCount != 0):
            self.failUnless(afterDelMarkedCount == beforeDelMarkedCount - selected_pics_count , 'Delete  marked pics failed...')
        else:
            pass
    
    def testSelectAllBusrtPicsDeleteMarkedInEditView(self):
        """
        Summary:This case test select all burst pictures delete marked in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon twice to enter burst edit view, then select all -> extra menu icon -> delete marked, wait some seconds
          3. Verify the test result
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        self._enterEditScreen()
        self.touch('3_selected_drop_down_menu.png')\
        .touch('4_selected_all_item.png')\
        .touch('5_extra_menu_icon.png')\
        .touch('6_delete_marked_item.png')\
        .sleep(3)
        #Step 3
        self.failUnless(self._getCount(fileType='burst') == 0, 'Delete marked pics failed...')
    
    def testRandomSelBusrtPicsDeleteUnMarkedInEditView(self):
        """
        Summary:This case test random select some burst pictures delete unmarked in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Get the burst picture count before delete unmarked
          2. Launch Intel gallery and enter to burst view
          3. Tap edit burst icon twice to enter burst edit view
          4. Get random generated a number and related (x,y) coordinate
          5. Choose the selected pictures -> extra menu icon -> delete unmarked
          6. Check if delete unmarked successful
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        beforeDelUnMarkedCount = self._getCount(fileType='burst')
        self.logger.debug("Before delete marked pics to gallery, the count is : %s " % str(beforeDelUnMarkedCount))
        #Step 2
        self._enterBurstView()
        #Step 3

        self._enterEditScreen()
        self.expect('3_enter_burst_edit_view_checkpoint.png')
        #Step 4
        selected_pics_count, touch_points = self._getRandomSlectedPicsPoint()
        #Step 5
        for i in range(len(touch_points)):
            self.touch(touch_points[i])
        self.touch('4_extra_menu_icon.png')\
        .touch('5_delete_unmarked_item.png')\
        .sleep(3)
        #Step 6
        afterDelUnMarkedCount = self._getCount(fileType='burst')
        self.logger.debug("After delete marked pics to gallery, the count is : %s " % str(afterDelUnMarkedCount))
        self.failUnless(afterDelUnMarkedCount == selected_pics_count or afterDelUnMarkedCount == 0, 'Delete  marked pics failed...')

    def testSelectAllBusrtPicsDeleteUnMarkedInEditView(self):
        """
        Summary:This case test select all burst pictures export to gallery in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Get the burst pictures count before delete unmarked
          2. Launch Intel gallery and enter to burst view
          3. Tap edit burst icon twice to enter burst edit view, then select all -> extra menu icon -> delete unmarked, wait some seconds
          4. Get the burt pictures count after delete unmarked
          5. Check if delete unmarked successful
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        beforeDeleteUnMarkedCount = self._getCount(fileType='burst')
        self.logger.debug("Before delete unmarked burt pics, the count is : %s " % str(beforeDeleteUnMarkedCount))
        #Step 2
        self._enterBurstView()
        #Step 3

        self._enterEditScreen()
        self.touch('3_selected_drop_down_menu.png')\
        .touch('4_selected_all_item.png')\
        .touch('5_extra_menu_icon.png')\
        .touch('6_delete_unmarked_item.png')\
        .sleep(3)
        #Step 4
        afterDeleteUnMarkedCount = self._getCount(fileType='burst')
        self.logger.debug("After delete unmarked pics , the count is : %s " % str(afterDeleteUnMarkedCount))
        #Step 5
        self.failUnless(afterDeleteUnMarkedCount == beforeDeleteUnMarkedCount, 'Delete unmarked pics failed...')

    def testDeleteBusrtPicsInEditView(self):
        """
        Summary:This case test delete burst pictures in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon twice to enter burst edit view, then tap extra menu icon -> delete burst, wait some seconds
          3. Get the burst pictures after delete burst and check the result
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        #self.touch(THUMBNAIL_IN_FULLVIEW)
        #self.touch((450,584))

        self._enterEditScreen()
        self.touch('3_extra_menu_icon.png')\
        .touch('4_delete_burst_item.png')
        #Step 3
        afterDeleteBurstPics = self._getCount(fileType='burst')
        self.logger.debug("After delete burst pics, the count is : %s " % str(afterDeleteBurstPics))
        self.failUnless(afterDeleteBurstPics == 0, 'Delete burst pics failed...')

    def testRandomSelectBusrtPicsConvertInEditView(self):
        """
        Summary:This case test random select some burst pictures convert in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon twice to enter burst edit view
          3. Get random generated a number and related (x,y) coordinate
          4. Choose the selected pictures -> extra menu icon -> Convert marked
          5. Check if convert successful(1 image can not be converted)
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        #Tap edit burst icon twice,the fist tap try to activity the tool bar due to it is disappeared
        self._enterEditScreen()
        self.expect('3_enter_burst_edit_view_checkpoint.png')
        #Step 3
        selected_pics_count, touch_points = self._getRandomSlectedPicsPoint()
        #Step 4
        for i in range(len(touch_points)):
            self.touch(touch_points[i])
        self.touch('4_extra_menu_icon.png')\
        .touch('5_convert_marked_item.png')
        #Step 5
        if (selected_pics_count == 1):
            #1 image can not be converted
            pass
        else:
            self.expect('7_convert_photo_pops_up_checkpoint.png')

    def testSelectAllBusrtPicsConvertInEditView(self):
        """
        Summary:This case test select all burst pictures export to gallery in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon twice to enter burst edit view, then select all -> extra menu icon -> convert marked, check the result.
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        self._enterEditScreen()
        self.touch('3_selected_drop_down_menu.png')\
        .touch('4_selected_all_item.png')\
        .touch('5_extra_menu_icon.png')\
        .touch('6_convert_marked_item.png')\
        .expect('7_convert_photo_pops_up_checkpoint.png')

    def testSelectDeselectBurstPicsInEditView(self):
        """
        Summary:This case test select and deselect pictures in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon to enter the burst edit view, the select all check the result,deselect all check the result
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        #Tap edit burst icon twice,the fist tap try to activity the tool bar due to it is disappeared
        self._enterEditScreen()
        self.touch('3_selected_drop_down_menu.png')\
        .touch('4_selected_all_item.png')\
        .expect('5_selected_all_sucessful_checkpoint.png')\
        .touch('3_selected_drop_down_menu.png')\
        .touch('6_deselected_all_item.png')\
        .expect('7_deselected_all_sucessful_checkpoint.png')
        
    def testMarkUnmarkBurstPicsInEditView(self):
        """
        Summary:This case test mark and unmark pictures in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon to enter the burst edit view
          3. Mark the pictures
          4. Unmark the pictures.
        """
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        #Tap edit burst icon twice,the fist tap try to activity the tool bar due to it is disappeared
        self._enterEditScreen()
        #Step 3
        marked_point = [(30,200), (160, 200), (310, 200)]
        for i in range(len(marked_point)):
            self.touch(marked_point[i])
        self.expect('3_marked_pictures_checkpoint.png', similarity=0.8)
        #Step 4
        unmarked_point = [(30,200), (160, 200)]
        for i in range(len(unmarked_point)):
            self.touch(unmarked_point[i])
        self.expect('4_unmarked_pictures_checkpoint.png', similarity=0.8)
        
    def testTouchCheckMarkIcon(self):
        """
        Summary:This case test touch check mark icon back to upper level.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap check mark icon then check the result
        """  
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        #Step 2
        #Tap small play burst icon twice,the fist tap try to activity the tool bar due to it is disappeared
        self._enterEditScreen()

        self.touch('3_checkmark_icon.png')\
        .expect('2_enter_burst_view_successful_checkpoing.png', interval=1, timeout=3)
    
    def testPlayBurstPictures(self):
        #Precondtion
        self._checkResource()
        #Step 1
        self._enterBurstView()
        self.touch(PLAY_BURST_ICON_POINT)
        self.sleep(10)
        self.expect('2_enter_burst_view_successful_checkpoing.png')
    
    def _enterBurstView(self):
        '''
        Enter the burst view...
        By launch the activity -> tap (350 550) -> tap (350 700)
        '''
        self.launch(component=self.runSocialGalleryComponent)\
        .expect('0_launch_social_gallery_successful_checkpoint.png')
        self.adbCmdNoReturn('input tap 355 665')
        self.expect('1_enter_100ANDRO_folder_successful_checkpoint.png')
        self.adbCmdNoReturn('input tap 355 665')
        self.expect('2_enter_burst_view_successful_checkpoing', interval=5, timeout=15)

    def _getRandomSlectedPicsPoint(self):
        '''
        Get the selected picture count and related coordinates.
        '''
        #Define the coordinates.
        touch_point = [(30,200), (160, 200), (310, 200), (460, 200), (600, 200)]
        random_count = random.randint(1, 5)
        self.logger.debug("----------- %s ------------" % str(random_count))
        selected_point = random.sample(touch_point, random_count)
        return random_count, selected_point                                                                           
    
    def _showUpOperations(self):
	time.sleep(5)
        self.touch(PULLUP_CARD_POP_MENU_POINT)
	time.sleep(1)
        self.touch(PULLUP_CARD_POP_MENU_POINT)
	time.sleep(1)
        self.touch(PULLUP_CARD_POP_MENU_POINT)
        self.touch(PULLUP_CARD_POP_MENU_POINT)
        self.touch(PULLUP_CARD_POP_MENU_POINT)
        self.touch(PULLUP_CARD_POP_MENU_POINT)
    
    
    def _enterEditScreen(self):
        """
        Enter edit screen 
        """
        self._showUpOperations()
	time.sleep(1)
        self.touch(EDIT_BUST_ICON_POINT)
    
    def _checkResource(self, path=SDCARD_PATH + FOLDER_NAME, expectedAtLeastCount=5, expectCount=None):
        '''
        Check if the resource meet the condition, if not push the test material to the devices.
        
        @type path:string
        @param path: The path in the devices, default is /sdcard/DCIM/100ANDRO
        @type expectedAtLeastCount:int
        @param expectedAtLeastCount: expected at least burst pictures
        @type expectCount:int
        @param expectCount: expected burst pictures
        '''
        self.util._clearAllResource()
        self.util._deleteTestResource()

        if expectCount == None:    
            if (self._getCount(path, 'burst') < expectedAtLeastCount):
                
                self._pushMediaFiles(path)
                self.failIf(self._getCount(path, 'burst') < expectedAtLeastCount, 'Push bust media files...')
            else:
                self.logger.debug('Burst media files meet expected...')
    
            if (self._getCount(path, 'other') > 0):
                #commands.getoutput('adb shell rm -r ' + path + '/[!BST]*.jpg')
                self.adbCmdNoReturn('rm -r ' + path + '/[!B]*.jpg')
                self.adbCmdNoReturn(MEDIA_MOUNTED_SCAN_COMMAND)
                self.failIf(self._getCount(path, 'other') > 0, 'Remove redundant media files failed...')
            else:
                self.logger.debug('Current in the %s the redundant media files is 0...' % path)
        else:
            if (self._getCount(path, 'burst') != expectCount):
                self.adbCmdNoReturn('rm -r ' + path + '/[^B]*.jpg')
                self._pushMediaFiles(path)
                self.failIf(self._getCount(path, 'burst') < expectCount, 'Push bust media files...')
            else:
                pass

    def _pushMediaFiles(self, path=SDCARD_PATH + FOLDER_NAME):
        '''
        Can push the test materials(/gallery_JellyBean_FeatureTest/resource/testburstpics) to the device.
        
        @type path:string
        @param path: The path in the devices, default is /sdcard/DCIM/100ANDRO
        '''
        #if not fileType:
        self.logger.debug('Push media files...')
        #commands.getoutput('adb shell ls /sdcard/DCIM/100ANDRO')
        command ='adb push ' + sys.path[1] + '/gallery22_RHB_FT/resource/testburstpics ' + path
        commands.getoutput('adb push ' + sys.path[1] + '/gallery22_RHB_FT/resource/testburstpics ' + path)
        print command
        self.adbCmdNoReturn(MEDIA_MOUNTED_SCAN_COMMAND)
        self.sleep(3)

    def _getCount(self, path=SDCARD_PATH + FOLDER_NAME, fileType='burst'):
        '''
        Can get the burst pictures and NOT burst picture from the given path.
        
        @type path:string
        @param path: The path in the devices, default is /sdcard/DCIM/100ANDRO
        @type fileType: string
        @param fileType: Defined two: 'burst' and 'other'
        '''
        if (fileType == 'burst'):
            #mediaFilesCount = commands.getoutput('adb shell find ' + path + ' -name [B]*.jpg | wc -l')
            mediaFilesCount = commands.getoutput('adb shell find ' + path + ' -name [B]*.jpg | wc -l')
            self.logger.debug("Current Burst media account in %s is %s" % (path, mediaFilesCount))
            return int(mediaFilesCount)
        elif (fileType == 'other'):
            mediaFilesCount = commands.getoutput('adb shell find ' + path + ' -name [^B]*.jpg | wc -l')
            self.logger.debug("Current Not burst media account in %s is %s" % (path, mediaFilesCount))
            return int(mediaFilesCount)
        else:
            self.logger.debug("Wrong parameters.......")
    
    def _deleteFoldersInDCIM(self):
        picNo = commands.getoutput('adb shell ls -l /mnt/sdcard/DCIM/100ANDRO/ | grep IMG | wc -l')
        if picNo != 0:
            commands.getoutput('adb shell rm -r /mnt/sdcard/DCIM/100ANDRO/*')
        commands.getoutput(MEDIA_MOUNTED_SCAN_COMMAND)
    
    def _deleteConvertFile(self):
        """
        Delete Convert File in /sdcard/Sharing/
        """
        resultNO1 = commands.getoutput('adb shell ls -l /sdcard/ | grep Sharing | wc -l')
        if string.atoi(resultNO1) != 0:
            resultNO2 = commands.getoutput('adb shell ls -l /sdcard/Sharing/ | wc -l')
            if string.atoi(resultNO2) != 0 :
                commands.getoutput('adb shell rm -r /sdcard/Sharing/*')
        commands.getoutput(MEDIA_MOUNTED_SCAN_COMMAND) 
    
    def _clearAllResource(self):
        self.logger.debug('delete all pictures')
        self._deleteFoldersInDCIM()
        resultNO = commands.getoutput('adb shell ls -l /sdcard/ | grep test | wc -l')
        if string.atoi(resultNO) != 0 :
            commands.getoutput('adb shell rm -r /mnt/sdcard/test*')
        commands.getoutput(MEDIA_MOUNTED_SCAN_COMMAND)
        
        resultNO1 = commands.getoutput('adb shell ls -l /sdcard/ | grep 001 | wc -l')
        if string.atoi(resultNO1) != 0 :
            commands.getoutput('adb shell rm -r /mnt/sdcard/001')
        commands.getoutput(MEDIA_MOUNTED_SCAN_COMMAND)
        
        #delete /sdcard/Sharing/ Convert files
        self._deleteConvertFile()

    def tearDown(self):
        self.press('back,back,back,home')
        super(GalleryBurstViewTest, self).tearDown()
