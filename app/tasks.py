from PIL import Image
import os
import time

def image_size(img, size_img, img_dir=None, img_n=None, ext=None):
    copy_img = img.copy()
    copy_img.thumbnail(size_img, Image.LANCZOS)
    assert img_dir != None, "Please fill a directory"
    
    filename = os.path.join(img_dir, img_n)
    if size_img[0] == 30:
        copy_img.save("{}-thumbnail.{}".format(filename, ext), optimize=True, quality=95)
    else:
        copy_img.save("{}-{}.{}".format(filename, size_img[0], ext), optimize=True, quality=95)

def create_image_set(image_dir, image_name):
    
    start ) = time.time()
    
    thumb = 30, 30
    small = 540, 540
    medium = 768, 768
    large = 1080, 1080
    xl = 1200, 1200
    
    image_ext = image_name.split(".")[-1]
    image_name = image_name.split(".")[0]
    
    ###### THUMBNAIL ######
    image_size(image, thumb, img_dir=image_dir, imge_n=image_name, ext=image_ext)
    
    ###### SAMLL ######
    image_size(image, small, img_dir=image_dir, imge_n=image_name, ext=image_ext)
    
    
    ###### MEDIUM ######
    image_size(image, medium, img_dir=image_dir, imge_n=image_name, ext=image_ext)
    
    ###### LARGE ######
    image_size(image, large, img_dir=image_dir, imge_n=image_name, ext=image_ext)
    
    ###### XL ######
    image_size(image, xl, img_dir=image_dir, imge_n=image_name, ext=image_ext)
    
    end = time.time()
    
    
    time_elapsed = end - start 
    
    print("Task complete in {}".format(time_elapsed))
    
    return True