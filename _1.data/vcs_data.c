/**********************************************************
 * Filename	:	vcs_data.c
 * Description	:	vcs¬ÛÃö¸ê®Æ»P¤ù¬qµ{¦¡
 **********************************************************/


³o¼Ë¼g¤]¥i¥H

            if (fileDialog.ShowDialog() == DialogResult.OK)
                pictureBox.ImageLocation = fileDialog.FileName;


¤¸¥ó¥iµø»P§_
            if (pictureList.Visible) {
                pictureList.Visible = false;
                addButton.Visible = false;
                removeButton.Visible = false;
                setButton.Visible = false;
                intervalText.Visible = false;
            }
            else {
                pictureList.Visible = true;
                addButton.Visible = true;
                removeButton.Visible = true;
                setButton.Visible = true;
                intervalText.Visible = true;
            }


BinaryReader	¥H¯S©w½s½X¤è¦¡¥Î ¤G¶i¦ì   §Î¦¡ Åª¨úÀÉ®×
BinaryWriter	¥H¯S©w½s½X¤è¦¡¥Î ¤G¶i¦ì   §Î¦¡ ±N¸ê®Æ¼g¤JÀÉ®×
StreamReader	¥H¯S©w½s½X¤è¦¡¥Î ¦r¤¸¦ê¬y §Î¦¡ Åª¨úÀÉ®×
StreamWriter	¥H¯S©w½s½X¤è¦¡¥Î ¦r¤¸¦ê¬y §Î¦¡ ±N¸ê®Æ¼g¤JÀÉ®×

StreamReaderªº¤èªk¡G
Read		¦ÛÀÉ®×¤¤Åª¨ú¤@­Ó¦r¤¸¡A¨Ã¦^¶Ç¸Ó¦r¤¸ªº¦r¤¸½X(ascii­È)¡C
ReadLine	¦ÛÀÉ®×¤¤Åª¨ú¤@¦C¦r¦ê¡A¥H´«¦æ²Å¸¹¬°¦r¦êµ²§À¡A¨Ã¦^¶Ç¸Ó¦r¦ê¡C
ReadToEnd	±NÀÉ®×¤¤ªº¤å¦r¥þ³¡Åª¨ú¡A¨Ã¥þ³¡¥H¦r¦ê«¬ºA¦^¶Ç¡C
Close		Ãö³¬ÀÉ®×¡A¨Ã¸Ñ°£ÀÉ®×ªº¼g¤JÂê©w¡A¤è«K¨ä¥Lµ{¦¡¨Ï¥Î¡C

StreamWriterªº¤èªk¡G
Write		±N¸ê®Æ¼g¤J¨ì½w½Ä(buffer)¤¤¡A¥iª½±µ¶Ç¤J¤j³¡¤Àªº¸ê®Æ«¬ºA¡C
WriteLine	±N¸ê®Æ¼g¤J¨ì½w½Ä(buffer)¤¤¡A¨Ã¦Û°Ê´«¦æ¡C
Flush		±N½w½Ä¤¤ªº¥Ø«eªº¸ê®Æ¼g¤J¨ìÀÉ®×¤¤¡C


StreamReader sr = new StreamReader(fileName, Encoding.Default);	//Encoding.Default¸Ñ¨MÅª¨ú¤@¯ë½s½XÀÉ®×¤¤¤å¦r¿ù¶Ãªº°ÝÃD




            string str = System.Windows.Forms.Application.StartupPath;
            richTextBox1.Text += "str = " + str + "\n";
            string str2 = str + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            richTextBox1.Text += "str2 = " + str2 + "\n";
            string str3 = "IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            richTextBox1.Text += "str3 = " + str3 + "\n";



MysonLink¤§comport°T®§¡A«öctrl+H¤Á´«text/hex mode




----------------vcs³W¹º ST----------------






dddd	draw¬ÛÃö
ffff	ÀÉ®×¬ÛÃö¡B¸ê®Æ§¨¬ÛÃö
eeee	encoding
ssss	syntax
cccc	control	±±¥ó



¯Â¤å¦r ÀÉ®×ªº¼g¤J»PÅª¥X
¤G¶i¦ì ÀÉ®×ªº¼g¤J»PÅª¥X



¹w­p·s±M®×¡G
vcs_MyPlayer
vcs_FolderFileName
vcs_MysonEdit

My«K±ø¯È
My¤p§@®a

MyNotepad


Åª¤@­ÓbinaryÀÉ¡A¥u¦s¤@³¡¥÷¡A¹F¨ìcutªº¥\¯à

¦n¥Îªºµ{¦¡½X¤ù¬q


delay
draw
syntax	foreach


­n·Ç³Æªºicon
¶}·sÀÉ®×¡B¶}±ÒÀÉ®×¡BÀx¦sÀÉ®×¡BÃö³¬ÀÉ®×
½Æ»s¡B¶K¤W
¦r«¬³]©w¡B¿ï¶µ³]©w¡BÀ°§U¿ï¶µ


¬D¾ÔVisual C# 2008µ{¦¡³]­p¼Ö¬¡¾Ç




vcs

¥~³¡¸ê·½Ãþ
	AGauge
	Digital Meter

·s¼Wªí³æÃþ
	¦bAªí³æ«öÁä¡A§â¸ê®Æ¸ê®ÆÅã¥Ü¦bBªí³æ

NetworkÃþ
ÀË´úºô¸ô³s½u¡BIP¬ÛÃö
WebBrower
§ìºô­¶¸ê®Æ¡B¤å¦r¡Bªþ¹Ï

¼´¥X©Ò¦³ÀÉ¦W¡A¥i¥H¤ñ¹ïÀÉ¦W¡A³o¼Ë·í·j´M¥\¯à¥Î¡A´M§äÀÉ®×®e¶q³Ì¤j³Ì¤pÀÉ®×
¥i±Æ§Ç§_¡H

ÀÉ®×³B²z
hexdump
cat
bin2hex
hex2bin

»s§@binaryÀÉ¤§½d¨Ò
»s§@textÀÉ¤§½d¨Ò







vcs
3M«K±ø¯È
¤pªºsinplot
¤pªºpwm generator


vcs

³Ì¤p¤Æ®É¡A¦b¨t²Î¦C¤WÅã¥Ü

­ìÀÉ¦W	±ý§ïÀÉ¦W	§ï


vcs¦p¦ó§PÂ_¨ì©³¬OUSB1.1ÁÙ¬OUSB2.0¡BUSB3.0¡H

vcs¦p¦ó°µ°ÊºA°O¾ÐÅé°t¸m¡H

vcs¥Ø¼Ð¡G

vcs±±¥óÃþ¡G¦UºØ±±¥óªº¨Ï¥Î
µe¹ÏÃþ¡G	Draw¡B¥­²¾¡B±ÛÂà¡B¦b¹Ï¤ù¤Wµe¹Ï		(¤pµe®a)
¹Ï¤ùÃþ¡G	¹Ï¤ùÅª¨ú¼½©ñ¡B±ÛÂà¡BÂàÀÉ		(ACDSee)
­µ°TÃþ¡G	1. ¼½©ñmp3¡Bwav				(Winamp)
		2. ³B²z­µ®Ä¡Bbeep
