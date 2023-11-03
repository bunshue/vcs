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

void MainWindow::on_action_2_triggered()
{
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
    Point center = Point( src.cols/2,src.rows/2 );
    double angle = -50.0;
    double scale = 0.6;
    rot_mat = getRotationMatrix2D( center, angle, scale );
    warpAffine(src, warp_rotate_dst, rot_mat, warp_dst.size() );
    ////OpenCV 1.0的形式
    //IplImage * img=cvLoadImage("baboon.jpg");
    //IplImage *img_rotate=cvCloneImage(img);
    //CvMat M =warp_mat;
    //cvWarpAffine(img,img_rotate, &M,CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS,cvScalarAll(0) );
    //cvShowImage("Wrap2",img_rotate);
    warp_rotate_dst.copyTo(dstImage);

    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));

}

void MainWindow::on_action_4_triggered()
{
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
    Point center = Point( src.cols/2,src.rows/2 );
    double angle = 0;
    double scale = 0.6;
    rot_mat = getRotationMatrix2D( center, angle, scale );
    warpAffine(src, warp_rotate_dst, rot_mat, warp_dst.size() );
    ////OpenCV 1.0的形式
    //IplImage * img=cvLoadImage("baboon.jpg");
    //IplImage *img_rotate=cvCloneImage(img);
    //CvMat M =warp_mat;
    //cvWarpAffine(img,img_rotate, &M,CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS,cvScalarAll(0) );
    //cvShowImage("Wrap2",img_rotate);
    warp_rotate_dst.copyTo(dstImage);

    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}


void MainWindow::on_action_3_triggered()
{
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
    Point center = Point( src.cols/2,src.rows/2 );
    double angle = 50.0;
    double scale = 0.6;
    rot_mat = getRotationMatrix2D( center, angle, scale );
    warpAffine(src, warp_rotate_dst, rot_mat, warp_dst.size() );
    ////OpenCV 1.0的形式
    //IplImage * img=cvLoadImage("baboon.jpg");
    //IplImage *img_rotate=cvCloneImage(img);
    //CvMat M =warp_mat;
    //cvWarpAffine(img,img_rotate, &M,CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS,cvScalarAll(0) );
    //cvShowImage("Wrap2",img_rotate);
    warp_rotate_dst.copyTo(dstImage);

    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));

}

void MainWindow::on_action_triggered()
{
    //顺时针无缩放效果
    //定义Point2f
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
    Point center = Point( src.cols/2,src.rows/2 );
    double angle = -50.0;
    double scale = 1;
    rot_mat = getRotationMatrix2D( center, angle, scale );
    warpAffine(src, warp_rotate_dst, rot_mat, warp_dst.size() );
    ////OpenCV 早期版本的形式
    //IplImage * img=cvLoadImage("baboon.jpg");
    //IplImage *img_rotate=cvCloneImage(img);
    //CvMat M =warp_mat;
    //cvWarpAffine(img,img_rotate, &M,CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS,cvScalarAll(0) );
    //cvShowImage("Wrap2",img_rotate);
    warp_rotate_dst.copyTo(dstImage);
    //显示结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action_5_triggered()
{


}

void MainWindow::on_action_6_triggered()
{


}

void MainWindow::on_action_7_triggered()
{

}

void MainWindow::on_action_8_triggered()
{

}

void MainWindow::on_copyright_triggered()
{
    QMessageBox::information(this,"版权",tr("本软件版权所有者为：天津职业技术师范大学。如果使用，请联系：lilizong@gmail.com"));
}

void MainWindow::on_Horizen_triggered()
{
    //水平方向翻转
    cv::flip(srcImage,dstImage,1);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_about_triggered()
{
    QMessageBox::information(this,"关于",tr("本软件为电子工业出版社《OpenCV编程案例教程》配套程序。联系信息：lilizong@gmail.com，QQ群：518998199"));
    return;
}

void MainWindow::on_openTestFile_triggered()
{
    srcImage = cv::imread("lena.jpg");
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("默认的测试文件不存在，可以用以下两种方式的一种：1）复制一个文件到当前目录下，并命名为lena.jpg. 2)使用自定义方式打开一个自定义文件。"));
        msgBox.exec();
    }
    else
    {
        cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(),  QImage::Format_RGB888);
        ui->label1->clear();
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        ui->label1->setPixmap(QPixmap::fromImage(img));
        //ui->processPushButton->setEnabled(true);
        //   ui->label1->resize(ui->label1->pixmap()->size());//设置当前标签为图像大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }
}

void MainWindow::on_myExit_triggered()
{
    exit(0);
}

