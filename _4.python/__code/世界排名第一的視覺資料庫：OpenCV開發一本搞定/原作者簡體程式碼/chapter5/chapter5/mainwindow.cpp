//开发：李立宗
//Email:lilizong@gmail.com
//开发时间：2015年07月17日
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QString>
#include <QFileDialog>
#include <QMessageBox>
#include <opencv/cv.h>
#include <QTextCodec>
using namespace cv;
//  版权信息：  lilizong[at]gmail.com
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_openTestJpg_triggered()
//默认打开当前目录下image\test\1.bmp文件，将其作为待检测图像。
{
    testImage = cv::imread("image\\test\\1.bmp");
    if(!testImage.data)  //文件未找到
    {
        QMessageBox msgBox;
        msgBox.setText(tr("默认的测试文件不存在，可以用以下两种方式的一种：1）复制一个文件到当前目录下image\test，并命名为1.bmp. 2)使用自定义方式打开一个自定义文件。"));
        msgBox.exec();
    }
    else
    {
        //将当前打开的图像显示在左侧的标签内。
        //先进行图像转换
        cv::cvtColor(testImage,testImage,CV_BGR2RGB);
        //将转换后的图像赋给img
        img = QImage((const unsigned char*)(testImage.data),testImage.cols,testImage.rows, testImage.cols*testImage.channels(), QImage::Format_RGB888);
        //label1清空
        ui->label1->clear();
        //调整图像大小以适应标签大小。
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        //让img显示在label1内
        ui->label1->setPixmap(QPixmap::fromImage(img));
    }
}

void MainWindow::on_exitSystem_triggered()
{
    exit(0);
}