¼v¤ùÃþ¡G	¼½©ñ¼v¤ù				(PotPlayer)
ÀÉ®×Á`ºÞÃþ¡G
	1. ·j´M¥þ³¡ÀÉ¦W
	2. ·j´MÀÉ®×
	3. ³B²zÀÉ®×¡G
	3.1. ¶}±Ò
	3.2. §R°£¡B§ï¦W¡B²¾°Ê
	3.3. ´M§ä¬Û¦PªºÀÉ®×

¨t²Î¸ê°TÃþ





vcs ¤jÃþ

¤w¸g°µ¦nªºvcs¤jÃþ¡G
vcs_test_all_01_Richtextbox	§ï¦Wvcs_test_all_01_RichTextBox
vcs_test_all_02_String		¦r¦ê³B²zÃþ
vcs_test_all_03_Network
vcs_test_all_04_Font		¦r«¬Ãþ
vcs_test_all_06_DirectoryFile	ÀÉ®×¤l§¨³B²z		File Directory IOÃþ	ÀÉ®×¦s¨úÃþ	¨Ï¥ÎDirectoryInfo»PFileInfo
vcs_test_all_06_Drive		ºÏºÐÃþ			¨Ï¥ÎDriveInfo
vcs_test_all_06_System		Windows¨t²Î¸ê°TÃþ
vcs_test_all_08_Media		¼v­µÃþ
vcs_test_all_09_Form		ªí³æ¥~Æ[Ãþ
vcs_test_all_10_Math		¼Æ¾ÇÃþ
vcs_test_all_11_Draw		µe¹ÏÃþ
vcs_test_all_12_Date		®É¶¡³B²zÃþ		DateTime


»yªkÃþ				vcs_Syntax
¤¸¥óÃþ	­^¤å??	control?	±±¨î¶µ	vcs_test_all_00_Controls
¤¸¥óÃþ¡B¤¸¥ó¨Ï¥ÎÃþ

»yªk¡B®æ¦¡¡B¡B¡B¡B
Åã¥Ü00123¡BÅã¥Ü0xabcd¡B¡B¡B

ThreadÃþ

¦r¦ê³B²zÃþ
	//±N¤«¦r¸¹²¾°£
	hex = hex.Replace("#", "");

¨ç¦¡¨Ï¥ÎÃþ

¥~Æ[Ãþ
ÃC¦âÃþ

¨Ï¥Î²{¦¨ªºª«¥óÃþ	AGauge¡BDigitalGauge


C# ±Ò°ÊÀ³¥Îµ{¦¡¨Ã¥B¶Ç¤J°Ñ¼Æ
https://dotblogs.com.tw/atowngit/2009/12/26/12681

vcs¨ú±o¤¸¥óÄÝ©Ê¡A¨Ò¦p¡GFont¡BSize¡BBackColor¡BForeColor








----------------vcs³W¹º SP----------------




namespace «Å§iÃþ§O¦¨­û
{
  class foo
  {
    public String strData;
    public int intData;
  }
}

namespace «Å§iÃþ§O¦¨­û
{
  class Program
  {
    static void Main(string[] args)
    {
      foo obj1 = new foo();
      obj1.strData = "¦r¦ê¸ê®Æ³]©w";
      obj1.intData = 100;
      Console.WriteLine("foo Ãþ§Oªº strData ¦¨­û¡G" + obj1.strData);
      Console.WriteLine("foo Ãþ§Oªº intData ¦¨­û¡G" + obj1.intData);
      Console.Read();
    }
  }
}
----------------------
namespace ÄÝ©Ê¦¨­û
{
  class Program
  {
    static void Main(string[] args)
    {
      circle objC1 = new circle();
      Console.Write("½Ð¿é¤J¥b®|¸ê°T¡G");
      objC1.radius = float.Parse(Console.ReadLine());
      Console.WriteLine("¥b®|¡G" + objC1.radius);
      Console.Read(); //¼È°±
    }
  }
}


namespace ÄÝ©Ê¦¨­û
{
  class circle
  {
    private float r;
    public float radius
        {
            get
            {
                return r;
            }
            set
            {
                r = value;
            }
        }
  }
}

----------------------------
        string filename;
        StreamReader fileread;
        StreamWriter filewriter;

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.InitialDirectory = "c:\\"; //³]©w¹w³]¥Ø¿ý
            openFileDialog1.Filter = "¯Â¤å¦rÀÉ(*.txt)|*.txt|©Ò¦³ÀÉ®×(*.*)|*.*"; //¹w³]¶}±ÒªºÀÉ®×Ãþ«¬
            openFileDialog1.Title = "¶}±ÒÂÂÀÉ"; //³]©w¹ï¸Ü¤è¶ôªº¼ÐÃD
            openFileDialog1.RestoreDirectory = true; //³]©w¬O§_¦bÃö³¬¤§«e­nÁÙ­ì¦Ü¥Ø«eªº¥Ø¿ý

            if (openFileDialog1.ShowDialog() == DialogResult.OK)  //°²¦p«ö¤U¶}±Ò«ö¶s®É
            {
                filename = openFileDialog1.FileName; //³]©wÀÉ®×¦WºÙ
                fileread = new StreamReader(filename); //Åª¨úÀÉ®×
                textBox1.Text = fileread.ReadToEnd(); //¦ÛÀÉ®×¥Ø«e¦ì¸mÅª¦ÜÀÉ®×§ÀºÝ
                fileread.Close(); //±NÀÉ®×Ãö³¬
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            saveFileDialog1.InitialDirectory = "D:\\"; //³]©w¹w³]¥Ø¿ý
            saveFileDialog1.Filter = "¯Â¤å¦rÀÉ(*.txt)|*.txt"; //¹w³]±ýÀx¦sªºÀÉ®×Ãþ«¬
            saveFileDialog1.RestoreDirectory = true; //³]©w¬O§_¦bÃö³¬¤§«e­nÁÙ­ì¦Ü¥Ø«eªº¥Ø¿ý
            saveFileDialog1.Title = "¦sÀÉ"; //³]©w¹ï¸Ü¤è¶ôªº¼ÐÃD

            if (saveFileDialog1.ShowDialog() == DialogResult.OK ) //°²¦p«ö¤UÀx¦s«ö¶s®É
            {
                filename = saveFileDialog1.FileName; //³]©wÀÉ®×¦WºÙ
                filewriter = new StreamWriter(filename, false);
                filewriter.Write(textBox1.Text); //±N¸ê®Æ¬y¼g¤J«ü©wªºÀÉ®×¤¤
                filewriter.Close(); //Ãö³¬ÀÉ®×
            }
        }

 ------------------



---------------------------------------------------------------



  namespace Exam2
{
  public class Bicycle
  {
    private string Color;
    private string Style;
    private int Price;

    public void GetData()
    {
        Console.Write("½Ð¿é¤JÃC¦â¡G");
        Color = Console.ReadLine();
        Console.Write("½Ð¿é¤J¨®«¬¡G");
        Style = Console.ReadLine();
        Console.Write("½Ð¿é¤J»ù®æ¡G");
        Price = int.Parse(Console.ReadLine());
    }

    public void DispData()
    {
        Console.WriteLine("¨®ªºÃC¦â¬°¡G" + Color);
        Console.WriteLine("¨®ªº«¬¦¡¬°¡G" + Style);
        Console.WriteLine("¨®ªº»ù®æ¬°¡G" + Price);
    }
  }


  public class RaceBike:Bicycle
  {
      private int Speed;

      public void GetSpeed()
      {
          GetData();
          Console.Write("¿é¤J´X¬qÅÜ³t:");
          Speed = int.Parse(Console.ReadLine());
      }

      public void DispCarData()
      {
          DispData();
          Console.WriteLine("¦¹¨®¬°" + Speed + "¬qÅÜ³t¨®");
      }
  }

  class Program
  {
    static void Main(string[] args)
    {
        RaceBike MyCar = new RaceBike();
        MyCar.GetSpeed();
        MyCar.DispCarData();
        Console.ReadLine();
    }
  }
}


---------------------------------------------------------------

  class Hello
  {
    public void SayHello()
    {
      Console.WriteLine("Hello¡IWorld¡I");
    }
  }

  class Program
  {
    static void Main(string[] args)
    {
      Hello obj =new Hello();
        obj.SayHello();
        Console.Read(); //¼È°±
    }
  }





---------------------------------------------------------------





---------------------------------------------------------------







»¡©ú¡GKeyDown»PKeyPress¤£¦P¦b©ó¡G
KeyDown¥iÅ¥¥\¯àÁä(¦pCtrl Alt F1....)
KeyPress¬OÅ¥¿é¤Jªº¤å¦r(¼Æ¦r¡B¦r¥À©Î¯S®í²Å¸¹)


private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
{
    if (!(e.KeyChar >= '0' && e.KeyChar <= '9'))
    {
        e.Handled = true;
    }
}
»¡©ú¡G³o¸ÌªºtextBox1¡A·|±Æ°£0~9¥H¥~ªº¤å¦r¡A´«¥y¸Ü»¡´N¬O¥uÅã¥Ü¼Æ¦r


vcs»P©I¥sPotPlayer
¥ÎCommand Line©I¥sPotPlayer¼½©ñ¤@ÀÉ
PotPlayerPortable.exe C:\______test_vcs_video\mmm.mp4

¥ÎCommand Line©I¥sPotPlayer¼½©ñ¤l¥Ø¿ý¤º¥þ³¡ÀÉ®×
PotPlayerPortable.exe C:\______test_vcs_video

¥ÎCommand Line©I¥sPotPlayer¼½©ñ¯S©w´X­ÓÀÉ®×¡A­n¥Î¤Þ¸¹¨í°_¨Ó¤Î¥ÎªÅ®æ¹j¶}
PotPlayerPortable.exe "C:\______test_vcs_video\mmm.mp4" "C:\______test_vcs_video\video2.mpg"







using System;	//¨Ï¥ÎSystem¦WºÙªÅ¶¡(namespace)


vcs±ÄUnicode½s½X¨t²Î¡AµL½×¬O¤¤¤å¦r¡B­^¤å¦r¥À©Î²Å¸¹¡A¨C­Ó¦r¤¸¬Òºâ¬O¤@­Ó¦r¤¸¡A¦b°O¾ÐÅé¤¤¬Ò¦û2«ô¡C


³æÀ»·Æ¹«Ä²µo¨Æ¥ó¶¶§Ç¡G
1. MouseDown
2. Click
3. MouseUp

ÂùÀ»·Æ¹«Ä²µo¨Æ¥ó¶¶§Ç¡G
1. MouseDown
2. Click
3. DoubleClick
4. MouseUp


c# WebBrowser Internet Explorer«ü¥O½X¿ù»~

¨Ï¥ÎWebBrowser.ScriptErrorsSuppressed ÄÝ©Ê
webBrowser.ScriptErrorsSuppressed = true;


ªí³æ¡G
Size: ªí³æ¤j¤p
ClientSize: ³]©w©Î¨ú±oªí³æ¤u§@°Ï°ìªº¤j¤p


c# form ªº size ©Mclientsize Œp©Ê ¦³¤°¤\ƒñg°Ú 5

size¬O¾ãƒªwindowªº‡¾«×©M°ª«×¡Cclientsize¬O¤u§@ƒñªº‡¾«×©M°ª«×¡A¥h±¼border©M‡á‹_Œwªº‡¾«×

size¬O¾ãƒªµ¡Ê^¤j¤p¡Aclientsize¬OX®Ø¤j¤p¡A¤]´N¬O„Gµ¡¤f§¤‡á­ìŠ»ºâ°_¡C

            int xx = this.ClientSize.Width;
            int yy = this.ClientSize.Height;
            label3.Text = "XX=" + xx.ToString() + " YY=" + yy.ToString();
            label5.Text = "W = " + this.Size.Width.ToString() + " H = " + this.Size.Height.ToString();
            //this.ClientSize.Width = 800;
            //this.ClientSize.Height = 600;
            this.ClientSize = new System.Drawing.Size(800, 600);


«öAlt+x¥i¥Hª½±µ¸õ¨ìlabelªº¤U¤@­Óindex¶µ¥Ø¡G
            label1.Text = "©m¦W(&N)";
            label2.Text = "¹q¸Ü(&T)";


text¤å¥ó
¤@¦¸Åª¤@¦æ¡AÅã¥Ü¦brichtextbox/listviewùØ¡A
[ÃöÁä¦r]<·j´M>
«ö<·j´M>«á¡A­«·s±½ºË¤@¦¸¡A¦³¹ï¨ì[ÃöÁä¦r]ªº¥ô·N³¡¤À¡AÅã¥Ü¥X¨Ó¡AÅã¥ÜÀÉ¦W»P®e¶q
¥i¥HÂI¿ï¥Î¨t²Î¹w³]µ{¦¡¥´¶}



¤ñ¸û®É¡A¤@«ß¥ý§â¦r¦êªºªÅ¥Õ©Mµu½u¥ý¥h±¼¦b¤ñ¸û¡A¦³¤ñ¨ì¡A¦A§â­ì¥»ªº¦r¦êÅã¥Ü¥X¨Ó¡A
­ì¥»ªº¦r¦ê©M°T®§¡A¥D­n¬OÀÉ®×¤j¤p

¥ý·Ç³Æ¨â­ÓÀÉ®×¡A¹w³]¶}±ÒÀÉ®×­Ó¼Æ¤£¤@¼Ë¡A¤@­Ó10­Ó¡B¤@­Ó1000­Ó¡A¬Ý½sÄ¶¥X¨Óªºµ{¦¡¤j¤p®t¦h¤Ö¡C



´ú¸ÕiconÀÉ®×¦³µL­­¨î¡A¨Ò¦pª½±µ§âjpg§ï¦W¡A¬O§_¦bvcs¤W¥i¥Î¡C
---------------------------------------------------



----------------vcs¤å³¹¤@¤j°ï ST----------------


vcs code
http://www.java2s.com/Code/CSharp/Components/ScreencaptureDemo.htm

DotNet¤é´Á­pºâÅã¥Ü
http://pramaire.pixnet.net/blog/post/7988372

XYZªºµ§°O¥»
http://xyz.cinc.biz/search/label/C%23?max-results=50

¦¡ªù¹P¥Ò	µ{¦¡ªº°O¾Ð
http://welkingunther.pixnet.net/blog

§E¤p³¹ @ ¤j¤º·µ°ó
https://dotblogs.com.tw/yc421206/1


¶Â·t¤ß±¡»P§Þ³N«þ¨©
http://blog.xuite.net/chu.hsing/Think

ªQÅSµ§ºÞÄÑ
http://trufflepenne.blogspot.tw/


olivermodeªº³¡¸¨®æ
http://olivermode.pixnet.net/blog



«Ý¬ã¨s¯}¸Ñvcsºô­¶¡G
https://dotblogs.com.tw/chou/archive/2009/04/12/7986.aspx


C# Examples
Best site for developers
http://csharpexamples.com/




vcs±Ð¾Çyoutube
https://www.youtube.com/user/LeftTechticle



vcs
http://jasonli13168.blogspot.tw/
http://jasonli13168.blogspot.tw/


vcs±Ð¾Ç
http://wang.mis.au.edu.tw/index.php/11-csharp

¦p¦ó¥Î C# ¨ú±o¥»¾÷©Ò¦³ªº IP ¦ì§}
http://blog.miniasp.com/post/2007/12/02/How-to-get-all-ip-at-local-machine-using-c.aspx

¦p¦ó¥Î C# ±N¸ê®Æ¶×¥X¨ì Excel
http://blog.miniasp.com/post/2007/11/28/How-to-transfer-data-to-an-Excel-workbook-by-using-Visual-Studio-2005.aspx

­·¹a
http://windechime.com/en/index.html

¦b.NET¤¤¾Þ§@ÀÉ®×¤Î¥Ø¿ý³Ì¥D­nªº¬OFile¤ÎDirectory¨â­ÓÃþ§O¡A§¡¦bSystem.IOªº©R¦WªÅ¶¡¤U¡C

http://einboch.pixnet.net/blog/post/266428691

need to check
http://cyfangnotepad.blogspot.tw/2013/08/cnet.html
http://cyfangnotepad.blogspot.tw/2013/04/cnet.html
http://cyfangnotepad.blogspot.tw/2013/02/cnet-ab.html

vcs
http://createps.pixnet.net/blog/category/1630969



C#
http://www.eyny.com/forum.php?mod=forumdisplay&fid=553
http://www.eyny.com/forum.php?mod=forumdisplay&fid=553


¦è®L´¶ªº³¡¸¨®æ

http://einboch.pixnet.net/blog

§K¶O¹q¤l®Ñ¡GC# µ{¦¡³]­p
http://cs0.wikidot.com/

C# µ{¦¡¾Ç²ß ¨t¦C	30°ó
http://ithelp.ithome.com.tw/users/20023570/ironman/110

µ{¦¡»y¨¥±Ð¾Ç»x
C »y¨¥¼Ð·Ç¨ç¼Æ®w¤ÀÃþ¾ÉÄý - ctype.h isprint()
http://pydoing.blogspot.tw/2010/07/c-isprint.html

[C#]µ¡Ê^©ñ¤j©ÎŠD¤p¦Z¡A±±¥ó¸ò•Mµ¡Ê^¤ñ¨Ò©ñ¤j

­pºâº~¦rªºµ§¹º
https://dotblogs.com.tw/jeff-yeh/2010/11/08/19291


http://www.codeproject.com/kb/cs/


http://pydoing.blogspot.tw/2013/01/Perl-Tutorial.html
http://pydoing.blogspot.tw/2013/01/Perl-Guide.html

.Net ª¾ÃÑ®a
https://dotblogs.com.tw/hung-chin/1

¬Ý½d¨Ò¾ÇC#-02 switch¡Bfor¡Bforeach»yªk±Ð¾Ç
https://dotblogs.com.tw/hung-chin/2011/09/29/38211

Huan-Lin ¾Ç²ßµ§°O
http://huan-lin.blogspot.com/

«ÛÀM ¹êÅçµ§°O
http://lolikitty.pixnet.net/blog

Visual Studio §Ö³tÁä
http://visualstudioshortcuts.com/


C# ±j¨îÃö³¬µ{¦¡
¥[¤J³o¤@¦æ§Y¥i±j¨îÃö³¬µ{¦¡ :
System.Environment.Exit(System.Environment.ExitCode);


¨Ï¥Î.Net Framework ¡GApplication.DoEvents( ) - ±Ncpu¥æ¥Iµ¹¨ä¥¦À³¥Î¦¡
¨Ï¥Î.Net Framework ¡GSystem.Threading.Thread.Sleep - ­°§Ccpu loading

vcs course
http://www.csie.ntu.edu.tw/~r93057/cs139/
http://www.csie.ntu.edu.tw/~r93057/cs139/
http://www.csie.ntu.edu.tw/~r93057/cs139/ch5.pdf

C# ¿é¥X Excel
http://xyz.cinc.biz/2013/10/csharp-create-excel.html



c#:
[C#]¨Ï¥Î DriveInfo Ãþ§O¨ú±oºÏºÐ¸ê°T
http://www.dotblogs.com.tw/chou/archive/2011/05/31/26665.aspx
[C#]¨Ï¥Î Path Ãþ§O¨ú±oÀÉ®×©Î¥Ø¿ý¸ô®|¸ê°T
http://www.dotblogs.com.tw/chou/archive/2011/05/30/26625.aspx
[C#]±Nµ{¦¡¥[¤J¥kÁä¿ï³æ
https://dotblogs.com.tw/chou/2011/04/17/22945
[C#]½Æ»s¯S©w°ÆÀÉ¦WÀÉ®×¨ì«ü©w¸ê®Æ§¨
https://dotblogs.com.tw/chou/2011/03/31/22186
[C#]­pºâ¥H¦r¦êªí¥Üªº¼Æ¾Ç¹Bºâ¦¡µ²ªG
https://dotblogs.com.tw/chou/2010/12/03/19881
[C#]°Î¦W«¬§O
https://dotblogs.com.tw/chou/2010/08/29/17485
[VB6]¦CÁ|¹q¸£¤w¸g¦w¸Ëªº¦r«¬
https://dotblogs.com.tw/chou/2010/05/27/15462
[C#][VB.NET]Ãö³¬µ{¦¡®ÉÅã¥Ü¹ï¸Ü®Ø¡A¥Î¥H¦A¦¸½T»{¬O§_Ãö³¬
https://dotblogs.com.tw/chou/2009/09/30/10849
[C#]¨ú±o¥»¾÷ºÝ¤W¡A°õ¦æ¤¤¦³ GUI ¤¶­±ªºÀ³¥Îµ{¦¡
https://dotblogs.com.tw/chou/2009/09/30/10848
[C#]°»´ú¬O§_¦³¨ø°£¦¡¦s©ñ¸Ë¸m´¡¤J¡A¨Ï¥Î WndProc ¤èªk»P DriveInfo Ãþ§O
https://dotblogs.com.tw/chou/2009/06/25/8993
	[C#]¨ú±oCPU·Å«×»P«¬¸¹
	https://dotblogs.com.tw/chou/2009/06/21/8927
[C#][VB.NET]¦è¤¸Âà¥Á°ê
https://dotblogs.com.tw/chou/2009/06/21/8925
C#ÀH¤â¤p§Þ¥©
https://dotblogs.com.tw/chou/2009/04/12/7986
[C#]ÅýMonthCalendar¬Y¬q¤é´Á½d³òÅÜ²ÊÅé
https://dotblogs.com.tw/chou/2009/04/11/7975
[C#]±N¼Æ¦r«e­±¸É0¡A¸É¨¬³]©wªºªø«×
https://dotblogs.com.tw/chou/2009/03/20/7574
[C#]¬d¸ßµwºÐ³Ñ¾lªÅ¶¡(³z¹LWinAPI)
https://dotblogs.com.tw/chou/2009/03/11/7450
[C#]¦p¦ó¹F¦¨¥þ°ìÅÜ¼Æªº¥\¯à
https://dotblogs.com.tw/chou/2009/03/11/7438
	[C#][VB.NET]¨ú±o¥Ø«e¿Ã¹õªº¸ÑªR«×
	https://dotblogs.com.tw/chou/2009/03/08/7411
[C#]¦hÀÉ®×½Æ»s¨ì¸ê®Æ§¨ªº¤pµ{¦¡
https://dotblogs.com.tw/chou/2009/02/20/7247
[C#]ªí³æ©ñ¤j©ÎÁY¤p«á¡A±±¨î¶µ¸òµÛªí³æ¤ñ¨Ò©ñ¤j
https://dotblogs.com.tw/chou/2009/02/19/7233
	[C#]¨ú±o§@·~¨t²Îª©¥»
	https://dotblogs.com.tw/chou/2009/02/18/7220
[C#][VB.NET]¬d¸ß§@·~¨t²Î©Ò¦bªººÏºÐ¦ì¸m
https://dotblogs.com.tw/chou/2009/02/17/7213
[C#]¤@­Ó¤£¿ùªº¤pµ{¦¡(¨ãÃþ§O»Pª«¥óªº¬ÛÃö·§©À)
https://dotblogs.com.tw/chou/2009/02/13/7139
[C#]¿é¤J¥Í¤éºâ¬P®y
https://dotblogs.com.tw/chou/2009/02/04/7024




vcs¼Æ¦r®æ¦¡
http://blog.xuite.net/linriva/blog/43023872-%5BC%23%5D+.net+tostring+format+%E6%A0%BC%E5%BC%8F%E8%AA%AA%E6%98%8E+~+%E8%BD%89%E8%B2%BC

¦p¦ó±Nform1ªº­È¶Ç¦Üform2 form3¨Ï¥Î
http://a7419.pixnet.net/blog/post/39233835


some vcs example
http://www.openwinforms.com/




µ{§Çƒ°¡G¤@¨Ç†Gª¾¹Dªº­^¤åŠD‡À
http://www.voidcn.com/blog/zzzili/article/p-592079.html

vcs¸ê°T
http://csharp.net-informations.com/

127´Á .NET µ{¦¡³]­p¤Jªù(¨Ï¥Î C#) ´»´Á¯Z
http://www.csie.ntu.edu.tw/~r93057/summer/cs127/



[C#]¨Ï¥Î Directory Ãþ§O¨ú±o¥Ø¿ý¬ÛÃö¤é´Á»P®É¶¡
http://www.dotblogs.com.tw/chou/archive/2011/05/31/26664.aspx

C# Date() ¤é´Á»P®É¶¡
http://www.eion.com.tw/Blogger/?Pid=1150

®É¶¡®æ¦¡¤Î¤èªk¹B¥Î
https://dotblogs.com.tw/skyline0217/2011/01/26/21047

[C#]¤wª¾®æ¦¡¤é´Á¦r¦êÂà¦^ DateTime
https://dotblogs.com.tw/chou/2010/12/25/20373

C# ¤é´Á»P®É¶¡
http://shioulo.16mb.com/node/686


C# ¦p¦ó¨ú±o¨â­Ó DateTime ¤é´Á¤§¶¡ªº¤Ñ¼Æ
http://blog.miniasp.com/post/2008/01/22/Find-the-difference-between-two-DateTime.aspx



®É¶¡®æ¦¡Âà´«
https://dotblogs.com.tw/grepu9/2013/03/14/96613


c#®É¶¡¬ÛÃö	TimeSpan µ²ºc
https://msdn.microsoft.com/zh-tw/library/system.timespan.aspx


[c#]­pºâ¨â­Ó®É¶¡ ¶¡¹j¬í¼Æ ©Î¤Ñ¼Æ
http://blog.xuite.net/yan.kee/CSharp/27113202

®É¶¡®æ¦¡¤Î¤èªk¹B¥Î
https://dotblogs.com.tw/skyline0217/archive/2011/01/26/21047.aspx



WMI Code Creator¦Û°Ê²£¥ÍWMIªºµ{¦¡½X
https://dotblogs.com.tw/jeff-yeh/archive/2009/11/11/11530.aspx

¦p¦ó¥Î C# ¨ú±o CPU §Ç¸¹
http://blog.miniasp.com/post/2007/12/29/How-to-get-CPU-ID-by-using-CSharp.aspx

C# ¨ú±o µwºÐ¾÷ §Ç¸¹ ( ª«²z / ÅÞ¿è ºÏºÐ)
https://dotblogs.com.tw/powerhammer/2008/03/24/2077
C# ¨ú±o µwºÐ¾÷ §Ç¸¹ ( ª«²z / ÅÞ¿è ºÏºÐ)
https://dotblogs.com.tw/powerhammer/2008/03/24/2142

¦p¦ó¨ú±o µwºÐ ¤Î ¥D¾÷ªO §Ç¸¹
http://wushinetlife.blogspot.tw/2010/07/blog-post_15.html

Åª¨úµwºÐ§Ç¸¹¡B¥D¾÷ªO§Ç¸¹¡BMAC¦ì§}(¨Ï¥Î WMI)
https://lawrencetech.blogspot.tw/2009/03/mac-wmi.html

C# ³z¹L WMI ¨ú±o µwºÐ§Ç¸¹ ( ª«²z / ÅÞ¿è ºÏºÐ)
http://blog.xuite.net/danny72.chen/blog/22988547-C%23+%E9%80%8F%E9%81%8E+WMI+%E5%8F%96%E5%BE%97+%E7%A1%AC%E7%A2%9F%E5%BA%8F%E8%99%9F+(+%E7%89%A9%E7%90%86+%2F+%E9%82%8F%E8%BC%AF+%E7%A3%81%E7%A2%9F)+





vcs sample code.
http://kilean.pixnet.net/blog/post/143351802-my-c%23-windows-form-lesson

±Ð¾Çºô¯¸¡G
Hans-Petter Halvorsen
http://home.hit.no/~hansha/

C# ƒyºâ¤å¥óªºMD5­È
http://www.cnblogs.com/anjou/archive/2008/08/05/1261290.html

Drawing Shapes
http://www.yevol.com/en/vcsharp/applicationdesign/lesson13.htm

http://fecbob.pixnet.net/blog/category/1813376/3
http://fecbob.pixnet.net/blog/post/38132415
http://fecbob.pixnet.net/blog/category/1813350
http://fecbob.pixnet.net/blog/post/38968537

http://fecbob.pixnet.net/blog/post/38121425-c%23%E8%A3%A1%E7%9A%84%E6%96%B9%E5%90%91%E9%8D%B5%E6%B6%88%E6%81%AF%E6%8D%95%E7%8D%B2-


http://readily-notes.blogspot.tw/search/label/C%23%20%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88%E7%AD%86%E8%A8%98
http://johnson560.pixnet.net/blog/post/313121832-c%23-%E8%A6%96%E7%AA%97%E7%A8%8B%E5%BC%8F%E7%AF%84%E4%BE%8B--%E9%8D%B5%E7%9B%A4%E4%BA%8B%E4%BB%B6
http://beckhamnaing.blogspot.tw/2013/12/functionc.html
https://hk.saowen.com/a/f166a8b85c97eaadf6488c1a88c8f5f990e32c42857bda8d4a848a2dbc4681c5
https://hk.saowen.com/a/ef3176c7e08764bf94d96f6a9710d7c9d37cc8d476b69226197fc0427ad71fcd
http://jian-zhoung.blogspot.tw/2012/07/c.html
https://coolong124220.nidbox.com/diary/read/8045380

http://www.dxper.net/thread-562-1-1.html

http://chcooboo.blogspot.tw/2011/04/blog-post_25.html


[C#] Â²Åé¶Ã½XÂà´«
https://dotblogs.com.tw/chou/2013/06/26/106113


VITO ÇU ¾Ç²ßµ§°O	½s½X»P¸Ñ½X
http://vito-note.blogspot.tw/2012/01/blog-post_86.html

½Í½ÍUnicode½s½X
http://flykof.pixnet.net/blog/post/23502355?pixfrom=related

EmguCV¨ú±oÄá¼v¾÷¼v¹³	//try ¤@¤U Julia
https://gnehcic.azurewebsites.net/category/c/page/6/


[C#] ÀÉ®×Åª¼g
http://blog.xuite.net/autosun/study/32576568-[C%23]+%E6%AA%94%E6%A1%88%E8%AE%80%E5%AF%AB


https://msdn.microsoft.com/zh-tw/library/system.io.streamreader%28v=vs.110%29.aspx

https://www.tutorialspoint.com/
https://www.tutorialspoint.com/csharp/

«Ü¦h¤å¥ó
https://doc.lagout.org/Others/

vcs
http://archive.oreilly.com/oreillyschool/courses/csharp2/



.Net ª¾ÃÑ®a
https://dotblogs.com.tw/hung-chin/1

https://dotblogs.com.tw/alonstar
http://www.csharp-examples.net/
http://www.csharp-examples.net/file-creation-modification-time/
http://www.csharp-examples.net/file-creation-modification-time/




mediainfoºô­¶¡G

MediaInfoƒò‡Û¤j¥þ
http://www.cnblogs.com/royzou/archive/2011/09/06/mediainfo_parameter.html
http://www.cnblogs.com/royzou/archive/2011/09/06/csharp_call_mediainfo.html







SerialPort Ãþ§O
https://msdn.microsoft.com/zh-tw/library/system.io.ports.serialport.aspx


SerialPort.ReadExisting ¤èªk ()
https://msdn.microsoft.com/zh-tw/library/system.io.ports.serialport.readexisting.aspx

https://msdn.microsoft.com/en-us/library/windows/apps/xaml/windows.devices.usb.aspx

¥´¦Linstalldate
https://social.msdn.microsoft.com/Forums/en-US/f2eba6ca-e66a-4659-9b96-7e99838a9518/how-to-convert-the-weird-date-and-time-to-normal-date-and-time?forum=csharplanguage

Win32_DiskDrive class
https://msdn.microsoft.com/en-us/library/aa394132(v=vs.85).aspx
https://msdn.microsoft.com/en-us/library/aa394132(v=VS.85).aspx

¦p¦ó¡G¨ú±o¦³ÃöÀÉ®×¡B¸ê®Æ§¨©MºÏºÐ¾÷ªº¸ê°T (C# µ{¦¡³]­p¤â¥U)
https://msdn.microsoft.com/zh-tw/library/6yk7a1b0.aspx






----------------vcs¤å³¹¤@¤j°ï SP----------------


#region ¦Û©w¸qªº¦WºÙ
¤¤¶¡¥[¤J§Aªºµ{¦¡½X
#endregion

openFileDialog1.Multiselect = false;	//³æ¿ï
openFileDialog1.Multiselect = true;	//¤¹³\¦h¿ïÀÉ®×

// °õ¦æºü
ThreadStart serverThreadStart = new ThreadStart(lc.ServerThreadProc);
Thread serverthread = new Thread(serverThreadStart);
serverthread.Start();


DateTime.Parse»{±oªº®æ¦¡¡G

1992¦~5¤ë9¤é
5¤ë9¤é1992¦~
3/11/2006 9:15:30 AM
3/11/2006 9:15:30
3/11/2006 9:15
3/11/2006
2006/3/11
2018/2/21 07:54¤U¤È

----------------¦n¥Îªºµ{¦¡¤ù¬q ST----------------

DateTime start_time = DateTime.Now;
richTextBox1.Text += DateTime.Now.ToString("yyyy-MM-dd hh:mm:ss") + "\n";
string filename = "Stage_Speed_Current." + DateTime.Now.ToString("MMdd.HH.mm") + ".txt";
richTextBox1.Text += "«Ø¥ß®É¶¡ÀÉ®×¡G" + filename + "\n";


int screenWidth = Screen.PrimaryScreen.Bounds.Width;
int screenHeight = Screen.PrimaryScreen.Bounds.Height;
MessageBox.Show("¿Ã¹õ¸ÑªR«×¬° " + screenWidth.ToString() + "*" + screenHeight.ToString());


private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
{
    switch (e.KeyCode)   //®Ú¾Úe.KeyCode¤À§O°õ¦æ
    {
        case Keys.Up:
            richTextBox1.Text += "¤W";
            break;
        case Keys.Down:
            richTextBox1.Text += "¤U";
            break;
        case Keys.Left:
            richTextBox1.Text += "¥ª";
            break;
        case Keys.Right:
            richTextBox1.Text += "¥k";
            break;
        case Keys.PageUp:
            richTextBox1.Text += "PageUp";
            break;
        case Keys.PageDown:
            richTextBox1.Text += "PageDown";
            break;
        default:
            richTextBox1.Text += "KeyCode: " + e.KeyCode.ToString() + "\n";
            break;
    }
}

textBox1.Text = value.ToString("D8");
8¦ì¡A¤£¨¬ªº†D¹s

¤Q¤»¶i¦ìÅã¥Ü¡A¤£¨¬¨â¦ì·|¸É¹s
richTextBox1.Text += i.ToString("X2") + "\n";

¤Q¶i¦ìÅã¥Ü¡A¤£¨¬¨â¦ì·|¸É¹s
richTextBox1.Text += i.ToString("D2") + "\n";

#region/#endregion ¥i¥H¦bVisual Studioµ{¦¡½X½s¿è¾¹ªº¤jºõ¥\¯à®É¡A¥i¥H®i¶}©ÎºPÅ|ªºµ{¦¡½X°Ï¶ô
Â²³æªº»¡¡A´N¬O¥i¥H§â³\¦hªºµ{¦¡½X°Ï¶ô (©ñ¦b¦P¤@­Ó°Ï°ì(region)¤º)¡AÅýµ{¦¡§ó¦n²z¸Ñ¤ÎºÞ²z...

try-catch-finallyªº¥Îªk
try
{
	//µ{¦¡¥D°õ¦æ°Ï©Î¥i¯àµo¥Í¿ù»~ªº¦a¤è
}
catch (Exception ex)
{
	//¨Ò¥~ªº³B²z¤èªk¡A¦p¨q¥XÄµ§i
}
finally
{
	//¤£½×¬O§_µo¥Í¨Ò¥~¨Æ¥ó³£·|°õ¦æªº°Ï¶ô¡A¥i¬Ù²¤
}

    try
    {   //¥i¯à·|²£¥Í¿ù»~ªºµ{¦¡°Ï¬q
        DateTime dt = DateTime.Parse(textBox1.Text);
        richTextBox1.Text += dt.ToString() + "\n";
    }
    catch (Exception ex)
    {   //©w¸q²£¥Í¿ù»~®Éªº¨Ò¥~³B²zµ{¦¡½X
        MessageBox.Show(ex.Message);
    }
    finally
    {
        //¤@©w·|³Q°õ¦æªºµ{¦¡°Ï¬q
        richTextBox1.Text += "DateTime.Parse§¹¦¨\n";
    }


private void delay(int delay)
{
    Application.DoEvents();         //°õ¦æ¬Y¤@¨Æ¥ó¡A¥H¹F¨ì©µ¿ð®ÄªG¡C
    for (int j = 0; j < delay; j++)
        System.Threading.Thread.Sleep(1);
}


try
{   //¥i¯à·|²£¥Í¿ù»~ªºµ{¦¡°Ï¬q
	serialPort1.Open();
}
catch (Exception ex)
{   //©w¸q²£¥Í¿ù»~®Éªº¨Ò¥~³B²zµ{¦¡½X
	MessageBox.Show(ex.Message);
}
finally
{
	//¤@©w·|³Q°õ¦æªºµ{¦¡°Ï¬q
	if (serialPort1.IsOpen)
	{
	    //MessageBox.Show("¤w¸g³s¤W" + serialPort1.PortName);
	}
	else
	    MessageBox.Show(language9[SelectedLanguage, 1]);
	}
}
----------------¦n¥Îªºµ{¦¡¤ù¬q SP----------------




----------------MSDN ST----------------

DockStyle ¦CÁ|
Bottom	The control's bottom edge is docked to the bottom of its containing control.
Fill	All the control's edges are docked to the all edges of its containing control and sized appropriately.
Left	The control's left edge is docked to the left edge of its containing control.
None	The control is not docked.
Right	The control's right edge is docked to the right edge of its containing control.
Top	The control's top edge is docked to the top of its containing control.


PictureBoxSizeMode ¦CÁ|	ex:pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
Normal		¼v¹³·|©ñ¦b¥ª¤W¨¤ªº PictureBox¡C ¦pªG¶W¹L¡A¼v¹³¤wµô°Å PictureBox ¥¦¥]§t¦b¡C
StretchImage	¤¤ªº¼v¹³ PictureBox ©µ¦ù©ÎÁY¤p¥H°t¦X¤j¤p PictureBox¡C
AutoSize	PictureBox ªº¤j¤p½Õ¾ã¬°¬Û·í©ó¥¦©Ò¥]§t¤§¬M¹³ªº¤j¤p¡C
CenterImage	¦pªG¼v¹³Åã¥Ü¦b¤¤¥¡ PictureBox ¤j©ó¬M¹³¡C ¦pªG¼v¹³¤j©ó PictureBox, ¡A¹Ï¤ù·|©ñ¸m¦b¤¤¥¡ PictureBox ©Mµô°Å¥~½t¡C
Zoom		¼v¹³ªº¤j¤p·|¼W¥[©Î´î¤Öºû«ù¤j¤p¤ñ¨Ò¡C


PictureBox.Load ¤èªk

¨Ò¥~ª¬ªp
InvalidOperationException	url ¬° null ©ÎªÅ¦r¦ê¡C
WebException			url «üªº¬OµLªk¦s¨úºô¯¸¤Wªº¼v¹³¡C
ArgumentException		url ¬O«ü¤£¬O¼v¹³ªºÀÉ®×¡C
FileNotFoundException		url °Ñ¦Ò¤£¦s¦bªºÀÉ®×¡C

"InvalidOperationException=" + InvalidOperationException.
WebException
ArgumentException
FileNotFoundException

FormStartPosition ¦CÁ|
CenterParent		ªí³æ·|¸m¤¤ªº¤÷ªí³æ½d³ò¤º¡C
CenterScreen		ªí³æ·|¶°¤¤¦b¥Ø«eªºÅã¥Ü¡A¨Ã¥B¨ã¦³«ü©wªºªí³æªº¤j¤p¡C
Manual			ªí³æªº¦ì¸m¥Ñ Location ÄÝ©Ê¡C
WindowsDefaultBounds	ªí³æ¦ì©ó Windows ¹w³]¦ì¸m¡A¨Ã¥B¨ã¦³¨ú¨M©ó Windows ¹w³]ªº¬É­­¡C
WindowsDefaultLocation	ªí³æ¦ì©ó Windows ¹w³]¦ì¸m¡A¨Ã¥B¨ã¦³«ü©wªºªí³æªº¤j¤p¡C

ex:
// Set the start position of the form to the center of the screen.
this.StartPosition = FormStartPosition.CenterScreen;



----------------MSDN SP----------------




eeee
¥xÆWªººô­¶±`¥Îªº½s½X¬°BIG5¡BUTF-8
­»´äªººô­¶±`¥ÎHK-SCS¡BUTF-8
¤j³°ªººô­¶±`¥ÎGBK¡BUTF-8
¤é¥»ªººô­¶±`¥ÎJIS¡BUTF-8



Filter¼gªk¡G
¿ï¶µ¦WºÙ1|¹LÂo³W«h1|¿ï¶µ¦WºÙ2|¹LÂo³W«h2|...
ex:
"JPGÀÉ|*.jpg|GIFÀÉ|*.gif|©Ò¦³ÀÉ®×|*.*"






¹ï¸Ü®ØªºFilter»PFilterIndex¡G

Filter  ­n¦b¹ï¸Ü¤è¶ô¤¤Åã¥ÜªºÀÉ¿z¿ï¾¹¡A¨Ò¦p¡A"¤å¦rÀÉ(*.txt)|*.txt|©Ò¦³ÀÉ(*.*)||*.*"
FilterIndex  ¦b¹ï¸Ü¤è¶ô¤¤¿ï¾ÜªºÀÉ¿z¿ï¾¹ªº¯Á¤Þ¡A¦pªG¿ï²Ä¤@¶µ´N³]¬°1

// ¥[¤JÀÉ®×¹LÂo±ø¥ó
openFileDialog1.Filter = "save files (*.sav)|*.sav|All files (*.*)|*.*";
openFileDialog1.Filter = "Image Files(*.BMP;*.JPG;*.GIF)|*.BMP;*.JPG;*.GIF";
openFileDialog1.Filter = "¹Ï¤ùÀÉ|*.jpg|*.bmp|*.png|©Ò¦³ÀÉ|*.*";
openFileDialog1.Filter = "*.jpg;*.png;*.bmp|*.jpg;*.png;*.bmp";
openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";

vcs¦p¦ó­­©wƒUÏú‰ã®×®æ¦¡
openFileDialog1.Filter = "exe files (*.exe)|*.exe|All files (*.*)|*.*";     //­­©wÀÉ®×®æ¦¡
openFileDialog1.Filter = "Excel ¬¡­¶Ã¯ (*.xlsx)|*.xlsx|Excel 97-2003 (*.xls)|*.xls|¤å¦rÀÉ (Tab ¦r¤¸¤À¹j) (*.txt)|*.txt";


openFileDialog1.Filter="¤å¦rÀÉ|*.*|C#¤å¥ó|*.cs|©Ò¦³ÀÉ|*.*";
openFileDialog1.FilterIndex=2;

eeee
µù: Encoding.GetEncoding(950) == Encoding.GetEncoding("big5")


protected override void OnKeyPress(KeyPressEventArgs e)
{
    base.OnKeyPress(e);

    if (ReadOnly) return; //°ßÅª¤£³B²z
    if (_maxByteLength == 0) return; //¨S³]©wMaxByteLength¤£³B²z
    if (char.IsControl(e.KeyChar)) return; //Backspace, Enter...µ¥±±¨îÁä¤£³B²z

    int textByteLength = Encoding.GetEncoding(950).GetByteCount(Text + e.KeyChar.ToString()); //¨ú±o­ì¥»¦r¦ê©M·s¦r¦ê¬Û¥[«áªºByteªø«×
    int selectTextByteLength = Encoding.GetEncoding(950).GetByteCount(SelectedText); //¨ú±o¿ï¨ú¦r¦êªºByteªø«×, ¿ï¨ú¦r¦ê±N·|³Q¨ú¥N
    if (textByteLength - selectTextByteLength > _maxByteLength) e.Handled = true; //¬Û´î«áªø«×­Y¤j©ó³]©w­È, «h¤£°e¥X¸Ó¦r¤¸
}

private void button1_Click(object sender, EventArgs e)
{
    //byte[] byteStr = Encoding.Default.GetBytes(textBox1.Text); //¨Ï¥ÎDefault¤èªk¦b«D¤¤¤å¨t²Î¤U¥i¯à·|¦³°ÝÃD, ·PÁÂBibby«ü¥¿
    byte[] byteStr = Encoding.GetEncoding("big5").GetBytes(textBox1.Text); //§âstringÂà¬°byte
    label1.Text = byteStr.Length.ToString(); //¨úbyteªºªø«×, ¤¤¤å¦r´N·|ºâ2½X¤F
}


ºô¯¸ico
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
<link rel="icon" href="/favicon.ico" type="image/x-icon">


´O¤Jyoutube
<iframe width="560" height="315" src="//www.youtube.com/embed/oPQKtwC1mh0" frameborder="0" allowfullscreen></iframe>


ffff
c# txt ±N¤å¦rªþ¥[¦Ü²{¦³ªºÀÉ®×
using (System.IO.StreamWriter file = new System.IO.StreamWriter(@"C:\Users\Public\TestFolder\WriteLines2.txt", true))
{
    file.WriteLine("Fourth line");
}

cccc
ASP.NET C# ­pºâCheckListBox ³Q¿ï¨ú­Ó¼Æ
ArrayList values =newArrayList();

for(int counter =0; counter <list.Items.Count; counter++)
{
	if(list.Items[counter].Selected)
	{
	   values.Add(list.Items[counter].Value);
	}
}

ffff

Listing all files in a specified folder

//FIND ALL FILES IN FOLDER
System.IO.DirectoryInfo dir = new System.IO.DirectoryInfo(Location);
foreach (System.IO.FileInfo f in dir.GetFiles("*.*"))
   {
   //LOAD FILES
   ListViewItem lSingleItem = listView1.Items.Add(f.Name);
   //SUB ITEMS
   lSingleItem.SubItems.Add(Convert.ToString(f.Length));
   lSingleItem.SubItems.Add(f.Extension);
   }

Listing all folders in a specified folder
//FIND ALL FOLDERS IN FOLDER
TreeNode Main =  treeView1.Nodes.Add("Folders in: " + Location);
Main.Tag = "";
   foreach (System.IO.DirectoryInfo g in dir.GetDirectories())
       {
       //LOAD FOLDERS
       TreeNode MainNext = Main.Nodes.Add(g.FullName);
       MainNext.Tag = (g.FullName);
       }


C# µ§°O¡G¨Ï¥Î var «Å§iÁô§t«¬§O
C# 3.0 ¼W¥[¤F var ÃöÁä¦r¡A§A¥i¥H¥Î¥¦¨Ó«Å§iÁô§t«¬§O¡A¨Ò¦p¡G

int i = 10;
var j = 10;


³o¨â¦æªº§@¥Î§¹¥þ¬Û¦P¡A³s½sÄ¶¥X¨Óªº IL code ¤]³£¤@­Ó¼Ò¼Ë¡G


ª½±µ¤U¸üÀÉ®×´ú¸Õºô§}
http://old.dylanbeattie.net/cheatsheets/dot_net_string_format_cheat_sheet.pdf

¤£¦P¹q¸£¬Ý¨ìªºµwºÐ§Ç¸¹¬O§_¬Û¦P¡H

¦P¤@­ÓµwºÐ¡BÀH¨­ºÐ¥Î¤£¦PªºPC¨ÓÅª¡A¬O§_·|Åª¨ì¤@¼Ëªº§Ç¸¹¡H
vcs·j´M©Ò¦³µwºÐ¡A¿ï¨úµwºÐ¡AÅã¥Ü¸ÓµwºÐ¸ê°T

¨Ï¥ÎOscar
	VolumeName: SILVER_8G
	VolumeSerialNumber: 700EBBBC

¨Ï¥ÎRomeo
	VolumeName: SILVER_8G
	VolumeSerialNumber: 700EBBBC

¨Ï¥ÎJulia
	VolumeName: SILVER_8G
	VolumeSerialNumber: 700EBBBC

¤º«ØµwºÐ
InterfaceType: IDE
Description: Local Fixed Disk
MediaType: Fixed hard disk media

ÀH¨­ºÐ
InterfaceType: USB
Description: Removable Disk
MediaType: Removable Media

USBµwºÐ
InterfaceType: USB
Description: Local Fixed Disk
MediaType: External hard disk media

©Ò¥H¡A¬O¥Î MediaType ¤À¿ëÀH¨­ºÐ©ÎUSBµwºÐ

eeee
C# GB2312©MUTF8¤¬‹H
public string GB2312ToUtf8(string gb2312String)
{
    Encoding fromEncoding = Encoding.GetEncoding("gb2312");
    Encoding toEncoding = Encoding.UTF8;
    return EncodingConvert(gb2312String, fromEncoding, toEncoding);
}

public string Utf8ToGB2312(string utf8String)
{
    Encoding fromEncoding = Encoding.UTF8;
    Encoding toEncoding = Encoding.GetEncoding("gb2312");
    return EncodingConvert(utf8String, fromEncoding, toEncoding);
}

public string EncodingConvert(string fromString, Encoding fromEncoding, Encoding toEncoding)
{
    byte[] fromBytes = fromEncoding.GetBytes(fromString);
    byte[] toBytes = Encoding.Convert(fromEncoding, toEncoding, fromBytes);

    string toString = toEncoding.GetString(toBytes);
    return toString;
}

C# ¥Í¦¨¦r²Å¦êªº Checksum
private static string CheckSum(string message)
{
    char[] chars = message.ToCharArray();
    int checksum = 0;
    for (int i = 0; i < chars.Length; i++)
    {
        checksum += (int)chars[i];
    }
    checksum = (~checksum & 0xFFFF) + 0x0001;
    return Convert.ToString(checksum, 16).ToUpper();
}

¨Ò¦p¡A¦r²Å¦ê¡§1234567890¡¨ ªº CheckSum ƒo¡G¡§FDF3¡¨

C# CRC8®ÕJ
http://www.cnblogs.com/anjou/archive/2011/10/19/2217783.html




cccc

ToolTip¼gªk¡G
private void Form1_Load(object sender, EventArgs e)
{
    //¥ý¥[¤JToolTip±±¨î¶µ
    //toolTip1.SetToolTip(±±¨î¶µ¦WºÙ, "­n´£¥Üªº¦r");
    toolTip1.SetToolTip(button19, "À°Button¥[¤J·Æ¹«²¾¹L¥h®Éªº´£¥Ü¤å¦r");
}

ToolTip´£¥Ü±±¨î¶µ±`¥Îªº¤èªk¡G
        public Form1()
        {
            InitializeComponent();
            this.Width = 850;
            this.Height = 600;
            richTextBox2.Focus();
            toolTip1.SetToolTip(button12, "XXXXXXXXXXXXXXXXXX");
        }




