from flask import Flask

from selenium import webdriver

import os

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


## Save a screenshot of the current page.
#  @param driver A webdriver object.
#  @param name The name of the file to save.
#  @param save_location Where to save the screenshot.
#  @return The full path to the saved image.
def take_screenshot(driver, name, save_location):
  # Make sure the path exists.
  path = os.path.abspath(save_location)
  if not os.path.exists(path):
    os.makedirs(path)
  full_path = '%s/%s' % (path, name)
  driver.get_screenshot_as_file(full_path)
  return full_path

@app.route('/')
def hello_world():
    driver = webdriver.PhantomJS()  # or add to your PATH
    driver.set_window_size(1024, 768)  # optional
    driver.get('http://qq.com/')
    driver.save_screenshot('screen.png')
    last_height = driver.execute_script("return document.body.scrollHeight")
    print  last_height
    driver.get_screenshot_as_file("ok.png")
    screenshot = take_screenshot(driver, 'google.png', 'path/to/screenshots')
    print "Screenshot saved to: %s" % screenshot

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
