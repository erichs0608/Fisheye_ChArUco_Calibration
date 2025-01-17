from calibration import CharucoCalibrator
import cv2
import os


ARUCO_DICT = cv2.aruco.DICT_5X5_100
SQUARES_VERTICALLY = 12
SQUARES_HORIZONTALLY = 9
SQUARE_LENGTH = 0.06
MARKER_LENGTH = 0.045
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
CALIBRATION_PATH = os.path.join(CURRENT_PATH, 'data/calibration')

if not os.path.exists(CALIBRATION_PATH):
    os.makedirs(CALIBRATION_PATH)

calibrator = CharucoCalibrator(ARUCO_DICT, SQUARES_VERTICALLY, SQUARES_HORIZONTALLY, SQUARE_LENGTH, MARKER_LENGTH)
calibrator.generate_charuco_board(CALIBRATION_PATH)