----------------¤£¬OVCS ST----------------

----------------¤£¬OVCS SP----------------




----------------BLDC ST----------------



©T©w¥[¤@­Ótoggle GPIO
comparator triggers
PWM ´«¬Û

FW °O CW 546231		CCW 645132

¤H­n¨Ó¬ÝCMPBCDªº¶¶§Ç¡BCMP trigger PWM¡BÂoªi¶¶§Ç¡B§ï¬Ý¤Wª@½t¤U­°½t¤è¦V




¤@ª½«öbutton¡A
¨C¦¸³£µo¤@­Ó©R¥Oµ¹¤U¦ì¡A
¨C¦¸¤U¦ì³£toggle gpio¡A
¬Ý¬Ý³Ì§Ö¤ÏÀ³¬O¦h§Ö¡C

¤U¦ì¤@ª½µo©R¥O¥X¨Ó¡A¤W¦ìÁYµu¼´rx buffer¶g´Á¡A¬Ý¬Ý³Ì§Ö³t«×¬O¦h¤Ö¡H


§¹¾ãª©
USE_FULL

Â²¼äª©
USE_COMPACT
¤Àputtyª©©MMysonLinkª©

putty¤@«ßVR½Õ±±
MysonLink¤ä´©VR½Õ±±¡B¤Î¤W¦ì±±¨î

¤£½×FULL©ÎCOMPACT¡A¤£½×NORMAL_MODE©ÎVR_MODE¡AMysonLink©R¥O¤@¨Ó¡A¤@«ß°±¥ÎVR

_ALIVE¶¶¹D¤W¶Ç§¹¾ãª©©ÎÂ²¼äª©
_FULL		0
_COMPACT	1

­Y¬OÂ²¼äª©¡A«h¤@«ß¥ÎVR±±¨î
­Y¬O§¹¾ãª©¡A«h¤@«ß¥ÎMysonLink±±¨î

¦ý¥i¥H¥ÎMysonLink¨Ó§ïÅÜ




¤W¦ìget¸ê®Æ¡A
«ö¤Fget«á¡Atextbox¥ýÅÜ¦¨disabled©Î¬OÅÜ¦â¡A
µ¥±o¨ì¸ê®Æ«á¡A¦A«ì´_¥¿±`¡C
­Y¸ê®Æ¤£¥¿½T¡A³]ªk³qª¾¡C
¦h¤@­Óget all«öÁä¡C

¥[¤@­Ómessage text box¡A©Î³\©Mtarget³q¥Î¡C

mysonlinkµ¹·s¨å¥Î¡A
¥u­n¯àÅã¥ÜÂà³t¡Bduty¡BVR¡Bcontrol´N¦n¡C

acceleration§ï¦¨¤U©Ô¦¡¿ï³æ
0 very slow	200
1 slow
2 medium	100
3 fast
4 very fast	35
©Î³\¤]¥i¥H¥Î¶ñ¼Æ¦r¡C¨Ã¥Î¨âºØ¡C

slow modify¡A­n¤£­n¥Îcheck box¨Ó¿ï¾Ü¡C

vcs mysonlink
¥¿¤ÏÂà¿W¥ß³]©w
³]©wmax speed§ïÅÜ»öªí¡A§ï¦¨«öEnter´N³]©w¡C

¸ÕµÛ¬Û®e©ó¤@ªê¡C



MysonLink
µwÅéª©¥»
Hardware Name & Version
Firmware Name & Version
Software Name & Version

Current Sense Resistor
PGA gain
VBUS ratio
³]Gate Driver Polarity
¤W¤UÁu¤§dead Time
¥Í²£°Ñ¼Æ
Hardware Serial
Hardware Date
Customer	//«È¤áªº¦W¦r
FW Serial
®Õ¥¿
Calibrate VBUS
Calibrate Current
Firmware Update
³]Baud rate, 9600 default


Â²¼äª© Mysonlink¤U¦ì¥u­n ¤W¶Çduty¡BÂà³t¡BVR¡A¦A¦h±Ò°±
CW/CCW

tabControl¥[¡GRecord­¶¡BADC´ú¸Õ­¶¡B¬Û¦ì¸ÉÀv½Õ¸Õ­¶
RecordÂà³t¡Bduty¡A©Mtarget_speed¡Breal_speed¡Bmax_speed¡Bmin_speedµe¦b¤@°_¡C


§ï¤F¡ã¡ã¡ã¡ã
Â²¼äª©µ{¦¡¡A±q¨S¦³Mysonlink¥[¤WMysonlink
¥[¤JÀÉ®×¡GSetup.h¡BCS8963_BLDC.h¡BCS8963_Compact_Function.h
KeilC±M®×¥[¤JCS8963_MysonLink.c¡BCS8963_Compact_Function.c

¬O§_§ï¦¨¹w³]´N¬Oslow modify

MysonLink¥[¤@­Ólog¤@«ß¥´¦Lhex®æ¦¡¡A·í¦¨MyLink¥Î¡ã¡ã

mysonlink +
ADC¡BCMP¡BDAC¤§¹qÀ£ºâ¦^¼Æ¦r¡B¼Æ¦r¦A¶ñ¦^¹qÀ£¡AÀ³±ÄµL±ø¥ó¶i¦ìªk
MysonLink
+ putty mode
+ hex mode
+ ´ú¸Õscript


¤W¦ì¶}¾÷®É¶¡
¤W¦ì¶}¾÷²Ö­p®É¶¡
¤U¦ì¶}¾÷²Ö­p®É¶¡
°¨¹F¹BÂà®É¶¡
¤U¦ìµ{¦¡±Ò°Ê®É¶¡
¤U¦ìµ{¦¡¨Ï¥Î²Ö¿n®É¶¡



----------------BLDC SP----------------


·Ç³Æ¦UºØ½s½XªºÀÉ®×

¦³µL¤é¤å¡BÂ²¤¤¡B¥¿¤¤³£¤@¼Ëªº¦r¦ê

¤é¤å¸Öµü¡H

¬O§_§O¤HªºinstallDate½d¨Òµ{¦¡¥´¦L¡A¥Îconsole mode´N¥i¥HÅã¥Ü¡H

http://jjnnykimo.pixnet.net/blog/post/21585509





byte[] msg = Encoding.ASCII.GetBytes("ABCD");
byte[] b;
b = System.Text.Encoding.UTF8.GetBytes("Hello Server");
b = System.Text.Encoding.UTF8.GetBytes("Hi");
b = System.Text.Encoding.UTF8.GetBytes("³o¬O " + myPublicIP + " ¸ê®Æ : " + i++);
b = System.Text.Encoding.UTF8.GetBytes("³o¬O'¦øªA¾¹'¦^¶Çªº°T®§ ~ " + i++);

string receive = System.Text.Encoding.UTF8.GetString(MyClient.uc.Receive(ref MyClient.otherIP));
string myPicIP = System.Text.Encoding.UTF8.GetString(uc.Receive(ref servrIP));
string receive = System.Text.Encoding.UTF8.GetString(uc.Receive(ref servrIP));
string receive = System.Text.Encoding.UTF8.GetString(uc.Receive(ref ipep));
string myPicIP = System.Text.Encoding.UTF8.GetString(uc.Receive(ref servrIP));
string receive = System.Text.Encoding.UTF8.GetString(uc.Receive(ref servrIP));
string receive = System.Text.Encoding.UTF8.GetString(MyClient.uc.Receive(ref MyClient.otherIP));



http://k-k-club.blogspot.tw/search/label/C%23?updated-max=2013-03-18T22:18:00-07:00&max-results=20&start=2&by-date=false


MD5 SHA
https://dotblogs.com.tw/jeff-yeh/2009/02/23/7269



Åª¤JBIG5½s½XªºÀÉ®×¦ÜUTF8½s½Xªº¦r¦ê


byte[] big5Bytes = null;

string FilePath = Server.MapPath("~/txt/test.txt");

using (System.IO.FileStream fs = new System.IO.FileStream(FilePath, System.IO.FileMode.Open))
 {
    //Åªbig5½s½Xbytes
    big5Bytes = new byte[fs.Length];
    fs.Read(big5Bytes, 0, (int)fs.Length);
 }

//±Nbig5Âà¦¨utf8½s½Xªºbytes
byte[] utf8Bytes = System.Text.Encoding.Convert(System.Text.Encoding.GetEncoding("BIG5"), System.Text.Encoding.UTF8, big5Bytes);

//±Nutf8 bytesÂà¦¨utf8¦r¦ê
System.Text.UTF8Encoding encUtf8 = new System.Text.UTF8Encoding();

string utf8Str = encUtf8.GetString(utf8Bytes);

Response.Write(utf8Str);

¦p¦ó°µ¦r¦ê½s½Xªº°Ê§@,BIG5 to UTF8

byte[] b=Encoding.Default.GetBytes(a);//±N¦r¦êÂà¬°byte[]
MessageBox.Show(Encoding.Default.GetString(b));//ÅçÃÒÂà½X«áªº¦r¦ê,¤´¥¿½TªºÅã¥Ü.
byte[] c = Encoding.Convert(Encoding.Default, Encoding.UTF8, b);//¶i¦æÂà½X,°Ñ¼Æ1,¨Ó·½½s½X,°Ñ¼Æ¤G,¥Ø¼Ð½s½X,°Ñ¼Æ¤T,±ý½s½XÅÜ¼Æ
MessageBox.Show(Encoding.UTF8.GetString(c));//Åã¥ÜÂà¬°UTF8«á,¤´¯à¥¿½TªºÅã¥Ü¦r¦ê


UTF8ÂàBIG5
    public static string ConvertUTF8toBIG5(string strInput)
    {
        byte[] strut8 = System.Text.Encoding.Unicode.GetBytes(strInput);
        byte[] strbig5 = System.Text.Encoding.Convert(System.Text.Encoding.Unicode, System.Text.Encoding.Default, strut8);
        return System.Text.Encoding.Default.GetString(strbig5);
    }


RichTextBox¦ü¥G¨S¦³¿ìªkÅý¤£¦P°Ï¶ô¤å¦rÅã¥Ü¤£¦P¦r«¬¡BÃC¦â

Convert UTF-8 to Chinese Simplified (GB2312)

byte[] bytes = Encoding.GetEncoding("gb2312").GetBytes(text);



MD5ªº¥þ†ï¬Omessage-digest algorithm 5(«H®§-ºK­nºâªk)


using System.Security.Cryptography;



result: ed076287532e86365e841e92bfc50d8c
  ! is: ed076287532e86365e841e92bfc50d8c.

// This code example produces the following output:
//
// The MD5 hash of Hello World! is: ed076287532e86365e841e92bfc50d8c.
// Verifying the hash...


µL±ø¥ó¶i¦ì¤§¨ç¼Æ


¦³µL¥i¯à°µ¨ì¿ï¥Î#define USE_HD§Y¨Ï¥Î¦Û¤vªº©Ò¦³°Ñ¼Æ­È¡A³o¼Ë¥i¥H¤£¥Î§ï¤Ó¦h


progress bar¥i§_¦³¦hºØÃC¦â¡H¬Ý¦³µLidx¬ÛÃö¡H	§ä¤£¨ì¡A¦ü¥G¥u¦³«e´º¦â¡B­I´º¦â¤GºØÃC¦â¥i½Õ¡C


vcs ¦p¦ó°µ¨ìbutton«öÁäÅã¥Ü¥\¯à¡H

¦p¦ó±qµ{¦¡¤º§ì¨ìrichtextboxªº¦r«¬¤j¤p
	richTextBox1.Text += "¦rÅé¤j¤p¡G" + richTextBox1.Font.Size.ToString();

Ãö³¬µ{¦¡ªº¹ï¸Ü®Ø¡A­nÃþ¦üMegaDownloader
¶}ÀÉ¦sÀÉªº¹ï¸Ü®Ø¡A­nÃþ¦üUltraEdit

¶}±Ò±M®×¡G
¶}±Ò*.sln	//Microsoft Visual Studio Solution

C# / C Sharp examples (example source code) Organized by topic

http://www.java2s.com/Code/CSharp/CatalogCSharp.htm
vcs±Ð¾Ç
https://www.youtube.com/user/LeftTechticle

vcs
http://lolikitty.pixnet.net/blog/post/46745588

1. ¤è®×Á`ºÞ/±M®×¥kÁä/¥[¤J/·s¼W¶µ¥Ø/¸ê·½ÀÉ¡A²£¥ÍResource1.resxÀÉ®×¡C
2. ÂIResource1.resx¡A¿ï¼v¹³¡A¿ï¥[¤J¸ê·½/¥[¤J²{¦³ÀÉ®×¡A¿ï¨ú¿ï¨ú¼v¹³ÀÉ
3. ¨Ï¥Î¡G
	pictureBox1.Image = Resource1.green_ball_icon;
	pictureBox1.Image = Resource1.red_ball_icon;

            //®æ¦¡¤Æ¿é¥X
            double num =1234.5678;
            richTextBox1.Text += num.ToString("00000000") + "\n";
            richTextBox1.Text += num.ToString("########") + "\n";
            richTextBox1.Text += num.ToString("########.00000000") + "\n";
            richTextBox1.Text += num.ToString("#,#") + "\n";
            richTextBox1.Text += num.ToString("#,#,") + "\n";

C#¶}µo¹ê¾Ô1200¨Ò¤ý¤p¬ì¤ý­x

vcs search c# dclock aclock digital clock analog clock
¹w³]button¤§size¡A¥ÎCorelDrawµe¹Ï®É¡A¬Ý¬O§_¥i¥H°µ­è¦n¤j¤p¡C

vcs
¤é´Á½d¨Ò¡G
2016/11/19 21:55	//¶¼®Æ©±
2017/2/8 01:36¤W¤È	//UltraEdit
IMG_20170214_102309.jpg	//¤â¾÷·Ó¬ÛÀÉ®×
putty log:
=~=~=~=~=~=~=~=~=~=~=~= PuTTY log 2016.08.26 09:59:03 =~=~=~=~=~=~=~=~=~=~=~=
=~=~=~=~=~=~=~=~=~=~=~= PuTTY log 2016.08.26 10:39:05 =~=~=~=~=~=~=~=~=~=~=~=



vcs
À³¥ý³]ªk¯àÅª¨úexcelÀÉ®×


ÀÉ®×¸ê®Æ±Æ§Ç
­YÀÉ®×¤£¦s¦b¡A»s³y¤@­ÓÀÉ®×¡A¤º®e¬°¡G

elephant.txt	895		2013/5/10
lion.txt	250		2010/01/31
dog		20		2008/12/05



³]©wÃC¦âªº¤èªk¡G
1. HTML
	button87.BackColor = ColorTranslator.FromHtml("#FF0000");
2. ARGB
	button87.BackColor = Color.FromArgb(255, 255, 0, 255);
3. ¦WºÙ
	button87.BackColor = System.Drawing.Color.FromName("Red");

¥ÑÃC¦â¦WºÙ§ä¨ìARGB

	Color test = System.Drawing.Color.FromName("Control");
	byte a = test.A;
	byte r = test.R;
	byte g = test.G;
	byte b = test.B;
	richTextBox1.Text += "A = " + a.ToString() + "\n";
	richTextBox1.Text += "R = " + r.ToString() + "\n";
	richTextBox1.Text += "G = " + g.ToString() + "\n";
	richTextBox1.Text += "B = " + b.ToString() + "\n";

	richTextBox1.BackColor = Color.FromArgb(255,212,208,200);	//Controlªº¦â½X

test_digital_display
4¦ì¡A«e­±¸É¹s
            clock++;
            digitalDisplayControl1.DigitText = clock.ToString("D4");

            panel1.BackColor = Color.FromArgb(hScrollBar4.Value, hScrollBar1.Value, hScrollBar2.Value, hScrollBar3.Value);
            panel2.BackColor = Color.FromArgb(hScrollBar4.Value, hScrollBar1.Value, 0, 0);
            panel3.BackColor = Color.FromArgb(hScrollBar4.Value, 0, hScrollBar2.Value, 0);
            panel4.BackColor = Color.FromArgb(hScrollBar4.Value, 0, 0, hScrollBar3.Value);
            panel5.BackColor = Color.FromArgb(hScrollBar4.Value, 0, 0, 0);




            int a = 0;
            for (a = 0; a < 255; a ++)
            {
                richTextBox1.Text = a.ToString();
                panel1.BackColor = Color.FromArgb(a, 128, 128, 128);
                Application.DoEvents();         //°õ¦æ¬Y¤@¨Æ¥ó¡A¥H¹F¨ì©µ¿ð®ÄªG¡C
                for (int j = 0; j < 100; j++)
                    System.Threading.Thread.Sleep(1);
            }

this.tabPage8_SVPWM.Parent = null;	ÁôÂÃ¤À­¶

if (tabControl1.SelectedIndex == 7)
{
	banner01.Visible = false;
	banner02.Visible = false;
}


AutoSize¿ïTrue
AutoSizeMode¿ïGrowAndShrink

                    else if (input[1] == _TIMER1)
                    {
                        timer1_th_tl = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: timer1 TH TL = " + Convert.ToString(timer1_th_tl, 16).ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBoxÅã¥Ü°T®§¦Û°Ê±²°Ê¡AÅã¥Ü³Ì«á¤@¦æ
                    }
textbox¦³µL¥i¯à§ïÅÜÃä®ØÃC¦â¡H	¦ü¥G§ä¤£¨ì

vcs
¦P¤@­Ótextbox¡Brichtextbox¤º¡AÃC¦â¤£¤@¼Ë¡A³o¦³¥i¯à¶Ü¡H

»²§U«öÁä (Modifier Key) (SHIFT¡BCTRL ©M ALT)

List view¥[¤W¥iÅý¨Ï¥ÎªÌ¿é¤J¤å¦r¡A¿ï¾Ü¦r«¬§Y¥iÅã¥Ü¥X¨Ó¡C

§ì¾ã­Óµe­±ªº·Æ¹«¦ì¸m

        private void Form1_Load(object sender, EventArgs e)
        {
            //¶}©lºÊÅ¥·Æ¹«¦ì¸m
            System.Threading.ThreadPool.QueueUserWorkItem(new System.Threading.WaitCallback(AutoGetCursorPosition), null);
        }

        void AutoGetCursorPosition(object obj)
        {
            Point pt = new Point();

            while (true)
            {
                Win32Native.Methods.GetCursorPos(out pt);
                try
                {
                    SetText(this.label1, "·Æ¹«¦ì¸m : ( " + pt.X + " , " + pt.Y + " )" );
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.StackTrace.ToString());
                    break;
                }

                System.Threading.Thread.Sleep(50);
            }
        }

range 1 ºñ 60%
range 2 ¶À 20%
range 3 ¬õ 20%

BaseArcRadius		¥D­n¶ê°é¥b®|

RangeInnerRadius	¦âÀô¤º¥b®|
RangeOuterRadius	¦âÀô¥~¥b®|

ScaleLinesMajorInnerRadius	¥D¨è«×¤º¥b®|
ScaleLinesMajorOuterRadius	¥D¨è«×¥~¥b®|

ScaleLinesInterInnerRadius	°Æ¨è«×¤º¥b®|
ScaleLinesInterOuterRadius	°Æ¨è«×¥~¥b®|

ScaleLinesMinorInnerRadius	²Ó¨è«×¤º¥b®|
ScaleLinesMinorOuterRadius	²Ó¨è«×¥~¥b®|

ScaleNumberRadius		¤å¦r¶ZÂ÷¥b®|



AGauge¥Ñ¹w³]­È©ñ¤j 1.5 ­¿¡A¨Ã§ïÅÜÃä¬É³]©w¡G

