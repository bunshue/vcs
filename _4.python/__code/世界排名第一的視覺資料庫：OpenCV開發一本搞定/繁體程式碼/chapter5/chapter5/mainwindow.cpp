//開發：李立宗
//Email:lilizong@gmail.com
//開發時間：2015年07月17日
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
//  版權訊息：  lilizong[at]gmail.com
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
//預設開啟目前目錄下image\test\1.bmp檔案，將其作為待檢驗圖形。
{
    testImage = cv::imread("image\\test\\1.bmp");
    if(!testImage.data)  //檔案找不到
    {
        QMessageBox msgBox;
        msgBox.setText(tr("預設的測試檔案不存在，可以用以下兩種模式的一種：1）複製一個檔案到目前目錄下image\test，並命名為1.bmp. 2)使用自訂模式開啟一個自訂檔案。"));
        msgBox.exec();
    }
    else
    {
        //將目前開啟的圖形顯示在左側的標簽內。
        //先進行圖形轉換
        cv::cvtColor(testImage,testImage,CV_BGR2RGB);
        //將轉換後的圖形賦給img
        img = QImage((const unsigned char*)(testImage.data),testImage.cols,testImage.rows, testImage.cols*testImage.channels(), QImage::Format_RGB888);
        //label1清理
        ui->label1->clear();
        //調整圖形大小以適應標簽大小。
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        //讓img顯示在label1內
        ui->label1->setPixmap(QPixmap::fromImage(img));
    }
}

void MainWindow::on_exitSystem_triggered()
{
    exit(0);
}

