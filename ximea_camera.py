from ximea import xiapi
import cv2
from ctypes import *

### runn this command first echo 0|sudo tee /sys/module/usbcore/parameters/usbfs_memory_mb  ###

# create instance for first connected camera
cam = xiapi.Camera()

# start communication
# to open specific device, use:
# cam.open_device_by_SN('41305651')
# (open by serial number)
print('Opening first camera...')
# settings
cam.set_exposure(10000)
cam.set_param('imgdataformat', "XI_RGB32")
cam.set_param("auto_wb", 1)
print('Exposure was set to %i us' % cam.get_exposure())

# create instance of Image to store image data and metadata
img = xiapi.Image()

# start data acquisition
print('Starting data acquisition...')
cam.start_acquisition()

counter = 0

while counter != 15:
    cam.get_image(img)
    image = img.get_image_data_numpy(invert_rgb_order=True)
    image = cv2.resize(image, (600, 600))
    cv2.imshow("test", image)
    key = cv2.waitKey(1)

    if key == ord(' '):
        print("Hej")
        filename = "image{}.jpg".format(counter)
        cv2.imwrite(filename, image)
        counter += 1
        print("Saved image to {}".format(filename))
    elif key == ord('q'):
        break



# stop data acquisition
print('Stopping acquisition...')
cam.stop_acquisition()

# stop communication
cam.close_device()

print('Done.')