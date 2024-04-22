## Question 1: Canny Edge Detection Manual vs Library Refer (Q1_Canny.ipynb)

I selected a frame and an ROI from it that is a corner of a LED monitor. And computed Canny Edge Detection manually and OpenCV Library.
Steps for manual:
1) Gaussian Blur
2) Sobel Operator to calucate gradients
3) Non-Maxima suppression
4) Hysteris Thresholding
Choice of angles in the non-maximum supression, hysterisis strong parameter all would have been, kernel size of Sobel Filter and Gaussian Blur will be optimized in the Opencv function hence a much better result
![image](https://github.com/pvdsan/Assignment2/assets/22724124/91fc70e1-b922-4a57-81aa-3fc4957b71d3)


## Question 2: Harris Corner Detection manual Vs Library Refer (Q2_Harris.ipynb)
Steps for maual:
1) Calculate gradients using Sobel
2) Find product of the gradients to get Ixx, Iyy, Ixy
3) Run Gaussian Blur on the Ixx,Iyy, Ixy
4) Harris response Calculation
I used the same ROI as the Canny Edge since there is a corner in the scene.
I have used the exact same parameters for both the manual and OpenCv implementation as in the blocksize, kernel size, yet the result seems to be different.

![image](https://github.com/pvdsan/Assignment2/assets/22724124/a863d1b2-8630-471e-8aef-9fb8176edcdc)



## Question 3 A) Computing SIFT and SSD  Refer Q3A_Compute_SIFT.ipybnb
Using Select_Image_Pair.ipynb we choose 2 frames that are atleast 2 sec apart and save them as image1.jpg and image2.jpg in the directory.
Next we select a 50x50 kernel that we choose in running the Q3A_Compute_SIFT.ipynb. The UI is designed to take only a 50 x 50 kernel hence ensuring same superpixel size.
Using OpenCV SIFT_create() we computer the SIFT feautures on both the patches and find the SSD on the features.
These are the two patches I selected:
![image](https://github.com/pvdsan/Assignment2/assets/22724124/aeabd18d-ef71-4570-af71-3f4f76cba12f)
![image](https://github.com/pvdsan/Assignment2/assets/22724124/1ef65ccf-513f-4146-bccb-a8f5d4f7211d)
Result : ![image](https://github.com/pvdsan/Assignment2/assets/22724124/b173cb3a-8f80-4937-bf51-a57550e938b9)



## Question 3 B) Compute Homography matrix and its inverse Refer Q3B_Compute_Homography.ipynb

On the same images image1.jpg , image2.jpg that we have selected earlier.
Using the Flann based matcher and doing a KNN , we find matching points from the two images that are 2 sec apart.
Next we choose matches that only fit a certain distance threshold and call them 'good matches'
If we have more than a certain good matches , we can  be confident of finding a homography H using the cv2 library function between the matches 
Also compute inverse of H
![image](https://github.com/pvdsan/Assignment2/assets/22724124/44d4009c-2763-4987-9461-ac0713779ef2)
![image](https://github.com/pvdsan/Assignment2/assets/22724124/61c3220d-27ca-49d8-b8cb-ed529797b6ac)


## Question 4: Integral  RGB Feed Refer Q4_Integral_RGB_Feed.py
Part of the Demo Video Uploaded on Classroom


## Question 5: Panaroma Image Stictching App
Two versions,
V1: Refer Image_Stiching_App.py
Take a video of 10 sec and stich the images using SIFT features, Flann Matching knn, and computing the homography.

