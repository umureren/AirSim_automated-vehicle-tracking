import airsim
import cv2
import numpy as np

# AirSim istemcisini oluştur ve bağlan
client = airsim.CarClient()
client.confirmConnection()

# Araç isimleri
vehicles = [f"Car{i}" for i in range(2, 11)]
target_vehicle = "Car1"
CAM_NAME = "0"  # Kameranın adı
image_type = airsim.ImageType.Scene

# Kameraların ayarlarını yap
for vehicle in vehicles:
    client.enableApiControl(True, vehicle)
    client.armDisarm(True, vehicle)
    client.simSetDetectionFilterRadius(CAM_NAME, image_type, 200 * 100, vehicle_name=vehicle)
    client.simAddDetectionFilterMeshName(CAM_NAME, image_type, target_vehicle, vehicle_name=vehicle)

def get_images():
    images = []
    for vehicle in vehicles:
        raw_image = client.simGetImage(CAM_NAME, image_type, vehicle_name=vehicle)
        if not raw_image:
            continue
        image = cv2.imdecode(airsim.string_to_uint8_array(raw_image), cv2.IMREAD_UNCHANGED)
        images.append(image)
    return images

def cleanup():
    for vehicle in vehicles:
        client.simClearDetectionMeshNames(CAM_NAME, image_type, vehicle_name=vehicle)
        client.enableApiControl(False, vehicle)
        client.armDisarm(False, vehicle)
