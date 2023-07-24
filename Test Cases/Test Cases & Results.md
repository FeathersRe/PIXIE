## Program Testing
Considering that our project is dealing with image processing, selecting the appropriate image resources greatly determines our testing effectiveness.

For our purpose, the key assessment criteria betweeen the test cases will be degree of colour step. This is mainly because the most integral and easily buggeed section of both First degree conversion(FDC1) and Final degree conversion(FDC2) goes around identifying some feature from the resource image. (For FDC1, it is mainly the image's outlines. For FDC2, it is the ability to seperate key characterisitcs from other counterparts) A image with high colour steps will likely lead to highly distinguishable image areas, while a image with low colour steps will imply a frequent occurance of non-differentiable sections, largely increasing the diffculty in image analysation.

Hence, the following section will cover how our program handles some of the Simple(High colour step), Moderate and Intricate(Low colour step) test cases.

### FDC1
To better evaluate the results, the below table depicts our assessment criteria for FDC1.

<b>Assessment criteria:<b>

![Criteria1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/criteria1.png) 

#### Simple
<b>Original:<b>

![S1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1.png) 

<b>Converted:<b>

![S1_FDC1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1_FDC1.png)

<b>Settings:<b> 

Pixel_size:5 Tolerance:700 Colourstep: 16 Ink_percentage: 0.7

<b>Outcome:<b> Acceptable, Lines are accurately identified and Image resemble pixelation.

![S2](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_2.jpg)

<b>Converted:<b>

![S2_FDC1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_2_FDC1.jpg)

<b>Settings:<b> 

Pixel_size:10 Tolerance:500 Colourstep: 16 Ink_percentage: 0.4

<b>Outcome:<b> Acceptable, Lines are accurately identified and Image resemble pixelation.

#### Moderate
<b>Original:<b>

![M1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/m_1.png) 

<b>Converted:<b>

![m1_FDC1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/m_1_FDC1.png)

<b>Original:<b>

![M2](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/m_2.jpg) 

<b>Converted:<b>

![m2_FDC1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/m_2_FDC1.jpg)

#### Intricate
<b>Original:<b>

![I1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/i_1.png) 

<b>Converted:<b>

![I1_FDC1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/i_1_FDC1.png)

<b>Original:<b>

![I2](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/i_2.jpg) 

<b>Converted:<b>

![I2_FDC1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/i_2_FDC1.jpg)

### FDC2
Assessment criteria:

![Criteria2](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/criteria2.png) 
#### Simple
<b>Original:<b>

![S1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1.png)

<b>Converted:<b>

![S1_FDC1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1_FDC2.png)

<b>Original:<b>

![S2](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_2.jpg) 

<b>Converted:<b>

![S2_FDC1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_2_FDC2.jpg)

#### Moderate
<b>Original:<b>

![M1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/m_1.png)

<b>Converted:<b>

![m1_FDC1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/m_1_FDC2.png)

<b>Original:<b>

![M2](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/m_2.jpg) 

<b>Converted:<b>

![m2_FDC1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/m_2_FDC2.jpg)

#### Intricate
<b>Original:<b>

![I1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/i_1.png)

<b>Converted:<b>

![I1_FDC1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/i_1_FDC2.png)

<b>Original:<b>

![I2](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/i_2.jpg) 

<b>Converted:<b>

![I2_FDC1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/i_2_FDC2.jpg)
