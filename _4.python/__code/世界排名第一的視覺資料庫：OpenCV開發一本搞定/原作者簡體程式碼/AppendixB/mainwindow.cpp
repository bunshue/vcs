#include "mainwindow.h"


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}
//  版权信息：  lilizong[at]gmail.com
MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_openLenaJpg_triggered()
{
    //菜单：文件=>打开测试文件lena.jpg
    //使用imread读取当前路径下"lena.jpg"
    srcImage = cv::imread("lena.jpg");
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setWindowTitle("测试文件不存在");
        msgBox.setText(tr("默认的测试文件不存在，可以用以下两种方式的一种：1）复制一个文件到当前目录下，并命名为lena.jpg. 2)使用自定义方式打开一个自定义文件。"));
        msgBox.exec();
    }
    else
    {
        //将BGR转换为RGB，方便操作习惯
        cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(), QImage::Format_RGB888);
        ui->label1->clear();
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        ui->label1->setPixmap(QPixmap::fromImage(img));
    }
}

void MainWindow::on_exitSystem_triggered()
{
    //菜单：文件=>退出
    exit(0);
}

void MainWindow::on_openCustomeFile_triggered()
{
    //菜单：文件=>打开自定义文件
    QString filename = QFileDialog::getOpenFileName(this,tr("打开自定义文件"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    //读取文件
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setWindowTitle("未找到数据");
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    else
    {
        //将BGR转换为RGB，方便操作习惯
        cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(), QImage::Format_RGB888);
        ui->label1->clear();
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        ui->label1->setPixmap(QPixmap::fromImage(img));
    }
}

void MainWindow::on_restoreFile_triggered()
{
    //菜单：文件=>复原
    //复制srcImage到dstImage。
    srcImage.copyTo(dstImage);
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_copyright_triggered()
{
    //版权
    QMessageBox::information(this,"版权",tr("本软件为《OpenCV编程案例详解》内所使用案例。有关详情请联系出版社或作者：lilizong【at】Gmail.com或者qq群：QT&OpenCV：303230397"));
}

void MainWindow::on_about_triggered()
{
    //关于
    QMessageBox::information(this,"关于",tr("本软件当前版本为1.0，由李立宗等人开发。如果有问题，欢迎联系作者：lilizong【at】Gmail.com或qq群：QT&OpenCV 518998199"));
}

void MainWindow::on_action_triggered()
{

}

void MainWindow::on_CLEAR_triggered()
{
    //菜单：文件=>清除
    //清除标签1的内容。
    ui->label1->clear();
    //清除标签2的内容。
    ui->label2->clear();
}
