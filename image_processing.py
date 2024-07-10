import cv2
import numpy as np

# Lacivert renk aralığını belirleyin (BGR formatında)
lower_navy = np.array([0, 0, 0])
upper_navy = np.array([255, 100, 100])

def get_average_color(image, box):
    """Verilen görüntüdeki kutu alanının ortalama rengini hesaplar."""
    x_min, y_min = int(box.min.x_val), int(box.min.y_val)
    x_max, y_max = int(box.max.x_val), int(box.max.y_val)
    region = image[y_min:y_max, x_min:x_max]
    average_color = cv2.mean(region)[:3]  # BGR formatında renk
    return average_color

def resize_images(images, new_width, new_height):
    """Görüntüleri yeni boyutlara göre yeniden boyutlandır."""
    resized_images = [cv2.resize(img, (new_width // 3, new_height // 3), interpolation=cv2.INTER_LINEAR) for img in images]
    row1 = np.hstack(resized_images[0:3])
    row2 = np.hstack(resized_images[3:6])
    row3 = np.hstack(resized_images[6:9])
    combined_image = np.vstack((row1, row2, row3))
    return combined_image