¥k»öªí³]©w
BaseArcStart		135	135	¥D­n¶ê°é¥b®|¡A¶}©l±½ºË¨¤«×
BaseArcSweep		270	270	¥D­n¶ê°é¥b®|¡AÁ`¦@±½ºË«×¼Æ
MinValue		-100	0	³Ì¤p­È
MaxValue		400	3000	³Ì¤j­È
BaseArcRadius		80	120	¥D­n¶ê°é¥b®|

ScaleLinesMajorInnerRadius	70	105	¥D¨è«×¤º¥b®|
ScaleLinesMajorOuterRadius	80	120	¥D¨è«×¥~¥b®|
ScaleLinesMajorStepValue	50	300

ScaleLinesInterInnerRadius	73	109	°Æ¨è«×¤º¥b®|
ScaleLinesInterOuterRadius	80	120	°Æ¨è«×¥~¥b®|

ScaleLinesMinorInnerRadius	75	112	²Ó¨è«×¤º¥b®|
ScaleLinesMinorOuterRadius	80	120	²Ó¨è«×¥~¥b®|

ScaleNumberRadius		95	142	¤å¦r¶ZÂ÷¥b®|

Range_Idx		0	1	2	²Ä0¶µ³]©w
RangeEnabled		true	true	true
RangeColor		ºñ	¶À	¬õ	¦¹¶µÃC¦â
RangeStartValue		0	2000	2500	¦¹¶µ°_©l­È
RangeEndValue		2000	2500	3000	¦¹¶µµ²§ô­È
RangeInnerRadius(70)	105	105	105	¦âÀô¤º¥b®|
RangeOuterRadius(80)	120	120	120	¦âÀô¥~¥b®|



¦A½Õ¾ã CapsText ¤å¦r»P¦ì¸mCapPosition
¦A½Õ¾ã Center ¦ì¸m	§ï¦¨(160,160)





³q«H¨óÄ³

§ó·sª¬ºA
°±¤î§ó·sª¬ºA

vcs ¥i§_«ö¤W¤UÁä¨Ó¥[´î³t¡H¥ýÅýVCS¯à§ì¨ì¤W¤UÁä
³]©wmax speed®É¡A«öenter§Y®M¥Î¡C¥ýÅýVCS¯à§ì¨ìEnterÁä


vcs DigitalDisplayControl ¼Æ¦ì¼Æ¦rÅã¥Ü
»Ý­n¦³¡G
A1Panel.cs
A1Panel.Designer.cs
DigitalDisplayControl.cs
DigitalDisplayControl.designer.cs
A1PanelGraphics.cs
Globals.cs
6­ÓÀÉ®×
¤è®×Á`ºÞ/¥[¤J/²{¦³¶µ¥Ø ¿ïA1Panel.cs¡BDigitalDisplayControl.cs¡BA1PanelGraphics.cs¡BGlobals.cs
½sÄ¶«á¡A¤u¨ã½c´N·|¦³A1Panel¡BDigitalDisplayControl¥i¥Î¡C

vcs AGuage
»Ý­n¦³ AGauge.cs ¡BAGauge.Designer.cs ¨â­ÓÀÉ®×
¤è®×Á`ºÞ/¥[¤J/²{¦³¶µ¥Ø ¿ïAGauge.cs
½sÄ¶«á¡A¤u¨ã½c´N·|¦³AGuage¥i¥Î¡C


 ¨ä¤¤¡ASystem.Environment.SystemDirectory´N¬OWindow.System32ªº¦ì¸m¡C

¦P²z´N¥i¥H©I¥s«Ü¦h¨t²Î¤º«Ø¤u¨ãÅo~

²¦³º¦Û¤v¼gÁä½LUI¥\¯à¤]¤£®e©ö¡A¯à¥Î¨t²Î¤º«Ø·íµM¬O³Ì¦nªº¡I

©Ò¥H¥u­n¦b¿é¤J®Ø(TextBox)ªºClick¨Æ¥ó¥[¤J³o¤@¦æ¡A´N¯àÅýÄ²±±¿Ã¹õ¨Ï¥Î¿é¤J¥\¯àÅo~

vcs
¦p¤U¦C½d¨Ò©Ò¥Ü¡A±z¥²¶·±N #define «ü¥Üµü©ñ¦bÀÉ®×ªº³»ºÝ¡C
#define DEBUG
//#define TRACE
#undef TRACE

using System;

public class TestDefine
{
    static void Main()
    {
#if (DEBUG)
        Console.WriteLine("Debugging is enabled.");
#endif

#if (TRACE)
     Console.WriteLine("Tracing is enabled.");
#endif
    }
}



//¨ú±o©Ò¦³ºÏºÐ¾÷ªºDriveInfoÃþ§O
DriveInfo[] ListDrivesInfo = DriveInfo.GetDrives();

DriveType ¦CÁ|Ãþ«¬
©R¦WªÅ¶¡:   System.IO

¦¨­û¦WºÙ	´y­z
CDRom		¥úºÐ¾÷¡A¨Ò¦p CD ©Î DVD-ROM¡C
Fixed		©T©w¦¡ºÏºÐ¡C
Network		ºô¸ôºÏºÐ¾÷¡C
NoRootDirectory	¦¹ºÏºÐ¨S¦³®Ú¥Ø¿ý¡C
Ram		RAM ºÏºÐ¡C
Removable	©â¨ú¦¡¦s©ñ¸Ë¸m¡A¨Ò¦p³nºÐ¾÷©Î USB §Ö°{ºÏºÐ¾÷¡C
Unknown		ºÏºÐÃþ«¬¤£©ú¡C

System.IO ©R¦WªÅ¶¡¡G
Directory
DirectoryInfo
DriveInfo
File
FileInfo
FileSystemInfo


google  serialPort1.ReadExisting() 0x3f

http://stackoverflow.com/questions/13980631/0xff-becomes-0x3f

serialPort1.ReadExisting()¬O¦bˆC‡ùªº°òŠß¤WŒÝ¨ú SerialPort †Á¶Hªº¬y©M‰r¤JˆGƒLƒñ¤¤©Ò¦³¥ß§Y¥i¥Îªº¦r…ë¡C
Àq‡P¬O¨Ï¥ÎASCIIEncoding¡A„±ÏúˆC‡ù¤è¦¡…²¤ä«ù0~0x7F¤§…}ªº­È¡A¦pªG­È¶W¥X7F¡A…ÑˆC¦¨3F¡A©Ò¥H0x88he 0xB5@¦¨¤F0x3F,

SerialPort±±¥óªº„±ƒªŒp©Ê„¦¸mƒotrue

¤U¦ì¦^ACK¡A¥u­n²Ä2«ô¥Ñ0x20§ï¬°0x02§Y¥i¡C¨ä¥L°Ñ¼Æ¤@¼Ë¡C

textBox1.ScrollBars = ScrollBars.Vertical;
textBox1.SelectionStart = textBox1.Text.Length;
textBox1.ScrollToCaret();

C# TextBox ¦p¦ó¦Û°Ê±²°Ê¨ì©³³¡
¥i¥H³z¹L SelectionStart ÄÝ©Ê³]©w¤å¦r¤è¶ô¤¤¿ï¨ú¤å¦rªº°_ÂI¡AµM«á¦A³z¹L ScrollToCaret ¤èªk±N±±¨î¶µªº¤º®e±²°Ê¨ì¥Ø«e´¡¤J¸¹ªº¦ì¸m
C# ªí³æÃö³¬®É¡A¥X²{°T®§µøµ¡¡A½T»{¬O§_Ãö³¬ªí³æ
ªí³æÃö³¬®É¡A¥X²{°T®§µøµ¡¡A½T»{¬O§_Ãö³¬ªí³æ
ªí³æÃö³¬®É¡A¥X²{°T®§µøµ¡¡A½T»{¬O§_Ãö³¬ªí³æ
protected override void WndProc(ref Message m)
{
	const int WM_SYSCOMMAND = 0x0112;
	const int SC_CLOSE = 0xF060;
	if (m.Msg == WM_SYSCOMMAND && (int)m.WParam == SC_CLOSE)
	{
		// Åã¥ÜMessageBox
		DialogResult Result = MessageBox.Show("½T©wÃö³¬ªí³æ", "ªí³æ°T®§", MessageBoxButtons.YesNo);
		if (Result == System.Windows.Forms.DialogResult.Yes)
		{
			// Ãö³¬Form
			this.Close();
		}
		else
		{
			return;
		}
	}
	base.WndProc(ref m);
}

¨ú±o¦ê¦C°ð¦ì¸m
¨ú±o©Ò¦³¹q¸£§Ç¦C°ð¦WºÙ
¦b C# ¤¤¡A¸Ó¦p¦ó¼gµ{¦¡¨ú±o©Ò¦³¹q¸£§Ç¦C°ð¦WºÙ
³o®É­Ô¥i¥H¨Ï¥ÎSerialPort.GetPortNames ¤èªk¡A¥\¯à´N¬O¥Î¨Ó¨ú±o¥Ø«e¹q¸£§Ç¦C°ð¦WºÙªº°}¦C
³q°T°ð¦WºÙ¥i±q¨t²Îµn¿ý¨ú±o (¨Ò¦p¡A¦b Windows 98 Àô¹Ò¤¤¡A³o¶µ¸ê°T¦ì©ó HKEY_LOCAL_MACHINE\HARDWARE\DEVICEMAP\SERIALCOMM ¤¤)¡C
¦pªGµn¿ý¤¤¥]§t¹L®É©Î¤£¥¿½Tªº¸ê®Æ¡A«h GetPortNames ¤èªk·|¶Ç¦^¤£¥¿½Tªº¸ê®Æ¡C

this.combobox1.Items.AddRange(System.IO.Ports.SerialPort.GetPortNames());


[C#] ¦p¦ó³]©w¬°¥þ¿Ã¹õ¼Ò¦¡

­n±Nµøµ¡³]©w¬°¥þ¿Ã¹õ¼Ò¦¡¡A¥D­n¦³¨â­Ó³¡¥÷
1. µøµ¡µL®Ø½u
2. µøµ¡¤j¤pµ¥©ó¿Ã¹õ¤j¤p

¦b .NET ªº Windows Form ¤¤¡A¥u»Ý­n³z¹LÂ²³æªº³]©w§Y¥i¹F¨ì³o­Ó®ÄªG¡A
1. Form.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None; //³]©w¦¨µL®Ø½u
2. Form.WindowState = FormWindowState.Maximized; // µøµ¡³]©w¬°³Ì¤j¤Æ

¹w³]¬°§ó·sª¬ºA¡A¥i¤Á´«¬°¤£§ó·sª¬ºA(§Yenable/disable timer1)


header	MYSON
pole_pair
max_speed
min_speed
normal_speed
normal_duty
max_current
oc_en
lock_en


§Ç¸¹
µwÅé¸ê°T
µwÅéª©¥»
¶}¾÷²Ö­p®É¶¡
ª©¥»¸¹½X


IndexOf()	//¨ú±o²Ä¤@­Ó²Å¦X«ü©w¦r¦êªº¯Á¤Þ¦ì¸m
¦^¶Ç-1¡A¥Nªí§ä¤£¨ì¡C

Substring(m,n)	//¨ú±o¦r¦ê¤¤ªº¤l¦r¦ê¡A±q²Äm«ô¶}©l¡A¨ú¥Xn«ô¡C

¬Ý¬Ý·j´M"\t"ªº¦^¶Ç­È¡A§ä¨ì©M§ä¤£¨ì¦³µL¤£¦P¡H¡I¡H¡I

lion	mouse	cat	dog	elephant	eagle	pig	horse

        \tªº¦ì¸m
t1	t2	rowdata
0	4	lion
5	10	mouse
11	14	cat
15	18	dog
19	27	elephant
28	33	eagle
34	37	pig
?	?	horse


38	43	horse


t1=°_©l
t2-t1 = ªø«×
Substring(t1, t2 - t1) // ±qt1¶}©l¡A§ì(t2-t1)«ô¸ê®Æ





vcs

½d¨Ò¥[»¡©ú«öÁä
TextBox¥[multiline
combobox¥[½d¨Ò
¥[comport scan

ÀË¬dÅX°Ê¾¹®e¶q.csproj
ÀË¬dÅX°Ê¾¹®e¶q
DateFunction.csproj

http://ocean2002n.pixnet.net/blog/post/91605623-[c%23]-richtextbox-%E9%A1%AF%E7%A4%BA%E8%A8%8A%E6%81%AF%E8%87%AA%E5%8B%95%E6%8D%B2%E5%8B%95%EF%BC%8C%E9%A1%AF%E7%A4%BA%E6%9C%80%E5%BE%8C%E4%B8%80

http://www.coctec.com/docs/linux/show-post-56595.html

ÅªÀÉ®×¡A¯Â¤å¦rÀÉ¡A¥Îtab°Ï¹j

CopyLotFiles.csproj



----------------vcs ¼È¦s°Ï ST----------------

MyClock
­n¨D¡G

¤Q¶i¨îÂà¤G¶i¨î
Console.WriteLine(Convert.ToString(123, 2));
¤Q¶i¨îÂà¤K¶i¨î
Console.WriteLine(Convert.ToString(123, 8));
¤Q¶i¨îÂà¤Q¤»¶i¨î
Console.WriteLine(Convert.ToString(123, 16));

¤G¶i¨îÂà¤Q¶i¨î
Console.WriteLine(Convert.ToInt32("100111101", 2));
¤K¶i¨îÂà¤Q¶i¨î
Console.WriteLine(Convert.ToInt32("123", 8));
¤Q¤»¶i¨îÂà¤Q¶i¨î
Console.WriteLine(Convert.ToInt32("FF", 16));


----------------vcs ¼È¦s°Ï SP----------------







----------------csharp vcs visual c# 2008 ST----------------

¦P¤@­Ótextbox¡Brichtextbox¤º¡A¤å¦rÃC¦â¤£¼Ë¡A¦ü¥G¤£¤Ó¥i¯à	richtextbox¥i¥H§ïÅÜ³¡¤ÀÃC¦â
button¥i¥H°Ï¤Àªø«öµu«ö¶Ü¡H
button¯à¤£¯à§ï¦¨¶ê§Îªº«ö¶s¡H
¦ü¥GConsole.Writeªº¼gªk¡A¦brichtextbox¤ºÀ³¸Ó¤£¯à¥Î¡C

¦p¦ó§ì·Æ¹«¥kÁä¨Æ¥ó¡H
¦p¦ó§ì·Æ¹«ºu½ü¨Æ¥ó¡H



¥[½d¨Ò¡G

1. ±qµ{¦¡¤º³¡§ïÅÜ¤¸¥ó¥~Æ[¡G¤j¤p¡B¦r«¬¡B¦ì¸m¡B¡B¡B¡B¡B¡B


ÁôÂÃ©ÎÅã¥Üª«¥ó¡G
            button8.Visible = true;
            button9.Visible = false;
            button10.Visible = true;

            richTextBox1.Visible = false;
            richTextBox2.Visible = true;
            richTextBox3.Visible = false;

Åª¨ú¾ã¼Æ©Î¯BÂI¼Æ
            value = int.Parse(richTextBox1.Text);
            value = float.Parse(richTextBox1.Text);
            value = double.Parse(richTextBox1.Text)
            DateTime dt = DateTime.Parse(richTextBox1.Text);	//¤é´Á



¤@­Óvcsµ{¦¡¦p¦óª¾¹D¦Û¤v¦³µL³Q©I¥s¹L¡H	¬Ý¨Ó¥i¥H°»´ú¨ì¡ã¡ã¡ã

­Y¬O¦³error¡AÀ³¸Ó¬O¨C­Ótimer¤¤Â_®ÉÀË¬d¤@¤U¡A¦³error­n¤W¶Ç¡CSend_Error_Speed_Cmd(ERROR_number);

[C#] delegate(©e¬£)

Thread.Sleep ¨ç¼Æ¨Ó¨Ïµ{¦¡µ¥«Ý¤@¬q®É¶¡
Thread.Sleep(0) ªí¥Ü±¾°_0²@¬í¡A§A¥i¯àÄ±±o¨S§@¥Î
MSDNªº»¡©ú¡G«ü©w¹s (0) ¥H«ü¥ÜÀ³±¾°_¦¹½uµ{¥H¨Ï¨ä¥Lµ¥«Ý½uµ{¯à°÷°õ¦æ¡C
Thread.Sleep(0) ¨Ã«D¬O¯uªº­n½uµ{µ¥«Ý0²@¬í¡A·N¸q¦b©ó³o¦¸½Õ¥ÎThread.Sleep(0)ªº·í«e½uµ{½T¹êªº³Q­áµ²¤F¤@¤U¡AÅý¨ä¥L½uµ{¦³¾÷·|Àu¥ý°õ¦æ¡C  Thread.Sleep(0) ¬O§Aªº½uµ{¼È®É©ñ±ócpu¡A¤]´N¬OÄÀ©ñ¤@¨Ç¥¼¥Îªº®É¶¡¤ùµ¹¨ä¥L½uµ{©Î¶iµ{¨Ï¥Î¡A´N¬Û·í©ó¤@­ÓÅý¦ì°Ê§@¡C

­Ó¤H«ØÄ³¡G¦pªG¤£­nÅýµ{¦¡loading¤Ó­« ¤£«ØÄ³¥[¤J Thread.Sleep(0) ¡A¥»¤H´ú¸Õµ²ªG¥[¤J Thread.Sleep(1) ·|¦n«Ü¦h
©Ò¥H«ØÄ³¨Ï¥Î Thread.Sleep(1) ¡C


¨Ï¥Î¤èªk¡G
¥[¤J using System.Threading;
Thread.Sleep(¤@­Ó¼Æ¦r);

Ehu vcs
¤W¶Ç¥Ø«eHallª¬ºA¡B«ùÄòªº¡B³æ¤@ªº¡B°±¤î¡C
¤W¶Ç¥Ø«eVRª¬ºA¡B«ùÄòªº¡B³æ¤@ªº¡B°±¤î¡C

±Ò°Ê®É¡A¥Î¤¤¦ì¥[90«×±Ò°Ê¡A¤]¬O­Ó¿ìªk
¤W¦ì¶ÇPIDµ¹¤U¦ì

»öªí¤å¦r
¦r«¬§ï¥Î¡GConsolas
Border Style §ï¥Î Fixed 3D
¤@¯ëTextBox¥ÎFixedSingle

µwºÐ¥úºÐÀH¨­ºÐÀÉ®×¨t²Î±M¥Î²V¦X½d¨Ò

¦p¦ó¶}±Ò¤@­Ó·sªºform¡AµM«á§â¦Û¤vªºform¬å±¼¡C
	Ãþ¦üFortior¥ý¿ï¾ÜIC¡AµM«á¸õ¥X¾Þ§@­¶­±¡C

¦p¦ó°µ¤@­Ó¾xÄÁµ{¦¡

¦p¦ó°O¿ý¤W¦ì¶}¾÷®É¶¡¡B¦p¦ó°O¿ý¤U¦ì¶}¾÷®É¶¡
­ì6257¤W¦ìµ{¦¡¬O¦p¦ó§ó·s¨t²Î®É¶¡ªº¡H°µ¦¨½d¨Ò¡C¤T¤ÀÄÁ«OÅ@¬O«ç»ò°µªº¡H

¦p¦ó°µ¨ì¦h­«»y¨t¥\¯à¡C¯à¤Á´«¤¤­^¤å»y¨t¡C¨Ã¯à°O¾Ð¤§«eªº³]©w¡C

ªì©l¤Æªº®É­Ô¡A³]©w»y¨t¡C

¦p¦ó°O¾Ð¨Ã®M¥Î¤§«eªº³]©w¡H

«öÁäx©Î²Õ¦XÁäctrl+Q¡AÂ÷¶}µ{¦¡

GUI«öReset¡A¬Ý¤U¦ì¦³¨S¦³¤ÏÀ³¡A¦h«ö´X¦¸¡A¬Ý¬Ý¬O¤£¬O³£¦³¤ÏÀ³¡A
­Y¦³®É­Ô¤U¦ì¨S¦^À³¡Aªí¥Ü³q«H¤£¨}¡A­n§ïCPU®É¯ß¡C

­Y¥Î¥ú¹jÂ÷RS232ÂàUSB¸Ë¸m¡A­nª`·NRXDªº¿O¦³¨S¦³«G°_¨Ó¡C
§Ú³oÃä·|¹J¨ìª¬ªp¡A­ì¥»RXD¦³«G¡A¤¤·L­·®°¤W¹q«á¡ARXD´Nº¶·À¤F¡C³o¼Ë´N¤£¯à³q«H¤F¡C
©Ò¥H¡A§Ú¥Ø«eÁÙ¬O¥ÎRS232¥ú¹jÂ÷ªO¡C

¹w³]¬°VR mode¡A±µ¨üVR«ü¥O¡C

·í¤W¦ì¾÷¤U©R¥O¨Óªº®É­Ô¡A´N¤Á´«¦¨GUI mode¡A±q¦¹VR¤£§@¥Î¡Aª½¨ì­«·s¶}¾÷¬°¤î¡C

