
windows media player
// ¼½©ñºq¦±
            axWMP.URL = @"D:\Music\02.AVRIL LAVIGNE »Å¨ì°©¤l¸Ì MY HAPPY ENDING.mp3";
            // ³]©w­«½Æ¼½©ñ
            //axWMP.settings.setMode("loop", true);
            // ³]©wÀH¾÷¼½©ñ
            //axWMP.settings.setMode("shuffle", true);
            
C# - ¦p¦óÅª¨ú¯S©w¦ì¸mRegistry Key
https://barryhungmvp.pixnet.net/blog/post/88133155-c%23---%E5%A6%82%E4%BD%95%E8%AE%80%E5%8F%96%E7%89%B9%E5%AE%9A%E4%BD%8D%E7%BD%AEregistry-key

¥[¤@­ÓÅª¨úRegistryKeyªº½d¨Ò

        private void button4_Click(object sender, EventArgs e)
        {
            RegistryKey mreg;
            mreg = Registry.LocalMachine;
            mreg = mreg.CreateSubKey("software\\Microsoft\\Internet Explorer");
            string IEVersion = "¥Ø«eIEÂsÄı¾¹ªºª©¥»°T®§¡G" + (String)mreg.GetValue("Version");
            mreg.Close();
            richTextBox1.Text += IEVersion + "\n";

        }

®à¥¬¦s©ñ¦ì¸m win7 romeo
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Themes\TranscodedWallpaper.jpg

¦p¦ó§ä¨ìWindows 10®à­±­I´º†¶¤ùªº¦ì¸m
http://www.xstui.com/read/446



 C# ®Ú¾Ú®à­±¤j¤p½Õ¾ãµøµ¡¤j¤p 
 
 private void Form1_Load(object sender, EventArgs e)
        {
            int DeskWidth = Screen.PrimaryScreen.WorkingArea.Width; //PrimaryScreen¬°¨ú±o¥DÅã¥Ü¾¹¡AWorkingArea¥i¨ú±oÅã¥Ü¾¹ªº¤u§@°Ï(¤£¥]§t¤u§@¦C¡Kµ¥)
            int DeskHeight = Screen.PrimaryScreen.WorkingArea.Height;
            this.Width = Convert.ToInt32(DeskWidth * 0.8);
            this.Height = Convert.ToInt32(DeskHeight * 0.8);
        }
 

Ray's Working Note 
http://ray19841984.blogspot.com/

'





¦rÅé°µ³±¼v®ÄªG ¦P¼Ë¦r©¹¥k¤U¼g¤@¹M ÃC¦â¤£¦P

            string test_string = "ª÷³®¹Ï";
            bmp = new Bitmap(500, 500);     //initial W, H
            g = Graphics.FromImage(bmp);

            font_type = "¼Ğ·¢Åé";
            font_size_default = 200;
            
            f = new Font(font_type, font_size_default);

            g.DrawString(test_string, f, new SolidBrush(Color.Pink), new PointF(0, 0));


            font_size_default = 200;

            f = new Font(font_type, font_size_default);

            g.DrawString(test_string, f, new SolidBrush(Color.Red), new PointF(5, 5));
            
            
            pictureBox1.Image = bmp;


picturebox + keydown
https://zhidao.baidu.com/question/495903236489591124.html


vcs
https://jojosula001.pixnet.net/blog/category/2297573







 27. ³]©w¨â­Ó©Î¨â­Ó¥H¤Wªº¦r«¬¼Ë¦¡ (¨Ò¦p¤@¬q¤å¦r³]©w²ÊÅé¥[±×Åé)¡C

°²¦p­n±N¤@¬q¤å¦r¡A¦P®É³]©w ²ÊÅé¤å¦r FontStyle.Bold »P ±×Åé¤å¦r FontStyle.Italic¡A«h»İ³z¹L FontFamily Ãş§O¡A³z¹L | °µ³sµ²

	// ±NRichTextBox¤¤¿ï¨úªº¤å¦r¡A³z¹L FontFamily Ãş§O 
// ¦P®É³]©w ²ÊÅé¤å¦r FontStyle.Bold »P ±×Åé¤å¦r FontStyle.Italic 
Font MyFont = new Font(new FontFamily("¼Ğ·¢Åé"), 10, FontStyle.Bold | FontStyle.Italic); 
this.richTextBox1.SelectionFont = MyFont;





33. String Âà¬° Byte §Ç¦C»P Byte §Ç¦CÂà¬° String¡C

¨Ï¥Î System.Text.Encoding Ãş§O¤¤ªº³o¨â­Ó¤èªk¡A¶·ª`·N½s½X¤è¦¡ :

Encoding.GetBytes ¤èªk : ±N¦r¤¸¶°½s½X¦¨¦ì¤¸²Õ§Ç¦C¡C

Encoding.GetString ¤èªk : ±N¦ì¤¸²Õ§Ç¦C¸Ñ½X¦¨¦r¦ê¡C

µ{¦¡½X

	String strOrg = "12345";
            // Encoding.GetBytes¤èªk¡A±N String Âà¬° Byte §Ç¦C
            byte[] stringConvByte = Encoding.Default.GetBytes(strOrg);
            // Encoding.GetString¤èªk¡A±N Byte §Ç¦C Âà¬° String
            string byteConvStrig = Encoding.Default.GetString(stringConvByte);


// ¥[¤J TextBox ¨ì Form
            TextBox tb1 = new TextBox();
            tb1.Name = "tb1";
            tb1.Location = new Point(10, 10);
            this.Controls.Add(tb1);

            // ¥[¤J TextBox ¨ì GroupBox
            TextBox tb3 = new TextBox();
            tb3.Name = "tb3";
            tb3.Location = new Point(10, 10);
            this.groupBox1.Controls.Add(tb3);
            
            // ¥[¤J TextBox ¨ì Panel
            TextBox tb4 = new TextBox();
            tb4.Name = "tb4";
            tb4.Location = new Point(10, 10);
            this.panel1.Controls.Add(tb4)
            

¤£¥ÎrichTextBoxªºdebug¤èªk            

¼g
System.Diagnostics.Debug.WriteLine("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX");

¨ì¡i¿é¥X¡jµøµ¡¬İ¿é¥X¸ê®Æ

¥ı¨ì±M®×/¥kÁä/Äİ©Ê/«Ø¸m ¤Ä¿ï ©w¸qDEBUG±`¼Æ





 C# byte Âà ¤å¦r
byteÂàchar©Î byteÂàstring

Convert.ToChar¬O§âhexÂà¦¨¬Û¹ïÀ³ascii code
¹³aªºascii code¬O0x61

byte[] b = new byte[2] { 0x61,0x62 };
string s=Convert.ToChar(b[0]); => s="a";
string s=Convert.ToChar(b[1]); => s="b";

¦pªG§A­n§âbyte codeÂà¦¨"¦r­±¤W"ªº¼Æ­È À³¸Ó³o¼Ë¼g

byte[] b = new byte[2] { 0x61,0x62 };
string s=b[0].ToString("X2"); => s="61";
string s=b[1].ToString("X2"); => s="62";

ToString("X2")³o­Ó®æ¦¡¤Æ¦r¦êÁÙÆZ¦n¥Îªº ¤@¤U´N¥i¥H§âbyteÂà¦¨¬Û¹ïÀ³ªº¤å¦r
¥H«e§Ú­n§âbyteÂà¦¨¤å¦r³£¬O¥Î¤U­±³o¤èªk

byte[] b = new byte[2] { 0x03,0x04 };
string s= Convert.ToString(b[1], 16);
if (s.Length == 1) //¤£º¡2¦ì­n¸É¤@­Ó¹s
{
s= "0"+s;
}
===> s="03";

¤Ó³Â·Ğ¤F ¨º»ò¦h¦æª½±µ¥Îb[0].ToString("X2")¤@¦æ´N¥i¥H¨ú¥N ÁÙ¤£¥Î¦Û¤v§PÂ_«e­±­n¤£­n¸É¹s 




ÅÜ§ó·Æ¹«¹«¼Ğ¹Ï®× ( ¦³®Ä½d³ò¦bForm¤º )¡C
this.Cursor = new Cursor("C:\\test.ico"); // "C:\\test.ico" §ï¦¨±zªº¹ÏÀÉ¡A±µ¨üªº¼v¹³®æ¦¡¬°cur»Pico






[ C# ] WinForm Åã¥Ü©ó©µ¦ù¿Ã¹õ¤§¤èªk
https://georgiosky2000.wordpress.com/2014/03/19/c-winform-%e9%a1%af%e7%a4%ba%e6%96%bc%e5%bb%b6%e4%bc%b8%e8%9e%a2%e5%b9%95%e4%b9%8b%e6%96%b9%e6%b3%95/


        Graphics g;
        Pen p;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            p = new Pen(Color.Red, 6);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            g = this.CreateGraphics();
            g.DrawString("ÅçÃÒ§¹¦¨", new Font("¼Ğ·¢Åé", 60), new SolidBrush(Color.Blue), new PointF(20, 20));

        }




richTextBox1.Text += "year = " + year.ToString("00") + "\n";
richTextBox1.Text += "month = " + month.ToString("00") + "\n";
richTextBox1.Text += "mday = " + mday.ToString("0000") + "\n";
richTextBox1.Text += "wday = " + wday.ToString() + "\n";
richTextBox1.Text += "hour = " + hour.ToString("00") + "\n";
richTextBox1.Text += "minutes = " + minutes.ToString("00") + "\n";
richTextBox1.Text += "seconds = " + seconds.ToString("00") + "\n";
richTextBox1.ScrollToCaret();       //RichTextBoxÅã¥Ü°T®§¦Û°Ê±²°Ê¡AÅã¥Ü³Ì«á¤@¦æ


richTextBox1.Text += receive_buffer_tmp[i].ToString("X2") + " ";

string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
string filename = "imsLink_log.long." + DateTime.Now.ToString("yyyy.MMdd.HHmm.ss") + 

string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");


lb_time1.Text = "PC®É¶¡ : " + DateTime.Now.ToString("yyyy" + '/' + "MM" + '/' + "dd ") + weekday + DateTime.Now.ToString(" HH" + ':' + "mm" + ':' + "ss");


string filename = "imsLink_log." + DateTime.Now.ToString("yyyy.MMdd.HHmm.ss") + ".txt";


                    else if (Comport_Mode == 2)  //hex mode
                    {
                        input = "";
                        for (int i = 0; i < BytesToRead; i++)
                        {
                            input += ((int)receive_buffer[i]).ToString("X2") + " ";
                        }
                        richTextBox1.AppendText(input);     //¥´¦L¤@¯ë¤å¦r°T®§
                        richTextBox1.ScrollToCaret();       //RichTextBoxÅã¥Ü°T®§¦Û°Ê±²°Ê¡AÅã¥Ü³Ì«á¤@¦æ
                    }
48 65 78 20 6D 6F 64 65 986F 793A 5167 5BB9 0A 






string©Mbyte[]ªºÂà´« (C#)

stringÃş«¬Âà¦¨byte[]¡G

byte[] byteArray = System.Text.Encoding.Default.GetBytes ( str );

¤Ï¹L¨Ó¡Abyte[]Âà¦¨string¡G

string str = System.Text.Encoding.Default.GetString ( byteArray );

¨ä¥¦½s½X¤è¦¡ªº¡A¦pSystem.Text.UTF8Encoding¡ASystem.Text.UnicodeEncoding classµ¥¡F¨Ò¦p¡G

stringÃş«¬Âà¦¨ASCII byte[]¡G¡]"01" Âà¦¨ byte[] = new byte[]{ 0x30, 0x31}¡^

byte[] byteArray = System.Text.Encoding.ASCII.GetBytes ( str );

ASCII byte[] Âà¦¨string¡G¡]byte[] = new byte[]{ 0x30, 0x31} Âà¦¨ "01"¡^

string str = System.Text.Encoding.ASCII.GetString ( byteArray );








