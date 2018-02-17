# Title        : Tarea2_Chris.py

from dronekit import connect, VehicleMode, LocationGlobalRelative, Command
import time
from pymavlink import mavutil
import Tkinter as tk

#



#este codigo regula la velocidad del drone

def set_velocity_body(vehicle, vx, vy, vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111, 
            0, 0, 0,        
            vx, vy, vz,     #
            0, 0, 0,        
            0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()
#conexion del drone
drone = connect('udp:127.0.0.1:14551', wait_ready=True)
#con este codigo el drone se eleva
def arm_and_takeoff(TargetAltitude):

    print("Executing takeoff")

    while not drone.is_armable:
        print("Vehicle is not armable, waiting...")
        time.sleep(1)

    print("ready to arm")
    drone.mode = VehicleMode("GUIDED")
    drone.armed = True
    while not drone.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print("Ready for takeoff, taking off...")
    drone.simple_takeoff(TargetAltitude)

    while True:
        Altitude = drone.location.global_relative_frame.alt
        print("altitude: ",Altitude)
        time.sleep(1)

        if Altitude >= TargetAltitude * 0.95:
            print("Altitude reached")
            break

#### your code here #####


#en este codigo, al oprimir las flehcas del teclado el drone se mueve de acuerdo a las flechas
def key(event):
    if event.char == event.keysym: #- - standard keys
        if event.keysym == 'r':
            drone.mode = VehicleMode("RTL")
            ### Add your code for what you want to happen when you press r #####
            
    else: #-- non standard keys
        if event.keysym == 'Up':
            set_velocity_body(drone,5,0,0)
            ### add your code for what should happen when pressing the up arrow ###
        elif event.keysym == 'Down':
            set_velocity_body(drone,-5,0,0)
            ### add your code for what should happen when pressing the down arrow ###
        elif event.keysym == 'Left':
            set_velocity_body(drone,0,-5,0)
            ### add your code for what should happen when pressing the Left arrow ###
        elif event.keysym == 'Right':
            set_velocity_body(drone,0,5,0)
            ### add your code for what should happen when pressing the Right arrow ###


### add your code to connect to the drone here ###

#este codigo marca cual es la altitud que alcanzara el drone
arm_and_takeoff(10)
 
#si se presiona r se cambia el modo a rtl
root = tk.Tk()
print(">> Control the drone with the arrow keys. Press r for RTL mode")
root.bind_all('<Key>', key)
root.mainloop()