void MainWindow::on_openCustomeFile_triggered()
{
    QString filename = QFileDialog::getOpenFileName(this,tr("Open Image"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    else
    {
        cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(),  QImage::Format_RGB888);
        ui->label1->clear();
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        ui->label1->setPixmap(QPixmap::fromImage(img));
        //ui->processPushButton->setEnabled(true);
        //   ui->label1->resize(ui->label1->pixmap()->size());//设置当前标签为图像大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }
}

void MainWindow::on_vertical_triggered()
{
    //垂直方向上翻转
    cv::flip(srcImage,dstImage,0);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_horizenAndVertical_triggered()
{
    //水平和垂直方向同时翻转
    //参数值为-1
    cv::flip(srcImage,dstImage,-1);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_restore_triggered()
{
    // cv::flip(srcImage,dstImage,-1);
    srcImage.copyTo(dstImage);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));

}

void MainWindow::on_about2_triggered()
{

}

void MainWindow::on_about3_triggered()
{

}

void MainWindow::on_actionSobel2_triggered()
{

}

void MainWindow::on_actionSobel_triggered()
{
    Sobel(srcImage,dstImage,srcImage.depth(),1,1);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));


}

void MainWindow::on_actionSobel5_triggered()
{

}

void MainWindow::on_actionLaplacian_triggered()
{
    Laplacian(srcImage,dstImage,srcImage.depth());
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionCanny_triggered()
{
    Mat dstImage2;
    // srcImage = cv::imread("a.jpg");
    //cvtColor(srcImage,srcImage,CV_BGR2RGB);
    // cvtColor(srcImage,dstImage,CV_RGB2GRAY);
    cvtColor(srcImage,dstImage2,CV_BGR2GRAY);
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

void MainWindow::on_normalizeFilter_triggered()
{
    //均值滤波
    //使用函数blur，设置默认值。根据需要可以调整为交互输入参数的形式。
    blur( srcImage, dstImage, Size( 7, 7 ), Point(-1,-1) );
    //显示处理结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}
void MainWindow::on_actionGuiyihua_triggered()
{

}

void MainWindow::on_actionFeiguiyihua_triggered()
{



}
void MainWindow::on_normalize_triggered()
{
    //菜单：滤波=>方框滤波=>归一化
    //调用boxFilter，使用默认参数，完成归一化
    boxFilter(srcImage,dstImage,-1,Size(5,5));
    //显示处理结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_NoNormalize_triggered()
{
    //菜单：滤波=>方框滤波=>非归一化
    //调用boxFilter,
    //使用Size大小为Size（1,1）时，显示其原有图像
    //Size大小超过Size（1，1）时，值全部超过255，在这里显示为纯白色。
    boxFilter(srcImage,dstImage,-1,Size(1,1),Point(-1,-1),false);
    //显示处理结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}


void MainWindow::on_GaussFilter_triggered()
{
    //高斯滤波
    //调用函数GaussianBlur
    GaussianBlur( srcImage, dstImage, Size( 7,7 ), 0, 0 );
    //显示结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_medianFilter_triggered()
{
    //中值滤波
    //调用函数medianBlur，参数采用默认值。
    medianBlur ( srcImage, dstImage, 7 );
    //显示处理结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_bilateralFilter_triggered()
{
    //双边滤波
    //调用bilateralFilter
    bilateralFilter ( srcImage, dstImage, 31, 31*2, 31/2 );
    //显示处理结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_Erosion_triggered()
{
    //腐蚀操作
    //定义类型
    int erosion_type;
    erosion_type = MORPH_RECT;
    //定义大小
    int erosion_size = 3;
    //调用getStructuringElement
    Mat element = getStructuringElement( erosion_type,
                                         Size( 2*erosion_size + 1, 2*erosion_size+1 ),
                                         Point( erosion_size, erosion_size ) );
    //调用腐蚀函数
    erode( srcImage, dstImage, element );
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    // imshow("erode",dstImage);
}

void MainWindow::on_dialation_triggered()
{
    //膨胀
    //定义大小
    int  dilation_size  = 2;
    //定义类型
    int dilation_type;
    dilation_type = MORPH_RECT;
    //调用getStructuringElement函数
    Mat element = getStructuringElement( dilation_type,
                                         Size( 2*dilation_size + 1, 2*dilation_size+1 ),
                                         Point( dilation_size, dilation_size ) );
    //调用膨胀函数
    dilate( srcImage,dstImage, element );
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    //imshow("dialate",dstImage);
}

void MainWindow::on_opening_triggered()
{
    //开运算
    //定义形状
    int morph_elem=MORPH_RECT;
    //定义大小
    int morph_size=3;
    //调用getStructuringElement
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    //调用morphologyEx函数
    morphologyEx( srcImage, dstImage, MORPH_OPEN, element );
    /*
     * MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    */
    //显示处理结果图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_closing_triggered()
{
    //闭运算
    //定义性转
    int morph_elem=MORPH_RECT;
    //定义大小
    int morph_size=3;
    //调用getStructuringElement
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    //实现闭运算
    morphologyEx( srcImage, dstImage, MORPH_CLOSE, element );
    /*
     * MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    */
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionMorphological_Gradient_triggered()
{
    //Morphological Gradient运算
    //定义形状
    int morph_elem=MORPH_RECT;
    //定义大小
    int morph_size=3;
    //调用getStructuringElement
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    //实现Morphological Gradient运算
    morphologyEx( srcImage, dstImage, MORPH_GRADIENT, element );
    /*
     * MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    */
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_topHat_triggered()
{
    //顶帽变换
    //定义形状
    int morph_elem=MORPH_RECT;
    //定义大小
    int morph_size=3;
    //调用getStructuringElement
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    //设置参数为“MORPH_TOPHAT”
    morphologyEx( srcImage, dstImage, MORPH_TOPHAT, element );
    /* 参数类型
    MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    */
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_blackHat_triggered()
{
    //黑帽变换
    //定义形状
    int morph_elem=MORPH_RECT;
    //定义大小
    int morph_size=3;
    //调用getStructuringElement
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    //设置参数为“MORPH_BLACKHAT”。
    morphologyEx( srcImage, dstImage, MORPH_BLACKHAT, element );
    /* 参数类型
    MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    */
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_PyrUpAction_triggered()
{
    //调用pyUp实现放大效果
    pyrUp( srcImage, dstImage, Size( srcImage.cols*2, srcImage.rows*2 ));
    //显示处理结果的局部
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_PyrDownAction_triggered()
{
    //调用pyrDown实现缩小效果
    pyrDown( srcImage, dstImage, Size( srcImage.cols/2, srcImage.rows/2));
    //显示处理结果的图像实际大小
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_ResizeUp_triggered()
{
    //调用resieze放大图像
    cv::resize(srcImage,dstImage,Size( srcImage.cols*4, srcImage.rows*4 ),0,0,3);
    //显示处理结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_ResizeDown_triggered()
{
    //调用resize缩小图像
    cv::resize(srcImage,dstImage,Size( srcImage.cols/4, srcImage.rows/4 ),0,0,3);
    //显示处理结果图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_cNresize_triggered()
{
    //顺时针无缩放效果
    //定义Point2f
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
    Point center = Point( src.cols/2,src.rows/2 );
    double angle = -50.0;
    double scale = 1;
    rot_mat = getRotationMatrix2D( center, angle, scale );
    warpAffine(src, warp_rotate_dst, rot_mat, warp_dst.size() );
    ////OpenCV 早期版本的形式
    //IplImage * img=cvLoadImage("baboon.jpg");
    //IplImage *img_rotate=cvCloneImage(img);
    //CvMat M =warp_mat;
    //cvWarpAffine(img,img_rotate, &M,CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS,cvScalarAll(0) );
    //cvShowImage("Wrap2",img_rotate);
    warp_rotate_dst.copyTo(dstImage);
    //显示结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_cResize_triggered()
{
    //顺时针无缩放效果
    //定义Point2f
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
    Point center = Point( src.cols/2,src.rows/2 );
    double angle = -50.0;
    double scale = 0.6;
    rot_mat = getRotationMatrix2D( center, angle, scale );
    warpAffine(src, warp_rotate_dst, rot_mat, warp_dst.size() );
    ////OpenCV 早期版本的形式
    //IplImage * img=cvLoadImage("baboon.jpg");
    //IplImage *img_rotate=cvCloneImage(img);
    //CvMat M =warp_mat;
    //cvWarpAffine(img,img_rotate, &M,CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS,cvScalarAll(0) );
    //cvShowImage("Wrap2",img_rotate);
    warp_rotate_dst.copyTo(dstImage);
    //显示处理效果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_antiClockwise_triggered()
{
    //逆时针效果
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
    Point center = Point( src.cols/2,src.rows/2 );
    double angle = 50.0;
    double scale = 0.6;
    rot_mat = getRotationMatrix2D( center, angle, scale );
    warpAffine(src, warp_rotate_dst, rot_mat, warp_dst.size() );
    //OpenCV 早期版本的形式
    //IplImage * img=cvLoadImage("baboon.jpg");
    //IplImage *img_rotate=cvCloneImage(img);
    //CvMat M =warp_mat;
    //cvWarpAffine(img,img_rotate, &M,CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS,cvScalarAll(0) );
    //cvShowImage("Wrap2",img_rotate);
    warp_rotate_dst.copyTo(dstImage);
    //显示处理效果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_NFlipResize_triggered()
{
    //零旋转缩放
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
    Point center = Point( src.cols/2,src.rows/2 );
    double angle = 0;
    double scale = 0.6;
    rot_mat = getRotationMatrix2D( center, angle, scale );
    warpAffine(src, warp_rotate_dst, rot_mat, warp_dst.size() );
    // OpenCV早期版本的形式
    //IplImage * img=cvLoadImage("baboon.jpg");
    //IplImage *img_rotate=cvCloneImage(img);
    //CvMat M =warp_mat;
    //cvWarpAffine(img,img_rotate, &M,CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS,cvScalarAll(0) );
    //cvShowImage("Wrap2",img_rotate);
    warp_rotate_dst.copyTo(dstImage);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_Clear_triggered()
{
    //菜单：文件=>清除
    //清除标签1的内容。
    ui->label1->clear();
    //清除标签2的内容。
    ui->label2->clear();
}