string text = "¬O¤£¬Oº~¦r¡AABC¡Akeleyi.com";
for (int i = 0; i < text.Length; i++)
{
	if (Regex.IsMatch(text[i].ToString(), @"[\u4e00-\u9fbb]+{1}quot;))
		Console.WriteLine("¬Oº~¦r");
	else
	Console.WriteLine("¤£¬Oº~¦r");
}

3400¡ã4DFFh¡G¤¤¤éÁú»{¦Pªí·N¤å¦rÂX¥RA°Ï¡AÁ`­p¦¬®e6,582­Ó¤¤¤éÁúº~¦r¡C
	4E00¡ã9FFFh¡G¤¤¤éÁú»{¦Pªí·N¤å¦r°Ï¡AÁ`­p¦¬®e20,902­Ó¤¤¤éÁúº~¦r¡C
A000¡ãA4FFh¡GÂU±Ú¤å¦r°Ï¡A¦¬®e¤¤°ê«n¤èÂU±Ú¤å¦r©M¦r®Ú¡C
AC00¡ãD7FFh¡GÁú¤å«÷­µ²Õ¦X¦r°Ï¡A¦¬®e¥HÁú¤å­µ²Å«÷¦¨ªº¤å¦r¡C
F900¡ãFAFFh¡G¤¤¤éÁú­İ®eªí·N¤å¦r°Ï¡AÁ`­p¦¬®e302­Ó¤¤¤éÁúº~¦r¡C
FB00¡ãFFFDh¡G¤å¦rªí²{§Î¦¡°Ï¡A¦¬®e²Õ¦X©Ô¤B¤å¦r¡B§Æ§B¨Ó¤å¡Bªü©Ô§B¤å¡B¤¤¤éÁúª½¦¡¼ĞÂI¡B¤p²Å¸¹¡B¥b¨¤²Å¸¹¡B¥ş¨¤²Å¸¹µ¥¡C

Hexadecimal value of °ò is 57FA
Hexadecimal value of ¥» is 672C
Hexadecimal value of ¹B is 904B
Hexadecimal value of ºâ is 7B97
Hexadecimal value of ¨î is 5236
Hexadecimal value of §@ is 4F5C
Hexadecimal value of U is 0055
Hexadecimal value of S is 0053
Hexadecimal value of B is 0042
Hexadecimal value of ? is 542F
Hexadecimal value of ? is 52A8
Hexadecimal value of ? is 76D8
Hexadecimal value of ? is 30A6
Hexadecimal value of ? is 30A3
Hexadecimal value of ? is 30AD
Hexadecimal value of ? is 30DA
Hexadecimal value of ? is 30C7
Hexadecimal value of ? is 30A3
Hexadecimal value of ? is 30A2
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ¥@ is 4E16
Hexadecimal value of ? is 003F
Hexadecimal value of ¥Í is 751F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ·§ is 6982
Hexadecimal value of ? is 003F
Hexadecimal value of ªí is 8868
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F



'

vcs
http://cs0.wikidot.com/introduction
https://jjnnykimo.pixnet.net/blog/category/1324785/9

Simple way to Zip files with C# .NET (Framework 4.5 /4.6)
https://coderwall.com/p/hgotua/simple-way-to-zip-files-with-c-net-framework-4-5-4-6
C# UNIX Timestamp Creation
https://coderwall.com/p/6mrs5a/c-unix-timestamp-creation

¡ic#¡j emgucv ³]©w
https://debbiedbaby.pixnet.net/blog/post/426657881-%E3%80%90c%23%E3%80%91-emgucv-%E8%A8%AD%E5%AE%9A

¦p¦ó¦Û­q¥kÁä¤u¨ã¿ï³æ
http://davidhsu666.com/archives/context_menu/



c# Delay 1¬íÄÁ¼gªk

using System.Threading;
Thread.Sleep(1000); //Delay 1¬í


codepage
http://www.lingoes.net/en/translator/codepage.htm

¨Ï¥Î¹w³]½s½X
System.IO.StreamReader file = new System.IO.StreamReader(@"c:\test.txt", Encoding.Default);

¨Ï¥Î«ü©w½s½X
System.IO.StreamReader file = new System.IO.StreamReader(@"c:\test.txt", Encoding.GetEncoding("big5"));


¬Û¦P
Encoding.GetEncoding("big5")
Encoding.GetEncoding(950)




C# ´£¨Ñ¤F³\¦h¤èªkµ¹string¨Ï¥Î

¤èªk				»¡©ú 					®æ¦¡
Length				¨ú±o¦r¦êªø«×ªø«×			x.Length
IndexOf('ÃöÁä¦r')		·j´M¸ÓÃöÁä¦r©Ò¦b°_©l¦ì¸mªº¯Á¤Ş­È	x.IndexOf("H")
Insert(¯Á¤Ş, 'ÃöÁä¦r')		±NÃöÁä¦r´¡¤J«ü©w¯Á¤Ş¦ì¸m		x.Insert(3,"Hello")
Remove(¯Á¤Ş)			²M°£¯Á¤Ş¦ì¸m¤§«áªº¦r¦ê			x.Remove(2)
Replace('­ì¦r¦ê', '·s¦r¦ê')	±N­ì¦r¦ê¨ú¥N¬°·s¦r¦ê			x.Replace("Hi","Hello")
Substring(¯Á¤Ş, ªø«×)		±q«ü©w¯Á¤Ş¦ì¸m¨ú±o«ü©wªø«×ªº¦r¦ê	x.Substring(3,10)
Contains('ÃöÁä¦r')		§PÂ_¬O§_¥]§t¸ÓÃöÁä¦r			x.Contains("Build")


            string x = "My name is Tom";

            int j = x.Length;
            Console.WriteLine(j);//14

            int p = x.IndexOf("me");
            Console.WriteLine(p);//5

            string k = x.Insert(0, "Hello! ");
            Console.WriteLine(k);//Hello! My name is Tom

            string l = x.Remove(10);
            Console.WriteLine(l);//My name is

            string m = x.Replace("Tom", "John");
            Console.WriteLine(m);//My name is John

            string i = x.Substring(3, 7);
            Console.WriteLine(i);//name is

            if (x.Contains("Tom"))
            {
                Console.WriteLine("Yes! You are Tom");
            }else
            {
                Console.WriteLine("Who are you?");
            }//Yes! You are Tom
            

¥t¥~¡Astring¸òarray¤@¼Ë¡A¯Á¤Şªº°_©l­È¤]¬O0
¦]¦¹¡A¥i¥Hª½±µ¾Ş§@¯Á¤Ş¨Ó¨ú±o¦r¤¸
½d¨Ò

string x = "Hello world";
Console.WriteLine(x[4]); //o






§ïÅÜ¦UºØ·Æ¹«Äİ¼Ğ

            pictureBox1.Cursor = Cursors.Cross;  //²¾¨ì±±¥ó¤W¡A§ïÅÜ¹«¼Ğ
            pictureBox1.Cursor = Cursors.Help;
            pictureBox1.Cursor = Cursors.HSplit;
            pictureBox1.Cursor = Cursors.No;
            
            this.Cursor = System.Windows.Forms.Cursors.Help;
            this.Cursor = Cursors.Help; 
            
            this.Cursor = Cursors.WaitCursor;	//µ¥«İ¼Ğ°O
            this.Cursor = Cursors.Default;	//¹w³]
            

¦Û©w¸q·Æ¹«Äİ¼Ğ
this.Cursor = new Cursor("icon.ico");
icon.ico­n©ñ¦bbin¤§¤U

¤£¥Î»s§@´å¼ĞÀÉªº°µªk:
this.Cursor = new Cursor(new Bitmap(@"C:\______test_vcs\reuse.bmp").GetHicon());


[C#] webBrowser¦p¦ó§PÂ_ºô­¶¬O§_Åª¨ú§¹¦¨


¦bWindows Mobile 6 ¤W¥ÎC# Åª¨ú¹Ï¤ù(¦pjpg)¶K¦bµe­±¤W 	µe¤W¤@¹Ï
Graphics g = this.CreateGraphics();

//¿ï¾Ü±z­n¶Kªºµe­±ªº¹Ï¤ù¦ì¸m
Bitmap br = new Bitmap("My Documents\\§Úªº¹Ï¤ù\\Waterfall.jpg");

//©ñ¸m±z©Ò«ü©wªº¹Ï¤ù
//¨Ã«ü©w¹Ï¤ù­n©ñ¸mªº¦ì¸m¡A(X,Y) = (0,0)
g.DrawImage(br, 0, 0);



¦bWindows Mobile 6 ¤W¥ÎC# Åª¨ú¤å¦rÀÉ®×

using System.IO;

FileStream fs = new FileStream("data.txt", FileMode.Open);
StreamReader sr = new StreamReader(fs, Encoding.Default);
string str = "";

//Åª¨ú¤å¦rÀÉ¸Ìªº¨C¤@¦C
//ª½¨ì¨S¦³¤å¦r´N°±¤U¨Ó
while( (str = sr.ReadLine()) != null)
{
      //­Y¬°ªÅ¥Õ¦C¡A«h¤£Åã¥Ü
      if(str != "") textBox.Text += str + "\r\n";
}



¦bWindows Mobile 6 ¤W¥ÎC# µeÂI»PÂI¤§¶¡ªº½u¬q¡A¤èªk¦³¤G! 

 ¤èªk¤@¡G(¨âÂI¤§¶¡ªº½u¬q)
      Graphics g = this.CreateGraphics();
      Pen pen = new Pen(Color.Blue, 2);     

      //10, 10 ¬°°_©l¦ì¸m¡A20, 20 ²×ÂI¦ì¸m
      g.DrawLine(pen, 10, 10, 20, 20);

 

¤èªk¤G¡G(¦hÂI¤§¶¡ªº½u¬q)
      Graphics g = this.CreateGraphics();
      Pen pen = new Pen(Color.Blue, 2);      

      //©w¸q¤@­Ó°}¦C¦³¤T­ÓÂI
      //¤À§O¬°(10,10)¡B(20,20)¡B(30,30)
      Point[] points = 
      {
            new Point(10, 10),
            new Point(20, 20),
            new Point(30, 30)
      };

      g.DrawLines(pen, points);




¦bWindows Mobile 6 ¤W¥ÎC# µe¹ê¤ß¶ê°é¡A´N¬O§â°é°é¶ñº¡¡A¤èªk¦³¤G!


¤èªk¤@¡G(¥Î¹Ï¤ù¶ñº¡¶ê°é)
      Graphics g = this.CreateGraphics();
      TextureBrush tb = new TextureBrush(new Bitmap(@"Program Files\\drawImage\\point.jpg"));
     
      //20, 20 ¬°®y¼Ğ¦ì¸m¡A10, 10 ¬°¶êªº¤j¤p
      g.FillEllipse(tb, 20, 20, 10, 10);

 

¤èªk¤G¡G(¥Îµ§¨ê¶ñº¡¶ê°é)
      Graphics g = this.CreateGraphics();
      SolidBrush sb = new SolidBrush(Color.Blue);
      
      //20, 20 ¬°®y¼Ğ¦ì¸m¡A10, 10 ¬°¶êªº¤j¤p
      g.FillEllipse(sb, 20, 20, 10, 10);




¦bWindows Mobile 6 ¥­»O¤WªºPDA ¼g¤@­Ó§ì¨úµL½uAP(µL½u°Ï°ìºô¸ô)°T¸¹±j®zªº¤pµ{¦¡(¨Ï¥ÎC#¦b.NET Compact Framework 2.0¤W) 

https://dreamtails.pixnet.net/blog/post/22318000




Áú¾Ô
1950¦~6¤ë25¤é¡Ğ1953¦~7¤ë27¤é[µù 19]
¡]3¦~1­Ó¤ë¤S2¤Ñ¡^



°O±o¦b((TextBox)sender).SelectAll();«áÃä¥[¤W¤@¥ye.SuppressKeyPress = true;

§_«hÁä½L®ø®§ÁÙ·|Ä~Äò¶Ç»¼¨ì°òÂ¦±±¥ó¡A¶Ç¥XÃø§vªº¡§¥m¡¨¤@Án





  uiMode:String; ¼½©ñ¾¹¬É­±¼Ò¦¡¡A¥i?Full, Mini, None, Invisible 
  
  
  
  
  
  
  
  
   [C#]¶}±ÒEXEÀÉ¨Ã¿é¤JEXEÀÉªº°Ñ¼Æ
¥ıUSING System.Diagnostics;

¦bµ{¦¡¸Ì©ñ¤J¤U¦Cµ{¦¡
System.Diagnostics.Process.Start("¸ô®|", "°Ñ¼Æ"); 



c# ­º¦r¥À¤j¼g ¤èªk
s.Substring(0,1).ToUpper()+s.Substring(1);






DateTimeÃş«¬¤¤ DayOfWeek®Éªº­^¤å¦p¦óÂà´«¦¨¤¤¤å

1.³o¬O¤@Ïú³Ì²Âªº¤èªk 

Code highlighting produced by Actipro CodeHighlighter (freeware)http://www.CodeHighlighter.com/-->int   i=(int)DateTime.Today.DayOfWeek;  
 switch(i)  
 {  
          case   0:  
                      txtDate.Text="¬P´Á¤Ñ"¡F  
                      break¡F  
          case   1:  
                      txtDate.Text="¬P´Á¤@"¡F  
                      break¡F  
          case   2:  
                      txtDate.Text="¬P´Á¤G"¡F  
                      break¡F  
          case   3:  
                      txtDate.Text="¬P´Á¤T"¡F  
                      break¡F  
          case   4:  
                      txtDate.Text="¬P´Á¥|"¡F  
                      break¡F  
          case   5:  
                      txtDate.Text="¬P´Á¤­"¡F  
                      break¡F  
          case   6:  
                      txtDate.Text="¬P´Á¤»"¡F  
                      break¡F  
          ¡K¡K  
 }
 
 
 
2.Áo©úªº¤èªk¡G
string strWeek = "¬P´Á"+"¤é¤@¤G¤T¥|¤­¤»".Substring((int)System.DateTime.Now.DayOfWeek,1); 


3.³Ì¦nªº¤èªk¡G 
string dateString = System.DateTime.Today.ToString("yyyy-M-d dddd", new System.Globalization.CultureInfo("zh-CN")); 







¥Î¤è¦VÁä²¾°Êpicturebox¦bform¤Wªº¦ì¸m

        private void Form1_Load(object sender, EventArgs e)
        {
            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
        }

        bool bIsEnterKeyPressed = false;
        private void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {

            if (e.KeyCode == Keys.Enter)
            {
                bIsEnterKeyPressed = true;
            }
            if (!bIsEnterKeyPressed)
            {
                int x = pictureBox1.Location.X;
                int y = pictureBox1.Location.Y;

                {
                    if (e.KeyCode == Keys.Right) x += 50;
                    else if (e.KeyCode == Keys.Left) x -= 50;
                    else if (e.KeyCode == Keys.Up) y -= 50;
                    else if (e.KeyCode == Keys.Down) y += 50;
                    pictureBox1.Location = new Point(x, y);
                }
            }
        }



	//C# ¨ú±o¸ê®Æ§¨¤Uªº©Ò¦³ÀÉ®×(¥]¬A¤l¥Ø¿ı)
	//Åã¥Ü¨C­ÓÀÉ®×ªº¸ê°T
        private void button1_Click(object sender, EventArgs e)
        {
            string path = String.Empty;
            string filetype = String.Empty;
            filetype = "*.*";

            //path = @"D:\_DATA2\_VIDEO_¥ş¬°³Æ¥÷\¦Ê®a??_²M¤Q¤G«ÒºÃ®×";
            path = @"C:\______test_vcs";

            //C# ¨ú±o¸ê®Æ§¨¤Uªº©Ò¦³ÀÉ®×(¥]¬A¤l¥Ø¿ı)
            string[] files = System.IO.Directory.GetFiles(path, filetype, System.IO.SearchOption.AllDirectories);
            foreach (string filename in files)
            {
                richTextBox1.Text += "­ì¼´¨ìªºÀÉ®× : " + filename + "\n";
                FileInfo fi = new FileInfo(filename);
                richTextBox1.Text += "Name :" + fi.Name + "\n";
                richTextBox1.Text += "FullName :" + fi.FullName + "\n";
                richTextBox1.Text += "Directory :" + fi.Directory + "\n";
                richTextBox1.Text += "DirectoryName :" + fi.DirectoryName + "\n";
                richTextBox1.Text += "Extension :" + fi.Extension + "\n";
                richTextBox1.Text += "Length :" + fi.Length.ToString() + "\n";
                //C# ¨ú±oÀÉ®×«Ø¥ß¤é´Á,¤Î³Ì«á­×§ï¤é´Á 
                richTextBox1.Text += "ÀÉ®×«Ø¥ß¤é´Á" + fi.CreationTime.ToString() + "\n";
                richTextBox1.Text += "ÀÉ®×³Ì«á­×§ï¤é´Á" + fi.LastWriteTime.ToString() + "\n";
                //C# ¨ú±oÀÉ®×¸ô®|¡B°ÆÀÉ¦W¡BÀÉ®×¤j¤p
                richTextBox1.Text += "ÀÉ®×¸ô®|¡G " + filename.ToString() + "\n";
                richTextBox1.Text += "°ÆÀÉ¦W¡G " + filename.Substring(filename.LastIndexOf(".") + 1, filename.Length - filename.LastIndexOf(".") - 1) + "\n";    //¨ú±o°ÆÀÉ¦W
                richTextBox1.Text += "ÀÉ®×¤j¤p¡G " + File.Open(filename, FileMode.Open).Length.ToString() + " ¦ì¤¸²Õ\n";
                richTextBox1.Text += "\n";
            }

        }




°£¥h´«¦æ²Å¸¹
            //¸m´«´«¦æ²Å¸¹¬°ªÅ¥Õ¡AÅımessagebox¨q¥X¿é¤Jªº¦r¦ê
            String a = textBox1.Text;
            a = a.Replace("\r\n", "");
            a = a.Replace("\n", "");
            a = a.Replace("\r", "");
            MessageBox.Show(a);
        
        
        
 C# ®Ú¾Ú®à­±¤j¤p½Õ¾ãµøµ¡¤j¤p 
             int DeskWidth = Screen.PrimaryScreen.WorkingArea.Width; //PrimaryScreen¬°¨ú±o¥DÅã¥Ü¾¹¡AWorkingArea¥i¨ú±oÅã¥Ü¾¹ªº¤u§@°Ï(¤£¥]§t¤u§@¦C¡Kµ¥)
            int DeskHeight = Screen.PrimaryScreen.WorkingArea.Height;
            this.Width = Convert.ToInt32(DeskWidth * 0.8);
            this.Height = Convert.ToInt32(DeskHeight * 0.8);


            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            richTextBox1.AppendText("¿Ã¹õ¸ÑªR«× : " + screenWidth.ToString() + "*" + screenHeight.ToString() + "\n");






[C#]WinForm§Q¥ÎBitmapªºMakeTransparent±N¹Ï¤ù¬Y¨ÇÃC¦â³z©ú¤Æ
            Bitmap bmp2 = new Bitmap(asm.GetManifestResourceStream(name + ".puma.bmp"));//¸ü¤J¹Ï¤ù¸ê·½
            bmp2.MakeTransparent(Color.White);//±N¹Ï¤ù¥Õ¦â³¡¤À³z©ú¤Æ;
            this.pictureBox2.Image = bmp2;
            
            bit = new Bitmap("picture1.jpg");  //¹Ï¤ù©ñ¦bdebug¤º
            bit.MakeTransparent(Color.White);  //±Nµøµ¡¤¤¥Õ¦âªº³¡¥÷ÅÜ¬°³z©ú
            
            

vcs§ìºô¸ô¤WªºÀÉ®×

            try
            {
                //§ì²{¦b®É¶¡
                DateTime dt = DateTime.Now;
                string filetime = dt.ToString("yyyy-MM-dd-HHmm");  //±NÀÉ®×¼g¤J²{¦b®É¶¡

                WebClient wc = new WebClient();
                wc.DownloadFile("http://data.taipei/bus/PathDetail",    //§ì¨úÀÉ®×ºô§}
                "C:\\TEMP\\1_PathDetail\\PathDetail_" + filetime + ".gz");    //¼g¤J¥»¾÷ªº¸ô®|
            }
            catch
            {
                Environment.Exit(0);    //¦pªG§ì¤£¨ìÀÉ®×´NÂ÷¶}µ{¦¡¡A¨S³o¦æµ{¦¡·|¤@ª½¥d¦b³o¦pªG¨S§ì¨ìÀÉ®×ªº¸Ü¡K
            }
        
C# Åıµøµ¡­I´ºÅã¥ÜGIF°Êµe 
private void Form1_Load(object sender, EventArgs e)
        {
            bit = new Bitmap("1.gif");
            this.pictureBox1.Image = bit;
        }        
        µù¡G1.gif¤@¼Ë¬O©ñ¦b±M®×¸ê®Æ§¨¤U¡GWindowsFormsApp1\WindowsFormsApp1\bin\Debug

 C# ­­©wtextbox¥u¯à¿é¤J¼Æ¦r 
 
        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (((int)e.KeyChar < 48 | (int)e.KeyChar > 57) & (int)e.KeyChar != 8)
            {
                e.Handled = true;
            }
        }
 
 
C# StreamReader Åª¨ú®É¡A¤¤¤å¦r³¡¤ÀÅÜ¦¨¶Ã½Xªº¸Ñ¨M¤èªk 
 ¦]¦¹¥u­n«ü©w½s½X¤è¦¡§Y¥i¸Ñ¨M
	// ¤£«ü©w Encoding¡A¨ä Encodeing ¬° Unicode
	System.IO.StreamReader srNoEncode = new System.IO.StreamReader("DataFile.txt");
	txtNoEncode.Text = srNoEncode.ReadToEnd();
	
	// «ü©w Encoding ¬° System.Text.Encoding.Default (§@·~¨t²Î¥Ø«e ANSI ¦r½X­¶ªº½s½X¤è¦¡)
	System.IO.StreamReader srDefault = new System.IO.StreamReader("DataFile.txt",System.Text.Encoding.Default);
	txtsrDefault.Text = srDefault.ReadToEnd();
	
            



            int[] tall = new int[] { 10, 20, 30, 40, 50 };
            int sum = 0;
            foreach (int height in tall)
            {
                sum += height;
            }
            richTextBox1.Text += "Sum = " + sum.ToString() + "\n";



            String[] animal = new String[] { "lion", "mouse", "cat", "dog", "elephant" };
            foreach (String name in animal)
            {
                richTextBox1.Text += name + "\n";
            }
            richTextBox1.Text += "\n";






±q²Ä5¶µ¶ñ¸ê®Æ¨ìListView
            //´ú¸Õ¤¤
            ListViewItem i1 = new ListViewItem("File_add.txt");
            ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
            sub_i1a.Text = "3333";
            i1.SubItems.Add(sub_i1a);
            ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
            sub_i1b.Text = "2016/5/25 02:10¤W¤È";
            i1.SubItems.Add(sub_i1b);

            listView1.Items.Add(i1);

            //³]¸mListView³Ì«á¤@¦æ¥i¨£
            listView1.Items[listView1.Items.Count - 1].EnsureVisible();





        private void nudgeWindow()
        {
            // °O¿ıµøµ¡ÂÂ¦ì¸m
            int oldLeft = Left;
            int oldTop = Top;
            // ÅÜ°Ê¦ì¸m
            Random r = new Random();
            for (int i = 0; i <= 500; i++)
            {
                int left = r.Next(Left - 20, Left + 20);
                Left = left;
                int top = r.Next(Top - 20, Top + 20);
                Top = top;
                Left = oldLeft;
                Top = oldTop;
            }
        }



            System.Drawing.StringFormat drawFormat = new System.Drawing.StringFormat();
            drawFormat.FormatFlags = StringFormatFlags.DirectionVertical;
            g.DrawString("µe¦r¦êµeª½ªº", this.Font, new SolidBrush(Color.Black), 300, 100, drawFormat);


----------------many ST----------------

richTextBox1.Text += System.DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
2019/05/21 14:52:41

richTextBox1.Text += DateTime.Now.ToString() + "\n";
2019/5/21 ¤U¤È 02:52:42

----------------many SP----------------

using System.Windows.Media.Imaging­n¤Ş¥ÎPresentationCore

¥u»İ­n¦b¤Ş¥Î-->µ{§Ç¶°-->®Ø¬[-->PresentationCore




string my_string = "   Åwªï¨Ó¨ìMyson Century!   ";

string str2 = "ON-C";
bool res;
res = my_string.ToLower().Replace(" ", "").Contains(str2.ToLower().Replace("-", ""));
richTextBox1.Text += "result = " + res.ToString() + "\n";



¦bWindows¤W¡A[¸ô®|]¥²¶·<248«ô¡A[ÀÉ¦W¥[¸ô®|]¦W¥²¶·<260«ô

	List<Point> points = new List<Point>(); // ¬ö¿ı·Æ¹«­y¸ñªº°}¦C¡C	

	List<MyFileInfo> fileinfos = new List<MyFileInfo>();             

1ºûlist«Å§i
	List<string> myLists = new List<string>();
	
	myLists.Add("A001");
	myLists.Add("A002");
	myLists.Add("A003"); 

2ºûlist«Å§i
	List<List<string>> myLists = new List<List<string>>();

	myLists.Add(new List<string>() { "A001", "David" });
	myLists.Add(new List<string>() { "A002", "John" });
	myLists.Add(new List<string>() { "A003", "Tom" });             
             
             
             
             
             
bmp
https://www.pcschool.com.tw/campus/share/lib/160/
http://crazycat1130.pixnet.net/blog/post/1345538-%E9%BB%9E%E9%99%A3%E5%9C%96%EF%BC%88bitmap%EF%BC%89%E6%AA%94%E6%A1%88%E6%A0%BC%E5%BC%8F

[C#] List ªº¥Îªk
http://frank1025.pixnet.net/blog/post/347251643-%5Bc%23%5D-list

C# axWindowsMediaPlayer¨î§@¼½©ñ¾¹
http://www.mamicode.com/info-detail-986551.html


AxWindowsMediaPlayer´CÊ^¤å¥ó¥D­n¤èªkÄİ©Ê
https://blog.csdn.net/ivan_ljf/article/details/9774231


AForge Webcam ¿ı¼v
https://blog.csdn.net/m_buddy/article/details/62417912

        private void button1_Click(object sender, EventArgs e)
        {

            /*
            Random ¶Ã¼Æ = new Random();//¶Ã¼ÆºØ¤l
            int i = ¶Ã¼Æ.Next(0, 100);//¦^¶Ç0-99ªº¶Ã¼Æ
            ¦pªG¥Îfor ©Î¨ä¥¦¦^°é§ì¶Ã¼Æ¡A¤@©w­n§â Random ¶Ã¼Æ = new Random();//¶Ã¼ÆºØ¤l ©ñ¦b¦^°é¥~­±¡C
            */


            Random ¶Ã¼Æ = new Random();//¶Ã¼ÆºØ¤l
            for (int i = 0; i < 100; i++)
            {
                int j = ¶Ã¼Æ.Next(0, 100);
                richTextBox1.Text += j.ToString() + "  ";
            }
            richTextBox1.Text += "\n";


        }

        //C# ¬O§_¬°JPGÀÉ®× record

        private bool ¬O§_¬°JPGÀÉ®×(string ÀÉ®×)
        {
            if (!File.Exists(ÀÉ®×))
                return false;

            using (System.Drawing.Image img = System.Drawing.Image.FromFile(ÀÉ®×))
            {
                if (img.RawFormat.Equals(System.Drawing.Imaging.ImageFormat.Jpeg))
                    return true;
            }
            return false;
        }



¤@¨Çvcs¸ê®Æ
http://createps.pixnet.net/blog/category/1630969/2

g.DrawString("ª½±µ³]©w¦r«¬»P¤j¤p", new Font("§ºÊ^", 30), Brushes.Red, 10, 10);


C# - ¨ú±oÀH¾÷¦r¦êªº§Ö³t¤èªk 


C#»y¨¥¤U¸ô®|«ü©w¤è¦¡¦³¨âºØ:

    ¬O¨Ï¥Î¨â­Ó±×½u¡A¨Ò¦p    "C:\\Test.txt"
    ²Ä¤GºØ¬O¦b¸ô®|«e¥[¤W@²Å¸¹¡A¨Ò¦p    @"C:\Test.txt"



¨ú±oµwºĞ¸ê°T
            System.IO.DriveInfo di = new System.IO.DriveInfo(@"C:\");
            richTextBox1.Text += "TotalFreeSpace : " + di.TotalFreeSpace.ToString() + "\n";
            richTextBox1.Text += "VolumeLabel : " + di.VolumeLabel + "\n";




         Bitmap myImage = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height); 
            Graphics g = Graphics.FromImage(myImage); 
            g.CopyFromScreen(new Point(0,0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height)); 
            IntPtr dc1 = g.GetHdc(); 
            g.ReleaseHdc(dc1); 
            myImage.Save(@"c:\screen0.jpg");
            
            




 ÁA¸Ñµ{¦¡°õ¦æ®É¶¡ 

using System.Diagnostics;
//-------------------------------------------
Stopwatch sw = new Stopwatch();
long num = 0;
sw.Reset();
sw = Stopwatch.StartNew();
//­n´ú³tªºµ{¦¡©ñ³o¸Ì
sw.Stop();
TimeSpan el = sw.Elapsed;
Console.WriteLine("ªá¶O {0} ", el);
long ms = sw.ElapsedMilliseconds;
Console.WriteLine("ªá¶O {0} ²@¬í", ms);

¸É¥R»¡©ú: ¤£¤@©w¨C¦¸´ú¨ìªº®É¶¡³£¬Û¦P³á!
«ØÄ³­È: ¶W¹L100²@¬í´N¦³ÂI¤ÓºCÅo¡K. (¹q¸£Äê·|Lag§óªø)






tmp code


            richTextBox1.Text += "¦~¡G" + dt.Year.ToString() + "\n";
            richTextBox1.Text += "¤ë¡G" + dt.Month.ToString() + "\n";
            richTextBox1.Text += "¤é¡G" + dt.Day.ToString() + "\n";
            richTextBox1.Text += "¤Ñ¡G" + dt.DayOfYear.ToString() + "\n";
            richTextBox1.Text += "¬P¡G" + dt.DayOfWeek.ToString() + "\n";
            richTextBox1.Text += "®É¡G" + dt.Hour.ToString() + "\n";
            richTextBox1.Text += "¤À¡G" + dt.Minute.ToString() + "\n";
            richTextBox1.Text += "¬í¡G" + dt.Second.ToString() + "\n";
            richTextBox1.Text += "²@¬í¡G" + dt.Millisecond.ToString() + "\n";
            richTextBox1.Text += "Ticks¡G" + dt.Ticks.ToString() + "\n";
            richTextBox1.Text += "TimeOfDay¡G" + dt.TimeOfDay.ToString() + "\n";

            System.Globalization.TaiwanCalendar TC = new System.Globalization.TaiwanCalendar();
            System.Globalization.TaiwanLunisolarCalendar TA = new System.Globalization.TaiwanLunisolarCalendar();

            DateTime dt = DateTime.Now;
            string message = "";
            message += string.Format("{0}", dt.Year) + "\n";
            message += ("¦è¤¸¦~:" + dt.Year.ToString()) + "\n";
            message += ("¥Á°ê¦~:" + TC.GetYear(dt)) + "\n";
            message += (string.Format("¦è¤¸:{0}/{1}/{2}", dt.Year, dt.Month, dt.Day)) + "\n";
            message += (string.Format("¥Á°ê:{0}/{1}/{2}", TC.GetYear(dt), TC.GetMonth(dt), TC.GetDayOfMonth(dt))) + "\n";
            message += (string.Format("¹A¾ä:{0}/{1}/{2}", TA.GetYear(dt), TA.GetMonth(dt), TA.GetDayOfMonth(dt))) + "\n";



            System.DateTime dt = System.DateTime.Now;
            richTextBox1.Text += "²{¦b¤é´Á¡G " + dt.ToLongDateString() + Environment.NewLine;
            richTextBox1.Text += "²{¦b®É¶¡¡G " + dt.ToLongTimeString() + Environment.NewLine;

            //²{¦b¤é´Á¥[¤Ñ¼Æ¼gªk(¥»¨Ò¬°¥[5¤Ñ):
            System.DateTime Add5Day = dt.AddDays(5);
            richTextBox1.Text += "²{¦b¤é´Á¥[5¤Ñ¡G " + Add5Day.ToLongDateString() + Environment.NewLine;

            //²{¦b®É¶¡¥[¤p®É¼gªk(¥»¨Ò¬°¥[12­Ó¤p®É):
            System.DateTime Add12Hours = dt.AddHours(12);
            richTextBox1.Text += "²{¦b®É¶¡¥[12¤p®É¡G " + Add12Hours.ToLongTimeString() + Environment.NewLine;

            //²{¦b®É¶¡´î¤ÀÄÁ¼gªk(¥»¨Ò¬°´î30¤ÀÄÁ):
            System.DateTime Minus30Minutes = dt.AddMinutes(-30);
            richTextBox1.Text += "²{¦b®É¶¡´î30¤ÀÄÁ¡G " + Minus30Minutes.ToLongTimeString() + Environment.NewLine;
        }
        
        
        
¬P´Á¤@        








C# ¨ú±oÀÉ®×ª©¥»¸ê°T
using System.Diagnostics;
            richTextBox1.Text += "data : " + FileVersionInfo.GetVersionInfo(@"C:\WINDOWS\NOTEPAD.EXE").FileVersion.ToString() + "\n"; 
data : 10.0.17134.220 (WinBuild.160101.0800)



        public Form1()
        {
            InitializeComponent();

            /*
            //´ú¸Õ¨S¦³¼ĞÃD¨S¦³Ãä®ØªºForm
            this.Text = string.Empty;
            this.ControlBox = false;
            */

        }
        

 ¨ú±o¥Ø«e¥i¥Î¦r«¬¡AÅã¥Ü©óListBox¡C

	this.listBox1.Items.AddRange(FontFamily.Families);


this.Cursor = System.Windows.Forms.Cursors.Hand;


§ïÅÜ¹«¼Ğ

        private void panel1_MouseHover(object sender, EventArgs e)
        {
            this.Cursor = System.Windows.Forms.Cursors.VSplit;
        }

        private void panel1_MouseLeave(object sender, EventArgs e)
        {
            this.Cursor = System.Windows.Forms.Cursors.Default;
        }
        
21. ÅÜ§ó·Æ¹«¹«¼Ğ¹Ï®× ( ¦³®Ä½d³ò¦bForm¤º )¡C
1             this.Cursor = new Cursor("C:\\test.ico"); // "C:\\test.ico" §ï¦¨±zªº¹ÏÀÉ¡A±µ¨üªº¼v¹³®æ¦¡¬°cur»Pico
        






C#ªìÅéÅç¡Aµe¹ÏªºÅª¡B¼g¡BÅã¥Ü 
https://darkblack01.blogspot.com/2014/03/c.html



vs2010ªºc#§ä¤£¨ìCalendar±±¥ó




C# µ{¦¡¾Ç²ß ¨t¦C	30½g
https://ithelp.ithome.com.tw/users/20023570/ironman/110


«Ü¦hC#½d¨Ò
http://fecbob.pixnet.net/blog/post/38088065-c%23-%E5%9C%93%E8%A7%92-panel


½Æ»s³¡¤À¹Ï¤ù


[C#] DrawRoundRetangle
//Ã¸»s¶ê¨¤¯x§Î
private GraphicsPath DrawRoundRect(float x, float y, float width, float height, float cornerRadius) {
            GraphicsPath roundedRect = new GraphicsPath();
            Rectangle rect = new Rectangle((int)x, (int)y, (int)width, (int)height);
            roundedRect.AddArc(rect.X, rect.Y, cornerRadius * 2, cornerRadius * 2, 180, 90);
            roundedRect.AddLine(rect.X + cornerRadius, rect.Y, rect.Right - cornerRadius * 2, rect.Y);
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y, cornerRadius * 2, cornerRadius * 2, 270, 90);
            roundedRect.AddLine(rect.Right, rect.Y + cornerRadius * 2, rect.Right, rect.Y + rect.Height - cornerRadius * 2);
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y + rect.Height - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 0, 90);
            roundedRect.AddLine(rect.Right - cornerRadius * 2, rect.Bottom, rect.X + cornerRadius * 2, rect.Bottom);
            roundedRect.AddArc(rect.X, rect.Bottom - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 90, 90);
            roundedRect.AddLine(rect.X, rect.Bottom - cornerRadius * 2, rect.X, rect.Y + cornerRadius * 2);
            roundedRect.CloseFigure();
            return roundedRect;
        }
        
        
        

[SDK] ©ó C#.net Àô¹Ò¤U, ¦p¦ó±N¬Û¾÷¼v¹³Ã¸»s©ó PictureBox ¤¤?
https://www.aisys.com.tw/web/tech/tech.php?question_id=127
[SDK] ©ó C#.net Àô¹Ò¤U, ¦p¦ó±N¬Û¾÷¼v¹³Ã¸»s©ó PictureBox ¤¤?

[«Å§i]
Graphics G;  //¦s©ñ Control.CreateGraphics «Ø¥ßªºª«¥ó
IntPtr pHdc; //¦s©ñ Graphics.GetHdc ¦^¶Çªº hdc ¦ì§}

[ªì©l¤Æ]
G = pictureBox1.CreateGraphics(); //¨Ï¥Î pictureBox1 «Ø¥ß¤@Graphicsª«¥ó

[Ã¸»s¼v¹³]
private void axAxAltairU1_OnSurfaceDraw(object sender, AxAxAltairUDrv.IAxAltairUEvents_OnSurfaceDrawEvent e)
{   // AltairU::OnSurfaceDraw ¨Æ¥ó
    pHdc = G.GetHdc(); //¨ú±o Hdc
    axAxAltairU1.DrawSurface(e.surfaceHandle, pHdc.ToInt32(), 1, 1, 0, 0); //Ã¸»s¼v¹³©ó Hdc
    G.ReleaseHdc();    //ÄÀ©ñ Hdc
}


´ú·sª©ªºvisual studio	¬İ¦³µL®Ñªş¥úºĞ




vcs
string»PString¦³¦ó¤£¦P¡H



vcs§ì¿Ã¹õµe­±¡A¦p¦ó°Ï¤À¥ş¿Ã¹õ©Mactiveµe­±¡H






ÀÉ®×¡GD://Xilinx_SDK_2018.3_1207_2324_Win64.exe,	


MD5¡G			0E83E8251D76B51B5D311EEA2B2FB8FC
MD5 SUM Value : 	0e83e8251d76b51b5d311eea2b2fb8fc    
			0E83E8251D76B51B5D311EEA2B2FB8FC

vcs_MD5

D:\Xilinx_SDK_2018.3_1207_2324_Win64.exe :   0E83E8251D76B51B5D311EEA2B2FB8FC

D:\Xilinx_SDK_2018.3_1207_2324_Win64.exe :   0E83E8251D76B51B5D311EEA2B2FB8FC




¤£¨¬¦ì¤¸¸É¹s ¤Q¶i¦ì¤Î¤Q¤»¶i¦ì

byte byteValue = 254;

// Display integer values by calling the ToString method.
richTextBox1.Text += byteValue.ToString("D8").ToString() + "\t" + byteValue.ToString("X8") + "\n";






vcs AForge

    ¥[¤J¤F°Ñ¦ÒAForge.Video.FFMPEG¡A½sÄ¶ÁÙ¬O¤£¹L

ª`·N¤@¤U¦³¨S¦³¥[¶iFFMPEGªº°Ñ¦Ò¡Aª½±µ¦bVisual Studio¸Ì¥[¬O¤£¦æªº¡A·|³ø¿ù¡C
­nª½±µ§â¥Ø¿ı¤UªºÀÉ®×½Æ»s¨ì¿é¥X¥Ø¿ı¡C

https://dahao.blogspot.com/2016/08/caforgenet.html



°ò¤_C#©MAforge.net¹ê²{¹Ï¹³¯À´y®ÄªG

https://blog.csdn.net/dark00800/article/details/41651499


¦UºØwebcamµ{¦¡¤ñ¸û
http://www.cnblogs.com/xrwang/archive/2010/02/13/HowToCaptureCameraVideoViaDotNet.html


AForge±Ò°Êwebcam
http://www.voidcn.com/article/p-kvujrudv-ru.html



       

vcs_WMP
richTextBox1.Text += " ºq¦±¦W†ï¡G" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Title");

mute & un-mute
        private void pictureBox7_Click(object sender, EventArgs e)//“C­µ
        {
            if (MM)
            {
                pictureBox7.Image = (Image)Properties.Resources.­µ¶q«ö…r@¦â;
                axWindowsMediaPlayer1.settings.mute = true;
                MM = false;
            }
            else
            {
                pictureBox7.Image = (Image)Properties.Resources.­µ¶q«ö…r;
                axWindowsMediaPlayer1.settings.mute = false;
                MM = true;
            }
        }


°Ñ¦Ò
063_¨Ï¥ÎC#¾Ş§@INI¤å¥ó
µ¹vcs_WMP ³]©w±`¥Îªºmp3¸ê®Æ§¨

vcs_WMP­n§ï¦¨¥i¥H¦h¿ïÀÉ®×  ©Î¿ï¾ã­Ó©Î¦h­Ó¸ê®Æ§¨ ¤@°_¼½©ñ








vcs

¬P´Á´X
            string[] Day = new string[] { "¬P´Á¤é", "¬P´Á¤@", "¬P´Á¤G", "¬P´Á¤T", "¬P´Á¥|", "¬P´Á¤­", "¬P´Á¤»" };
            string week = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();
            richTextBox1.Text += week + "\n";



vcs
ex069	Åª¨ú¥¿¤¤¡BÂ²¤¤¡B¤é¤å¡A¬O§_±µOK¡H
ex062	½Æ»s¤å¥ó®ÉÅã¥Ü½Æ»s¶i«×¡AÀ³¥ÎºC³tU½L¨Ó´ú



string color
color_r
color_g
color_b




[C#]¦p¦ó§ì¨úGoogle Static Map
https://dotblogs.com.tw/larrynung/2013/01/06/86807

Supalogo-§K¶Oªº½u¤WLogo¹Ï¤ù²£¥Í¾¹
https://dotblogs.com.tw/larrynung/2010/07/15/16580

[C#]­ì¤l¯à©e­û·|¿ç®gºÊ±±«D©x¤èAPI
https://dotblogs.com.tw/larrynung/2011/03/17/21890




[C#] QRCode Generator & Reader 
http://foxktr560.blogspot.com/2013/08/c-qrcode-generator-reader.html


vcs
vcsªºQR code½s½X¸Ñ½X
°Ñ¦Ò¡Ghttp://foxktr560.blogspot.com/2013/08/c-qrcode-generator-reader.html
§â zxing.dll ¥[¤J°Ñ¦Ò

¥ı¤U¸ü¤@­Ó¶}©ñªº¨ç¥Ü®w(DLL) "Zxing"
http://zxingnet.codeplex.com/



C#¤¤¨Ï¥ÎSendMessage¶i¦æ¶iµ{³q«Hªº¹ê¨Ò
https://blog.csdn.net/yl2isoft/article/details/20227421


(C#)WinAPIªºSendMessage¶Ç°e

[DllImport("user32.dll")]

public static extern long SendMessage(int hWnd, uint msg, uint wparam, string text);

public const uint WM_SETTEXT = 0x0c;
public const uint WM_GETTEXT = 0x0d;
public const uint WM_LBUTTONUP = 0x0202;
public const uint WM_LBUTTONDOWN = 0x0201;

SendMessage(¿é¤JÄæ¦ìªºHandle, WM_SETTEXT, 0, "§A­n°eªº¦r¦ê" );

¹ï«ö¶s«ö¤U¥hªº°T¸¹¡G

SendMessage(«ö¶sªºHandle, WM_LBUTTONDOWN, 0, null);

SendMessage(«ö¶sªºHandle, WM_LBUTTONUP, 0, null);


¨â­Ó°õ¦æÀÉ¶¡¼Æ­Èªº¶Ç»¼»P±µ¦¬



vcs ¤§ WebCam ¨Ï¥Î¤j¶°¦¨










/**
* @brief   Convert a 6 digit HTML code (hex) into a color value.
*/
#define HTML2COLOR(h)		((color_t)((((h) & 0xF80000)>>8) | (((h) & 0x00FC00)>>5) | (((h) & 0x0000F8)>>3)))
#define HTML2COLOR(h)		((COLOR_TYPE)(HTML2COLOR_R(h) | HTML2COLOR_G(h) | HTML2COLOR_B(h)))
#define HTML2COLOR(h)		((COLOR_TYPE)(((((h)&0xFF0000)>>16)+(((h)&0x00FF00)>>7)+((h)&0x0000FF)) >> (10-COLOR_BITS)))

#define COLOR_BITS		16
#define COLOR_TYPE		uint16_t
#define COLOR_TYPE_BITS		16


		
/**
 * @name   Some basic colors
 * @{
 */
#define White			HTML2COLOR(0xFFFFFF)
#define Black			HTML2COLOR(0x000000)
#define Gray			HTML2COLOR(0x808080)
#define Grey			Gray
#define Blue			HTML2COLOR(0x0000FF)
#define Red			HTML2COLOR(0xFF0000)
#define Fuchsia			HTML2COLOR(0xFF00FF)
#define Magenta			Fuchsia
#define Green			HTML2COLOR(0x008000)
#define Yellow			HTML2COLOR(0xFFFF00)
#define Aqua			HTML2COLOR(0x00FFFF)
#define Cyan			Aqua
#define Lime			HTML2COLOR(0x00FF00)
#define Maroon			HTML2COLOR(0x800000)
#define Navy			HTML2COLOR(0x000080)
#define Olive			HTML2COLOR(0x808000)
#define Purple			HTML2COLOR(0x800080)
#define Silver			HTML2COLOR(0xC0C0C0)
#define Teal			HTML2COLOR(0x008080)
#define Orange			HTML2COLOR(0xFFA500)
#define Pink			HTML2COLOR(0xFFC0CB)
#define SkyBlue			HTML2COLOR(0x87CEEB)
/** @} */
      


vcs ¨ú±oWebCam¼v¹³¡G		¨Ï¥ÎEmgu

°Ñ¦Ò¡G
C# ±±¨î Webcam ¡iusing Emgu¡j 
http://blog.kenyang.net/2012/03/04/c-webcam-using-emgu
[C#] ¨ú±oWebCam¼v¹³
http://foxktr560.blogspot.com/2013/08/c-webcam.html

OpenCV¬O¤@®M±j¤jªº¼v¹³³B²zlibrary¡A¥ÑINTEL¶}µo¡A
«D±`±j¤j¡A¬Æ¦Ü§A¥i¥H§Q¥ÎOpenCV¥h°µ¨ìOCR¡A«Ü¤è«K¡C
¤]¥Ñ©óOpenCV¨S¦³¤ä´©C#¡A¨ºC#­n«ç»ò¨Ï¥ÎOpenCV©O?
´N¬O¾aEmgu¡AEmgu¬O¤@®M¤¹³\OpenCVªºfunction¦bC#µ¥»y¨¥¤¤³Q¨Ï¥Î¡C

¶}±Òvcs±M®×¡A©Ô¤@­ÓpictureBox¡A·Ç³ÆÅã¥ÜWebCam¦^¶Çªº¼v¹³

±M®×¥[¤J°Ñ¦Ò¡G
C:/Emgu/emgucv-windows-x86 2.3.0.1416/bin/ ¦³4­Ódll

    Emgu.CV.dll
    Emgu.CV.ML.dll
    Emgu.CV.UI.dll
    Emgu.Util.dll
    
¥[¤J¥H«á¡A½Ğ¥ıÀx¦s§Aªº±M®×¡A
«ş¨©¥H¤U2­Ódll
    opencv_core231.dll
    opencv_highgui231.dll
©ñ¨ì±M®×ªº/bin/Debug/©³¤U

¦]¬°Emgu.CV.dll·|¨Ï¥Î¨ì¤W­z¨â­Ódll¡C


¥ıimport·|¨Ï¥Î¨ìªºlib¡A¦p¤U:

	using Emgu.CV;
	using Emgu.CV.Structure;

¥ı«Å§i¤@­ÓCaptureª«¥ó¡A¦p¤U:

	private Capture cap = null;                 // Webcamª«¥ó

³o­Óª«¥ó´N¬O¥Î¨Ó³sµ²¨ì§Aªºwebcam¡C



Form1_Load event¡A
³sµ²¨ìÄá¼v¾÷¥H¤Î«Ø¥ß¤@­Óevent¥Î¨Ó§ì¨úµe­±¡A¦p¤U:

private void Form1_Load(object sender, EventArgs e)
{
     cap = new Capture(0); // ³sµ²¨ìÄá¼v¾÷0¡A¦pªG§A¦³¨â¥xÄá¼v¾÷¡A²Ä¤G¥x´N¬O1
     Application.Idle += new EventHandler(Application_Idle); // ¦bIdleªºevent¤U¡A§âµe­±³]©w¨ìpictureBox¤W(·íµM§A¤]¥i¥H¥Îtimer¨Æ¥ó)
}


±µ¤U¨Ó­n¼g§ì¨úµe­±eventªºcode¡A

void Application_Idle(object sender, EventArgs e)
{
     Image<Bgr, Byte> frame = cap.QueryFrame(); // ¥hquery¸Óµe­±
     pictureBox1.Image = frame.ToBitmap(); // §âµe­±Âà´«¦¨bitmap«¬ºA¡A¦AÁıµ¹pictureBox¤¸¥ó
}

        


¥[¤J¥|­Ó°Ñ¦Ò 
Emgu.CV.dll
Emgu.CV.ML.dll
Emgu.CV.UI.dll
Emgu.Util.dll
 (¸Ódll©ñ©óEmguCV¦w¸Ë§¹ªºbin©³¤U)




3.2 ±`¥Î±µ¤f‡S©ú
caputure
        public Capture();			//Create a capture using the default camera
        public Capture(int camIndex);		//†Á‰ØŒs¹³‰³ªºŠD¼v, „G0…{©l
        public Capture(string fileName);	//The name of a file, or an url pointed to a stream.
        





2011/5/8(SUN)
2011/5/8(¤é) 20:28 µÛ«H


string»PString¦³¦ó¤£¦P¡H



vcs§ì¿Ã¹õµe­±¡A¦p¦ó°Ï¤À¥ş¿Ã¹õ©Mactiveµe­±¡H


bmp.Save(@"D:\ssss.jpg");


vcs_WMP
richTextBox1.Text += " ºq¦±¦W†ï¡G" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Title");

mute & un-mute
        private void pictureBox7_Click(object sender, EventArgs e)//“C­µ
        {
            if (MM)
            {
                pictureBox7.Image = (Image)Properties.Resources.­µ¶q«ö…r@¦â;
                axWindowsMediaPlayer1.settings.mute = true;
                MM = false;
            }
            else
            {
                pictureBox7.Image = (Image)Properties.Resources.­µ¶q«ö…r;
                axWindowsMediaPlayer1.settings.mute = false;
                MM = true;
            }
        }


°Ñ¦Ò
063_¨Ï¥ÎC#¾Ş§@INI¤å¥ó
µ¹vcs_WMP ³]©w±`¥Îªºmp3¸ê®Æ§¨

vcs_WMP­n§ï¦¨¥i¥H¦h¿ïÀÉ®×  ©Î¿ï¾ã­Ó©Î¦h­Ó¸ê®Æ§¨ ¤@°_¼½©ñ





C# ¦p¦ó¨ú±o¨â­Ó DateTime ¤é´Á¤§¶¡ªº¤Ñ¼Æ

¨ú±o¨â­Ó¤é´Á¤§¶¡ªº¡u¤Ñ¼Æ¡v¡]¤£¨¬¤@¤ÑªÌ±Ä¡uµL±ø¥ó§R¥hªk¡v¡^ 

    new TimeSpan(date1.Ticks - date2.Ticks).Days

¨ú±o¨â­Ó¤é´Á¤§¶¡ªº¡u¤Ñ¼Æ¡v¡]¦^¶Ç«¬§O¬° double Âùºë½T«×¡^

    new TimeSpan(date1.Ticks - date2.Ticks).TotalDays

¨ú±o¨â­Ó¤é´Á¤§¶¡ªº¡u¤p®É¼Æ¡v¡]¦^¶Ç«¬§O¬° double Âùºë½T«×¡^

    new TimeSpan(date1.Ticks - date2.Ticks).TotalHours

¨ú±o¨â­Ó¤é´Á¤§¶¡ªº¡u¤ÀÄÁ¼Æ¡v¡]¦^¶Ç«¬§O¬° double Âùºë½T«×¡^ 

    new TimeSpan(date1.Ticks - date2.Ticks).TotalMinutes




DateTime date1 = new DateTime(2008, 12,31, 23,59,59, DateTimeKind.Local);
DateTime date2 = new DateTime(2003, 2,13, 23,59,59, DateTimeKind.Local);
TimeSpan s = new TimeSpan(date1.Ticks - date2.Ticks);    







ID3®æ¦¡


¶}ÀY 	3 	¡uTAG¡v¡A¼ĞÅÒ¡C
¼ĞÃD 	30 	ºq¦±¼ĞÃD¡A³Ì¦h30­Ó­^¤å¦r¤¸¡C
ÃÀ³N®a 	30 	§@¦±©Îºt°ÛªÌªº¦W¦r¡A³Ì¦h30­Ó­^¤å¦r¤¸¡C
±M¿è 	30 	±M¿è¦WºÙ¡A³Ì¦h30­Ó­^¤å¦r¤¸¡C
¦~¤À 	4 	¦è¤¸¦~¤À¡A¥|­Ó¼Æ¦r¡C
µû½× 	28[3]©Î30 	´N¬Oµû½×¡C
¹s¦ì¤¸²Õ[3] 	1 	¦pªG¦³Àx¦s¦±¥Ø¡A¨º»ò³o­Ó¦ì¤¸²Õ·|Àx¦s¤@­Ó¤G¶i¦ìªº0¡C
¦±¥Ø[3] 	1 	³o­ººq¦b¸Ó±M¿è¤¤ªº¦±¥Ø¡A©ÎªÌ¬°0¡C­Y«e¤@­Ó¦ì¤¸²Õ«D¹s¡A«h¦¹Äæ¤º®eµL®Ä¡C
ÃÀ³NÃş«¬ 