void MainWindow::on_openCustomeFile_triggered()
{
    //调用打开文件对话框，并将返回值赋给filename
    QString filename = QFileDialog::getOpenFileName(this,tr("Open Image"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    //定义编码类型
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    //类型转换
    std::string name = code->fromUnicode(filename).data();
    //读取文件
    testImage = cv::imread(name);
    //判断文件是否存在。
    if(!testImage.data)
    {
        //要打开的文件不存在，或在打开文件对话框内单击取消，或未选择文件直接关闭时。
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    else
    {
        //将当前打开的图像显示在左侧的标签内。
        //先进行图像转换
        cv::cvtColor(testImage,testImage,CV_BGR2RGB);
        //将转换后的图像赋给img
        img = QImage((const unsigned char*)(testImage.data),testImage.cols,testImage.rows, testImage.cols*testImage.channels(), QImage::Format_RGB888);
        //label1清空
        ui->label1->clear();
        //调整图像大小以适应标签大小。
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        //让img显示在label1内
        ui->label1->setPixmap(QPixmap::fromImage(img));
    }
}

void MainWindow::on_restoreFile_triggered()
{
    ui->label1->clear();
    ui->label2->clear();
}

void MainWindow::on_copyright_triggered()
{
    QMessageBox::information(this,"版权",tr("本软件版权所有者为：天津职业技术师范大学。如果使用，请联系：lilizong@gmail.com"));
}

void MainWindow::on_about_triggered()
{
    QMessageBox::information(this,"关于",tr("本软件当前版本为1.0，由李立宗等人开发。如果有问题，欢迎联系：lilizong@gmail.com"));
    return;
}

//提取图像特征
void MainWindow::getFeature(cv::Mat m,float a[25])
{
    int M,N;  //用来存储图像m的宽高
    int i,j;
    M=m.cols;
    N=m.rows;
    for(i=0;i<25;i++)
        a[i]=0;
    //转换为灰度图像
    cv::cvtColor(m,m,COLOR_RGB2GRAY);
    //转换为二值图像
    cv::threshold(m,m,100,255,THRESH_BINARY);
    //将图像划分为5*5个子块，计算每块像素值的和
    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
            if(m.at<uchar>(i,j)==255)
            {
                a[i/(M/5)*5+j/(N/5)]++;
            }
    //计算当前像素块的平均值
    for(i=0;i<25;i++)
    {
        a[i]=a[i]/((M/5)*(N/5));
    }
}
//计算欧式距离
float MainWindow::ouDistance(float a[25],float b[25])
//这个函数不要忘记写MainWindow的类关系！
{
    int i;
    float distance=0;
    //不要忘记了初始化置零，否则出错！！！
    //根据欧式距离计算公式，计算距离的平方
    for(i=0;i<25;i++)
        distance+=(a[i]-b[i])*(a[i]-b[i]);
    //对上述计算结果开根号
    distance=sqrt(distance);
    return distance;
}
float  MainWindow::oDistance(float a[25],float b[25])   //这个函数是ouDistance出问题时测试的，并没有用
{
    int i;
    float distance=0;   //不能忘记置零，会出错！！！
    //,为了测试ouDistance函数，重写了oDistance发现问题，结果再次出现问题一直却一直在此函数修改。而调用函数用的还是ouDistance
    for(i=0;i<25;i++)
        distance+=(a[i]-b[i])*(a[i]-b[i]);
    distance=sqrt(distance);
    return distance;
}


void MainWindow::on_showImage_triggered()
//将与当前测试图像匹配的图像显示在label2内
{
    //获取数字结果
    int mini=getResultNumber();
    //色彩空间转换
    cv::cvtColor(srcImage[mini],srcImage[mini],CV_BGR2RGB);
    //img赋值
    img = QImage((const unsigned char*)(srcImage[mini].data),srcImage[mini].cols,srcImage[mini].rows, srcImage[mini].cols*srcImage[mini].channels(), QImage::Format_RGB888);
    //清空右侧的标签
    ui->label2->clear();
    //调整img大小以匹配标签
    img=  img.scaled(ui->label2->width(), ui->label2->height());
    //在标签内显示img
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_showMessage_triggered()
//以消息框的形式显示识别结果
{
    int mini=getResultNumber();
    //将当前图像的匹配结果显示在一个消息框内
    QMessageBox::information(NULL, "测试结果", "当前测试图像的识别结果为数字："+QString::number(mini), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
}

void MainWindow::on_ImageAndMessage_triggered()
//同时以标签和消息框形式显示
{
    int mini=getResultNumber();
    //在标签内显示
    cv::cvtColor(srcImage[mini],srcImage[mini],CV_BGR2RGB);
    img = QImage((const unsigned char*)(srcImage[mini].data),srcImage[mini].cols,srcImage[mini].rows, srcImage[mini].cols*srcImage[mini].channels(), QImage::Format_RGB888);
    ui->label2->clear();
    img=  img.scaled(ui->label2->width(), ui->label2->height());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    //将当前图像的匹配结果显示在一个消息框内
    QMessageBox::information(NULL, "测试结果", "当前测试图像的识别结果为数字："+QString::number(mini), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
}

int MainWindow::getResultNumber()
{
    int i;
    float min; //用来存储最小的欧式距离
    int mini;   //用来存储最小的欧氏距离的数字号。
    getFeature(testImage,testFeature);
    //获取测试图像的特征值，并将其放到testFeature数组内。
    for(i=0;i<10;i++)
    {
        QString filePath,fileName,allName;
        filePath="image\\stand\\";    //当前图像目录
        fileName=".bmp";       //当前图像的扩展名
        allName=filePath+"\\"+QString::number(i)+fileName;  //i是文件名，使用QString::number(i)完成将其转换为QString类型，当前为数值型
        String s=allName.toStdString();    //转换为标准的字符串型，imread不识别QString类型
        srcImage[i] = cv::imread(s);
    }
    //以下部分用于测试上述代码是否能够将srcImage的值获取到。
    /*
    cv::cvtColor(srcImage[3],srcImage[3],CV_BGR2RGB);
    img = QImage((const unsigned char*)(srcImage[3].data),srcImage[1].cols,srcImage[1].rows, srcImage[1].cols*srcImage[1].channels(), QImage::Format_RGB888);
    ui->label1->clear();
    img=  img.scaled(ui->label1->width(), ui->label1->height());
    ui->label1->setPixmap(QPixmap::fromImage(img));
*/
    // 获取原始数字图像的特征值。
    for(i=0;i<10;i++)
        getFeature(srcImage[i],srcFeature[i]);
    /*
     * 用于测试中间过程！
    for(i=0;i<25;i++)
                QMessageBox::information(NULL, "Title", QString::number(srcFeature[0][i]), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
  */
    float ouDistanceValue[10]={0};   //存储当前测试图像与已知的十个数字图像之间的欧氏距离
    for(i=0;i<10;i++)
    {
        ouDistanceValue[i]=ouDistance(testFeature,srcFeature[i]);
    }
    //测试下ouDistance有没有问题。
    /*
     * 用于中间过程的测试
    for(i=0;i<10;i++)
        QMessageBox::information(NULL, "Title", QString::number(ouDistanceValue[i]), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
    */
    mini=0;
    min=ouDistanceValue[0];  //给min赋个初始值，假设与数字0的距离最小。
    for(i=0;i<10;i++)
    {
        if(min>ouDistanceValue[i])
        {
            min=ouDistanceValue[i];
            mini=i;
        }
    }
    return mini;
}
void MainWindow::showLabel(Mat m, QLabel *l)
{
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    l->clear();
    img=img.scaled(l->width(),l->height());
    l->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_horizenFlip_triggered()
{
    cv::flip(testImage,dstImage,1);
    /*
     * void flip(InputArray src, OutputArray dst, int flipCode)
     * Parameters:
    src – input array.
    dst – output array of the same size and type as src.
    flipCode – a flag to specify how to flip the array;
     0 means flipping around the x-axis and positive value (for example, 1)
     means flipping around y-axis. Negative value (for example, -1)
    means flipping around both axes (see the discussion below for the formulas).
    The example scenarios of using the function are the following:

    Vertical flipping of the image (flipCode == 0) to
    switch between top-left and bottom-left image origin.
     This is a typical operation in video processing on Microsoft Windows* OS.
    Horizontal flipping of the image with the subsequent horizontal shift
    and absolute difference calculation to check for a vertical-axis symmetry (flipCode > 0).
    Simultaneous horizontal and vertical flipping of
     the image with the subsequent shift and absolute difference calculation to
     check for a central symmetry (flipCode < 0).
    Reversing the order of point arrays (flipCode > 0 or flipCode == 0).
    */
    showLabel(dstImage,ui->label2);


}

void MainWindow::on_VerticalFlip_triggered()
{
    cv::flip(testImage,dstImage,0);
    showLabel(dstImage,ui->label2);
    /*
 * void flip(InputArray src, OutputArray dst, int flipCode)
 * 参加函数：void MainWindow::on_horizenFlip_triggered()内的注释
*/
}

void MainWindow::on_VerticalAndHorizen_triggered()
{
    cv::flip(testImage,dstImage,-1);
    showLabel(dstImage,ui->label2);
}
/*
 * void flip(InputArray src, OutputArray dst, int flipCode)
 * 参见函数：void MainWindow::on_horizenFlip_triggered()内的注释
*/


void MainWindow::on_erode_triggered()
{
    int erosion_type;
    erosion_type = MORPH_RECT;
    int erosion_size = 1;
    Mat element = getStructuringElement( erosion_type,
                                         Size( 2*erosion_size + 1, 2*erosion_size+1 ),
                                         Point( erosion_size, erosion_size ) );
    erode( testImage, dstImage, element );
    /*
 * C: void cvErode(const CvArr* src, CvArr* dst, IplConvKernel* element=NULL, int iterations=1)

Parameters:
src – input image; the number of channels can be arbitrary,
but the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F` or ``CV_64F.
dst – output image of the same size and type as src.
element – structuring element used for erosion; if element=Mat() ,
 a 3 x 3 rectangular structuring element is used.
anchor – position of the anchor within the element; default value (-1, -1)
means that the anchor is at the element center.
iterations – number of times erosion is applied.
borderType – pixel extrapolation method (see borderInterpolate() for details).
borderValue – border value in case of a constant border (see createMorphologyFilter() for details).
*/
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_dialate_triggered()
{
    int  dilation_size  = 1;
    int dilation_type;
    dilation_type = MORPH_RECT;
    Mat element = getStructuringElement( dilation_type,
                                         Size( 2*dilation_size + 1, 2*dilation_size+1 ),
                                         Point( dilation_size, dilation_size ) );
    ///膨胀操作
    dilate( testImage,dstImage, element );
    /*
     *C: void cvDilate(const CvArr* src, CvArr* dst, IplConvKernel* element=NULL, int iterations=1 )
Python: cv.Dilate(src, dst, element=None, iterations=1) → None
Parameters:
src – input image; the number of channels can be arbitrary,
but the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F` or ``CV_64F.
dst – output image of the same size and type as src.
element – structuring element used for dilation; if element=Mat() ,
 a 3 x 3 rectangular structuring element is used.
anchor – position of the anchor within the element;
default value (-1, -1) means that the anchor is at the element center.
iterations – number of times dilation is applied.
borderType – pixel extrapolation method (see borderInterpolate() for details).
borderValue – border value in case of a constant border
(see createMorphologyFilter() for details).
*/
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_open_triggered()
{
    int morph_elem=MORPH_RECT;
    int morph_size=3;
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    morphologyEx( testImage, dstImage, MORPH_OPEN, element );
    showLabel(dstImage,ui->label2);
    /*
        * MORPH_OPEN - an opening operation
       MORPH_CLOSE - a closing operation
       MORPH_GRADIENT - a morphological gradient
       MORPH_TOPHAT - “top hat”
       MORPH_BLACKHAT - “black hat”
       */
}

void MainWindow::on_close_triggered()
{
    int morph_elem=MORPH_RECT;
    int morph_size=3;
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    morphologyEx( testImage, dstImage, MORPH_CLOSE, element );
    showLabel(dstImage,ui->label2);
    /*
     * MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    */
}

void MainWindow::on_topHat_triggered()
{
    int morph_elem=MORPH_RECT;
    int morph_size=3;
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    morphologyEx( testImage, dstImage, MORPH_TOPHAT, element );
    showLabel(dstImage,ui->label2);
    /*
     * MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    */
}

void MainWindow::on_blackHat_triggered()
{
    int morph_elem=MORPH_RECT;
    int morph_size=3;
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    morphologyEx( testImage, dstImage, MORPH_BLACKHAT, element );
    showLabel(dstImage,ui->label2);
    /*
     * MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    */
}

void MainWindow::on_actionSobel_triggered()
{
    Sobel(testImage,dstImage,testImage.depth(),1,1);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_actionCanny_triggered()
{
    Mat dstImage2;
    // srcImage = cv::imread("a.jpg");
    //cvtColor(srcImage,srcImage,CV_BGR2RGB);
    // cvtColor(srcImage,dstImage,CV_RGB2GRAY);
    cvtColor(testImage,dstImage2,CV_BGR2GRAY);
    // srcImage.copyTo(dstImage);
    Canny(dstImage2,dstImage2,30,100);
    //  img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_Indexed8);
    //QImage img2(dstImage.size,QImage::Format_Indexed8);
    // img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    img = QImage((const unsigned char*)(dstImage2.data),dstImage2.cols,dstImage2.rows,dstImage2.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //说明：如果重置图像大小会导致全黑，无法观看。这里仅仅显示一部分
    ui->label2->setPixmap(QPixmap::fromImage(img));

    // imshow("li",dstImage);
    // srcImage.copyTo(dstImage);

    /*
    Mat gray;

    cvtColor(srcImage,gray,CV_BGR2GRAY);
    Canny(gray,gray,30,100);
    // cvtColor(gray,gray,CV_bg)
  //  imshow("li",gray);

    // cv::cvtColor(image,image,CV_BGR2RGB);
    //      img = QImage((const unsigned char*)(image.data),image.cols,image.rows,image.cols*image.channels(),  QImage::Format_RGB888);
    img = QImage((const unsigned char*)(gray.data),gray.cols,gray.rows,gray.step,  QImage::Format_Indexed8);

    ui->label2->setPixmap(QPixmap::fromImage(img));
imshow("daf",gray);
*/
}

void MainWindow::on_actionLaplacian_triggered()
{
    Laplacian(testImage,dstImage,testImage.depth());
    showLabel(dstImage,ui->label2);
}



void MainWindow::on_actionScharr_triggered()
{
    Scharr(testImage,dstImage,testImage.depth(),0,1);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_gray_triggered()
{
    // 灰度转换
    cvtColor(testImage,dstImage, CV_RGB2GRAY);
    //定义大小
    Size dsize = Size(ui->label2->width(),ui->label2->height());
    //定义一个目标图像
    Mat image2 = Mat(dsize,CV_32S);
    //调整大小
    cv::resize(dstImage, image2,dsize);
    //先对图像进行灰度化，再对QImage进行缩放处理，结果可能会显示黑色。
    //先对Mat图像进行缩放，然后再将其转换为QImage。
    //给img赋值
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows,image2.step,  QImage::Format_Indexed8);
    //清空label2
    ui->label2->clear();
    // 将img赋给label2，即主界面内右侧的标签。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}


void MainWindow::on_binValue_triggered()
//图像二值化
{
    cvtColor( testImage,dstImage, CV_RGB2GRAY );  //先转换成灰度图像
    //使用threshold实现二值化
    threshold(dstImage,dstImage, 100, 255,   THRESH_BINARY );
    /*更多threshold函数的具体介绍参见第1章。
     * double threshold(InputArray src, OutputArray dst, double thresh, double maxval, int type)
     * Parameters:
    src – input array (single-channel, 8-bit or 32-bit floating point).
    dst – output array of the same size and type as src.
    thresh – threshold value.
    maxval – maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
    type – thresholding type (see the details below).
    The function applies fixed-level thresholding to a single-channel array.
    The function is typically used to get a bi-level (binary) image out of a grayscale image
    ( compare() could be also used for this purpose) or for removing a noise, that is,
     filtering out pixels with too small or too large values. There are several types of
    thresholding supported by the function.
    */
    //获取右侧标签的大小（label2）
    Size dsize = Size(ui->label2->width(),ui->label2->height());
    //定义一个image2
    Mat image2 = Mat(dsize,CV_32S);
    //调整目标图像为image2的大小为
    cv::resize(dstImage, image2,dsize);
    //设置imge为image2
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows, image2.cols*image2.channels(), QImage::Format_Indexed8);
    //清空右侧标签（label2）
    ui->label2->clear();
    //在右侧标签内显示img。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_invertColor_triggered()
//图像反色
{
    cvtColor( testImage,dstImage, CV_RGB2GRAY );  //先转换成灰度图像
    //threshold内参数THRESH_BINARY_INV表示要反色
    //更多函数threshold的介绍参考第1章
    threshold(dstImage,dstImage, 100, 255,  THRESH_BINARY_INV );
    //获取右侧标签的大小（label2）
    Size dsize = Size(ui->label2->width(),ui->label2->height());
    //定义一个image2
    Mat image2 = Mat(dsize,CV_32S);
    //调整目标图像为image2的大小为
    cv::resize(dstImage, image2,dsize);
    //设置imge为image2
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows, image2.cols*image2.channels(), QImage::Format_Indexed8);
    //清空右侧标签（label2）
    ui->label2->clear();
    //在右侧标签内显示img。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_rSpace_triggered()
{
    Mat bgr_res;
    Mat bgr[3];
    split(testImage,bgr);
    Mat temp(testImage.size(), bgr[0].type(),Scalar::all(0));
    temp.copyTo(bgr[1]);
    temp.copyTo(bgr[2]);
    merge(bgr,3, bgr_res);
    /*
    * C++: void split(const Mat& src, Mat* mvbegin)
    * Parameters:
    src – input multi-channel array.
    mv – output array or vector of arrays;
    in the first variant of the function the number of arrays must match src.channels();
     the arrays themselves are reallocated, if needed.
    * /
    /*
    * C++: void merge(const Mat* mv, size_t count, OutputArray dst)
    *Parameters:
    mv – input array or vector of matrices to be merged; all the matrices in mv must have
    the same size and the same depth.
    count – number of input matrices when mv is a plain C array; it must be greater than zero.
    dst – output array of the same size and the same depth as mv[0]; The number of channels
     will be the total number of channels in the matrix array.
    The functions merge merge several arrays to make a single multi-channel array.
    That is, each element of the output array will be a concatenation of the elements of the input arrays,
    where elements of i-th input array are treated as mv[i].channels()-element vectors.
    * 函数的具体介绍看本章5.2.4通道处理部分
    */
    img = QImage((const unsigned char*)(bgr_res.data),bgr_res.cols,bgr_res.rows, bgr_res.cols*bgr_res.channels(), QImage::Format_RGB888);
    ui->label2->clear();
    img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_gSpace_triggered()
{
    Mat bgr_res;
    Mat bgr[3];
    split(testImage,bgr);
    Mat temp(testImage.size(), bgr[0].type(),Scalar::all(0));
    temp.copyTo(bgr[0]);
    temp.copyTo(bgr[2]);
    merge(bgr,3, bgr_res);
    /*
     * 关于split函数和merge函数可以参考【R通道】中的注释，
     * 即函数：
     *void MainWindow::on_rSpace_triggered()
     * 内的注释
     * 函数具体介绍参考本章5.2.4部分
    */
    img = QImage((const unsigned char*)(bgr_res.data),bgr_res.cols,bgr_res.rows, bgr_res.cols*bgr_res.channels(), QImage::Format_RGB888);
    ui->label2->clear();
    img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_bSpace_triggered()
{
    Mat bgr_res;
    Mat bgr[3];
    split(testImage,bgr);
    Mat temp(testImage.size(), bgr[0].type(),Scalar::all(0));
    temp.copyTo(bgr[0]);
    temp.copyTo(bgr[1]);
    merge(bgr,3, bgr_res);
    /*
     * 关于split函数和merge函数可以参考【R通道】中的注释，
     * 即函数：
     *void MainWindow::on_rSpace_triggered()
     * 内的注释
     * 函数具体介绍参考本章5.2.4部分
    */
    img = QImage((const unsigned char*)(bgr_res.data),bgr_res.cols,bgr_res.rows, bgr_res.cols*bgr_res.channels(), QImage::Format_RGB888);
    ui->label2->clear();
    img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionRtong_triggered()
{
    Mat bgr[3];
    split(testImage, bgr);
    /*
      * C++: void split(const Mat& src, Mat* mvbegin)
      * Parameters:
      src – input multi-channel array.
      mv – output array or vector of arrays;
      in the first variant of the function the number of arrays must match src.channels();
       the arrays themselves are reallocated, if needed.
      */
    Size dsize = Size(ui->label2->width(),ui->label2->height());
    //定义一个image2
    Mat image2 = Mat(dsize,CV_32S);
    //调整目标图像为image2的大小为
    cv::resize(bgr[0], image2,dsize);
    //设置imge为image2
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows, image2.cols*image2.channels(), QImage::Format_Indexed8);
    //清空右侧标签（label2）
    ui->label2->clear();
    //在右侧标签内显示img。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_Rchannel_triggered()
{
    Mat bgr[3];
    split(testImage, bgr);
    /*
      * C++: void split(const Mat& src, Mat* mvbegin)
      * Parameters:
      src – input multi-channel array.
      mv – output array or vector of arrays;
      in the first variant of the function the number of arrays must match src.channels();
       the arrays themselves are reallocated, if needed.
      */
    Size dsize = Size(ui->label2->width(),ui->label2->height());
    //定义一个image2
    Mat image2 = Mat(dsize,CV_32S);
    //调整目标图像为image2的大小为
    cv::resize(bgr[2], image2,dsize);
    //设置imge为image2
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows, image2.cols*image2.channels(), QImage::Format_Indexed8);
    //清空右侧标签（label2）
    ui->label2->clear();
    //在右侧标签内显示img。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_Gchannel_triggered()
{
    Mat bgr[3];
    split(testImage, bgr);
    /*
      * C++: void split(const Mat& src, Mat* mvbegin)
      * Parameters:
      src – input multi-channel array.
      mv – output array or vector of arrays;
      in the first variant of the function the number of arrays must match src.channels();
       the arrays themselves are reallocated, if needed.
      */
    Size dsize = Size(ui->label2->width(),ui->label2->height());
    //定义一个image2
    Mat image2 = Mat(dsize,CV_32S);
    //调整目标图像为image2的大小为
    cv::resize(bgr[1], image2,dsize);
    //设置imge为image2
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows, image2.cols*image2.channels(), QImage::Format_Indexed8);
    //清空右侧标签（label2）
    ui->label2->clear();
    //在右侧标签内显示img。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_Bchannel_triggered()
{
    Mat bgr[3];
    split(testImage, bgr);
    /*
      * C++: void split(const Mat& src, Mat* mvbegin)
      * Parameters:
      src – input multi-channel array.
      mv – output array or vector of arrays;
      in the first variant of the function the number of arrays must match src.channels();
       the arrays themselves are reallocated, if needed.
      */
    Size dsize = Size(ui->label2->width(),ui->label2->height());
    //定义一个image2
    Mat image2 = Mat(dsize,CV_32S);
    //调整目标图像为image2的大小为
    cv::resize(bgr[0], image2,dsize);
    //设置imge为image2
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows, image2.cols*image2.channels(), QImage::Format_Indexed8);
    //清空右侧标签（label2）
    ui->label2->clear();
    //在右侧标签内显示img。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_about_2_triggered()
{

}

void MainWindow::on_aboutMe_triggered()
{
    QMessageBox::information(this,"关于",tr("本软件为手写数字识别学习系统，当前版本为1.0，由李立宗等人开发。"));
    return;
}

void MainWindow::on_contacctUs_triggered()
{
    QMessageBox::information(this,"联系我们",tr("如有问题请联系：lilizong(at)Gmail。QQ群：QT+OpenCV，群号：107416004"));
    return;
}

void MainWindow::on_openLenaJpg_triggered()
{

}

void MainWindow::on_Clear_triggered()
{
    //菜单：文件=>清除
    //清除标签1的内容。
    ui->label1->clear();
    //清除标签2的内容。
    ui->label2->clear();

}
