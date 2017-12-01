
from time import sleep
import  RPi.GPIO as gpio
# car = Stepper([22,23,27,24],accel=100,speed=200)
class Stepper():
	def __init__(self,pin,accel= 100,speed= 200): # accel step/sencond^2, Speed step/second
		self.pin=pin
		self.dir1 = pin[0]
		self.pulse1=pin[1]
		self.dir2 = pin[2]
		self.pulse2=pin[3]
		self.timeAccel= 1/accel
		self.timeSpeed = 1/speed
	def _go(self):
		# hàm cơ bản cấp xung trực tiếp điều khiển
		time =  self.timeSpeed
		self.step = self.step*16 # sử dụng microstep 16 bước, xe chạy êm hơn 
		if self.step > 0:
			for i in range(0,self.step):
			#	if time > self.timeSpeed:
			#		time = time - self.timeAccel
				gpio.output(self.pulse1,1)
				gpio.output(self.pulse2,1)
				sleep(time)
				gpio.output(self.pulse1,0)
				gpio.output(self.pulse2,0)
				sleep(time)
		if self.step == 0:
			pass
	def goStraight(self,step=0):# step
		self.step = step
		gpio.setmode(gpio.BCM) # khởi tạo chân gpio
		gpio.setup(self.pin,gpio.OUT) # cấu hình các chân xuất tín hiệu điều khiển
		gpio.output(self.dir1,0) # xuất tín hiện low cho chân dir1
		gpio.output(self.dir2,1) # xuất tín hiệu high cho chân dir2
		self._go()
		gpio.cleanup() # đóng chân gpio
	def goBack(self,step = 0):
		self.step = step
		gpio.setmode(gpio.BCM)
		gpio.setup(self.pin,gpio.OUT)
		gpio.output(self.dir1,1)
		gpio.output(self.dir2,0)
		self._go()
		gpio.cleanup()
	def turnRight(self,step = 0):
		self.step = step
		gpio.setmode(gpio.BCM)
		gpio.setup(self.pin,gpio.OUT)
		gpio.output(self.dir1,0)
		gpio.output(self.dir2,0)
		self._go()
		gpio.cleanup()
	def turnLeft(self,step=0):
		self.step = step
		gpio.setmode(gpio.BCM)
		gpio.setup(self.pin,gpio.OUT)
		gpio.output(self.dir1,1)
		gpio.output(self.dir2,1)
		self._go()
		gpio.cleanup()
	def test(self,motor):# kiểm tra từng motor  bánh xe 
		gpio.setmode(gpio.BCM)
		gpio.setup(self.pin,gpio.OUT)
		if motor == 1 :
			gpio.output(self.dir1,1)
			for i in range(0,200):
				gpio.output(self.pulse1 ,1)
				sleep(0.005)
				gpio.output(self.pulse1,0)
				sleep(0.005)
			gpio.output(self.dir1,0)
			for i in range(0,200):
				gpio.output(self.pulse1,1)
				sleep(0.005)
				gpio.output(self.pulse1,0)
				sleep(0.005)
		if motor == 2:
			gpio.output(self.dir2,1)
			for i in range(0,200):
				gpio.output(self.pulse2,1)
				sleep(0.005)
				gpio.output(self.pulse2,0)
				sleep(0.005)
			gpio.output(self.dir2,0)
			for i in range(0,200):
				gpio.output(self.pulse2,1)
				sleep(0.005)
				gpio.output(self.pulse2,0)
				sleep(0.005)
		gpio.cleanup()

#car = Stepper([22,23,27,24])

