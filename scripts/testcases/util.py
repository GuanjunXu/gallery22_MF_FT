#!/usr/bin/env python
import unittest,string
import commands
import sys
from com.android.monkeyrunner import MonkeyRunner

product_name = 'gallery22_RHB_FT'

class Util:
    def __init__(self):
        pass
    
    def _deleteFoldersInDCIM(self):
        picNo = commands.getoutput('adb shell ls -l /mnt/sdcard/DCIM/100ANDRO/ | wc -l')
        if string.atoi(picNo) != 0:
            commands.getoutput('adb shell rm -r /mnt/sdcard/DCIM/100ANDRO/*')
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
    
    def _deleteConvertFile(self):
        """
        Delete Convert File in /sdcard/Sharing/
        """
        resultNO1 = commands.getoutput('adb shell ls -l /sdcard/ | grep Sharing | wc -l')
        if string.atoi(resultNO1) !=0:
            resultNO2 = commands.getoutput('adb shell ls -l /sdcard/Sharing/ | wc -l')
            if string.atoi(resultNO2) != 0 :
                commands.getoutput('adb shell rm -r /sdcard/Sharing/*')
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
        
    def _clearAllResource(self):
        self._deleteFoldersInDCIM()
        self._deleteTestResource()
        #delete /sdcard/Sharing/ Convert files
        self._deleteConvertFile()
    
    def _deleteTestResource(self):
        resultNO = commands.getoutput('adb shell ls -l /sdcard/ | grep test | wc -l')
        if string.atoi(resultNO) != 0 :
            commands.getoutput('adb shell rm -r /mnt/sdcard/test*')
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
    
    
    def _confirmResourceExists(self):
        """
        If not exists resource ,push the resource to sdcard
        """
        result = commands.getoutput('adb shell ls -l /sdcard/ | grep testalbum | wc -l')
        if string.atoi(result) == 0:
            self._clearAllResource()
            commands.getoutput('adb push ' + sys.path[1] + '/' + product_name +'/resource/testalbum/ ' + '/sdcard/testalbum')
            self.sleep(2)
        else:
            result1 = commands.getoutput('adb shell ls -l /sdcard/testalbum/test* | grep jpg | wc -l')
            if string.atoi(result1) != 40 :
                self._clearAllResource()
                commands.getoutput('adb push ' + sys.path[1] + '/' + product_name + '/resource/testalbum/ ' + '/sdcard/testalbum')
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard/')
        
    def _pushResourcesVideo(self):
        result2 = commands.getoutput('adb shell ls -l /sdcard/testvideo/ | grep 3gp | wc -l')
        if string.atoi(result2) == 0:
            commands.getoutput('adb push ' + sys.path[1] + '/' + product_name + '/resource/testvideo/ '+'/sdcard/testvideo')
            self.sleep(2)
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
    
    def _push1Picture(self):
        result = commands.getoutput('adb shell ls -l /sdcard/ | grep test | wc -l')
        resultNO = commands.getoutput('adb shell ls -l /sdcard/testpic1/ | grep jpg | wc -l')
        if string.atoi(result) != 1 :
            self._clearAllResource()
            commands.getoutput('adb push ' + sys.path[1] + '/' + product_name + '/resource/testpic1/ ' + '/sdcard/testpic1')
        elif string.atoi(resultNO) != 1:
            self._clearAllResource()
            commands.getoutput('adb push ' + sys.path[1] + '/' + product_name + '/resource/testpic1/ ' + '/sdcard/testpic1')
            
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
        
    def _pushConvertPicture(self):
        resultNO = commands.getoutput('adb shell ls -l /sdcard/testConvertPics/ | grep jpg | wc -l')
        if string.atoi(resultNO) == 0 :
            commands.getoutput('adb push ' + sys.path[1] + '/' + product_name + '/resource/testConvertPics/ ' + '/sdcard/testConvertPics')
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
    
    def _enterSingleView(self):
        commands.getoutput('adb shell input tap 355 706')
        self.sleep(2)
        commands.getoutput('adb shell input tap 355 706')
        self.sleep(3)
        
    def _enterGridView(self):
        commands.getoutput('adb shell input tap 355 706')
        self.sleep(2)
    
    def _discardGmailDraft(self):
        self.press('menu')
        self.touch('gmail_discard.png')
        self.touch('gmail_discard_OK.png')
    
    def _prepareVideo(self):
        resultNO = commands.getoutput('adb shell ls -l /sdcard/ | grep test | wc -l')
        if string.atoi(resultNO) != 1:
            self._clearAllResource()
            commands.getoutput('adb push ' + sys.path[1] + '/' + product_name + '/resource/testvideo/ ' + '/sdcard/testvideo')
            commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
        else:
            resultNo1 = commands.getoutput('adb shell ls -l /sdcard/ | grep testvideo | wc -l')
            if string.atoi(resultNo1) != 1:
                self._clearAllResource()
                commands.getoutput('adb push ' + sys.path[1] + '/' + product_name + '/resource/testvideo/ ' + '/sdcard/testvideo')
                commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
    
    def _checkBurstResource(self):
        self._deleteConvertFile()
        self._deleteTestResource()
        resultNO = commands.getoutput('adb shell ls -l /sdcard/DCIM/100ANDRO/ | wc -l')
        resultNO1 = commands.getoutput('adb shell ls -l /sdcard/DCIM/100ANDRO/ | grep BST | wc -l')
        if string.atoi(resultNO) != string.atoi(resultNO1):
            self._clearAllResource()
            commands.getoutput('adb push ' + sys.path[1] + '/' + product_name + '/resource/testburstpics/ ' + '/sdcard/DCIM/100ANDRO/')
            commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
        elif string.atoi(resultNO1) != 10 :
            self._clearAllResource()
            commands.getoutput('adb push ' + sys.path[1] + '/' + product_name + '/resource/testburstpics/ ' + '/sdcard/DCIM/100ANDRO/')
            commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
        self.sleep(5)
    
    def _getBurstPicturesNum(self):
        result = commands.getoutput('adb  shell ls -l /sdcard/DCIM/100ANDRO/ | grep BST | wc -l')
        return result
    
    def _getPictureNumber(self):
        result = commands.getoutput('adb shell ls -l /sdcard/test*/* | grep IM | wc -l')
        return result
        
    def _getConvertFileNum(self):
        """
        Get convert file number
        """
        result = commands.getoutput('adb shell ls /sdcard/Sharing/| wc -l')
        return result 
    
    def _getPictureNoInAndro(self):
        no = commands.getoutput('adb shell ls -l /mnt/sdcard/DCIM/100ANDRO/ | wc -l')
        return no
     
    def _clearCache(self):
        commands.getoutput('adb shell pm clear com.intel.android.gallery3d')
        
    def sleep(self,tsec):
        MonkeyRunner.sleep(tsec)
        return self
