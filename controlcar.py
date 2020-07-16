import time
import os
import subprocess as call
import car
import camera

car = car.instanceCar()


def raw_input(content):
    return str(input(content))

if __name__ == "__main__":
    try:
        while True:
            #Get command from user
            os.system ("clear")
            print ("W = forward")
            print ("Z = background")
            print ("A = left")
            print ("D = right")
            print ("S = stop")

            print("t = take pictures")
            print("v = record video")

            command = raw_input("Enter command(Q to quit)")
            
            if (command == "w" or command == "W" ):
                car.moveForward()
                time.sleep(5)
                car.stop()
                continue
            elif (command == "a" or command == "A" ):
                car.spinLeft()
                time.sleep(5)
                car.stop()
                continue
            elif (command == "z" or command == "Z" ):
                car.moveBackground ()
                time.sleep (5)
                car.stop()
                continue
            elif (command == "d" or command == "D" ):
                car.spinRight()
                time.sleep(5)
                car.stop()
                continue
            elif (command == "s" or command == "S" ):
                car.stop()
                time.sleep(5)
                continue
            elif "q" == command or "Q" == command:
                car.stop()
                car.cleanup()
                break
            else:
                print("Enter Error")
                continue
            
  except (KeyboardInterrupt, SystemExit):
        car.stop()
        GPIO.clearup()
              