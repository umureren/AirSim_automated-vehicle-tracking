#import setup_path
import airsim
import time

# Connect to the AirSim simulator
client = airsim.CarClient()
client.confirmConnection()

# Enable API control for Car1
client.enableApiControl(True, vehicle_name="Car1")

# Enable API control for Car2
client.enableApiControl(True, vehicle_name="Car11")

# Car controls for both cars
car_controls_car1 = airsim.CarControls()
car_controls_car2 = airsim.CarControls()

# Hedef konumu belirle
waypoint_x = -0.12
waypoint_y = 148.6
waypoint_y2 = 138.6

while True:
    # Car1 ve Car2'nin konumunu al
    car1_position = client.simGetVehiclePose(vehicle_name="Car1").position
    car2_position = client.simGetVehiclePose(vehicle_name="Car11").position

    # Hedef konuma olan mesafeyi hesapla
    distance_car1 = (((car1_position.x_val - waypoint_x) ** 2) + ((car1_position.y_val - waypoint_y) ** 2)) ** 0.5
    distance_car2 = (((car2_position.x_val - waypoint_x) ** 2) + ((car2_position.y_val - waypoint_y2) ** 2)) ** 0.5

    # Mesafeyi ekrana yazdır
    print(f"Car1 Hedef Konum Mesafesi: {distance_car1}")
    print(f"Car11 Hedef Konum Mesafesi: {distance_car2}")

    # Hedef konuma belirli bir mesafe yaklaşıldığında Car2'yi sağa döndür
    if distance_car2 < 3.0:
        car_controls_car2.throttle = 0.50
        car_controls_car2.steering = 1.0
        client.setCarControls(car_controls_car2, vehicle_name="Car11")
        time.sleep(1.96)
    else:
        # Hareket etmeye devam et
        car_controls_car2.throttle = 0.50
        car_controls_car2.steering = 0.0
        client.setCarControls(car_controls_car2, vehicle_name="Car11")
    
    # Hedef konuma belirli bir mesafe yaklaşıldığında Car1'i sağa döndür
    if distance_car1 < 3.9:
        car_controls_car1.throttle = 0.50
        car_controls_car1.steering = 1.0
        client.setCarControls(car_controls_car1, vehicle_name="Car1")
        time.sleep(1.96)
    else:
        # Hareket etmeye devam et
        car_controls_car1.throttle = 0.50
        car_controls_car1.steering = 0.0
        client.setCarControls(car_controls_car1, vehicle_name="Car1")

    time.sleep(0.1) 