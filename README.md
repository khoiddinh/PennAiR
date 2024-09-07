# PennAiR

Running Code:
1) Ensure that all of the source data files (images, videos) are in the same folder as the script.
2) Make sure that they are named PennAir_2024_App_Dynamic.mp4, PennAir_2024_App_Dynamic_Hard.mp4, PennAir_2024_App_Static.png
3) Run the script using Python3 (python3 {script_name})
4) Outputs will be written in the same folder

Part 1 (static image) Answers:
My approach for the static image essentially consistented of doing preprocessing on the image (blur), and then finding the average color of the image. I then subtracted this average color from the original image. I then ran contouring to find the borders and labeled them on the image.
Part 2 (video) Answers:
I did some additional hyperparameter tuning to make the processing on the video work better. I used the area of the contour to detect any unwanted noise so that it doesn't appear as a shape. Originally, I used a lot of RGB seperation and morphology, but I found that these algorithms did not significantly impact the performance of the algorithm results-wise but increased the runtime.

Solutions:

Image: https://drive.google.com/file/d/18Alsh0HAh5eIyVRYHlICDZsxSKFFAIel/view?usp=sharing
Video for Part 2 (too large to embed): https://drive.google.com/file/d/178CoHF73xEnsujNrhqgarvcU5tTsyoK9/view?usp=sharing



