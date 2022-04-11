import RPi.GPIO as GPIO
import time
from pin_dic import pin_dic

class RGB_LED(object):
    def __init__(self,pin_R,pin_G,pin_B):
        self.pins = [pin_R,pin_G,pin_B]
        
        # 设置为输出引脚，初始化第电平，灯灭
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)   
            GPIO.output(pin, GPIO.LOW)
            
        # 设置三个引脚为pwm对象，频率2000
        self.pwm_R = GPIO.PWM(pin_R, 2000)  
        self.pwm_G = GPIO.PWM(pin_G, 2000)
        self.pwm_B = GPIO.PWM(pin_B, 2000)
    
        # 初始占空比为0
        self.pwm_R.start(0)      
        self.pwm_G.start(0)
        self.pwm_B.start(0)

    def color2ratio(self,x,min_color,max_color,min_ratio,max_ratio):
        return (x - min_color) * (max_ratio - min_ratio) / (max_color - min_color) + min_ratio

    def setColor(self,col):
        R_val,G_val,B_val = col
   
        R =self.color2ratio(R_val, 0, 255, 0, 100)
        G =self.color2ratio(G_val, 0, 255, 0, 100)
        B =self.color2ratio(B_val, 0, 255, 0, 100)
        # 改变占空比
        self.pwm_R.ChangeDutyCycle(R)     
        self.pwm_G.ChangeDutyCycle(G)
        self.pwm_B.ChangeDutyCycle(B)
        
    def destroy(self):    
        self.pwm_R.stop()
        self.pwm_G.stop()
        self.pwm_B.stop()
        for pin in self.pins:
            GPIO.output(pin, GPIO.HIGH)    
        GPIO.cleanup()

if __name__ == "__main__":

    # 设置引脚编号模式
    GPIO.setmode(GPIO.BOARD)
    
    # 定义三个引脚 
    pin_R = pin_dic['G17']
    pin_G = pin_dic['G16']
    pin_B = pin_dic['G13']
    
    # 定义 RGB_LED 对象
    m_RGB_LED = RGB_LED(pin_R,pin_G,pin_B)
    
    # 定义显示的颜色（R，G，B）
    colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,197,204),(192,255,62),(148,0,211),(118,238,00)];
    
    # 循环显示各种颜色
    try:
        while True:
            for col in colors:
                # 打印颜色
                print(col)
                # 设置颜色
                m_RGB_LED.setColor(col)
                # 延时
                time.sleep(3)
    except KeyboardInterrupt:
        print('\n Ctrl + C QUIT')   
    finally:
        m_RGB_LED.destroy()

    
    
    
   