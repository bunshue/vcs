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

void MainWindow::on_action_2_triggered()
{
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
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
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
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
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
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
    //順時針無縮放效果
    //定義Point2f
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
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
    //顯示結果
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
    QMessageBox::information(this,"版權",tr("本軟體版權所有者為：天津職業技術師范大學。若果使用，請聯繫：lilizong@gmail.com"));
}

void MainWindow::on_Horizen_triggered()
{
    //水平方向翻轉
    cv::flip(srcImage,dstImage,1);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_about_triggered()
{
    QMessageBox::information(this,"關於",tr("本軟體為電子工業出版社《OpenCV寫程式案例教學》配套程式。聯繫訊息：lilizong@gmail.com，QQ群：518998199"));
    return;
}

void MainWindow::on_openTestFile_triggered()
{
    srcImage = cv::imread("lena.jpg");
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("預設的測試檔案不存在，可以用以下兩種模式的一種：1）複製一個檔案到目前目錄下，並命名為lena.jpg. 2)使用自訂模式開啟一個自訂檔案。"));
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
        //   ui->label1->resize(ui->label1->pixmap()->size());//設定目前標簽為圖形大小
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
        msgBox.setText(tr("找不到資料"));
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
        //   ui->label1->resize(ui->label1->pixmap()->size());//設定目前標簽為圖形大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }
}

void MainWindow::on_vertical_triggered()
{
    //垂直方向上翻轉
    cv::flip(srcImage,dstImage,0);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_horizenAndVertical_triggered()
{
    //水平和垂直方向同時翻轉
    //參數值為-1
    cv::flip(srcImage,dstImage,-1);
    //顯示圖形
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

void MainWindow::on_normalizeFilter_triggered()
{
    //均值濾波
    //使用函數blur，設定預設值。根據需要可以調整為互動輸導入參數數的形式。
    blur( srcImage, dstImage, Size( 7, 7 ), Point(-1,-1) );
    //顯示處理結果
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
    //選單：濾波=>方框濾波=>歸一化
    //呼叫boxFilter，使用預設參數，完成歸一化
    boxFilter(srcImage,dstImage,-1,Size(5,5));
    //顯示處理結果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_NoNormalize_triggered()
{
    //選單：濾波=>方框濾波=>非歸一化
    //呼叫boxFilter,
    //使用Size大小為Size（1,1）時，顯示其原有圖形
    //Size大小超過Size（1，1）時，值全部超過255，在這裡顯示為純白色。
    boxFilter(srcImage,dstImage,-1,Size(1,1),Point(-1,-1),false);
    //顯示處理結果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}


void MainWindow::on_GaussFilter_triggered()
{
    //高斯濾波
    //呼叫函數GaussianBlur
    GaussianBlur( srcImage, dstImage, Size( 7,7 ), 0, 0 );
    //顯示結果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_medianFilter_triggered()
{
    //中值濾波
    //呼叫函數medianBlur，參數采用預設值。
    medianBlur ( srcImage, dstImage, 7 );
    //顯示處理結果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_bilateralFilter_triggered()
{
    //雙邊濾波
    //呼叫bilateralFilter
    bilateralFilter ( srcImage, dstImage, 31, 31*2, 31/2 );
    //顯示處理結果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_Erosion_triggered()
{
    //腐蝕動作
    //定義型態
    int erosion_type;
    erosion_type = MORPH_RECT;
    //定義大小
    int erosion_size = 3;
    //呼叫getStructuringElement
    Mat element = getStructuringElement( erosion_type,
                                         Size( 2*erosion_size + 1, 2*erosion_size+1 ),
                                         Point( erosion_size, erosion_size ) );
    //呼叫腐蝕函數
    erode( srcImage, dstImage, element );
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    // imshow("erode",dstImage);
}

void MainWindow::on_dialation_triggered()
{
    //膨脹
    //定義大小
    int  dilation_size  = 2;
    //定義型態
    int dilation_type;
    dilation_type = MORPH_RECT;
    //呼叫getStructuringElement函數
    Mat element = getStructuringElement( dilation_type,
                                         Size( 2*dilation_size + 1, 2*dilation_size+1 ),
                                         Point( dilation_size, dilation_size ) );
    //呼叫膨脹函數
    dilate( srcImage,dstImage, element );
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    //imshow("dialate",dstImage);
}

void MainWindow::on_opening_triggered()
{
    //開運算
    //定義形狀
    int morph_elem=MORPH_RECT;
    //定義大小
    int morph_size=3;
    //呼叫getStructuringElement
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    //呼叫morphologyEx函數
    morphologyEx( srcImage, dstImage, MORPH_OPEN, element );
    /*
     * MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    */
    //顯示處理結果圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_closing_triggered()
{
    //閉運算
    //定義性轉
    int morph_elem=MORPH_RECT;
    //定義大小
    int morph_size=3;
    //呼叫getStructuringElement
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    //實現閉運算
    morphologyEx( srcImage, dstImage, MORPH_CLOSE, element );
    /*
     * MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    */
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionMorphological_Gradient_triggered()
{
    //Morphological Gradient運算
    //定義形狀
    int morph_elem=MORPH_RECT;
    //定義大小
    int morph_size=3;
    //呼叫getStructuringElement
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    //實現Morphological Gradient運算
    morphologyEx( srcImage, dstImage, MORPH_GRADIENT, element );
    /*
     * MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    */
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_topHat_triggered()
{
    //頂帽變換
    //定義形狀
    int morph_elem=MORPH_RECT;
    //定義大小
    int morph_size=3;
    //呼叫getStructuringElement
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    //設定參數為“MORPH_TOPHAT”
    morphologyEx( srcImage, dstImage, MORPH_TOPHAT, element );
    /* 參數型態
    MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    */
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_blackHat_triggered()
{
    //黑帽變換
    //定義形狀
    int morph_elem=MORPH_RECT;
    //定義大小
    int morph_size=3;
    //呼叫getStructuringElement
    Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );
    //設定參數為“MORPH_BLACKHAT”。
    morphologyEx( srcImage, dstImage, MORPH_BLACKHAT, element );
    /* 參數型態
    MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    */
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_PyrUpAction_triggered()
{
    //呼叫pyUp實現拉近效果
    pyrUp( srcImage, dstImage, Size( srcImage.cols*2, srcImage.rows*2 ));
    //顯示處理結果的局部
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_PyrDownAction_triggered()
{
    //呼叫pyrDown實現拉遠效果
    pyrDown( srcImage, dstImage, Size( srcImage.cols/2, srcImage.rows/2));
    //顯示處理結果的圖形實際大小
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_ResizeUp_triggered()
{
    //呼叫resieze拉近圖形
    cv::resize(srcImage,dstImage,Size( srcImage.cols*4, srcImage.rows*4 ),0,0,3);
    //顯示處理結果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_ResizeDown_triggered()
{
    //呼叫resize拉遠圖形
    cv::resize(srcImage,dstImage,Size( srcImage.cols/4, srcImage.rows/4 ),0,0,3);
    //顯示處理結果圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_cNresize_triggered()
{
    //順時針無縮放效果
    //定義Point2f
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
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
    //顯示結果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_cResize_triggered()
{
    //順時針無縮放效果
    //定義Point2f
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
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
    //顯示處理效果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_antiClockwise_triggered()
{
    //逆時針效果
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
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
    //顯示處理效果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_NFlipResize_triggered()
{
    //零旋轉縮放
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
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
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_Clear_triggered()
{
    //選單：檔案=>清除
    //清除標簽1的內容。
    ui->label1->clear();
    //清除標簽2的內容。
    ui->label2->clear();
}