header 	3 	"TAG"
title 	30 	30 characters of the title
artist 	30 	30 characters of the artist name
album 	30 	30 characters of the album name
year 	4 	A four-digit year
comment 	28[7] or 30 	The comment.
zero-byte[7] 	1 	If a track number is stored, this byte contains a binary 0.
track[7] 	1 	The number of the track on the album, or 0. Invalid, if previous byte is not a binary 0.
genre 	1 	Index in a list of genres, or 255 












¬İ½d¨Ò¾ÇC# ¨t¦C
https://ithelp.ithome.com.tw/users/20044155/ironman/241



wmp§ïÅÜµøµ¡¤j¤p
https://blog.csdn.net/ivan_ljf/article/details/9774231
axWindowsMediaPlayer1.DisplaySize¡@¡@¡@¡@¡@¡@¡@?¸m¼½©ñ?¶H¤j¤p  
¡@¡@¡@¡@1-MpDefaultSize¡@¡@¡@¡@¡@¡@¡@¡@¡@­ì©l¤j¤p  
¡@¡@¡@¡@2-MpHalfSize¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@ ­ì©l¤j¤pªº¤@¥b  
¡@¡@¡@¡@3-MpDoubleSize¡@¡@¡@¡@¡@¡@¡@¡@¡@ ­ì©l¤j¤pªº?­¿  
¡@¡@¡@¡@4-MpFullScreen¡@¡@¡@¡@¡@¡@¡@¡@¡@ ¥ş«Ì  
¡@¡@¡@¡@5-MpOneSixteenthScreen¡@¡@¡@¡@¡@ «Ì¹õ¤j¤pªº1/16  
¡@¡@¡@¡@6-MpOneFourthScreen¡@¡@¡@¡@¡@¡@¡@«Ì¹õ¤j¤pªº1/4  
¡@¡@¡@¡@7-MpOneHalfScreen¡@¡@¡@¡@¡@¡@¡@¡@«Ì¹õ¤j¤pªº1/2  