void MainWindow::on_openCustomeFile_triggered()
{
    //呼叫開啟檔案交談視窗，並將傳回值賦給filename
    QString filename = QFileDialog::getOpenFileName(this,tr("Open Image"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    //定義解碼型態
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    //型態轉換
    std::string name = code->fromUnicode(filename).data();
    //讀取檔案
    testImage = cv::imread(name);
    //判斷檔案是否存在。
    if(!testImage.data)
    {
        //要開啟的檔案不存在，或在開啟檔案交談視窗內點選取消，或未選取檔案直接關閉時。
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    else
    {
        //將目前開啟的圖形顯示在左側的標簽內。
        //先進行圖形轉換
        cv::cvtColor(testImage,testImage,CV_BGR2RGB);
        //將轉換後的圖形賦給img
        img = QImage((const unsigned char*)(testImage.data),testImage.cols,testImage.rows, testImage.cols*testImage.channels(), QImage::Format_RGB888);
        //label1清理
        ui->label1->clear();
        //調整圖形大小以適應標簽大小。
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        //讓img顯示在label1內
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
    QMessageBox::information(this,"版權",tr("本軟體版權所有者為：天津職業技術師范大學。若果使用，請聯繫：lilizong@gmail.com"));
}

void MainWindow::on_about_triggered()
{
    QMessageBox::information(this,"關於",tr("本軟體目前版本為1.0，由李立宗等人開發。若果有問題，歡迎聯繫：lilizong@gmail.com"));
    return;
}

//分析圖形特征
void MainWindow::getFeature(cv::Mat m,float a[25])
{
    int M,N;  //用來儲存圖形m的長寬
    int i,j;
    M=m.cols;
    N=m.rows;
    for(i=0;i<25;i++)
        a[i]=0;
    //轉為灰階圖形
    cv::cvtColor(m,m,COLOR_RGB2GRAY);
    //轉為二值圖形
    cv::threshold(m,m,100,255,THRESH_BINARY);
    //將圖形劃分為5*5個子塊，計算每塊像素值的和
    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
            if(m.at<uchar>(i,j)==255)
            {
                a[i/(M/5)*5+j/(N/5)]++;
            }
    //計算目前像素塊的平均值
    for(i=0;i<25;i++)
    {
        a[i]=a[i]/((M/5)*(N/5));
    }
}
//計算歐式距離
float MainWindow::ouDistance(float a[25],float b[25])
//這個函數不要忘記寫MainWindow的類別關系！
{
    int i;
    float distance=0;
    //不要忘記了起始化置零，否則出錯！！！
    //根據歐式距離計算公式，計算距離的平方
    for(i=0;i<25;i++)
        distance+=(a[i]-b[i])*(a[i]-b[i]);
    //對上述計算結果開根號
    distance=sqrt(distance);
    return distance;
}
float  MainWindow::oDistance(float a[25],float b[25])   //這個函數是ouDistance出問題時測試的，並沒有用
{
    int i;
    float distance=0;   //不能忘記置零，會出錯！！！
    //,為了測試ouDistance函數，重新定義了oDistance發現問題，結果再次出現問題一直卻一直在此函數修改。而呼叫函數用的還是ouDistance
    for(i=0;i<25;i++)
        distance+=(a[i]-b[i])*(a[i]-b[i]);
    distance=sqrt(distance);
    return distance;
}


void MainWindow::on_showImage_triggered()
//將與目前測試圖形比對的圖形顯示在label2內
{
    //取得數字結果
    int mini=getResultNumber();
    //色彩空間轉換
    cv::cvtColor(srcImage[mini],srcImage[mini],CV_BGR2RGB);
    //img給予值
    img = QImage((const unsigned char*)(srcImage[mini].data),srcImage[mini].cols,srcImage[mini].rows, srcImage[mini].cols*srcImage[mini].channels(), QImage::Format_RGB888);
    //清理右側的標簽
    ui->label2->clear();
    //調整img大小以比對標簽
    img=  img.scaled(ui->label2->width(), ui->label2->height());
    //在標簽內顯示img
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_showMessage_triggered()
//以訊息框的形式顯示識別結果
{
    int mini=getResultNumber();
    //將目前圖形的比對結果顯示在一個訊息框內
    QMessageBox::information(NULL, "測試結果", "目前測試圖形的識別結果為數字："+QString::number(mini), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
}

void MainWindow::on_ImageAndMessage_triggered()
//同時以標簽和訊息框形式顯示
{
    int mini=getResultNumber();
    //在標簽內顯示
    cv::cvtColor(srcImage[mini],srcImage[mini],CV_BGR2RGB);
    img = QImage((const unsigned char*)(srcImage[mini].data),srcImage[mini].cols,srcImage[mini].rows, srcImage[mini].cols*srcImage[mini].channels(), QImage::Format_RGB888);
    ui->label2->clear();
    img=  img.scaled(ui->label2->width(), ui->label2->height());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    //將目前圖形的比對結果顯示在一個訊息框內
    QMessageBox::information(NULL, "測試結果", "目前測試圖形的識別結果為數字："+QString::number(mini), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
}

int MainWindow::getResultNumber()
{
    int i;
    float min; //用來儲存最小的歐式距離
    int mini;   //用來儲存最小的歐氏距離的數字號。
    getFeature(testImage,testFeature);
    //取得測試圖形的特征值，並將其放到testFeature陣列內。
    for(i=0;i<10;i++)
    {
        QString filePath,fileName,allName;
        filePath="image\\stand\\";    //目前圖形目錄
        fileName=".bmp";       //目前圖形的副檔名
        allName=filePath+"\\"+QString::number(i)+fileName;  //i是檔名，使用QString::number(i)完成將其轉為QString型態，目前為數值型
        String s=allName.toStdString();    //轉為標准的字串型，imread不識別QString型態
        srcImage[i] = cv::imread(s);
    }
    //以下部分用於測試上述程式碼是否能夠將srcImage的值取得到。
    /*
    cv::cvtColor(srcImage[3],srcImage[3],CV_BGR2RGB);
    img = QImage((const unsigned char*)(srcImage[3].data),srcImage[1].cols,srcImage[1].rows, srcImage[1].cols*srcImage[1].channels(), QImage::Format_RGB888);
    ui->label1->clear();
    img=  img.scaled(ui->label1->width(), ui->label1->height());
    ui->label1->setPixmap(QPixmap::fromImage(img));
*/
    // 取得原始數字圖形的特征值。
    for(i=0;i<10;i++)
        getFeature(srcImage[i],srcFeature[i]);
    /*
     * 用於測試中間過程！
    for(i=0;i<25;i++)
                QMessageBox::information(NULL, "Title", QString::number(srcFeature[0][i]), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
  */
    float ouDistanceValue[10]={0};   //儲存目前測試圖形與已知的十個數字圖形之間的歐氏距離
    for(i=0;i<10;i++)
    {
        ouDistanceValue[i]=ouDistance(testFeature,srcFeature[i]);
    }
    //測試下ouDistance有沒有問題。
    /*
     * 用於中間過程的測試
    for(i=0;i<10;i++)
        QMessageBox::information(NULL, "Title", QString::number(ouDistanceValue[i]), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
    */
    mini=0;
    min=ouDistanceValue[0];  //給min賦個初值，假設與數字0的距離最小。
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
 * 參加函數：void MainWindow::on_horizenFlip_triggered()內的注解
*/
}

void MainWindow::on_VerticalAndHorizen_triggered()
{
    cv::flip(testImage,dstImage,-1);
    showLabel(dstImage,ui->label2);
}
/*
 * void flip(InputArray src, OutputArray dst, int flipCode)
 * 參見函數：void MainWindow::on_horizenFlip_triggered()內的注解
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
    ///膨脹動作
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
    //  img=img.scaled(ui->label2->size());  //說明：若果重設圖形大小會導致全黑，無法觀看。這裡僅僅顯示一部分
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
    // 灰階轉換
    cvtColor(testImage,dstImage, CV_RGB2GRAY);
    //定義大小
    Size dsize = Size(ui->label2->width(),ui->label2->height());
    //定義一個目的圖形
    Mat image2 = Mat(dsize,CV_32S);
    //調整大小
    cv::resize(dstImage, image2,dsize);
    //先對圖形進行灰階化，再對QImage進行縮放處理，結果可能會顯示黑色。
    //先對Mat圖形進行縮放，然後再將其轉為QImage。
    //給img給予值
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows,image2.step,  QImage::Format_Indexed8);
    //清理label2
    ui->label2->clear();
    // 將img賦給label2，即主界面內右側的標簽。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}


void MainWindow::on_binValue_triggered()
//圖形二值化
{
    cvtColor( testImage,dstImage, CV_RGB2GRAY );  //先轉換成灰階圖形
    //使用threshold實現二值化
    threshold(dstImage,dstImage, 100, 255,   THRESH_BINARY );
    /*更多threshold函數的實際介紹參見第1章。
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
    //取得右側標簽的大小（label2）
    Size dsize = Size(ui->label2->width(),ui->label2->height());
    //定義一個image2
    Mat image2 = Mat(dsize,CV_32S);
    //調整目的圖形為image2的大小為
    cv::resize(dstImage, image2,dsize);
    //設定imge為image2
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows, image2.cols*image2.channels(), QImage::Format_Indexed8);
    //清理右側標簽（label2）
    ui->label2->clear();
    //在右側標簽內顯示img。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_invertColor_triggered()
//圖形反色
{
    cvtColor( testImage,dstImage, CV_RGB2GRAY );  //先轉換成灰階圖形
    //threshold內參數THRESH_BINARY_INV表示要反色
    //更多函數threshold的介紹參考第1章
    threshold(dstImage,dstImage, 100, 255,  THRESH_BINARY_INV );
    //取得右側標簽的大小（label2）
    Size dsize = Size(ui->label2->width(),ui->label2->height());
    //定義一個image2
    Mat image2 = Mat(dsize,CV_32S);
    //調整目的圖形為image2的大小為
    cv::resize(dstImage, image2,dsize);
    //設定imge為image2
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows, image2.cols*image2.channels(), QImage::Format_Indexed8);
    //清理右側標簽（label2）
    ui->label2->clear();
    //在右側標簽內顯示img。
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
    * 函數的實際介紹看本章5.2.4通道處理部分
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
     * 關於split函數和merge函數可以參考【R通道】中的注解，
     * 即函數：
     *void MainWindow::on_rSpace_triggered()
     * 內的注解
     * 函數實際介紹參考本章5.2.4部分
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
     * 關於split函數和merge函數可以參考【R通道】中的注解，
     * 即函數：
     *void MainWindow::on_rSpace_triggered()
     * 內的注解
     * 函數實際介紹參考本章5.2.4部分
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
    //定義一個image2
    Mat image2 = Mat(dsize,CV_32S);
    //調整目的圖形為image2的大小為
    cv::resize(bgr[0], image2,dsize);
    //設定imge為image2
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows, image2.cols*image2.channels(), QImage::Format_Indexed8);
    //清理右側標簽（label2）
    ui->label2->clear();
    //在右側標簽內顯示img。
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
    //定義一個image2
    Mat image2 = Mat(dsize,CV_32S);
    //調整目的圖形為image2的大小為
    cv::resize(bgr[2], image2,dsize);
    //設定imge為image2
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows, image2.cols*image2.channels(), QImage::Format_Indexed8);
    //清理右側標簽（label2）
    ui->label2->clear();
    //在右側標簽內顯示img。
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
    //定義一個image2
    Mat image2 = Mat(dsize,CV_32S);
    //調整目的圖形為image2的大小為
    cv::resize(bgr[1], image2,dsize);
    //設定imge為image2
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows, image2.cols*image2.channels(), QImage::Format_Indexed8);
    //清理右側標簽（label2）
    ui->label2->clear();
    //在右側標簽內顯示img。
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
    //定義一個image2
    Mat image2 = Mat(dsize,CV_32S);
    //調整目的圖形為image2的大小為
    cv::resize(bgr[0], image2,dsize);
    //設定imge為image2
    img = QImage((const unsigned char*)(image2.data),image2.cols,image2.rows, image2.cols*image2.channels(), QImage::Format_Indexed8);
    //清理右側標簽（label2）
    ui->label2->clear();
    //在右側標簽內顯示img。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_about_2_triggered()
{

}

void MainWindow::on_aboutMe_triggered()
{
    QMessageBox::information(this,"關於",tr("本軟體為手寫數字識別研讀系統，目前版本為1.0，由李立宗等人開發。"));
    return;
}

void MainWindow::on_contacctUs_triggered()
{
    QMessageBox::information(this,"聯繫我們",tr("如有問題請聯繫：lilizong(at)Gmail。QQ群：QT+OpenCV，群號：107416004"));
    return;
}

void MainWindow::on_openLenaJpg_triggered()
{

}

void MainWindow::on_Clear_triggered()
{
    //選單：檔案=>清除
    //清除標簽1的內容。
    ui->label1->clear();
    //清除標簽2的內容。
    ui->label2->clear();

}