Àx¦s³Ìªñ´X¤Q¦¸ADCµ²ªG¡C

FormBorderStyle	¿ïFixedSingle¡AÅýForm¤£¥i©Ô¤j©Ô¤p

vcs­n¸T¤îForm³Ì¤j¤Æ¡A­n«ç»ò°µ¡H

´ú«G·tÂIµ{¦¡¡G«ör¡Bg¡Bb¡Bw¡Bk¡BESC¡B¡B¡B
±Ò°Ê®É§Y¬°¥þ¿Ã¹õ¡A©ÎªÌ¡A«ö¤°»òÁä¤Á´«¡C

¥Î¹«¼Ð§âLabelªº¤å¦r°é¿ï°_¨Ó¡A·|Ä²µo¤°»ò·Æ¹«¨Æ¥ó¡H


Ãþ¦üint.parseÁÙ¦³¤°»ò¡H	float.Parse¡Bdouble.Parse¡BDateTime.Parse¡BIPAddress.Parse

listBox½d¨Ò¡G
private void Form1_Load(object sender, System.EventArgs e)
{
	string[] funcStr = {"ÀÉ®×","½s¿è","ÀËµø","±M®×","«Ø¸m","°»¿ù","¤u¨ã","µøµ¡","»¡©ú"};
	foreach(string str in funcStr)
		allLB.Items.Add(str);
}

vcs ¥i§_Åª¤JExcelÀÉ®×

List.Sort() ¡÷ ±Æ§ÇT
List.Find() ¡÷ §ä¥X¤@­ÓT
List.FindAll() ¡÷§ä¥X¦h­ÓT
List.Exist() ¡÷§PÂ_T¬O§_¦s¦b

using¥Îªk¡G C# µ{¦¡³]­p¤j¶q¨Ï¥Î©R¦WªÅ¶¡ªº­ì¦]¦³¨â­Ó¡C
²Ä¤@¡A.NET Framework ·|¨Ï¥Î©R¦WªÅ¶¡²ÕÂ´¨ä¦hºØÃþ§O¡C
²Ä¤G¡A«Å§i±z¦Û¤vªº©R¦WªÅ¶¡¡A±N¦³§U©ó¦b¸û¤j«¬ªºµ{¦¡³]­p±M®×¤¤±±¨îÃþ§O©M¤èªk¦WºÙªº½d³ò¡C


vcs + CS8963 °µ¡G
¤T¥Î¹qªí

®ÉÄÁ

¾xÄÁ
¶Ã¼Æ¨ú¦W¦r
¦~¥N
±q¤å¦rÀÉÅª¸ê®Æ¨Ã¥´¦L

good avsªº¸ê®Æ
©m¦W	¤é¤å	­^¤å	¥X¥Í	²{¦~	¥X¹D	¤Þ°h	¸ê®Æ



¹³¬O§KªÅ¤U¸ü¤@¼Ëªº­Ë¼Æ­p®É
¹³¬OBitCometªº ¿ï¶µ¡BºÊÅ¥port§@ªk¡C
¹³¬O¦Û°ÊÃö¾÷µ{¦¡
¹³¬O¤l¥Ø¿ý²£¥XÀÉ®×¦WºÙµ{¦¡

°µ¨ìUI¿ï¨úÀÉ®×¡A«öÁä¡A¥ÑbinaryÂàasc¡A¥i¥Hµ¹winmerge°µ¤ñ¸û¥Î¡C
©Î¦p¦Phj-split¡A°µjoin¡A
©Î¦p¦P ¥Ø¿ý¤UÀÉ¦WÂà¥X¯Â¤å¦rµ{¦¡
©Î¦p¦P UltraEditªº¤Q¤»¶i¦ìÅã¥Ü¼Ò¦¡

¦p¦ó°µ¨ìÅª¼gICªº¼È¦s¾¹¡A³z¹LI2C©Î¬OUART¨ÓÅª¼g¡H

¶R¶¼®Æªº§Ç¸¹³æ¡G
½s¸¹¡G413 02/08 21:21


vcs½d¨Ò¡G
 1. ¤¤¦è¾ä¹ï´«ªí
 2. ·Å«×¹ï´«áá¡B¥[´î­¼°£¾¹¡B¶ê¶gªø¶ê­±¿n­pºâ
 3. ¸Öµü«ö¶sÅã¥Ü¡A«ö«áÅã¥Ü¦btextBox¤W
 4. Åª¤@¸ÖµüÀÉ®×¡AÅã¥Ü¥X¨Ó(Åª¤@ÀÉ®×¡A¥ÎtextBoxÅã¥Ü¥X¨Ó)
 6. ¶Z¤µ®Éµ{µ{¦¡¡B¬Y¥¼¨Ó¨Æ¥ó¶Z¤µ´X¦~´X¤ë´X¤é´X¤Q´X¤À´X¬í¡C
 7. ±b¸¹±K½Xªº½T»{¥\¯à
 8. ¿ï¨ú¤@256«ôÀÉ®×¡A¸Ñ¥Xbinary¸ê®ÆÅã¥Ü¥X¨Ó¡AÃþ¦ü¸ÑÅªEDID¸ê®Æ¡C
 9. ¿ï¨ú¨â­ÓÀÉ®×¡A¨Ã¤ñ¸û¬O§_¬Û¦P¡C

°ÝÃD¡G
1. textBox¥i§_ª½¦æÅã¥Ü¡H

----------------csharp vcs visual c# 2008 SP----------------


vcs¥Ø¼Ð¡G
CPU-Z¡Bpicpick¡Bfile copy¡Bfile compare¡Bfile check(MD5¡BSHA1)
hjsplit








¡@¡@Visual C#¬O·L³n¤½¥q±À¥Xªº¤U¤@¥Nµ{§Ç¶}µo»y¨¥¡C
¥L¤£¶È¨ã¦³Visual C++¥\¯à±j¤jªº¯SÂI¡A¤S¨ã¦³Visual BasicªºÂ²¼ä¡A©ö¤W¤âªº¯SÂI¡C©Ò¥H¤@¸g±À¥X¡A´N¦¬¨ì¤F¼s¤jµ{§Ç¶}µo¤H­ûªºÅwªï¡C

Visual C#©MVisual C++ªº¤@­Ó©úÅãªº°Ï§O¦b©ó¡AVisual C#¥»¨­¬O¨S¦³Ãþ®wªº¡A¦ÓVisual C++«o¬O¦Û¨­´N±a¦³Ãþ®w¡C

Visual C#ÁöµM¨S¦³Ãþ®w¡A¦ý§@¬°.Net®Ø¬[¤¤ªº¤@­Ó¤Q¤À­«­nªº¶}µo»y¨¥¡C¥L¥i¥H¨Ï¥Î.Net®Ø¬[´£¨Ñªº¤@­Ó³q¥Îªº³n¥ó¶}µo¥]--.Net FrameWork SDK¡C
³o­Ó³n¥ó¶}µo¥]¥i¥H»¡¬OVisual C#¥\¯àªº©µ¦ù¡AVisual C#´N¬O³q¹L¥L¹ê²{¤F¦Û¨­µLªk¹ê²{ªº«Ü¦h¥\¯à¡C



¥»¤å´N¬O¨Ó¤¶²ÐVisual C#¦p¦ó§Q¥Î³o­Ó³n¥ó¶}µo¥]¨Óµo°e¹q¤l¶l¥óªº¡C
¡@¡@¤@¡D³n¥ó¶}µo©M¹B¦æªºÀô¹Ò³]¸m¡G
¡@¡@I > .µøµ¡¨t²Î2000ªA°È¾¹ª©
¡@¡@II > ..Net FrameWork SDK Beta 2ª©
¡@¡@III > .¥´¶}"±±¨î­±ªO"¡A¶i¤J"²K¥[©M§R°£µ{§Ç"¡AµM«á¦AÂIÀ»"²K¥[/§R°£Windows²Õ¥ó"¡A´N¥i¥H¬Ý¨£¥H¤U¬É­±¡G



















----------------syntax »yªk ST----------------


°}¦C«Å§i

°}¦C«Å§i½d¨Ò
	int[] A = new int[5];
	int[] B = new int[] { 1, 2, 3, 4, 5 };
	int[] C = { 1, 3, 5, 7, 9 };
	int[,] D = new int[3, 3];
	int[,] E = new int[,] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
	int[,] F = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
	int[, ,] G = new int[3, 4, 5];
	String[,] language = new string[3, 6] { { "¥¿¤¤1", "¥¿¤¤2", "¥¿¤¤3", "¥¿¤¤4", "¥¿¤¤5", "¥¿¤¤6" }, { "Â²¤¤1", "Â²¤¤2", "Â²¤¤3", "Â²¤¤4", "Â²¤¤5", "Â²¤¤6" }, { "­^»y1", "­^»y2", "­^»y3", "­^»y4", "­^»y5", "­^»y6" } };
	Point[] pt = new Point[360];    //¤@ºû°}¦C¤º¦³360­ÓPoint

»yªk
¸ê®Æ«¬§O[ ]   °}¦C¦WºÙ =  new  ¸ê®Æ«¬§O[°}¦C¤j¤p];