axWindowsMediaPlayer1.settings.balance = 1; ¦ñ°Û
axWindowsMediaPlayer1.settings.balance = -1;­ì°Û





windows media player
¦bµøÀW¼½©ñ¤§«á,¥i¥H³q¹L¦p¤U¤è¦¡Åª¨ú·½µøÀWªº¼e«×©M°ª«×,µM«á³]¸m¨äÁÙ­ì¬°­ì©lªº¤j¤p.
         private void ResizeOriginal()
         {
             int intWidth = axWindowsMediaPlayer1.currentMedia.imageSourceWidth;
             int intHeight = axWindowsMediaPlayer1.currentMedia.imageSourceHeight;
             axWindowsMediaPlayer1.Width = intWidth + 2;
             axWindowsMediaPlayer1.Height = intHeight + 2;
         }
         
         
         
         



//Wait
System.Threading.Thread.Sleep( 5000 ); // wait 5 seconds (5000 milliseconds)



//Take a screenshot 

// Take a screenshot
// By Ali Hamdar (http://alihamdar.com/)
// http://social.msdn.microsoft.com/Forums/en/csharpgeneral/thread/79efecc4-fa6d-4078-afe4-bb1379bb968b

// Default values for full screen
int width = System.Windows.Forms.Screen.PrimaryScreen.Bounds.Width;
int height = System.Windows.Forms.Screen.PrimaryScreen.Bounds.Height;
int top = 0;
int left = 0;

