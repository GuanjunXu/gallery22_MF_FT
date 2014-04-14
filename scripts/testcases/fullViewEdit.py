#!/usr/bin/env python
import unittest,string
import gallery22_RHB_FT.cases.util

PACKAGE_NAME = 'com.intel.android.gallery3d'
ACTIVITY_NAME = PACKAGE_NAME + '.app.Gallery'

HIGHEST_BRIGHTNESS = (636,830)
LOWEST_BRIGHTNESS = (36,830)
CROP_SETTING = (80,1000)
EDIT_MODE_RIGHT_MOST = (708,1000)
EDIT_MODE_LEFT_MOST = (23,1000)

class FullViewEditTest(unittest.TestCase):
    def setUp(self):
        super(FullViewEditTest,self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        self.util = gallery22_RHB_FT.cases.util.Util()
        self.util._confirmResourceExists()
        
    def _launchGallery(self):
        """
        method: launchgallery app.
        """
        self.launch(component=self.runComponent)\
        .expect('0_launchgallery_checkpoint.png',interval=2,timeout=4)
    
    def testEnterEditScreen(self):
        """
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
        """
        #Step 1
        self._launchGallery()
        
        #Step 2
        self.util._enterSingleView()
        
        self._enterEditScreen()
        self.expect('4_edit_screen.png')
    
    def testEditWithToneNone(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch toning icon
              5.Touch none mode
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self._enterEditScreen()
        
        self.touch('5_tone_icon.png')
        self.touch(('6_none_icon.png'))
        self._cropAndSavePicture(0)
        
    def testEditWithTonePunch(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch toning icon
              5.Touch punch mode
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self._enterEditScreen()
        
        self.touch('5_tone_icon.png')
        self.touch(('6_punch_icon.png'))
        self._cropAndSavePicture(1)
        
    def testEditWithTonePunchRedoAndUndo(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch toning icon
              5.Touch punch mode
              6.Touch undo
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self._enterEditScreen()
        beforePicNo = self.util._getPictureNumber()
        
        self.touch('5_tone_icon.png')
        self.touch(('6_punch_icon.png'))
        self.press('menu')
        self.touch('7_undo.png')
        self.press('menu')
        self.touch('8_redo.png')
        #self.drag((700,600),(20,600),4,6)
        #self.expect('8_history_list.png')
        
        afterPicNo = self.util._getPictureNumber()
        self.failIf(beforePicNo != afterPicNo,'Edit picture then undo failed!!!')
        
    def testEditWithTonePunchReset(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch toning icon
              5.Touch punch mode
              6.Touch reset
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self._enterEditScreen()
        beforePicNo = self.util._getPictureNumber()
        
        self.touch('5_tone_icon.png')
        self.touch(('6_punch_icon.png'))
        self.press('menu')
        self.touch('7_reset.png')
        #self.drag((700,600),(20,600),4,6)
        #self.expect('8_history_list.png')
        afterPicNo = self.util._getPictureNumber()
        self.failIf(beforePicNo != afterPicNo,'Enter edit screen failed!!!')        

        
    def testEditWithTonePunchShowHistory(self):
        """
        Summary:Enter enter interface select a mode and click Show history  
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch toning icon
              5.Touch punch
              6.Touch setting menu
              7.Touch Show History
              8.Touch Save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self._enterEditScreen()
        self.touch('5_tone_icon.png')
        self.touch(('6_punch_icon.png'))
        self.press('menu')
        self.touch('7_show_history.png')
        self.expect('8_history_list.png')
        self.touch('9_reset.png')
    
    def testEditWithToneVintage(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch toning icon
              5.Touch vintage mode
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self._enterEditScreen()
        
        self.touch('5_tone_icon.png')
        self.touch(('6_vintage_icon.png'))
        self._cropAndSavePicture(1)

    def testEditWithToneBW(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch toning icon
              5.Touch BW mode
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self._enterEditScreen()
        
        self.touch('5_tone_icon.png')
        self.touch(('6_BW_icon.png'))
        self._cropAndSavePicture(1)

    def testEditWithToneBleach(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch toning icon
              5.Touch Bleach mode
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self._enterEditScreen()
        
        self.touch('5_tone_icon.png')
        self.touch(('6_bleach_icon.png'))
        self._cropAndSavePicture(1)     

    def testEditWithToneInstant(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch toning icon
              5.Touch Instant mode
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self._enterEditScreen()
        
        self.touch('5_tone_icon.png')
        self.drag((708,1000),(23,1000),4,6)
        self.touch(('6_intant_icon.png'))
        self._cropAndSavePicture(1)


    def testEditWithToneLatte(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch toning icon
              5.Touch Latte mode
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self._enterEditScreen()
        
        self.touch('5_tone_icon.png')
        self.drag((708,1000),(23,1000),4,6)
        self.touch(('6_latte_icon.png'))
        self._cropAndSavePicture(1)
        
    def testEditWithToneBlue(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch toning icon
              5.Touch Blue mode
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self._enterEditScreen()
        
        self.touch('5_tone_icon.png')
        self.drag((708,1000),(23,1000),4,6)
        self.touch(('6_blue_icon.png'))
        self._cropAndSavePicture(1)
        

    def testEditWithToneLitho(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch toning icon
              5.Touch Litho mode
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self._enterEditScreen()
        
        self.touch('5_tone_icon.png')
        self.drag((708,1000),(23,1000),4,6)
        self.drag((708,1000),(23,1000),4,6)
        self.touch(('6_litho_icon.png'))
        self._cropAndSavePicture(1)
        

    def testEditWithToneXProcess(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch toning icon
              5.Touch XProcess mode
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        self._enterEditScreen()
        
        self.touch('5_tone_icon.png')
        self.drag((708,1000),(23,1000),4,6)
        self.drag((708,1000),(23,1000),4,6)
        self.touch(('6_xprocess_icon.png'))
        self._cropAndSavePicture(1)
        
    def testEditWithFrame1(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch frame icon
              5.Touch  first style
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        
        #Step 4
        self.touch('5_frame_icon.png')
        
        #Step 5
        self.touch((80+130*0,1000))
        
        #Step 6
        self._cropAndSavePicture(0)
        
        
    def testEditWithFrame2(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch frame icon
              5.Touch  2th style
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        
        #Step 4
        self.touch('5_frame_icon.png')
        
        #Step 5
        self.touch((80+130*1,1000))
        
        #Step 6
        self._cropAndSavePicture(1)
        
        
    def testEditWithFrame3(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch frame icon
              5.Touch  3th style
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        
        #Step 4
        self.touch('5_frame_icon.png')
        
        #Step 5
        self.touch((80+130*2,1000))
        
        #Step 6
        self._cropAndSavePicture(1)
        
        
    def testEditWithFrame4(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch frame icon
              5.Touch  4th style
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        
        #Step 4
        self.touch('5_frame_icon.png')
        
        #Step 5
        self.touch((80+130*3,1000))
        
        #Step 6
        self._cropAndSavePicture(1)        
        
    def testEditWithFrame5(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch frame icon
              5.Touch  5th style
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        
        #Step 4
        self.touch('5_frame_icon.png')
        
        #Step 5
        self.touch((80+130*4,1000))
        
        #Step 6
        self._cropAndSavePicture(1)

        
    def testEditWithFrame6(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch frame icon
              5.Touch  6th style
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        
        #Step 4
        self.touch('5_frame_icon.png')
        
        #Step 5
        self.drag((708,1000),(23,1000),4,6)
        self.touch((80+130*3,1000))
        
        #Step 6
        self._cropAndSavePicture(1)       
        
        
    def testEditWithFrame7(self):
        """
        Summary:Enter toning interface with selected none mode 
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch frame icon
              5.Touch  7th style
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('5_frame_icon.png')
        
        #Step 5
        self.drag((708,1000),(23,1000),4,6)
        self.touch((80+130*4,1000))
        
        #Step 6
        self._cropAndSavePicture(1)  
    
    
    def testEnterCropScreen(self):
        """
        Summary:Enter Crop interface
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Crop icon
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_crop_icon.png')
        self.expect('5_crop_screen.png')
        
        
    def testEditWithCropStraighten(self):
        """
        Summary:Enter Crop interface with selected straighten mode
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Crop icon
              5.Touch straighten mode
              6.Apply one positive straightening adjustment
              7.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_crop_icon.png')
        self.touch('5_straighten_icon.png')
        
        self.drag((600,700),(100,700),4,6)
        #self.expect('6_apply_straighten_posi45.png')
        self._cropAndSavePicture(1)
    
    def testEditWithCropWith1ratio1(self):
        """
        Summary:Enter Crop interface with selected Crop mode
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Crop icon
              5.Touch Crop mode and select 1:1 option
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_crop_icon.png')
        self.touch('5_crop_option.png')
        
        #Step 5 
        self.touch(CROP_SETTING)
        self.expect('6_modelist.png')
        self.touch('7_1_rotate_1.png')
        #Step 6
        self._cropAndSavePicture(1)
        
    
    def testEditWithCropWith4ratio3 (self):
        """
        Summary:Enter Crop interface with selected Crop mode
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Crop icon
              5.Touch Crop mode and select 4:3 option
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_crop_icon.png')
        self.touch('5_crop_option.png')
        
        #Step 5 
        self.touch(CROP_SETTING)
        self.expect('6_modelist.png')
        self.touch('7_4_rotate_3.png')
        
        #Step 6
        self._cropAndSavePicture(1)
        
    def testEditWithCropWith3ratio4 (self):
        """
        Summary:Enter Crop interface with selected Crop mode
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Crop icon
              5.Touch Crop mode and select 4:3 option
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_crop_icon.png')
        self.touch('5_crop_option.png')
        
        #Step 5 
        self.touch(CROP_SETTING)
        self.expect('6_modelist.png')
        self.touch('7_3_rotate_4.png')
        
        #Step 6
        self._cropAndSavePicture(1)

        
    def testEditWithCropWith5ratio7 (self):
        """
        Summary:Enter Crop interface with selected Crop mode
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Crop icon
              5.Touch Crop mode and select 4:3 option
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_crop_icon.png')
        self.touch('5_crop_option.png')
        
        #Step 5 
        self.touch(CROP_SETTING)
        self.expect('6_modelist.png')
        self.touch('7_5_rotate_7.png')
        
        #Step 6
        self._cropAndSavePicture(1)        
        
    def testEditWithCropWith7ratio5 (self):
        """
        Summary:Enter Crop interface with selected Crop mode
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Crop icon
              5.Touch Crop mode and select 4:3 option
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_crop_icon.png')
        self.touch('5_crop_option.png')
        
        #Step 5 
        self.touch(CROP_SETTING)
        self.expect('6_modelist.png')
        self.touch('7_7_rotate_5.png')
        
        #Step 6
        self._cropAndSavePicture(1)
        
    def testEditWithCropWithNone (self):
        """
        Summary:Enter Crop interface with selected Crop mode
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Crop icon
              5.Touch Crop mode and select 4:3 option
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_crop_icon.png')
        self.touch('5_crop_option.png')
        
        #Step 5 
        self.touch(CROP_SETTING)
        self.expect('6_modelist.png')
        self.touch('7_none.png')
        
        #Step 6
        self._cropAndSavePicture(0)
        
    def testEditWithCropWithOriginal (self):
        """
        Summary:Enter Crop interface with selected Crop mode
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Crop icon
              5.Touch Crop mode and select 4:3 option
              6.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        self.sleep(3)
        #Step 4
        self.touch('4_crop_icon.png',waittime=2)
        self.touch('5_crop_option.png')
        
        #Step 5 
        self.touch(CROP_SETTING)
        self.expect('6_modelist.png')
        self.touch('7_original.png',waittime=2)
        
        #Step 6
        self._cropAndSavePicture(0)     
        
        
    def testEditWithCropWithRotate(self):
        """
        Summary:Enter Crop interface with selected Rotate mode
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Crop icon
              5.Touch Rotate mode
              6.Apply rotate 0
              7.Exit socialgallery app
        
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_crop_icon.png')
        self.touch('5_rotate_icon.png')
        #self.expect('6_apply_rotate0.png')
        self.drag((600,700),(100,700),4,6)
        #self.expect('7_rotate90.png')
        self._cropAndSavePicture(1)
    
        
    def testEditWithCropWithMirror(self):
        """
        Summary:Enter Crop interface with selected Mirror mode
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Crop icon
              5.Touch Mirror mode
              6.Drag screen from left to right
              7.Touch save icon
        
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_crop_icon.png')
        self.touch('5_mirror_icon.png')
        self.drag((600,700),(100,700),4,6)
        self._cropAndSavePicture(1)
        
        
    def testEditWithBrightnessWithAutocolor(self):
        """
        Summary:Enter Brightness interface
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Brightness icon
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_brightness_icon.png')
        self.touch('5_autocolor_icon.png')
        self._cropAndSavePicture(0)

        
    def testEditWithBrightnessWithExposure(self):
        """
        Summary:Enter Brightness interface
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Brightness icon
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_brightness_icon.png')
        self.touch('5_exposure.png')
        #self.expect('6_exposure_posi99.png')
        self.touch(HIGHEST_BRIGHTNESS)
        self._cropAndSavePicture(1)
        
        
    def testEditWithBrightnessWithHue(self):
        """
        Summary:Enter Brightness interface
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Brightness icon
              5.Touch Hue mode
              6.Apply Hue for positive straightening
              7.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_brightness_icon.png')
        self.drag(EDIT_MODE_RIGHT_MOST,EDIT_MODE_LEFT_MOST,4,6)
        self.drag(EDIT_MODE_RIGHT_MOST,EDIT_MODE_LEFT_MOST,4,6)
        self.touch('5_hue.png')
        #self.expect('6_hue_posi.png')
        self.touch(HIGHEST_BRIGHTNESS)
        self._cropAndSavePicture(1)
    
    def testEditWithBrightnessWithSaturation(self):
        """
        Summary:Enter Brightness interface
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Brightness icon
              5.Touch saturation mode
              6.Apply saturation for positive straightening
              7.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_brightness_icon.png')
        self.drag(EDIT_MODE_RIGHT_MOST,EDIT_MODE_LEFT_MOST,4,6)
        self.drag(EDIT_MODE_RIGHT_MOST,EDIT_MODE_LEFT_MOST,4,6)
        self.touch('5_saturation.png')
        #self.expect('6_saturation_posi.png')
        self.touch(HIGHEST_BRIGHTNESS)
        self._cropAndSavePicture(1)
    
    def testEditWithBrightnessWithBW(self):
        """
        Summary:Enter Brightness interface
        Initial:Make sure there are not less than 1 photo in gallery
        Steps:1.Enter full view
              2.Click setting menu
              3.Touch edit
              4.Touch Brightness icon
              5.Touch bw filter mode
              6.Apply bw filter for negative straightening
              7.Touch save
        """
        #Step 1
        self._launchGallery()
        #Step 2
        self.util._enterSingleView()
        #Step 3
        self._enterEditScreen()
        #Step 4
        self.touch('4_brightness_icon.png')
        self.drag(EDIT_MODE_RIGHT_MOST,EDIT_MODE_LEFT_MOST,4,6)
        self.drag(EDIT_MODE_RIGHT_MOST,EDIT_MODE_LEFT_MOST,4,6)
        self.touch('5_bwfilter.png')
        #self.expect('6_bwfilter_posi.png')
        self.touch(HIGHEST_BRIGHTNESS)
        self._cropAndSavePicture(1)

        
    def _cropAndSavePicture(self,no):
        """
        Crop and Save picture
        """
        beforePicNo = self.util._getPictureNumber()
        self.touch('SAVE_icon.png',similarity=0.6)
        afterPicNo = self.util._getPictureNumber()
        self.failIf(string.atoi(beforePicNo) != string.atoi(afterPicNo)-no,'Edit picture with crop  failed!!!')  
    
    
    def _enterEditScreen(self):
        """
        Enter edit screen by touch menu option
        """
        self.press('menu')
        self.touch('1_edit_option.png')
        if self.exists('2_choose_an_action.png'):
            self.touch('3_socialgallery_icon.png',waittime=3)

    def tearDown(self):
        self.press('back,back,back,back,home')
        super(FullViewEditTest,self).tearDown()