¤@ºû°}¦C¥Îªk¡G
int[] myArray = new int[10];
string[] studentName = new string[100];
int[] a = new int[5] {0,1,2,3,4};
Point[] pt = new Point[360];    //¤@ºû°}¦C¤º¦³360­ÓPoint

¤Gºû°}¦C¥Îªk¡G
int[,] b = new int[2,3];
int[,] c = new int[2,3] {{1,2,3},{4,5,6}};
int[,] myArray = new int[2,3] {{1,2,3},{4,5,6}};

vcs«Å§i¡G
      char[] cbuffer = new char[256];
      byte[] RecvBytes = new byte[256];


console mode»yªk:

Console.WriteLine("¤é´ÁÅÜ¼Æ {0}: ",timeBirth);
Console.WriteLine("NanaoSeconds: {0}", nanoseconds);
Console.Read(); //¼È°±

¦r¦ê«Å§i¡G
string[] A = new string[10];
string Temp = "";
string D1, D2 = "", D3;
D1 = textBox1.Text;
string[] Stu_Name = { "±i¤T", "§õ¥|", "¤ý¤­", "¶¯¶¯" };
string[] Stu_Name = { "±i¤T", "§õ¥|", "¤ý¤­", "¶¯¶¯" };

vcs«Å§i°}¦C
int[] x = {0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600};
int[] y = {200, 328, 396, 373, 268, 131, 26,  3, 71, 200, 328, 396, 373, 268, 131, 26};

¤@ºû°}¦C«Å§i¡G
int[] A = new int[6];
int[] A = new int[10];
int[] A = { 60, 70, 80, 85, 90, 100 };
int[] Stu_Sum = new int[4];         //¾Ç¥ÍÁ`¦¨ÁZ
int[] Stu_Average = new int[4];     //¾Ç¥Í¥­§¡¦¨ÁZ
int[] Subject_Sum = new int[5];     //¬ì¥ØÁ`¦¨ÁZ
int[] Subjcet_Average = new int[5]; //¬ì¥Ø¥­§¡¦¨ÁZ
Point[] pt = new Point[360];    //¤@ºû°}¦C¤º¦³360­ÓPoint

¤Gºû°}¦C«Å§i¡G
int[,] Stu_Sum = new int[3, 4];         //¾Ç¥ÍÁ`¦¨ÁZ
int[,] Stu_Average = new int[3, 4];     //¾Ç¥Í¥­§¡¦¨ÁZ
int[,] Subject_Sum = new int[3, 5];     //¬ì¥ØÁ`¦¨ÁZ
int[,] Subjcet_Average = new int[3, 5]; //¬ì¥Ø¥­§¡¦¨ÁZ
int[,] Score = new int[,] { { 65, 85, 78, 75, 69 }, { 66, 55, 52, 92, 47 }, { 75, 99, 63, 73, 86 }, { 77, 88, 99, 91, 100 } };

¤Tºû°}¦C«Å§i¡G

int[, ,] Score = { { { 65, 85, 78, 75, 69 }, { 66, 55, 52, 92, 47 }, { 75, 99, 63, 73, 86 }, { 77, 88, 99, 91, 99 } }, { { 77, 88, 66, 77, 66 }, { 65, 66, 88, 55, 77 }, { 70, 88, 56, 88, 88 }, { 80, 90, 95, 99, 99 } }, { { 55, 67, 56, 98, 67 }, { 66, 69, 76, 66, 78 }, { 77, 89, 88, 77, 77 }, { 88, 89, 99, 97, 88 } } };

¶Ã¼Æ¡G
Random r = new Random();
Number = r.Next();		//²£¥Í   >=0   ªº¶Ã¼Æ­È
Number = r.Next(101);		//²£¥Í   0~101 ªº¶Ã¼Æ­È
Number = r.Next(25, 101);	//²£¥Í  25~100 ªº¶Ã¼Æ­È
Number = r.NextDouble();	//²£¥Í 0.0~1.0 ªº¶Ã¼Æ­È

Number = r.Next(1,7);	//²£¥Í  1~6 ªº¾ã¼Æ¶Ã¼Æ­È¡AÂY»ë¤l¥Î¡C




List¥Îªk¡G	¦³ÂI¹³¬O¤£¥Î«Å§iªø«×ªº°}¦C(Array)

// «Å§imyIntLists ¬°List
// ¥H¤UList ¸Ì¬°int «¬ºA
List<int> myIntLists = new List<int>();

// «Å§imyStringLists ¬°List
// ¥H¤UList ¸Ì¬°string «¬ºA
List<string> myStringLists = new List<string>();

// ¦bList ¸Ì·s¼Wint ¾ã¼Æ
myIntLists.Add(123456);

// ¦bList ¸Ì·s¼Wstring ¦r¦ê
myStringLists.Add("¤j®a¦n!");

// ¥i¥Îforeach ¨ú¥XList ¸Ìªº­È
foreach(string myStringList in myStringLists)
{
        Console.WriteLine(myStringList);
}
// ¨ú¥X³æ¤@­ÓList ¸Ìªº­È¡A¦p¦P°}¦C(Array)¥Îªk
// 123456
myIntLists[0];

// ¤j®a¦n!
myStringLists[0];

// ±oª¾List ¸ÌªºÁ`¼Æ
myIntLists.Count;
myStringLists.Count;





¦r¦ê°}¦Cªº¼gªk¡G
	string[] atoms = { "¤ô²~®y", "Âù³½®y", "¨d¦Ï®y", "ª÷¤û®y", "Âù¤l®y", "¥¨ÃÉ®y", "·à¤l®y", "³B¤k®y", "¤Ñ¯¯®y", "¤ÑÃÈ®y", "®g¤â®y", "Å]½~®y" };
	string ret = string.Empty;

¦r¦êªº¼gªk¡G
String[] Day = new string[] { "¬P´Á¤é", "¬P´Á¤@", "¬P´Á¤G", "¬P´Á¤T", "¬P´Á¥|", "¬P´Á¤­", "¬P´Á¤»" };
string week = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();

DialogResult myResult = MessageBox.Show
("§A­n¿ï¬OÁÙ¬O§_?", "Åã¥Ü¦b¼u¥Xµøµ¡¤W­±ªº¦r"
, MessageBoxButtons.YesNo, MessageBoxIcon.Question);

MessageBoxButtons©M MessageBoxIcon³o­Ó¸Ì­±¦³«Ü¦h¦CÁ|¡A¥i¦Û¤v¿ï¦Û¤v­nªº

if ( myResult  == DialogResult.Yes)
{
   //«ö¤F¬O
}
else if (myResult== DialogResult.No)
{
   //«ö¤F§_
}

	 //not vcs
	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1");
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 1",MessageBoxButtons::OK);
	 MessageBox::Show("Yuki Oh's Picture3","Title Here 2",MessageBoxButtons::OKCancel);
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 3",MessageBoxButtons::AbortRetryIgnore);
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 4",MessageBoxButtons::RetryCancel);
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 5",MessageBoxButtons::YesNoCancel);
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 6",MessageBoxButtons::YesNo);

	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1",MessageBoxIcon::Error);
	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1",MessageBoxIcon::Question);
	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1",MessageBoxIcon::Information);
	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1",MessageBoxIcon::Warning);




MessageBox.Show ¤èªkªº¨Ï¥Î
http://blog.xuite.net/chu.hsing/Think/29672699-MessageBox.Show+%E6%96%B9%E6%B3%95%E7%9A%84%E4%BD%BF%E7%94%A8

MessageBox.Show("Àx¦sÀÉ®×OK, ÀÉ¦W¡G" + filename4, "Àx¦sÀÉ®×´ú¸Õ", MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);



int[,] myArray = new int[2,3] {{1,2,3},{4,5,6}};
String[] funcStr = {"ÀÉ®×","½s¿è","ÀËµø","±M®×","«Ø¸m","°»¿ù","¤u¨ã","µøµ¡","»¡©ú"};


String[] animal_name = {"¹«","¤û","ªê","¨ß"};



String[,] animal_name2 = {{"¹«","¤û","ªê","¨ß"},{"mouse","bull","tiger","rabbit"},{"Mickey","Benny","Eric","Cony"}};

¹«	mouse	Mickey	¦Ì©_	1928/11/18
¤û	bull	Benny	¯Z¥§	2000/8/14
ªê	tiger	Eric	¥©ªê	1993/12/13
¨ß	rabbit	Cony	¨ß¨ß	2013/4/17



----------------syntax »yªk SP----------------



----------------Process.Start() ST----------------


System.Diagnostics.Process.Start(currentPath);

Process.Start(@"C:\WINDOWS\system32\calc.exe");


Process Ãþ§O´£¨Ñ¹ï¥»¾÷©M»·ºÝ³B²z§Ç (Process) ªº¦s¨ú¡A¨ÃÅý±z¯à°÷±Ò°Ê©M°±¤î¥»¾÷¨t²Î³B²z§Ç¡C¦]¦¹¡A¥i¥H³z¹L Process.Start ¨Ó³B²z«ü©wªº¤å¥ó¡A©Ò¥H¡A¦pªG¦b Start ªº°Ñ¼Æ¤¤µ¹¤©¤@­Ó¹q¤l«H½cªº¶W³sµ²¡A´N¥i¥H±Ò°Ê¨t²Î¤¤¹w³]ªº¹q¤l¶l¥ó³B²zµ{¦¡¡C¦p¤U¡G

System.Diagnostics.Process.Start("mailto:abc@hotmail.com");




C# Process.Start()¤èªk†H¸Ñ
http://blog.csdn.net/chen_zw/article/details/7896264

[C#]§Q¥Î Process ¨Ó°õ¦æ¨ä¥¦¥~³¡µ{¦¡

C# ¶}±Ò¥~³¡ÀÉ®×
using System.Diagnostics;
Process.Start (@"C:\Users\Est\Desktop\GodHand3D\GodHand3D.exe");
using System.Diagnostics;
Process.Start("\\Program Files\\TransData2.exe","");

System.Diagnostics.Process.Start("" + System.Environment.SystemDirectory + "/notepad.exe");
notepad.exe	°O¨Æ¥»

C# ¶}±Ò°õ¦æÀÉ
System.Diagnostics.Process.Start("notepad.exe"); // °O¨Æ¥»
System.Diagnostics.Process.Start("calc.exe");    // ¤pºâ½L
System.Diagnostics.Process.Start("" + System.Environment.SystemDirectory + "/osk.exe");

calc.exe	¤pºâ½L
cmd.exe		command line
mspaint.exe	¤pµe®a
notepad.exe	°O¨Æ¥»
osk.exe		¿Ã¹õ¤pÁä½L
write.exe	WordPad

vcs¥i§_¶}±ÒÀÉ®×Á`ºÞ¡H Ãþ¦ü360¤§U½LºÞ²zµ{¦¡¡C
visual c# ¶}±ÒÀÉ®×Á`ºÞ

C# ¶}±Ò¥~³¡ÀÉ®×
½Ð¥ý¶×¤J¡Gusing System.Diagnostics;
¼gªk¤@¡G
Process.Start (@"C:\Users\Est\Desktop\GodHand3D\GodHand3D.exe");
¼gªk¤G¡G
ProcessStartInfo open = new ProcessStartInfo ();
open.FileName = "GodHand3D.exe"; // ÀÉ®×¦WºÙ
open.WorkingDirectory = @"C:\Users\Est\Desktop\GodHand3D"; // ¸ê®Æ§¨¸ô®|
Process.Start (open);


¶}±Òµ{¦¡
Process.Start(@oFD.FileName);
Process.Start(@ezisp_path);

¶}±Òºô­¶³sµ²
Process.Start("http://www.foo.com");


C# °õ¦æ¥~³¡exe
using System.Diagnostics;
ProcessStartInfo Info = new ProcessStartInfo();
Info.FileName = "xxx.exe"; //°õ¦æªºÀÉ®×¦WºÙ
Info.WorkingDirectory = @"C:\xxx\xxx"; //ÀÉ®×©Ò¦bªº¥Ø¿ý
Process.Start(Info);