System.Drawing.Bitmap printscreen = new System.Drawing.Bitmap( width, height );
System.Drawing.Graphics graphics = System.Drawing.Graphics.FromImage( printscreen as Image );
graphics.CopyFromScreen( top, left, 0, 0, printscreen.Size );
printscreen.Save( outputfile, imagetype );




PNG Âà BMP
using System.Drawing.Imaging;   //for PixelFormat

        private void button1_Click(object sender, EventArgs e)
        {
            System.Drawing.Image PngImg = System.Drawing.Image.FromFile(@"C:\______test_vcs\sample.png");
            Bitmap myImage = new Bitmap(PngImg.Width, PngImg.Height, PixelFormat.Format32bppRgb);
            using (Graphics g = Graphics.FromImage(myImage))
            {
                g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                g.CompositingQuality = System.Drawing.Drawing2D.CompositingQuality.HighQuality;
                g.DrawImage(PngImg, 0, 0);
            }
            PngImg.Save(@"C:\______test_vcs\sample.bmp", ImageFormat.Bmp);
        }



label ¤§ cursor ¥i¥H§ïÅÜ´å¼Ğ«ü¨ìlabel®É¡A·|§ïÅÜªº·Æ¹«´å¼Ğ¡C


®Ú¾Ú®É¶¡«Ø¥ß¤å¥ó
File.Create("C:\\______test_vcs\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".jpg");//«Ø¥ß¤å¥ó


vcs¤Hª«¤ÀÃş
«Ò¤ıÃş
¨ä¥L


vcs·Ó¤ù+¤å¦r¡B·Ó¤ù+¯B¤ô¦L



vcs history
¤jscale
¤pscale
¥i¸m´«table
³B²zBC¼Æ¦r


VCS¨ì¬Y°Ï°ì¤º¡A¹«¼Ğ´«¦¨ºwºŞ¡A³o¼Ë¥Î¨ÓÀË´ú¨C­ÓÂIªºRGB­È

C#	w/ XML¤ÀªR



vcs
richtextbox¸Ì¡A¦p¦óª¾¹D¥Ø«e´å¼Ğ©Ò¦bªºline»Pposition

bmp
¦p¦ó§âbmpÀÉÅª¥X©Ò¦³ÂI ª½±µ¥h§ï¸Ì­±¼Æ¦r ¥t¦s·sÀÉ
¬İ¯à¤£¯à°µ¨ìÃC¦â¥­²¾ªº®ÄªG



vcs
ImageViewer is from _Yusuf Shakeel_CSharp



            
            
            
"
Bitmap Image (.bmp)|*.bmp|
Gif Image (.gif)|*.gif|
JPEG Image (.jpeg)|*.jpeg|
Png Image (.png)|*.png|
Tiff Image (.tiff)|*.tiff|
Wmf Image (.wmf)|*.wmf

";







vcs¶}±Ò¤@­Ó¯Â¤å¦rÀÉ¨ìrichtextbox¸Ì­±
¥Ø«e¨S¿ìªk³B²z¥¿¤¤¡BÂ²¤¤¡B¤é¤å¦P®É¦s¦bªº¯Â¤å¦rÀÉ


