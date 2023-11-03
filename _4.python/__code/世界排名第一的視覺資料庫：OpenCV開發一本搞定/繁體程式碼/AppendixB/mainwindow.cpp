#include "mainwindow.h"


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}
//  版權訊息：  lilizong[at]gmail.com
MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_openLenaJpg_triggered()
{
    //選單：檔案=>開啟測試檔案lena.jpg
    //使用imread讀取目前路徑下"lena.jpg"
    srcImage = cv::imread("lena.jpg");
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setWindowTitle("測試檔案不存在");
        msgBox.setText(tr("預設的測試檔案不存在，可以用以下兩種模式的一種：1）複製一個檔案到目前目錄下，並命名為lena.jpg. 2)使用自訂模式開啟一個自訂檔案。"));
        msgBox.exec();
    }
    else
    {
        //將BGR轉為RGB，方便動作習慣
        cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(), QImage::Format_RGB888);
        ui->label1->clear();
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        ui->label1->setPixmap(QPixmap::fromImage(img));
    }
}

void MainWindow::on_exitSystem_triggered()
{
    //選單：檔案=>離開
    exit(0);
}

void MainWindow::on_openCustomeFile_triggered()
{
    //選單：檔案=>開啟自訂檔案
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟自訂檔案"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    //讀取檔案
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setWindowTitle("找不到資料");
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    else
    {
        //將BGR轉為RGB，方便動作習慣
        cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(), QImage::Format_RGB888);
        ui->label1->clear();
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        ui->label1->setPixmap(QPixmap::fromImage(img));
    }
}

void MainWindow::on_restoreFile_triggered()
{
    //選單：檔案=>復原
    //複製srcImage到dstImage。
    srcImage.copyTo(dstImage);
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_copyright_triggered()
{
    //版權
    QMessageBox::information(this,"版權",tr("本軟體為《OpenCV寫程式案例詳解》內所使用案例。有關詳情請聯繫出版社或作者：lilizong【at】Gmail.com或是qq群：QT&OpenCV：303230397"));
}

void MainWindow::on_about_triggered()
{
    //關於
    QMessageBox::information(this,"關於",tr("本軟體目前版本為1.0，由李立宗等人開發。若果有問題，歡迎聯繫作者：lilizong【at】Gmail.com或qq群：QT&OpenCV 518998199"));
}

void MainWindow::on_action_triggered()
{

}

void MainWindow::on_CLEAR_triggered()
{
    //選單：檔案=>清除
    //清除標簽1的內容。
    ui->label1->clear();
    //清除標簽2的內容。
    ui->label2->clear();
}
