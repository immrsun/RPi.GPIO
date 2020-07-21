# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
//后轮驱动,前轮带转向舵机小车
class Car():
        def __init__(self, back_in1, back_in2, left_in3, right_in4, low_electrical_level, hight_electrical_level):
        GPIO.setwarnings(False)  //禁用运行警告(RuntimeWarning)
        GPIO.setmode(GPIO.BOARD) //设置引脚编号规则为BOARD
        
        self.back_in1 = back_in1
        self.back_in2 = back_in2
        self.back_ena = back_ena
        if self.back_ena > 0:
            GPIO.setup(self.back_ena, GPIO.OUT) //将back_ena号引脚设置成输出模式
        
        GPIO.setup(self.back_in1, GPIO.OUT)
        GPIO.setup(self.back_in2, GPIO.OUT)
                
        self.left_in3 = left_in3
        self.right_in4 = right_in4
        self.right_enb = right_enb
        
        
        GPIO.setup(self.left_in3, GPIO.OUT)
        GPIO.setup(self.right_in4, GPIO.OUT)
        if self.right_enb > 0:
            GPIO.setup(self.right_enb, GPIO.OUT)

        self.hight_electrical_level = hight_electrical_level
        self.low_electrical_level = low_electrical_level

    
    '''
    后轮驱动前进
    '''
    def lFoward(self):
        GPIO.output(self.back_in1, self.hight_electrical_level)
        GPIO.output(self.back_in2, self.low_electrical_level)
        if self.back_ena > 0:
            GPIO.output(self.back_ena, self.hight_electrical_level)
 

    '''
    后轮驱动后退
    '''
    def lBackward(self):
        GPIO.output(self.back_in1, self.low_electrical_level)
        GPIO.output(self.back_in2, self.hight_electrical_level)
        if self.back_ena > 0:
            GPIO.output(self.back_ena, self.hight_electrical_level)
    

    '''
    驱动轮子停止
    '''
    def lStop(self):
        if self.back_ena > 0:
            GPIO.output(self.back_ena, self.low_electrical_level)
        else:
            GPIO.output(self.back_in2, self.low_electrical_level)
            GPIO.output(self.back_in1, self.low_electrical_level)
            
    '''
    小车前进
    '''
    def moveForward(self):
        GPIO.output(self.back_in1, self.hight_electrical_level)
        GPIO.output(self.back_in2, self.low_electrical_level)
    
    '''
    小车后退
    '''
    def moveBackground(self):
        GPIO.output(self.back_in1, self.low_electrical_level)
        GPIO.output(self.back_in2, self.hight_electrical_level)
    
    '''
    小车左转
    '''
    def spinRight(self):
        GPIO.output(self.left_in3, self.hight_electrical_level)
        GPIO.output(self.right_in4, self.low_electrical_level)
    
    '''
    小车右转
    '''
    def spinLeft(self):
        GPIO.output(self.left_in3, self.low_electrical_level)
        GPIO.output(self.right_in4, self.hight_electrical_level)
    
    '''
    小车停止
    '''
    def stop(self):
        GPIO.output(self.back_in2, self.low_electrical_level)
        GPIO.output(self.back_in1, self.low_electrical_level)

    def cleanup(self):
        GPIO.cleanup()

def instanceCar():
    return Car(11, 13, 38, 40, 0, 1)