System.Diagnostics.Process.Start(); ¯à°µ¤°¤\©O¡H¥¦¥D­n¦³¥H¤U¤Lƒª¥\¯à¡G
1¡B¥´…{¬Yƒª‹Î±µÊI§}¡]‡Éµ¡¡^¡C
2¡B©w¦ì¥´…{¬Yƒª¤å¥ó¥Ø‰£¡C
3¡B¥´…{¨t„i¯S®í¤å¥óƒH¡A¦p¡§±±¨î­±ªO¡¨µ¥¡C
(1)
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            process.StartInfo.FileName = "firefox.exe";   //firefox
            process.StartInfo.Arguments = "http://www.google.com";	//ºô§}
            process.Start();
(2)
            System.Diagnostics.ProcessStartInfo processStartInfo = new System.Diagnostics.ProcessStartInfo();
            processStartInfo.FileName = "explorer.exe";  //ÀÉ®×Á`ºÞ
            processStartInfo.Arguments = @"F:\";	 //¦ì¸m
            System.Diagnostics.Process.Start(processStartInfo);
(3)
	    System.Diagnostics.Process.Start(@"D:\Program Files\Tencent\QQ\Bin\QQ.exe");  //ª½±µˆ`¥Î¥´…{¤å¥ó
(4)
	    System.Diagnostics.Process.Start("explorer.exe", "D:\\Readme.txt");   //ª½±µ¥´…{¤å¥óReadme.txt

----------------Process.Start() SP----------------








----------------Dialog ST----------------

            // «Å§i OpenFileDialog ±±¨î¶µ¡A¨Ã¥B¹ê¨Ò¤Æ
            OpenFileDialog OFD = new OpenFileDialog();

Dialog
OpenFileDialog	¥´¶}¤å¥ó¹ï¸Ü¤è¶ô
SaveFileDialog	«O¦sÀÉ¹ï¸Ü
FolderBrowserDialog
FontDialog	¦rÅé¹ï¸Ü¤è¶ô
ColorDialog	ÃC¦â¹ï¸Ü¤è¶ô



1¡B OpenFileDialog±±¨î¶µ¦³¥H¤U°ò¥»ÄÝ©Ê

InitialDirectory  ¹ï¸Ü¤è¶ôªºªì©l¥Ø¿ý
Filter  ­n¦b¹ï¸Ü¤è¶ô¤¤Åã¥ÜªºÀÉ¿z¿ï¾¹¡A¨Ò¦p¡A"¤å¦rÀÉ(*.txt)|*.txt|©Ò¦³ÀÉ(*.*)||*.*"
FilterIndex  ¦b¹ï¸Ü¤è¶ô¤¤¿ï¾ÜªºÀÉ¿z¿ï¾¹ªº¯Á¤Þ¡A¦pªG¿ï²Ä¤@¶µ´N³]¬°1
RestoreDirectory  ±±¨î¹ï¸Ü¤è¶ô¦bÃö³¬¤§«e¬O§_«ì´_¥Ø«eªº¥Ø¿ý
FileName  ²Ä¤@­Ó¦b¹ï¸Ü¤è¶ô¤¤Åã¥ÜªºÀÉ©Î³Ì«á¤@­Ó¿ï¨úªºÀÉ
Title  ±NÅã¥Ü¦b¹ï¸Ü¤è¶ô¼ÐÃD¦C¤¤ªº¦r¤¸
AddExtension  ¬O§_¦Û°Ê²K¥[Àq»{°ÆÀÉ¦W
CheckPathExists


¦b¹ï¸Ü¤è¶ôªð¦^¤§«e¡AÀË¬d«ü©w¸ô®|¬O§_¦s¦b

DefaultExt  Àq»{°ÆÀÉ¦W
DereferenceLinks  ¦b±q¹ï¸Ü¤è¶ôªð¦^«e¬O§_¨ú®ø¤Þ¥Î§Ö±¶¤è¦¡
ShowHelp
±Ò¥Î"À°§U"«ö¶s
ValiDateNames  ±±¨î¹ï¸Ü¤è¶ôÀË¬dÀÉ®×¦W¤¤¬O§_¤£§t¦³µL®Äªº¦r¤¸©Î§Ç¦C





1¡ASaveFileDialog±±¨î¶µªºÄÝ©Ê

Filter  ­n¦b¹ï¸Ü¤è¶ô¤¤Åã¥ÜªºÀÉ¿z¿ï¾¹¡A¨Ò¦p¡A"¤å¦rÀÉ(*.txt)|*.txt|©Ò¦³ÀÉ(*.*)|*.*"
FilterIndex  ¦b¹ï¸Ü¤è¶ô¤¤¿ï¾ÜªºÀÉ¿z¿ï¾¹ªº¯Á¤Þ¡A¦pªG¿ï²Ä¤@¶µ´N³]¬°1
RestoreDirectory  ±±¨î¹ï¸Ü¤è¶ô¦bÃö³¬¤§«e¬O§_«ì´_¥Ø«eªº¥Ø¿ý
AddExtension  ¬O§_¦Û°Ê²K¥[Àq»{°ÆÀÉ¦W
CheckFileExists
CheckPathExists

¦b¹ï¸Ü¤è¶ôªð¦^¤§«e¡AÀË¬d«ü©w¸ô®|¬O§_¦s¦b
Container  ±±¨î¦b±N­n³Ð«ØÀÉ®É¡A¬O§_´£¥Ü¥Î¤á¡C¥u¦³¦bValidateNames¬°¯u­È®É¡A¤~¾A¥Î¡C
DefaultExt  ¯Ê¬Ù°ÆÀÉ¦W
DereferenceLinks

¦b±q¹ï¸Ü¤è¶ôªð¦^«e¬O§_¨ú®ø¤Þ¥Î§Ö±¶¤è¦¡
FileName  ²Ä¤@­Ó¦b¹ï¸Ü¤è¶ô¤¤Åã¥ÜªºÀÉ©Î³Ì«á¤@­Ó¿ï¨úªºÀÉ
InitialDirector  ¹ï¸Ü¤è¶ôªºªì©l¥Ø¿ý
OverwritePrompt  ±±¨î¦b±N­n¦b§ï¼g²{¦bÀÉ®É¬O§_´£¥Ü¥Î¤á¡A¥u¦³¦bValidateNames¬°¯u­È®É¡A¤~¾A¥Î
ShowHelp  ±Ò¥Î"?©ú"«ö¶s
Title  ±NÅã¥Ü¦b¹ï¸Ü¤è¶ô¼ÐÃD¦C¤¤ªº¦r¤¸
ValidateNames  ±±¨î¹ï¸Ü¤è¶ôÀË¬dÀÉ®×¦W¤¤¬O§_¤£§t¦³µL®Äªº¦r¤¸©Î§Ç¦C

2¡BSaveFileDialog¨Æ¥ó¦p¤U¡G





C#,Dialog¥þ¤¶²Ð
http://blog.xuite.net/teuton/wretch/expert-view/144416418
C#,Dialog¥þ¤¶²Ð
¤@¡B ¦rÅé¹ï¸Ü¤è¶ô(FontDialog)±`¥ÎÄÝ©Ê
ShowColor ±±¨î¬O§_Åã¥ÜÃC¦â¿ï¶µ
AllowScriptChange ¬O§_Åã¥Ü¦rÅéªº¦r¤¸¶°
Font ¦b¹ï¸Ü¤è¶ôÅã¥Üªº¦rÅé
AllowVerticalFonts ¬O§_¥i¿ï¾Ü««ª½¦rÅé
Color ¦b¹ï¸Ü¤è¶ô¤¤¿ï¾ÜªºÃC¦â
FontMustExist ·í¦rÅé¤£¦s¦b®É¬O§_Åã¥Ü¿ù»~
MaxSize ¥i¿ï¾Üªº³Ì¤j¦r«¬¤j¤p
MinSize ¥i¿ï¾Üªº³Ì¤p¦r«¬¤j¤p
ScriptsOnly Åã¥Ü±Æ°£OEM©MSymbol¦rÅé
ShowApply ¬O§_Åã¥Ü"À³¥Î"«ö¶s
ShowEffects ¬O§_Åã¥Ü©³½u¡B§R°£½u¡B¦rÅéÃC¦â¿ï¶µ
ShowHelp ¬O§_Åã¥Ü"À°§U"«ö¶s



C#,Dialog¥þ¤¶²Ð
http://jjnnykimo.pixnet.net/blog/post/21585509-c%23,dialog%E5%85%A8%E4%BB%8B%E7%B4%B9


----------------Dialog SP----------------


----------------File directory ST----------------



ÀÉ®×³B²z­n°µªº¨Æ¡G

¼´¥X¯S©w¤l¥Ø¿ý¤º©Ò¦³ÀÉ®×
Åã¥Ü¥XÀÉ®×ªº¤j¤p¡B³Ð«Ø®É¶¡¡B­×§ï®É¶¡¡B¡B¡B
§âbinaryÂà¦¨hexÀÉ¡C


C# ¨úªº¥Ø«e±M®×¤u§@ªº¥Ø¿ý(bin)
String str = System.IO.Directory.GetCurrentDirectory();





using system.io.file;
§R°£¥Ø¿ý Directory.Delete (¥u¯à§R°£ªÅªº¥Ø¿ý)
§R°£ÀÉ®× File.Delete
§PÂ_¬O§_¦s¦b File.Exists


// ÁôÂÃÀÉ®×
String strFileName = @"C:\test.txt";
FileInfo fileInfo = new FileInfo(strFileName);
fileInfo.Attributes = FileAttributes.Hidden;

// ÁôÂÃ¸ê®Æ§¨
String strDirName = @"C:\test";
DirectoryInfo diMyDir = new DirectoryInfo(strDirName);
diMyDir.Attributes = FileAttributes.Hidden;

ÀË¬dÀÉ®×¬O§_¦s¦b
if (System.IO.File.Exists(ezisp_path) == false)
{
	MessageBox.Show("ÀÉ®× " + ezisp_path + " ¤£¦s¦b, ¿ï¨ú¤@­ÓeZISP+ÀÉ");
}
else
{
	MessageBox.Show("ÀÉ®× " + ezisp_path + " ¦s¦b, ¶}±Ò¤§¡C");
}


test_txt.txt

StreamReader sw = new StreamReader(@"c:test_txt.txt");
Console.WriteLine( sw.ReadToEnd() );

StreamWriter sw=new StreamWriter(fileName,false,Encoding.Default);
sw.Write(str);
sw.Close();

//§â¨t„iµw¥ó«H®§«O¦s¨ì«ü©w¥Ø‰£bin\Debug\data  | bin\Release\data
string FilePath = Application.StartupPath + @"\data\" + DateTime.Now.ToString("yyyy-MM-dd HH-mm-ss") + ".txt";
if (!Directory.Exists(Application.StartupPath + @"\data\")) Directory.CreateDirectory(Application.StartupPath + @"\data\");
StreamWriter writer = File.CreateText(FilePath);

----------------File directory SP----------------


----------------DateTime ®É¶¡ ST----------------



¦~¬ö¬Û´î

¨Ï¥Î
DateTime.Now.ToString("yyyy/MM/dd", System.Globalization.DateTimeFormatInfo.InvariantInfo);
or
Console.WriteLine(string.Format("{0:yyyy\\/MM\\/dd}", DateTime.Today));

Åã¥Ü¤W¤È/¤U¤È
DateTime.Now.ToString().SubString(0,2)>12?( "¤U¤È"+ DateTime.Now):( "¤W¤È"+ DateTime.Now):


®É¶¡¬Û´î¡A­Y¨âªÌ¦³¤@­ÓµL¸ê®Æ¡A«h¤£¬Û´î
¨âªÌ¬Û´î¡A¦p¦óªí²{¥X¤j¤p¡HÀ³¸Ó­n¥ý¥þ³¡¤Æ¦¨¤é¼Æ¡A¦A¨Ó¤ñ¸û¡C

¤åªk¡G(°Ñ¼Æ¤j¤p¼g¸ÑÄ¶¤£¦P MM=month, mm=Minutes, HH=24hours, hh=12hours)

Âà´«¦r¦ê®æ¦¡¬°¤é´Á
DateTime dt = Convert.ToDateTime(myDateString);


¤@¨Ç DateTime ³B²z¨ç¼Æ

°µ²Î­p³øªí¥i¯à»Ý­n¥Î¨ìªº¤é´Á³B²z¨ç¼Æ¡G

GetTheHoursOfDay(): ¬Y¤é´Áªº 24 ¤p®É®É¨è¦Cªí
GetTheFirstDayOfWeek(): ¬Y¤é´Á¦b¸Ó¬P´Áªº²Ä¤@¤Ñ (¬P´Á¤é)
GetTheLastDayOfWeek(): ¬Y¤é´Á¦b¸Ó¬P´Áªº³Ì«á¤@¤Ñ (¬P´Á¤»)
GetTheFirstDayOfMonth(): ¬Y¤é´Á¦b¸Ó¤ë¥÷ªº²Ä¤@¤Ñ
GetTheLastDayOfMonth(): ¨ú±o¬Y¤é´Á¦b¸Ó¤ë¥÷ªº³Ì«á¤@¤Ñ
GetTheFirstDaysOfWeekInMoth(): ¬Y¤é´Á¦b¸Ó¤ë¥÷¨C©Pªº²Ä¤@¤Ñ¦Cªí
GetTheFirstDayOfQuarter(): ¬Y¤é´Á¦b¸Ó©uªº²Ä¤@¤Ñ
GetTheLastDayOfQuarter(): ¬Y¤é´Á¦b¸Ó©uªº³Ì«á¤@¤Ñ
GetTheFirstDaysOfMonthInQuarter(): ¨ú±o¬Y¤é´Á¦b¸Ó©u¨C­Ó¤ëªº²Ä¤@¤Ñ¦Cªí
GetTheFirstDayOfYear(): ¬Y¤é´Á¦b·í¦~ªº²Ä¤@¤Ñ
GetTheLastDayOfYear(): ¬Y¤é´Á¦b·í¦~ªº³Ì«á¤@¤Ñ
GetTheFirstDaysOfQuarterInYear(): ¬Y¤é´Á©ó·í¦~¨C¤@©uªº²Ä¤@¤Ñ¦Cªí





----------------DateTime ®É¶¡ SP----------------



¦p¦óª¾¹Dvcsµ{¦¡¤w¸g¥Î¤F¦h¤Ö°O¾ÐÅé¡H
¨Ò¦p¡Aload¤pÀÉ¡Bload¤jÀÉ¦Ü°O¾ÐÅé¡A¦p¦ó¬Ý°O¾ÐÅé¤j¤p¡A¬O§_¦³¤W­­¡H


«ö¤U·Æ¹«¡A²¾°Ê¹«¼Ð¡A§â³ò¦íªº¦JÅã¥Ü¥X¨Ó¡Aª½¨ì©ñ¶}¹«¼Ð¬°¤î¡C









WMI(Windows Management Instrumentation)

Windows Management Instrumentation (WMI) ¬O¤@ºØ¥Î¨ÓºÞ²z°õ¦æ Microsoft Windows §@·~¨t²Îªº¥»¾÷¤Î»·ºÝ¹q¸£¤§¸ê®Æ©M¥\¯àªº¥D­n¸ê·½¡C

C#¥i¥H¨Ï¥ÎManagementObjectSearcher§Q¥Î¤UQueryªº¤è¦¡§ì¨ú¨t²Îªº¸ê°T

"»Ý­n¥[¤JSystem.Management°Ñ¦Ò¡A¥H¤Î¤Þ¥ÎSystem.ManagementÃþ§O"


WMI(Windows Management Instrumentation)
1. ±M®×->°Ñ¦Ò->¥kÁä->¥[¤J°Ñ¦Ò->.NET->¿ïSystem.Management->½T©w
2. using System.Management;


¨ú±o CPU §Ç¸¹¥i¥H¥Î¨Ó¿ëÃÑ¥Î¤áºÝ¹q¸£ªº°ß¤@©Ê¡A¦]¬°³q±` CPU ¤£·|Ãa¤]¤£±`´«¡C
1. ±M®×½Ð¥ý¥[¤J°Ñ¦Ò System.Management
2. ³z¹L ManagementObjectSearcher ¬d¸ß

WMI¬ÛÃö­n¥[¤J¡G
¤è®×Á`ºÞ/°Ñ¦Ò/¥[¤J°Ñ¦Ò/.Net/System.Management


²Õ¦XÁä
        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)//«ö¤UESC
            {
                Application.Exit();//Ãö³¬µ{¦¡
            }
            else
            {
                if (e.Control == true && e.Alt == true && e.KeyCode == Keys.T)//«ö¦í²Õ¦XÁä Ctrl + Alt + T
                {
                    MessageBox.Show("Ctrl + Alt + T");
                }
            }
        }
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //Ãö³¬µ{¦¡«e ½T»{µøµ¡
            DialogResult Result = MessageBox.Show("©|¥¼Àx¦s½T©w­nÃö³¬µ{¦¡?", "Ãö³¬½T»{", MessageBoxButtons.YesNo);
            if (Result == System.Windows.Forms.DialogResult.Yes)
            {
                // Ãö³¬Form
                e.Cancel = false;
            }
            else
            {
                e.Cancel = true;
            }
        }
            switch (e.KeyCode)   //®Ú¾Úe.KeyCode¤À§O°õ¦æ
            {
                case Keys.Up:
                    this.Top -= 10;
                    break;
                case Keys.Down:
                    this.Top += 10;
                    break;
                case Keys.Left:
                    this.Left -= 10;
                    break;
                case Keys.Right:
                    this.Left += 10;
                    break;
            }




        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            richTextBox1.Text += "tttt";
            switch (e.KeyCode)
            {
                case Keys.D1:
                    richTextBox1.Text += "aaaaaaaaaaaaaaaaaa\n";
                    Console.Beep(262,500);
                    break;
                case Keys.D2:
                    Console.Beep(294, 500);
                    break;
                case Keys.D3:
                    Console.Beep(330, 500);
                    break;
                case Keys.D4:
                    Console.Beep(349, 500);
                    break;
                case Keys.D5:
                    Console.Beep(392, 500);
                    break;
                case Keys.D6:
                    Console.Beep(440, 500);
                    break;
                case Keys.D7:
                    Console.Beep(493, 500);
                    break;
                case Keys.D8:
                    Console.Beep(523, 500);
                    break;
            }
        }










----------------Windows Media Player ¼v­µ¬ÛÃöST----------------



DLLImport ¨Ï¥Î¤è¦¡

	¥[¤J¤Þ¥Î:
	using System.Runtime.InteropServices;
	using System.Runtime.InteropServices;   //for DllImport

	DllImportªº¥Îªk¡G

	[DllImport("kernel32.dll")]
	public static extern bool Beep(int frequency, int duration);

	¨Ï¥Î¡G
	//Beep() ¬O¦b kernel32.lib ¤¤©w¸qªº¡ABeep¨ã¦³¥H¤U­ì«¬¡G
	//BOOL Beep(DWORD dwFreq, DWORD dwDuration);
	Beep(1000, 100);


(C#)¼½©ñ­µ¼Ö
System.Media.SoundPlayer myPlayer = new
System.Media.SoundPlayer(@"C:\Music\welkin.wav");
myPlayer.Play();
¤]¥i¥H¼½©ñ¨t²Î¹w³]ªº­µ®Ä
//¹Í¹ÍÁn
System.Media.SystemSounds.Beep.Play();



¦p¦ó¼·©ñ Wave ­µ®ÄÀÉ
ª½±µ¨Ï¥Î System.Media.SoundPlayer Ãþ§O

System.Media.SoundPlayer sp = new System.Media.SoundPlayer();
sp.SoundLocation = @"C:\Wave­µ®ÄÀÉ\DoReMe.wav";
sp.Play(); // ¼·©ñ
sp.Stop(); // °±¤î

C# ¼½©ñ mp3 wav
http://olivermode.pixnet.net/blog/post/305842398-c%23--%E6%92%AD%E6%94%BE-mp3-wav

C# ¦p¦ó¼½©ñ mp3
https://dotblogs.com.tw/kylin/2009/07/29/9721

C# ¦p¦ó¼·©ñ Wave ­µ®ÄÀÉ
https://dotblogs.com.tw/powerhammer/2008/03/24/2147

vcs¼½©ñmp3
¥[¤J°Ñ¦Ò
Microsoft.DirectX.AudioVideoPlayback		//§ä¤£¨ì
private void button1_Click(object sender, System.EventArgs e)
{
	Microsoft.DirectX.AudioVideoPlayback.Audio.FromFile(@"C:\music.mp3").Play();
}

[C#][VB.NET]¨Ï¥ÎAxWindowsMediaPlayer¼·©ñ¦h´CÅé
https://dotblogs.com.tw/larrynung/2009/03/01/7325


¥[¤J°Ñ¦Ò    COM>>Windows Media Player (wmp.dll)

¥[¤J
using System.Threading; //for thread
using WMPLib;


¨ú±o¼v¤ù¸ê°T

C:\____¤â¾÷¨Óªº¹Ï\__¼v¤ù\VID_20170217_114050.3gp

string filename = "C:\____¤â¾÷¨Óªº¹Ï\__¼v¤ù\VID_20170217_114050.3gp";
WindowsMediaPlayer wmp = new WindowsMediaPlayerClass();
IWMPMedia mediainfo = wmp.newMedia(filename);
//Console.WirteLine(mediainfo.duration);


http://cyfangnotepad.blogspot.tw/2013/12/cnet-windows-media-player-wmv.html





// Test whether Windows Media Player is in the playing state.
if (wplayer.playState == WMPLib.WMPPlayState.wmppsPlaying)	//net
{
    playStateLabel.Text = "Windows Media Player is playing!";
}
else
{
    playStateLabel.Text = "Windows Media Player is NOT playing!";
}

¸õ¦Ü²Ä100¬í¼½©ñ
            wplayer.controls.currentPosition = 100;
            wplayer.controls.play();

msdn
https://msdn.microsoft.com/en-us/library/windows/desktop/dd564338(v=vs.85).aspx

WMPLibªº°ò¥»ÄÝ©Ê¤Î¤èªk

URL:(String); «ü©w´CÅé¦ì¸m¡A¥»¾÷©Îºô¸ô¦ì§}
uiMode:(String); ¼½©ñ¾¹¤¶­±¼Ò¦¡¡A¥i¬°Full, Mini, None, Invisible
playState:(integer); ¼½©ñª¬ºA¡A1=°±¤î¡A2=¼È°±¡A3=¼½©ñ¡A6=¥¿¦b½w½Ä¡A9=¥¿¦b³s½u¡A10=·Ç³Æ´Nºü
enableContextMenu:(Boolean); ±Ò¥Î/¸T¥Î¥kÁä¿ï³æ
fullScreen:(boolean); ¬O§_¥þ«ÌÅã¥Ü

//¼½©ñ¾¹°ò¥»±±¨î
[controls] wmp.controls
controls.play; ¼½©ñ
controls.pause; ¼È°±
controls.stop; °±¤î
controls.currentPosition:double; ·í«e¶i«×
controls.currentPositionString:string; ·í«e¶i«×¡A¦r¦ê®æ¦¡¡C¦p¡§00:23¡¨
controls.fastForward; §Ö¶i
controls.fastReverse; §Ö°h
controls.next; ¤U¤@¦±
controls.previous; ¤W¤@¦±

[settings] wmp.settings //¼½©ñ¾¹°ò¥»³]©w
settings.volume:integer; ­µ¶q¡A0-100
settings.autoStart:Boolean; ¬O§_¦Û°Ê¼½©ñ
settings.mute:Boolean; ¬O§_ÀR­µ
settings.playCount:integer; ¼½©ñ¦¸¼Æ

[currentMedia] wmp.currentMedia //·í«e´CÅéÄÝ©Ê
currentMedia.duration:double; ´CÅéÁ`ªø«×
currentMedia.durationString:string; ´CÅéÁ`ªø«×¡A¦r¦ê®æ¦¡¡C¦p¡§03:24¡¨
currentMedia.getItemInfo(const string); Àò¨ú·í«e´CÅé¸ê°T"Title"=´CÅé¼ÐÃD¡A"Author"=ÃÀ³N®a¡A"Copyright"=ª©Åv¸ê°T¡A"Description"=´CÅé¤º®e´y­z¡A"Duration"=«ùÄò®É¶¡¡]¬í¡^¡A"FileSize"=ÀÉ®×¤j¤p¡A"FileType"=ÀÉ®×Ãþ«¬¡A"sourceURL"=­ì©l¦ì§}
currentMedia.setItemInfo(const string); ³q¹LÄÝ©Ê¦W³]¸m´CÅé¸ê°T
currentMedia.name:string; ¦P currentMedia.getItemInfo("Title")

[currentPlaylist] wmp.currentPlaylist //·í«e¼½©ñ²M³æÄÝ©Ê
currentPlaylist.count:integer; ·í«e¼½©ñ²M³æ©Ò¥]§t´CÅé¼Æ
currentPlaylist.Item[integer]; Àò¨ú©Î³]¸m«ü©w±M®×´CÅé¸ê°T¡A¨ä¤lÄÝ©Ê¦Pwmp.currentMedia
axWindowsMediaPlayer1.currentMedia.sourceURL; //Àò¨ú¥¿¦b¼½©ñªº´CÅé¤å¥óªº¸ô®|
axWindowsMediaPlayer1.currentMedia.name;          //Àò¨ú¥¿¦b¼½©ñªº´CÅé¤å¥óªº¦WºÙ
axWindowsMediaPlayer1.Ctlcontrols.Play¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¼½©ñ
axWindowsMediaPlayer1.Ctlcontrols.Stop¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@°±¤î
axWindowsMediaPlayer1.Ctlcontrols.Pause¡@¡@¡@¡@¡@¡@¡@¡@¡@ ¼È°±
axWindowsMediaPlayer1.Ctlcontrols.PlayCount¡@¡@¡@¡@¡@¡@¡@¡@¤å¥ó¼½©ñ¦¸¼Æ
axWindowsMediaPlayer1.Ctlcontrols.AutoRewind¡@¡@¡@¡@¡@¡@¡@¬O§_°j°é¼½©ñ
axWindowsMediaPlayer1.Ctlcontrols.Balance¡@¡@¡@¡@¡@¡@¡@¡@¡@Án¹D
axWindowsMediaPlayer1.Ctlcontrols.Volume¡@¡@¡@¡@¡@¡@¡@¡@¡@­µ¶q
axWindowsMediaPlayer1.Ctlcontrols.Mute¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@ÀR­µ
axWindowsMediaPlayer1.Ctlcontrols.EnableContextMenu¡@¡@¡@¡@¬O§_¤¹³\¦b±±¨î¤¸¥ó¤WÂI¿ï·Æ¹«¥kÁä®É¼u¥X§Ö±¶¿ï³æ
axWindowsMediaPlayer1.Ctlcontrols.AnimationAtStart¡@¡@¡@¡@¬O§_¦b¼½©ñ«e¥ý¼½©ñ°Êµe
axWindowsMediaPlayer1.Ctlcontrols.ShowControls¡@¡@¡@¡@¡@¡@¬O§_Åã¥Ü±±¨î¤¸¥ó¤u¨ãÄæ
axWindowsMediaPlayer1.Ctlcontrols.ShowAudioControls¡@¡@¡@¡@¬O§_Åã¥ÜÁn­µ±±¨î«ö¶s
axWindowsMediaPlayer1.Ctlcontrols.ShowDisplay¡@¡@¡@¡@¡@¡@¡@¬O§_Åã¥Ü¸ê®Æ¤å¥óªº¬ÛÃö¸ê°T
axWindowsMediaPlayer1.Ctlcontrols.ShowGotoBar¡@¡@¡@¡@¡@¡@¡@¬O§_Åã¥ÜGotoÄæ
axWindowsMediaPlayer1.Ctlcontrols.ShowPositionControls¡@¡@¬O§_Åã¥Ü¦ì¸m½Õ¸`«ö¶s
axWindowsMediaPlayer1.Ctlcontrols.ShowStatusBar¡@¡@¡@¡@¡@¡@¬O§_Åã¥Üª¬ºA¦C
axWindowsMediaPlayer1.Ctlcontrols.ShowTracker¡@¡@¡@¡@¡@¡@¡@¬O§_Åã¥Ü¶i«×±ø
axWindowsMediaPlayer1.Ctlcontrols.FastForward¡@¡@¡@¡@¡@¡@¡@§Ö¶i
axWindowsMediaPlayer1.Ctlcontrols.FastReverse¡@¡@¡@¡@¡@¡@¡@§Ö°h
axWindowsMediaPlayer1.Ctlcontrols.Rate¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@§Ö¶i¡þ§Ö°h³t²v
axWindowsMediaPlayer1.AllowChangeDisplaySize¡@¬O§_¤¹³\¦Û¥Ñ³]©w¼½©ñ¹Ï¶H¤j¤p
axWindowsMediaPlayer1.DisplaySize¡@¡@¡@¡@¡@¡@¡@³]©w¼½©ñ¹Ï¶H¤j¤p
¡@¡@¡@¡@1-MpDefaultSize¡@¡@¡@¡@¡@¡@¡@¡@¡@­ì©l¤j¤p
¡@¡@¡@¡@2-MpHalfSize¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@ ­ì©l¤j¤pªº¤@¥b
¡@¡@¡@¡@3-MpDoubleSize¡@¡@¡@¡@¡@¡@¡@¡@¡@ ­ì©l¤j¤pªº¨â­¿
¡@¡@¡@¡@4-MpFullScreen¡@¡@¡@¡@¡@¡@¡@¡@¡@ ¥þ«Ì
¡@¡@¡@¡@5-MpOneSixteenthScreen¡@¡@¡@¡@¡@ ¿Ã¹õ¤j¤pªº1/16
¡@¡@¡@¡@6-MpOneFourthScreen¡@¡@¡@¡@¡@¡@¡@¿Ã¹õ¤j¤pªº1/4
¡@¡@¡@¡@7-MpOneHalfScreen¡@¡@¡@¡@¡@¡@¡@¡@¿Ã¹õ¤j¤pªº1/2
axWindowsMediaPlayer1.ClickToPlay¡@¡@¡@¡@¡@¡@¡@¬O§_¤¹³\³æÀ»¼½©ñµøµ¡±Ò°ÊMedia Player
¦bµø°T¼½©ñ¤§«á,¥i¥H³q¹L¦p¤U¤è¦¡Åª¨ú·½µø°Tªº¼e«×©M°ª«×,µM«á³]©w¨äÁÙ­ì¬°­ì©lªº¤j¤p.
         private void ResizeOriginal()
         {
             int intWidth = axWindowsMediaPlayer1.currentMedia.imageSourceWidth;
             int intHeight = axWindowsMediaPlayer1.currentMedia.imageSourceHeight;
             axWindowsMediaPlayer1.Width = intWidth + 2;
             axWindowsMediaPlayer1.Height = intHeight + 2;
         }


----------------Windows Media Player ¼v­µ¬ÛÃöSP----------------




----------------¦³ÃöToString¡BString.Formatªº¬ÛÃö¸ê®Æ ST----------------

«e­±¸É0ªº¼Æ¦r¦r¦ê
String.Format("{0:0000}", 157);	//¿é¥X 0157

«e«á³£¸É0ªº¼Æ¦r¦r¦ê
String.Format("{0:0000.0000}", 157.42);	//¿é¥X 0157.4200

®æ¦¡¤Æ¹q¸Ü¸¹½X
(String.Format("{0:(###) ###-####}", 8005551212);	//¿é¥X (800) 555-1212

¤£º¡¯S©wªø«×ªº¦r¦ê¡A«á­±¸ÉªÅ¥Õ
String.Format("{0,-10}", "Hello");	//¡uHello     ¡v

¤£º¡¯S©wªø«×ªº¦r¦ê¡A«e­±¸ÉªÅ¥Õ
String.Format("{0,10}", "Hello");	//¡u     Hello¡v

«e­±¸É0ªº¼Æ¦r¦r¦ê
String.Format("{0:0000}", 157);	//¿é¥X 0157

«e«á³£¸É0ªº¼Æ¦r¦r¦ê
String.Format("{0:0000.0000}", 157.42);	//¿é¥X 0157.4200

ª÷ÃBªºªí¥Ü¡G¨C3¦ì¼Æ¥[³r¸¹
String.Format("{0:n}",  123456789);	//¿é¥X 123,456,789.00
String.Format("{0:n0}", 123456789);	//¿é¥X 123,456,789

ª÷ÃBªºªí¥Ü
String.Format("{0:$#,##0.00;($#,##0.00);Zero}", 0); // ³o­Ó·|Åã¥Ü Zero
String.Format("{0:$#,##0.00;($#,##0.00);Zero}", 1243.50); // ³o­Ó·|Åã¥Ü $1,243.50

ª÷ÃBªºªí¥Ü_§ï¨}_¨ú¨ì¤p¼Æ2¦ì
String.Format("{0:$###,###,###,##0.00}", 0);	//$0.00
String.Format("{0:$###,###,###,##0.00}", 12.5);	//$12.50
String.Format("{0:$###,###,###,##0.00}", 3456234532);	//$3,456,234,532.0

ª÷ÃBªºªí¥Ü_§ï¨}2_¨ú¨ì­Ó¦ì
String.Format("{0:$#,0}", 0);	//$0
String.Format("{0:$#,0}", 12.5);	//$13,¥|¬B¤­¤J¨ì­Ó¦ì
String.Format("{0:$#,0}", 3456234532);	//$3,456,234,532

®æ¦¡¤Æ¹q¸Ü¸¹½X
String.Format("{0:(###) ###-####}", 8005551212); //¿é¥X (800) 555-1212

¦Ê¤À¤ñ
String.Format("{0:0%}", 17 / (float)60);	//¿é¥X 28%

¨ì¤p¼Æ2¦ìªº¦Ê¤À¤ñ
String.Format("{0:0.00%}", 17 / (float)60);	//¿é¥X 28.33%

¨ú¤p¼ÆÂI4¦ì¡A¨Ã¹ï²Ä5¦ì°µ¥|±Ë¤­¤J
String.Format("{0:#,0.####}", 1234.56789);	//1,234.5679

¤p¼ÆÂI¤£¨¬4¦ì¤£¸É0
String.Format("{0:0.####}", 1234.567);	//1234.567

¦~/¤ë/¤é ®É:¤À:¬í ²@¬í
DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss ffff");

C³f¹ô
2.5.ToString("C")	//¢D2.50

D¤Q¶i¦ì¼Æ¦r
25.ToString("D5")	//00025

E¬ì¾Ç«¬
25000.ToString("E")	//2.500000E+005

F©T©wÂI
25.ToString("F2")	//25.00

G±`³W
2.5.ToString("G")	//2.5

