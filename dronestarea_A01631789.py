from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

#Con este codigo lograre encender el drone y elevarlo
def arm_and_takeoff(TargetAltitude):
	print("Executing takeoff")

	while not drone.is_armable:
		print("Vehicle is not armable, waiting....")
		time.sleep(1)

	print("ready to arm")
	drone.mode = VehicleMode("GUIDED")
	drone.armed = True
	while not drone.armed:
		print("Waiting for arming....")
		time.sleep(1)

	print("Ready for takooff, taking off...")
	drone.simple_takeoff(TargetAltitude)

	while True:
		Altitude = drone.location.global_relative_frame.alt
		print("altitude: ",Altitude)
		time.sleep(1)

		if Altitude >= TargetAltitude * 0.95:
			print("Altitude reached")
			break

#se genera una conexion con la computadora
drone = connect('127.0.0.1:14551', wait_ready=True)
arm_and_takeoff(20)

#latitud, altitud y coordenadas de mi vuelo
drone.airspeed = 10
a_location = LocationGlobalRelative(20.736273,-103.456900,25)
b_location = LocationGlobalRelative(20.735873,-103.456906,25)
c_location = LocationGlobalRelative(20.735945,-103.457458,25)


print("Se mueve al punto a")
drone.simple_goto(a_location)
time.sleep(25)
print("Se mueve al punto b")
drone.simple_goto(b_location)
time.sleep(25)
print("Se mueve al punto c")
drone.simple_goto(c_location)
time.sleep(25)

#regresa a su lugar de origen
drone.mode = VehicleMode("RTL")

#es la bateria
print(drone.batery.level,"v")