# Editor shenrongqiang
# 第一次作业date 2021/10/13
## OpenCV-python
  导入一张图片并显示
```python
import cv2 as cv
image = cv.imread("")
cv.imshow("input",image)
cv.waitKey(0)
cv.destoryAllWindows()
```
***
## OpenCV-C#
在一张图片的左上角画9个矩形
```C#
using System;
using OpenCvSharp;
namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {![ebbe2de2d43867d26fbfe0b17fa3cb6](https://user-images.githubusercontent.com/92438840/137623242-eed87493-99b2-4b46-9304-e05492e049f4.png)

            Console.WriteLine("Hello World!");
            int frix = 50;
            int friy = 50;
            Rect rect = new Rect(frix, friy, 100, 100);
            Scalar color = new Scalar(255, 0, 0);
            Mat str = Cv2.ImRead(@"C:\CAXA\QQ20210502000604.jpg", ImreadModes.AnyColor);
            for (int i=0; i<3; i++)
            {
                for(int j=0;j<3;j++)
                {
                    rect = new Rect(frix, friy, 100, 100);
                    Cv2.Rectangle(str, rect, color, 2, LineTypes.AntiAlias);
                    friy += 120;
                }
                friy = 50;
                frix += 120;
            }
            Cv2.ImShow("test", str);
            Cv2.WaitKey(0);
            Cv2.DestroyAllWindows();
        }
    }
}
```
![test](https://ibb.co/3f023cJ)