//¶}±ÒÀÉ®×
FileStream myFile = File.Open(@"C:\myWriter.txt", FileMode.OpenOrCreate, FileAccess.ReadWrite);

BinaryReader myReader = new BinaryReader(myFile);

int dl = System.Convert.ToInt16(myFile.Length);
//Åª¨ú¦ì¤¸°}¦C

byte[] myData = myReader.ReadBytes(dl);
//ÄÀ©ñ¸ê·½

myReader.Close();

myFile.Close();



ImageViewer	¬ã¨s¿ï³æ¬[ºc


using System.Drawing.Imaging;

           Bitmap mimg = new Bitmap(width * 2, height);

            for (int y = 0; y < height; y++)
            {
                for (int lx = 0, rx = width * 2 - 1; lx < width; lx++, rx--)
                {
                    cnt++;
                    //get source pixel value
                    Color p = simg.GetPixel(lx, y);
                    if ((cnt % 10000) == 0)
                    {
                        richTextBox1.Text += p.A.ToString("X2") + p.R.ToString("X2") + p.G.ToString("X2") + p.B.ToString("X2") + "  ";
                        //richTextBox1.Text += p.A.ToString() + p.R.ToString() + p.G.ToString() + p.B.ToString() + "  ";
                    }

                    //set mirror pixel value
                    mimg.SetPixel(lx, y, p);
                    mimg.SetPixel(rx, y, p);
                }
            }

            //load mirror image in picturebox2
            pictureBox2.Image = mimg;

            //save (write) mirror image
            //mimg.Save("C:\\MirrorImage.png");
            mimg.Save("C:\\MirrorImage.jpg", ImageFormat.Jpeg);
            mimg.Save("C:\\MirrorImage.png", ImageFormat.Png);
            mimg.Save("C:\\MirrorImage.bmp", ImageFormat.Bmp);


vcs¤£¥iµeÂI¡A¥Îµe¾ò¶ê¨ú¥N




//-------------------------------------------------------------------------------------

            this.pictureBox1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pictureBox1.Dock = System.Windows.Forms.DockStyle.Bottom;


openFileDialog1.Filter = "XML³]©wÀÉ|*.xml";
openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.wmf";

            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "jpg (*.jpg)|*.jpg|bmp (*.bmp)|*.bmp|png (*.png)|*.png";


            SaveFileDialog sfd = new SaveFileDialog();
            sfd.Filter = "jpg (*.jpg)|*.jpg|bmp (*.bmp)|*.bmp|png (*.png)|*.png";


            

        //----¿ï¨ìtextbox®É¡A¿ï¨ú¥ş³¡¤å¦r
        private void TextBox_Enter(object sender, EventArgs e)
        {
            TextBox tb = sender as TextBox;
            tb.SelectAll();
        }



        //ÁY¤ppictureBox1
        //pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;/*AutoSize¥i¯àµLªkÁY¤p¹Ï¤ù*/
        //¥ı§ï¦¨µ¥¤ñ¨ÒÁY¤p¹Ï¤ùSizeMode
        pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;












§ïÅÜpictureBox¤j¤p§ïÅÜªí³æ¦ì¸m

pictureBox1.Image.Save(@"D:\bbbbb.jpg");




§ïÅÜ³¡¤À¦rÅéÃC¦â
            richTextBox1.SelectionStart = 10;
            richTextBox1.SelectionLength = 5;
            richTextBox1.SelectionColor = Color.Red;
            richTextBox1.SelectionBackColor = Color.Green;



Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);
DrawImage(bmp, 0, 0);
DrawImage(bmp, 0, 0); // ¦bªí³æ¤WÅã¥Ü bmp °O¾ĞÅé¹Ï¹³
this.Refresh() ; //°õ¦æ Form1_Paint()


