from PIL import ImageGrab
import Keys
from selenium import webdriver
import cv2
import time

browser = webdriver.Chrome()
browser.get("https://www.google.com/search?q=snake+game&oq=snake+game&aqs=chrome..69i57j69i60l4j0.898j0j7&sourceid=chrome&ie=UTF-8")
browser.maximize_window()

game_start = browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]')
game_start.click()

time.sleep(5)

leftBound = 680
rightBound = 1220
upBound = 375
lowerBound = 850

boardCoords = [leftBound, upBound, rightBound, lowerBound]

im = ImageGrab.grab(bbox = boardCoords)
im.save('snakeMenu2.png', 'png')
#Keys.right()

#for i in range(20):
##    start = time.time()
 #   image = ImageGrab.grab(bbox = boardCoords)
#    end = time.time()
#    print("Frame %i captured in %f seconds" % (i , end-start))