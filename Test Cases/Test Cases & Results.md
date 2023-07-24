## Program Testing
Considering that our project is dealing with image processing, selecting the appropriate image resources greatly determines our testing effectiveness.

For our purpose, the key assessment criteria betweeen the test cases will be degree of colour step. This is mainly because the most integral and easily buggeed section of both First degree conversion(FDC1) and Final degree conversion(FDC2) goes around identifying some feature from the resource image. (For FDC1, it is mainly the image's outlines. For FDC2, it is the ability to seperate key characterisitcs from other counterparts) A image with high colour steps will likely lead to highly distinguishable image areas, while a image with low colour steps will imply a frequent occurance of non-differentiable sections, largely increasing the diffculty in image analysation.

Hence, the following section will cover how our program handles some of the Simple(High colour step), Moderate and Intricate(Low colour step) test cases.

### FDC1
#### Simple
![S1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1.png)

#### Moderate
#### Intricate

### FDC2
#### Simple
#### Moderate
#### Intricate