Bitmap bmp =new Bitmap(@"D:\bear.jpg");


pictureBox1.SizeMode = pictureBoxSizeMode.AutoSize; //¦Û°Ê½Õ¾ã¤j¤p
pictureBox1.Image = bmp; //Åã¥Ü¦b pictureBox1 ¹Ï¤ù±±¨î¶µ¤¤

// bmp ªº¤j¤p©MpictureBox1 ¬Û¦P
Bitmap bmp = new Bitmap(this.PictureBox1.Width,
this.PictureBox1.Height);
// ¥H°O¾ĞÅé¹Ï¹³ bmp «Ø¥ß myDraw °O¾ĞÅéµe¥¬
Graphics myDraw = Graphics.FromImage(bmp);
MyDraw.Clear(this.pictureBox1.BackColor); //µe¥¬­I´º¦â
MyDraw.DrawLine(new pen(Color.Red,2),x,y,e.X,e.Y); //¥i



¤ıÀà¼Ó²î¤U¯q¦{¡Aª÷³®¤ı®ğÅfµM¦¬¡C
¤d´MÅKÂê¨I¦¿©³¡A¤@¤ù­°¼n¥X¥ÛÀY¡C
¤H¥@´X¦^¶Ë©¹¨Æ¡A¤s§Î¨ÌÂÂªE´H¬y¡C
¤µ³{¥|®ü¬°®a¤é¡A¬GÂS¿½¿½Äª²ı¬î¡C
¦¶³¶¾ôÃä³¥¯óªá¡A¯Q¦ç«Ñ¤f¤i¶§±×¡C
ÂÂ®É¤ıÁÂ°ó«e¿P¡A­¸¤J´M±`¦Ê©m®a¡C
§^·R©s¤Ò¤l¡A­·¬y¤Ñ¤U»D¡C¬õÃC±ó°a°Ã¡A¥Õ­ºª×ÃP¶³¡C
¾K¤ëÀW¤¤¸t¡A°gªá¤£¨Æ§g¡C°ª¤s¦w¥i¥õ¡A®{¦¹´¥²Mªâ¡C
¹é¸¨¥j¦æ®c¡A®cªá±I¹æ¬õ¡C
¥ÕÀY®c¤k¦b¡A¶¢§¤»¡¥È©v¡C
¥\»\¤T¤À°ê¡A¦W¦¨¤K°}¹Ï¡C
¦¿¬y¥Û¤£Âà¡A¿ò«ë¥¢§]§d¡C





------------------------------------------------------------------------------------------------------------------------


char[] bbv={'¦¿','¤@','¤H'};

¤ıÀà¼Ó²î¤U¯q¦{¡Aª÷³®¤ı®ğÅfµM¦¬¡C
¤d´MÅKÂê¨I¦¿©³¡A¤@¤ù­°¼n¥X¥ÛÀY¡C
¤H¥@´X¦^¶Ë©¹¨Æ¡A¤s§Î¨ÌÂÂªE´H¬y¡C
¤µ³{¥|®ü¬°®a¤é¡A¬GÂS¿½¿½Äª²ı¬î¡C";



            char[] bbv={'¿½','¤@','¼Ó'};
            string abc = "¤ıÀà¼Ó²î¤U¯q¦{¡Aª÷³®¤ı®ğÅfµM¦¬¡C¤d´MÅKÂê¨I¦¿©³¡A¤@¤ù­°¼n¥X¥ÛÀY¡C¤H¥@´X¦^¶Ë©¹¨Æ¡A¤s§Î¨ÌÂÂªE´H¬y¡C¤µ³{¥|®ü¬°®a¤é¡A¬GÂS¿½¿½Äª²ı¬î¡C";
       
            int aa = abc.IndexOfAny(bbv);
            int bb = abc.IndexOfAny(bbv, 32);
            int cc = abc.IndexOfAny(bbv, 32, 10);
            int dd = abc.IndexOfAny(bbv, 32, 20);
            int ee = abc.IndexOfAny(bbv, 32, 30);

            richTextBox2.Text += "length of abc = " + abc.Length.ToString() + "\n";
            richTextBox2.Text += "aa = " + aa.ToString() + "\n";
            richTextBox2.Text += "bb = " + bb.ToString() + "\n";
            richTextBox2.Text += "cc = " + cc.ToString() + "\n";
            richTextBox2.Text += "dd = " + dd.ToString() + "\n";
            richTextBox2.Text += "ee = " + ee.ToString() + "\n";




------------------------------------------------------------------------------------------------------------------------


this.richTextBox1.Size = new System.Drawing.Size(382, 594);



------------------------------------------------------------------------------------------------------------------------




------------------------------------------------------------------------------------------------------------------------






------------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------------






------------------------------------------------------------------------------------------------------------------------


        const int GB = 1024 * 1024 * 1024;//©w¸qGBªº­pºâ±`¶q
        const int MB = 1024 * 1024;//©w¸qMBWªº­pºâ±`¶q
        const int KB = 1024;//©w¸qKBªº­pºâ±`¶q
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / GB >= 1)
                return (Math.Round(KSize / (float)GB, 2)).ToString() + "GB";
            else if (KSize / MB >= 1)
                return (Math.Round(KSize / (float)MB, 2)).ToString() + "MB";
            else if (KSize / KB >= 1)
                return (Math.Round(KSize / (float)KB, 2)).ToString() + "KB";
            else
                return KSize.ToString() + "Byte";//Åã¥ÜByte­È
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += ByteConversionGBMBKB(Convert.ToInt64(textBox1.Text)) + "\n";
        }



------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------------



------------------------------------------------------------------------------------------------------------------------

            int[] x = { 0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600 };
            int[] y = { 200, 295, 368, 399, 381, 319, 228, 129, 48, 4, 8, 58, 144, 243, 331, 387, 397, 359, 282, 184, 91 };
            Bitmap bitM = new Bitmap(this.panel1.Width, this.panel1.Height);
            //MessageBox.Show("Width = " + this.panel1.Width + "  Height = " + this.panel1.Height);
            Graphics g = Graphics.FromImage(bitM);
            g.Clear(Color.WhiteSmoke);
            Point[] points = new Point[21];
            Random r = new Random();
            for (int i = 0; i < 21; i++)
            {
                points[i].X = x[i];
                points[i].Y = y[i];
            }
            g.DrawLines(new Pen(Color.FromArgb(r.Next(1, 255), r.Next(1, 255), r.Next(1, 255))), points);  //Ã¸»s§é½u 
            this.panel1.BackgroundImage = bitM;

------------------------------------------------------------------------------------------------------------------------


            int[] x = { 0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600 };
            int[] y = { 200, 328, 396, 373, 268, 131, 26, 3, 71, 200, 328, 396, 373, 268, 131, 26 };

            for (int i = 0; i < 10; i++)
            {
                Application.DoEvents();
                for (int j = 0; j < 20; j++)
                    System.Threading.Thread.Sleep(1);

                g.DrawLine(Pens.Red, new Point(x[i], 400 - y[i]), new Point(x[i + 1], 400 - y[i + 1]));
            }
            MessageBox.Show("OK");


------------------------------------------------------------




-----------------------------------------





XML µù¸Ñ	<!-- --> ªº¤º®e¡C


@"C:\______test_vcs\cat\cat2.png"

Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);



DrawImage(bmp, 0, 0);
DrawImage(bmp, 0, 0); // ¦bªí³æ¤WÅã¥Ü bmp °O¾ĞÅé¹Ï¹³

this.Refresh() ; //°õ¦æ Form1_Paint()


Bitmap bmp =new Bitmap(@"D:\bear.jpg");
pictureBox1.SizeMode = pictureBoxSizeMode.AutoSize; //¦Û°Ê½Õ¾ã¤j¤p
pictureBox1.Image = bmp; //Åã¥Ü¦b pictureBox1 ¹Ï¤ù±±¨î¶µ¤¤

// bmp ªº¤j¤p©MpictureBox1 ¬Û¦P
Bitmap bmp = new Bitmap(this.PictureBox1.Width,
this.PictureBox1.Height);
// ¥H°O¾ĞÅé¹Ï¹³ bmp «Ø¥ß myDraw °O¾ĞÅéµe¥¬
Graphics myDraw = Graphics.FromImage(bmp);
MyDraw.Clear(this.pictureBox1.BackColor); //µe¥¬­I´º¦â
MyDraw.DrawLine(new pen(Color.Red,2),x,y,e.X,e.Y); //¥i¥HÃ¸¹Ï¤F






Ã¸»s¹Ï§Îª«¥óªº¤èªk

GraphicsÃş§OGDI+´£¨Ñ¤U¦C¤èªk¨ÓÃ¸»s¤W­z²M³æ¤¤ªº¶µ¥Ø¡G 


DrawLines

