import cv2
import time
import matplotlib.pyplot as plt
import module1
import image_processing as ip
import graph_processing as gp

cv2.namedWindow("Car Detection from Multiple Vehicles", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Car Detection from Multiple Vehicles", 1920, 1080)

selected_camera = None
selected_time = None
highlight_duration = 6  # Süre: 6 saniye

def on_mouse(event, x, y, flags, param):
    global selected_camera, selected_time
    if event == cv2.EVENT_LBUTTONDOWN:
        col_width = 1920 // 3
        row_height = 1080 // 3
        col = x // col_width
        row = y // row_height
        index = row * 3 + col
        if index < len(module1.vehicles):
            selected_camera = module1.vehicles[index]
            selected_time = time.time()
            print(f"Selected Camera: {selected_camera}")

cv2.setMouseCallback("Car Detection from Multiple Vehicles", on_mouse)

while True:
    images = module1.get_images()
    if len(images) == 9:
        window_width = cv2.getWindowImageRect("Car Detection from Multiple Vehicles")[2]
        window_height = cv2.getWindowImageRect("Car Detection from Multiple Vehicles")[3]
        combined_image = ip.resize_images(images, window_width, window_height)

        if selected_camera:
            current_time = time.time()
            elapsed_time = current_time - selected_time
            if elapsed_time < highlight_duration:
                selected_neighbors = list(gp.G.neighbors(selected_camera))
                for vehicle in module1.vehicles:
                    if vehicle == selected_camera or vehicle in selected_neighbors:
                        index = module1.vehicles.index(vehicle)
                        row = index // 3
                        col = index % 3
                        start_x = col * (window_width // 3)
                        start_y = row * (window_height // 3)
                        end_x = start_x + (window_width // 3)
                        end_y = start_y + (window_height // 3)
                        cv2.rectangle(combined_image, (start_x, start_y), (end_x, end_y), (255, 0, 0), 10)

        cv2.imshow("Car Detection from Multiple Vehicles", combined_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

module1.cleanup()
cv2.destroyAllWindows()
