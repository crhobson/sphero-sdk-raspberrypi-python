import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import time

from sphero_sdk import SpheroRvrObserver

rvr = SpheroRvrObserver()


def on_color_detected(red, green, blue, confidence, colorClassification):
    print('Color detected: ', red, green, blue, confidence, colorClassification)


def main():
    """ This program uses the color sensor on RVR (located on the down side of RVR, facing the floor) to report colors detected.

    """
    rvr.wake()

    # Give RVR time to wake up
    time.sleep(2)

    # Register handler to be called when message is received
    rvr.on_color_detection_notify(handler=on_color_detected)

    rvr.enable_color_detection(enable=True)

    # Color detection is reported at 100 ms intervals. Handler is called only if color is detected with
    # confidence level  0 or above
    rvr.enable_color_detection_notification(enable=True, interval=100, minimum_confidence_threshold=0)

    time.sleep(5)

    rvr.close()


main()