DrawCurve
DrawClosedCurve


        private void Form1_Resize(object sender, EventArgs e)
        {
            pictureBox1.Width = this.ClientSize.Width - 20;
            pictureBox1.Height = this.ClientSize.Height - 20;
        }

	DrawCircle(200, 200, 100);

        private void DrawCircle(int center_x, int center_y, int radius)
        {
            int linewidth = 5;
            // Create a Graphics object for the Control.
            Graphics g = pictureBox1.CreateGraphics();
            // Create a new pen.
            Pen PenStyle = new Pen(Color.Red, 5);
            // Set the pen's width.
            PenStyle.Width = linewidth;
            // Draw the circle
            g.DrawEllipse(PenStyle, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));
            //Dispose of the pen.
            PenStyle.Dispose();
        }


	private void DrawPixel(int xx, int yy)
	{
		
	}
	


PictureBoxSizeMode

                case 0: pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize; break;
                case 1: pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage; break;
                case 2: pictureBox1.SizeMode = PictureBoxSizeMode.Normal; break;
                case 3: pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage; break;
                case 4: pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; break;


«Ø¥ßµe¥¬

Graphics µe¥¬ª«¥óÅÜ¼Æ;
µe¥¬ª«¥óÅÜ¼Æ = ±±¨î¶µ¦WºÙ.CreateGraphics();

¨Ò¦p¡G¦bªí³æ¤W«Ø¥ßµe¥¬g¡G
Graphics g;
g = this.CreateGraphics();


¨Ò¦p¡G¦b¹Ï¤ù¤è¶ôpictureBox1¤W«Ø¥ßµe¥¬g¡G
Graphics g;
g = pictureBox1.CreateGraphics();

µeµ§Penª«¥ó

Pen µeµ§ = new Pen(µeµ§ÃC¦â, µeµ§²Ê²Ó);
Pen p = new Pen(Color.Blue, 5);
p.Color = Color.Red;
p.Width = 2;

µ§¨êª«¥ó¡]³æ¦âS¡B¹Ï®×T¡Bªá¯¾H¡Bº¥¼hL¡^

µ§¨êÃş§O
SolidBrush		«Ø¥ß³æ¤@ÃC¦âªºµ§¨ê
	SolidBrush sb = new SolidBrush(Color.Red);
	Pen p = new Pen(sb, 2);
TextureBrush		«Ø¥ß¥H¹Ï§Îª«¥ó·í§@¹Ï®×ªºµ§¨ê
	TextureBrush tb = new TextureBrush("bmp1.bmp");
	Pen p = new Pen(tb, 2);
HatchBrush		«Ø¥ßªá¯¾µ§¨ê
	HatchBrush ªá¯¾µ§¨êÅÜ¼Æ = new HatchBrush(ªá¯¾µ§¨ê, «e´ºÃC¦â, ­I´ºÃC¦â);
	HatchBrush hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Red);
	Pen p = new Pen(hb, 10);
	(­n¥ı¥[¤J¡Gusing System.Drawing.Drawing2D;)
LinearGradienBrush	«Ø¥ßº¥¼hµ§¨ê
	LinearGradientBrush º¥¼hµ§¨êÅÜ¼Æ = new LinearGradientBrush(º¥¼h¯x§Î°Ï°ì, «e´ºÃC¦â, ­I´ºÃC¦â, º¥¼h¶É±×¨¤«×);
	
	Rectangle rect1 = new Rectangle(0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);
	LinearGradientBrush lgb = new LinearGradientBrush(rect1, Color.Blue, Color.Red, 90);
	Pen p = new Pen(lgb, 10);
	(­n¥ı¥[¤J¡Gusing System.Drawing.Drawing2D;)


Pen µeµ§ = new Pen(µeµ§ÃC¦â, µeµ§²Ê²Ó);






³]©wÃC¦âªº¤èªk	©I¥sÀRºA¨ç¦¡¡GColor.FromArgb()

ex:
Color red= Color.FromArgb(255,0,0)
this.BackColor=Color.White;


Pen¥u¦³¤@Ãş
Brush¦³¥|Ãş

Pen¥Î©ó§i¶DGraphics¦p¦óÃ¸»s½u±ø
Brush¥Î©ó¶ñ¥R°Ï°ì

Pointªº¥Îªk
Point b=new Point(20,10);
Point a=new Point();
a.X=20;
a.Y=10;


Ã¸»sµê½u¡A¥i³]©wPenªºDashStyleÄİ©Ê¬°Dash,Dot,DashDot©ÎªÌDashDotDotµ¥
§ïÅÜª½½uºİÂIªº§Îª¬¡A¥i¥H³]©wStartCap©MEndCapÄİ©Ê

blackPen.StartCap=LineCap.ArrowAnchor;







¦Û¤vÃ¸»sbitmap¹Ï¤ù«O¦s,¥Í¦¨ico¤å¥ó©ÎªÌ¹ï¶H
¤µ¤Ñ¦^µª¤@­Ó°İÃDªº®É­ÔªºÀHµ§
 

Bitmap bit = new Bitmap(100, 30);
Graphics g = Graphics.FromImage(bit);
SolidBrush sb = new SolidBrush(Color.Blue);
Rectangle rg = new Rectangle(new Point(0, 0), bit.Size);
g.FillRectangle(sb, rg);
g.DrawString("´ú¸Õ´ú¸Õ¨ş¨ş", this.Font, new SolidBrush(Color.White), new PointF(0, 0));
bit.Save("d://123.bmp");//«O¦s¤U¨Ó³o­Ó¥i¥H¬İ¥Í¦¨ªº¹Ï¤ù 
                
                

vcs
Form2ªº¤¸¥óªºModifiers­n§ï¦¨Internal, ¹w³]¬°private

//char * wday[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
¦b¹w³]ªº±¡ªp¤U¡AC# ¤£¯à¨Ï¥Î«ü¼Ğ¡A­Y­n¥Î«ü¼Ğªº¸Ü¡A­n¦b½sÄ¶¾¹³]©w¤¤±Ò¥Î unsafe ¼Ò¦¡¤~¦æ¡C



¦@¥Î¨Æ¥ó½d¨Ò	WinEventHandler

            Color cl = Color.Red;
            panel1.BackColor = cl;
            richTextBox1.Text += cl.R.ToString() + "," + cl.G.ToString() + "," + cl.B.ToString() + "\n";
            //txtColor.Text = ColorTranslator.ToHtml(cl).ToString();

            byte Alpha = 0xff;
            byte Red = 0x00;
            byte Green = 0xff;
            byte Blue = 0x00;

            Color cc = Color.FromArgb(Alpha, Red, Green, Blue);
            panel1.BackColor = cc;
            richTextBox1.Text += cl.R.ToString() + "," + cl.G.ToString() + "," + cl.B.ToString() + "\n";



-------------------------------------------------------------------------------------------------------------------------------------
®Ú¾Ú¤º®e¤ñ¹ïÀÉ®×

using System.IO;


            StreamReader sr1 = new StreamReader(textBox1.Text);		//³Ğ«ØStreamReader¹ï¶H
            StreamReader sr2 = new StreamReader(textBox2.Text);		//³Ğ«ØStreamReader¹ï¶H
            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()))	//Åª¨ú¤å¥ó¤º®e¨Ã§PÂ_
            {
                MessageBox.Show("¨â­ÓÀÉ®×¬Û¦P");
            }
            else
            {
                MessageBox.Show("¨â­ÓÀÉ®×¤£¬Û¦P");
            }
            
-------------------------------------------------------------------------------------------------------------------------------------
«Ø¥ßÁ{®ÉÀÉ®×

            FolderBrowserDialog P_FolderBrowserDialog = new FolderBrowserDialog();	//¿ï¾Ü¸ê®Æ§¨
            if (P_FolderBrowserDialog.ShowDialog() == DialogResult.OK)	//¿ï¾Ü¸ê®Æ§¨
            {
                File.Create(P_FolderBrowserDialog.SelectedPath + "\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".txt");//³Ğ«Ø¤å¥ó
            }


-------------------------------------------------------------------------------------------------------------------------------------
­pºâ®É¶¡¶¡¹j
dtpicker_first dtpicker_second ¬°DateTimePicker
            MessageBox.Show("¶¡¹j "+
                DateAndTime.DateDiff(	//¨Ï¥ÎDateDiff¤èªkÀò¨ú¤é´Á¶¡¹j
                DateInterval.Day, dtpicker_first.Value, dtpicker_second.Value,
                FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString()+" ¤Ñ", "¶¡¹j®É¶¡");






-------------------------------------------------------------------------------------------------------------------------------------
        //¤@¦æ¤@¦æÅª¨ú¯Â¤å¦rÀÉ®×¤¤ªº¤º®e
        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                openFileDialog1.ShowDialog();
                textBox1.Text = openFileDialog1.FileName;
                StreamReader SReader = new StreamReader(textBox1.Text, Encoding.Default);
                string strLine = string.Empty;
                while ((strLine = SReader.ReadLine()) != null)
                {
                    textBox2.Text += strLine + Environment.NewLine;
                }
            }
            catch { }
        }





-------------------------------------------------------------------------------------------------------------------------------------
¨Ï¥ÎMD5¥[±K

using System.Security.Cryptography; //for MD5

        public string Encrypt(string strPwd)
        {
            MD5 md5 = new MD5CryptoServiceProvider();   //³Ğ«ØMD5¹ï¶H
            byte[] data = System.Text.Encoding.Default.GetBytes(strPwd);//±N¦r¦ê½s½X¬°¤@­ÓByte§Ç¦C
            byte[] md5data = md5.ComputeHash(data);//­pºâdataByteªºHash­È
            md5.Clear();    //²MªÅMD5¹ï¶H
            string str = "";//©w¸q¤@­ÓÅÜ¶q¡A¥Î¨Ó°O¿ı¥[±K«áªº±K½X
            for (int i = 0; i < md5data.Length - 1; i++)//¹M¾úbyte¼Æ²Õ
            {
                str += md5data[i].ToString("x").PadLeft(2, '0');//¹ï¹M¾ú¨ìªºByte¶i¦æ¥[±K
            }
            return str;//ªğ¦^±o¨ìªº¥[±K¦r¦ê
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string P_str_Code = "ABCDEFG";
            richTextBox1.Text += "¨Ï¥ÎMD5¥[±K«áªºµ²ªG¬°¡G" + Encrypt(P_str_Code) + "\n";
        }






-------------------------------------------------------------------------------------------------------------------------------------
­pºâGB MB KB

        const int GB = 1024 * 1024 * 1024;//©w¸qGBªº­pºâ±`¶q
        const int MB = 1024 * 1024;//©w¸qMBWªº­pºâ±`¶q
        const int KB = 1024;//©w¸qKBªº­pºâ±`¶q
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / GB >= 1)
                return (Math.Round(KSize / (float)GB, 2)).ToString() + "GB";
            else if (KSize / MB >= 1)
                return (Math.Round(KSize / (float)MB, 2)).ToString() + "MB";
            else if (KSize / KB >= 1)
                return (Math.Round(KSize / (float)KB, 2)).ToString() + "KB";
            else
                return KSize.ToString() + "Byte";//Åã¥ÜByte­È
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += ByteConversionGBMBKB(Convert.ToInt64(textBox1.Text)) + "\n";
        }






-------------------------------------------------------------------------------------------------------------------------------------

µ{¦¡¥u¯à¦P®É¹B¦æ¤@­Ó  ¦bForm1_Load¥[¤J:

        private void Form1_Load(object sender, EventArgs e)
        {
            bool Exist;//©w¸q¤@­ÓboolÅÜ¶q ¥Î¨Óªí¥Ü¬O§_¤w¸g¹B¦æ
            //³Ğ«ØMutex¤¬¥¸¹ï¶H
            System.Threading.Mutex newMutex = new System.Threading.Mutex(true, "¶È¤@¦¸", out Exist);
            if (Exist)//¦pªG¨S¦³¹B¦æ
            {
                newMutex.ReleaseMutex();//¹B¦æ·sµ¡Ê^
            }
            else
            {
                MessageBox.Show("¥»µ{¦¡¤@¦¸¥u¯à¹B¦æ¤@­Ó¹ê¨Ò¡I", "´£¥Ü", MessageBoxButtons.OK, MessageBoxIcon.Information);//¼u¥X´£¥Ü«H®§
                this.Close();//Ãö³¬·í«eµ¡Ê^
            }

        }
        






-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------










-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------









-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------









-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------






