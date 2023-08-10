## Unit testing
During implementation, PIXIE is divided into 2 seperate units: First degree conversion(OpencvResize.py) and Final degree conversion(AIProcessing.py). Testing under this section will surround the testing methods of this 2 features.

### First degree conversion
Using <em>First_degree_test.py</em>, the key functions of OpencvResize could be easily tested. Below shows our demo of the test case.

<b>Original:<b>

![S1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1.png)

<b>Converted:<b>

![S1_1](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1_1.png)

![S1_2](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1_2.png)

![S1_3](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1_3.png)

![S1_4](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1_4.png)

![S1_5](https://github.com/FeathersRe/PIXIE/blob/main/Test%20Cases/Test%20Pics/s_1_5.png)

Different sets of variables clearly results different resolution and quality of pixelation. FDC1 is working as intended.