N¼Æ¦r
2500000.ToString("N")	//2,500,000.00

X¤Q¤»¶i¦ì
255.ToString("X")	//FF

----------------¦³ÃöToString¡BString.Formatªº¬ÛÃö¸ê®Æ SP----------------


----------------xxxxx ST----------------





------------------------------------------------------------------------------
«Ý´ú¸Õ¡A«Ý¼g¤J½d¨Ò¶µ¥Ø¡G
------------------------------------------------------------------------------

(C#)¸g¹L¤F¦h¤Ö¬í¤§Ticks

¦³®É¤£·Q¥ÎTimer¡A´N¥Î¥H¤U¤èªk¥h´î
//¥ý¦bClassªº¥þ°ìÅÜ¼Æªº¦a¤è«Å§i¶}©lªº®É¶¡
long StartDate = DateTime.Now.Ticks;

while(±ø¥ó)
{
  //µM«á¤@ª½¶]°j°é¥h¬Ý²{¦bªºTicks¡A¬Û´î«á°£¥H10000000´N¬O´X¬í¤F
//¦]¬°1 Ticks¬O100©`¬í

if(((DateTime.Now.Ticks - StartDate) / 10000000)>15)
{
   //·í¹L¤F15¬í¤§«á¡A´N·|°õ¦æ³o
   break;
}
------------------------------------------------------------------------------
(C#)¨ú±o°Å¶KÃ¯Clipboardªº¤º®e

IDataObject data = Clipboard.GetDataObject();
if (data.GetDataPresent(DataFormats.Text))
{
richTextBox1.Text += data.GetData(DataFormats.Text).ToString();
}

------------------------------------------------------------------------------
(C#)Win Form§ï¤£³W«h§Îª¬

§Ú­Ì¬Ý¨ìªºWinFormÁ`¬O¤è§Îªº
¦ý¥i¥H§ï¦¨¶ê§Î©Î¬O¦hÃä§Î
(¦b³]­pµe­±¬Ý¤£¨ì¡A¤@©w­n°ÊºA§ó§ï)

System.Drawing.Drawing2D.GraphicsPath myPath = new System.Drawing.Drawing2D.GraphicsPath();

//¶ê§Î
myPath.AddEllipse(0, 0, this.Width, this.Height);

Region myRegion = new Region(myPath);

this.Region = myRegion;

¤]¥i¥H¥Î¦hÃä§Î¦p¤U

myPath.AddPolygon(new Point[] { new Point(0, 0), new Point(0, this.Height),
new Point(this.Width, 0) });
------------------------------------------------------------------------------


------------------------------------------------------------------------------


------------------------------------------------------------------------------





±Nµ¡ÅéForm1ªº FormBorderStyle ÄÝ©Ê­È³]¬° None «á¡A´Nµ¡Åé´NÅÜ¦¨¤FµLÃä®Ø¡BµL¼ÐÃDÄæ¡BµLControlBox¡]§Y³Ì¤j¤Æ³Ì¤p¤ÆÃö³¬«ö¶s¡^ªºµ¡Åé¡C






------------------------------------------------------------------------------


richTextBox1.Text += "¥Ø«e¤u§@¥Ø¿ý¡G" + Directory.GetCurrentDirectory() + "\n";

string new_directory = "C:\\";
richTextBox1.Text += "§ïÅÜ¤u§@¥Ø¿ý¦Ü¡G" + new_directory + "\n";

Directory.SetCurrentDirectory(new_directory);

richTextBox1.Text += "¥Ø«e¤u§@¥Ø¿ý¡G" + Directory.GetCurrentDirectory() + "\n";


------------------------------------------------------------------------------



using System.Net;
// ¨ú±oLocal¥D¾÷ªºÃÑ§O¦WºÙ
string localHostName = Dns.GetHostName();
richTextBox1.Text += "Local¥D¾÷ªºÃÑ§O¦WºÙ¡G" + localHostName + "\n";



------------------------------------------------------------------------------




------------------------------------------------------------------------------



ssss
enum»yªk
enum Seasons { spring, summer, autumn, winter };
private void button1_Click(object sender, EventArgs e)
{
    Seasons today = Seasons.summer;	//«Å§i
    int seasonNumber = (int)today;
    richTextBox1.Text += "get number : " + seasonNumber.ToString() + "\n";

}




------------------------------------------------------------------------------


µ{¦¡¤º³¡³y¥X¥iµø¤¸¥ó

            Button a1 = new Button();
            this.Controls.Add(a1);
            a1.Size = new System.Drawing.Size(100, 50);
            a1.Location = new System.Drawing.Point(50, 350);
            a1.Text = "a1";

            Button a2 = new Button();
            this.Controls.Add(a2);
            a2.Size = new System.Drawing.Size(100, 50);
            a2.Location = new System.Drawing.Point(200, 350);
            a2.Text = "a2";

            Button a3 = new Button();
            this.Controls.Add(a3);
            a3.Size = new System.Drawing.Size(100, 50);
            a3.Location = new System.Drawing.Point(350, 350);
            a3.Text = "a3";

            Button a4 = new Button();
            this.Controls.Add(a4);
            a4.Size = new System.Drawing.Size(100, 50);
            a4.Location = new System.Drawing.Point(500, 350);
            a4.Text = "a4";

            Button a5 = new Button();
            this.Controls.Add(a5);
            a5.Size = new System.Drawing.Size(100, 50);
            a5.Location = new System.Drawing.Point(650, 350);
            a5.Text = "a5";


------------------------------------------------------------------------------



//C# ¨Ï¥Î Stopwatch „ò¶q¥N‡ù†b¦æƒº…}
richTextBox1.Text += "¨Ï¥Î Stopwatch „ò¶q¥N‡ù†b¦æƒº…}\n";
System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
sw.Start();
System.Threading.Thread.Sleep(3000);
sw.Stop();
richTextBox1.Text += "¸g¹L®É¶¡¡G" + sw.Elapsed.ToString() + "\n";





------------------------------------------------------------------------------





