from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import requests
import io
from datetime import datetime as dt
from PIL import Image
import time
import os

def download_image(down_path, url, file_name, image_type='JPEG',
                   verbose=True):
    try:
        time = dt.now()
        curr_time = time.strftime('%H:%M:%S')
        #Content of the image will be a url
        img_content = requests.get(url).content
        #Get the bytes IO of the image
        img_file = io.BytesIO(img_content)
        #Stores the file in memory and convert to image file using Pillow
        image = Image.open(img_file)
        file_pth = down_path + file_name

        with open(file_pth, 'wb') as file:
            image.save(file, image_type)

        if verbose == True:
            print(f'The image: {file_pth} downloaded successfully at {curr_time}.')
    except Exception as e:
        print(f'Unable to download image from Google Photos due to\n: {str(e)}')

# Function for scrolling to the bottom of Google
# Images results
def scroll_to_bottom():

	last_height = driver.execute_script('\
	return document.body.scrollHeight')

	while True:
		driver.execute_script('\
		window.scrollTo(0,document.body.scrollHeight)')

		# waiting for the results to load
		# Increase the sleep time if your internet is slow
		time.sleep(3)

		new_height = driver.execute_script('\
		return document.body.scrollHeight')

		# click on "Show more results" (if exists)
		"""
		try:
			driver.find_element_by_css_selector(".YstHxe input").click()

			# waiting for the results to load
			# Increase the sleep time if your internet is slow
			time.sleep(3)

		except:
			pass
		"""
		# checking if we have reached the bottom of the page
		if new_height == last_height:
			break

		last_height = new_height


# Calling the function

def get_images_from_google(num_images = 400):

	# NOTE: If you only want to capture a few images,
	# there is no need to use the scroll_to_bottom() function.
	scroll_to_bottom()

	image_urls = set()

	# Number of image URLs to store
	#num_images = 2

	# Find thumbnails
	thumbnails = driver.find_elements(By.CLASS_NAME, "mNsIhb")

	print(len(thumbnails))
	# Iterate over thumbnails to get the image URLs
	for thumbnail in thumbnails:
		try:
		    # Click the thumbnail to load the full-size image
		    thumbnail.click()
		    time.sleep(1)  # Wait for the image to load
		    
		    # Find the full-size image element
		    images = driver.find_elements(By.CSS_SELECTOR, "img.sFlh5c.pT0Scc.iPVvYb")
		    for image in images:
		        src = image.get_attribute('src')
		        #if src in image_urls:
		        #	continue
		        if src: #and 'http' in src:
		            image_urls.add(src)
		            print(len(image_urls))
		        if len(image_urls) >= num_images:
		            break
		    if len(image_urls) >= num_images:
		        break
		except Exception as e:
		    #print(f"Error: {e}")
		    continue
	
	return image_urls

# What you enter here will be searched for in
# Google Images
query = "ai generated woman"

# Creating a webdriver instance
driver = webdriver.Chrome('/usr/bin/chromedriver')

# Maximize the screen
driver.maximize_window()

#driver.get("https://www.google.com/search?q=ai+generated+images&tbm=isch&hl=en&chips=q:ai+generated+images,g_1:person:ezzScy_HGu4%3D&sa=X&ved=2ahUKEwic9KWgld2GAxXYoWMGHVyzCPAQ3VYoAHoECAEQLA&biw=1294&bih=656")

# Open Google Images in the browser
driver.get('https://images.google.com/')

# Finding the search box
box = driver.find_element(by=By.XPATH,value='//*[@id="APjFqb"]')

# Type the search query in the search box
box.send_keys(query)

# Pressing enter
box.send_keys(Keys.ENTER)

# Print the image URLs
#for url in image_urls:
#    print(url)

labels = [ 'ai-woman' ]

path = 'images/'

# Make the directory if it doesn't exist
for lbl in labels:
    if not os.path.exists(path + lbl):
        print(f'Making directory: {str(lbl)}')
        os.makedirs(path+lbl)

    image_urls = get_images_from_google(175)
    
    print(len(image_urls))
    
    for i, url in enumerate(image_urls):
	    download_image(down_path=f'{path}{lbl}/', 
                        url=url, 
                        file_name=str(i+385)+ '.jpg',
                        verbose=True)
    
    #driver = webdriver.Chrome('/usr/bin/chromedriver')
    #driver.get("https://www.google.com/search?q=ai+generated+images&tbm=isch&hl=en&chips=q:ai+generated+images,g_1:person:ezzScy_HGu4%3D&sa=X&ved=2ahUKEwic9KWgld2GAxXYoWMGHVyzCPAQ3VYoAHoECAEQLA&biw=1294&bih=656")

# Close the browser
driver.quit()
