## Question 1: Canny Edge Detection Manual vs Library Refer (Q1_Canny.ipynb)

I selected a frame and an ROI from it that is a corner of a LED monitor. And computed Canny Edge Detection manually and OpenCV Library.
Steps for manual:
1) Gaussian Blur
2) 
Choice of angles in the non-maximum supression, hysterisis strong parameter all would have been, kernel size of Sobel Filter and Gaussian Blur will be optimized in the Opencv function hence a much better result
![image](https://github.com/pvdsan/Assignment2/assets/22724124/91fc70e1-b922-4a57-81aa-3fc4957b71d3)


## Question 2: Harris Corner Detection manual Vs Library Refer (Q2_Harris.ipynb)

I used the same ROI as the Canny Edge since there is a corner in the scene.
I have used the exact same parameters for both the manual and OpenCv implementation as in the blocksize, kernel size, yet the result seems to be different.

![image](https://github.com/pvdsan/Assignment2/assets/22724124/a863d1b2-8630-471e-8aef-9fb8176edcdc)



## Question 3 A) Computing SIFT among 
Using Select_Image_Pair.ipynb we choose 2 frames that are atleast 2 sec apart and save them as image1.jpg and image2.jpg in the directory.
Next we select a 50x50 kernel that we choose in running the Q3A_Compute_SIFT.ipynb. The UI is designed to take only a 50 x 50 kernel hence ensuring same superpixel size.
Using OpenCV SIFT_create() we computer the SIFT feautures on both the patches and find the Sum of Squared Differences on the features.
These are the two patches I selected:
![image](https://github.com/pvdsan/Assignment2/assets/22724124/aeabd18d-ef71-4570-af71-3f4f76cba12f)
![image](https://github.com/pvdsan/Assignment2/assets/22724124/1ef65ccf-513f-4146-bccb-a8f5d4f7211d)


