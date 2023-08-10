## Unit testing
During implementation, PIXIE is divided into 2 seperate units: First degree conversion(OpencvResize.py) and Final degree conversion(AIProcessing.py). Testing under this section will surround the testing methods of this 2 features.

### First degree conversion
Using <em>First_degree_test.py</em>, the key functions of First Degree Conversion could be easily tested. Below shows our demo of the test case.

<b>Original:<b>

![S1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1.png)

<b>Converted:<b>

![S1_1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1_1.png)

![S1_2](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1_2.png)

![S1_3](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1_3.png)

![S1_4](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1_4.png)

![S1_5](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1_5.png)

Different sets of variables clearly results different resolution and quality of pixelation. This indicates our first degree conversion module is working as intended.

### Final degree conversion
Using <em>Final_degree_test.py</em>, the key functions of Final Degree Conversion could be easily tested. Below shows our demo of the test case.

<b>Original:<b>

![S1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1.png)

<b>Converted:<b>

![S1_11](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/(F2)s_1_1.png)

![S1_22](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/(F2)s_1_2.png)

![S1_33](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/(F2)s_1_3.png)

![S1_44](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/(F2)s_1_4.png)

![S1_55](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/(F2)s_1_5.png)

For different rounds of generation, a consistent posture(character either facing the front or left/right corner) and some characteristics from the original picture is shown. This indicates our final degree conversion module is working as intended.
