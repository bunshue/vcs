//剪貼簿程式

　　　　　　　 /// <summary>
　　　　　　　 /// 刪除指定文件夾
　　　　　　　 /// </summary>
　　　　　　　 /// <param name="strDir">文件夾完整路徑</param>
　　　　　　　 /// <param name="recursive">是否刪除文件夾子項</param>
　　　　　　　 public static void DeleteFolder(string strDir, bool recursive)
　　　　　　　 {
　　　　　　　　　　　 Directory.Delete(strDir, recursive);
　　　　　　　 }

　　　　　　　 /// <summary>
　　　　　　　 /// 返回指定路徑的DirectoryInfo
　　　　　　　 /// </summary>
　　　　　　　 /// <returns></returns>
　　　　　　　 public static DirectoryInfo GetDir(string path)
　　　　　　　 {
　　　　　　　　　　　 return new DirectoryInfo(path);
　　　　　　　 }





　　　　　　　 /// <summary>
　　　　　　　 /// 讀取顯示
　　　　　　　 /// </summary>
　　　　　　　 /// <param name="filename">文本文件名</param>
　　　　　　　 /// <param name="contents">內容</param>
　　　　　　　 public static string Display(string filename)
　　　　　　　 {//讀取顯示
　　　　　　　　　　　 try
　　　　　　　　　　　 {
　　　　　　　　　　　　　　　 string contents;
　　　　　　　　　　　　　　　 FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read);　　 //讀出所打開的文本文件
　　　　　　　　　　　　　　　 StreamReader reader = new StreamReader(fs);　　　　 //實例化一個streamreader
　　　　　　　　　　　　　　　 contents = reader.ReadToEnd();　　　　　　　　　　 //將數據顯示
　　　　　　　　　　　　　　　 fs.Close();
　　　　　　　　　　　　　　　 return contents;
　　　　　　　　　　　 }
　　　　　　　　　　　 catch (Exception ex)
　　　　　　　　　　　 {
　　　　　　　　　　　　　　　 MessageBox.Show(ex.Message);
　　　　　　　　　　　　　　　 return "";
　　　　　　　　　　　 }
　　　　　　　 }
　　　　　　　 /// <summary>
　　　　　　　 /// 打開
　　　　　　　 /// </summary>
　　　　　　　 /// <param name="ofd">打開對話框</param>
　　　　　　　 /// <param name="fullname">文本文件名</param>
　　　　　　　 /// <param name="contents">內容</param>
　　　　　　　 public static void Open(OpenFileDialog ofd,string fullname,string contents)
　　　　　　　 {//打開文本
　　　　　　　　　　　 try
　　　　　　　　　　　 {
　　　　　　　　　　　　　　　 if (ofd.ShowDialog() == DialogResult.OK)
　　　　　　　　　　　　　　　 {
　　　　　　　　　　　　　　　　　　　 string fileName = ofd.FileName;　　　　 //文件名
　　　　　　　　　　　　　　　　　　　 FileStream fs = new FileStream(fileName, FileMode.Open, FileAccess.Read);
　　　　　　　　　　　　　　　　　　　 StreamReader reader = new StreamReader(fs);
　　　　　　　　　　　　　　　　　　　 fullname = fileName;
　　　　　　　　　　　　　　　　　　　 contents = reader.ReadToEnd();
　　　　　　　　　　　　　　　　　　　 fs.Close();
　　　　　　　　　　　　　　　 }
　　　　　　　　　　　 }
　　　　　　　　　　　 catch (Exception ex)
　　　　　　　　　　　 {
　　　　　　　　　　　　　　　 MessageBox.Show(ex.Message);
　　　　　　　　　　　 }
　　　　　　　 }
　　　　　　　 /// <summary>
　　　　　　　 /// 保存
　　　　　　　 /// </summary>
　　　　　　　 /// <param name="fullname">文本文件名</param>
　　　　　　　 /// <param name="contents">內容</param>
　　　　　　　 public static void Save(string fullname,string contents)
　　　　　　　 {//保存
　　　　　　　　　　　 try
　　　　　　　　　　　 {
　　　　　　　　　　　　　　　 StreamWriter writer = new StreamWriter(fullname);
　　　　　　　　　　　　　　　 writer.Write(contents);　　　　　 //用write()方法把txtContent的數據寫入文件
　　　　　　　　　　　　　　　 writer.Close();
　　　　　　　　　　　 }
　　　　　　　　　　　 catch (Exception ex)
　　　　　　　　　　　 {
　　　　　　　　　　　　　　　 MessageBox.Show(ex.Message);
　　　　　　　　　　　 }
　　　　　　　 }
　　　　　　　 /// <summary>
　　　　　　　 /// 另存為
　　　　　　　 /// </summary>
　　　　　　　 /// <param name="sfd">保存對話框</param>
　　　　　　　 /// <param name="contents">內容</param>
　　　　　　　 public static void SaveAs(SaveFileDialog sfd,string contents)
　　　　　　　 {
　　　　　　　　　　　 if (sfd.ShowDialog() == DialogResult.OK)
　　　　　　　　　　　 {
　　　　　　　　　　　　　　　 string fileName = sfd.FileName;
　　　　　　　　　　　　　　　 try
　　　　　　　　　　　　　　　 {
　　　　　　　　　　　　　　　　　　　 Stream stream = File.OpenWrite(fileName);
　　　　　　　　　　　　　　　　　　　 using (StreamWriter writer = new StreamWriter(stream))
　　　　　　　　　　　　　　　　　　　 {
　　　　　　　　　　　　　　　　　　　　　　　 writer.Write(contents);
　　　　　　　　　　　　　　　　　　　　　　　 writer.Close();
　　　　　　　　　　　　　　　　　　　 }
　　　　　　　　　　　　　　　 }
　　　　　　　　　　　　　　　 catch (Exception ex)
　　　　　　　　　　　　　　　 {
　　　　　　　　　　　　　　　　　　　 MessageBox.Show(ex.Message);
　　　　　　　　　　　　　　　 }
　　　　　　　　　　　 }
　　　　　　　 }
　　　　　　　 /// <summary>
　　　　　　　 /// 粗體
　　　　　　　 /// </summary>
　　　　　　　 /// <param name="rtb"></param>
　　　　　　　 public static void Bold(RichTextBox rtb)
　　　　　　　 {
　　　　　　　　　　　 Font newFont = new Font(rtb.SelectionFont,
　　　　　　　　　　　　　　　　　　　　　　　 (rtb.SelectionFont.Bold ?
　　　　　　　　　　　　　　　　　　　　　　　　 rtb.SelectionFont.Style & ~FontStyle.Bold :
　　　　　　　　　　　　　　　　　　　　　　　　 rtb.SelectionFont.Style | FontStyle.Bold));
　　　　　　　　　　　 rtb.SelectionFont = newFont;
　　　　　　　 }
　　　　　　　 /// <summary>
　　　　　　　 /// 斜體
　　　　　　　 /// </summary>
　　　　　　　 /// <param name="rtb"></param>
　　　　　　　 public static void Italic(RichTextBox rtb)
　　　　　　　 {
　　　　　　　　　　　 Font newFont = new Font(rtb.SelectionFont,
　　　　　　　　　　 (rtb.SelectionFont.Italic ?
　　　　　　　　　　　 rtb.SelectionFont.Style & ~FontStyle.Italic :
　　　　　　　　　　　 rtb.SelectionFont.Style | FontStyle.Italic));
　　　　　　　　　　　 rtb.SelectionFont = newFont;
　　　　　　　 }
　　　　　　　 /// <summary>
　　　　　　　 /// 下劃線
　　　　　　　 /// </summary>
　　　　　　　 /// <param name="rtb"></param>
　　　　　　　 public static void Underline(RichTextBox rtb)
　　　　　　　 {
　　　　　　　　　　　 Font newFont = new Font(rtb.SelectionFont,
　　　　　　　　　　 (rtb.SelectionFont.Underline ?
　　　　　　　　　　　 rtb.SelectionFont.Style & ~FontStyle.Underline :
　　　　　　　　　　　 rtb.SelectionFont.Style | FontStyle.Underline));
　　　　　　　　　　　 rtb.SelectionFont = newFont;
　　　　　　　 }
　　　　　　　 /// <summary>
　　　　　　　 /// 復制
　　　　　　　 /// </summary>
　　　　　　　 /// <param name="rtb"></param>
　　　　　　　 public static void Copy(RichTextBox rtb)
　　　　　　　 {
　　　　　　　　　　　 if (rtb.SelectedText.Equals(""))
　　　　　　　　　　　　　　　 return;
　　　　　　　　　　　 Clipboard.SetDataObject(rtb.SelectedText, true);
　　　　　　　 }
　　　　　　　 /// <summary>
　　　　　　　 /// 剪切
　　　　　　　 /// </summary>
　　　　　　　 /// <param name="rtb"></param>
　　　　　　　 public static void Cut(RichTextBox rtb)
　　　　　　　 {
　　　　　　　　　　　 if (rtb.SelectedText.Length > 0)
　　　　　　　　　　　 {
　　　　　　　　　　　　　　　 try
　　　　　　　　　　　　　　　 {
　　　　　　　　　　　　　　　　　　　 rtb.Cut();
　　　　　　　　　　　　　　　 }
　　　　　　　　　　　　　　　 catch (Exception ex)
　　　　　　　　　　　　　　　 {
　　　　　　　　　　　　　　　　　　　 MessageBox.Show(ex.Message);
　　　　　　　　　　　　　　　 }
　　　　　　　　　　　 }
　　　　　　　 }
　　　　　　　 /// <summary>
　　　　　　　 /// 粘貼
　　　　　　　 /// </summary>
　　　　　　　 /// <param name="rtb"></param>
　　　　　　　 public static void Paste(RichTextBox rtb)
　　　　　　　 {
　　　　　　　　　　　 rtb.Paste();
　　　　　　　 }
　　　　　　　 /// <summary>
　　　　　　　 /// 退出
　　　　　　　 /// </summary>
　　　　　　　 /// <param name="fullname">文本文件全名</param>
　　　　　　　 /// <param name="contents">內容</param>
　　　　　　　 public static void Exit(string fullname,string contents)
　　　　　　　 {
　　　　　　　　　　　 if (MessageBox.Show("　　　　　 是否保存文件",

"提示", MessageBoxButtons.OKCancel) == DialogResult.OK)
　　　　　　　　　　　 {
　　　　　　　　　　　　　　　 try
　　　　　　　　　　　　　　　 {
　　　　　　　　　　　　　　　　　　　 StreamWriter writer = new StreamWriter(fullname);
　　　　　　　　　　　　　　　　　　　 writer.Write(contents);　　　　　 //用write()方法把txtContent的數據寫入文件
　　　　　　　　　　　　　　　　　　　 writer.Close();
　　　　　　　　　　　　　　　 }
　　　　　　　　　　　　　　　 catch (Exception ex)
　　　　　　　　　　　　　　　 {
　　　　　　　　　　　　　　　　　　　 MessageBox.Show(ex.Message);
　　　　　　　　　　　　　　　 }
　　　　　　　　　　　 }
　　　　　　　 }









        /// <summary>
        /// 文件轉化為Char[]數組
        /// </summary>
        /// <param name="fileName"></param>
        /// <returns></returns>
        public static char[] FileRead(string fileName)
        {
            if (!Exists(fileName))
            {
                return null;
            }
            var byData = new byte[1024];
            var charData = new char[1024];
            try
            {
                var fileStream = new FileStream(fileName, FileMode.Open);
                fileStream.Seek(135, SeekOrigin.Begin);
                fileStream.Read(byData, 0, 1024);
            }
            catch (Exception ex)
            {
                throw new Exception(ex.Message);
            }
            var decoder = Encoding.UTF8.GetDecoder();
            decoder.GetChars(byData, 0, byData.Length, charData, 0);
            return charData;
        }



        /// <summary>
        /// 文件轉化為byte[]
        /// </summary>
        /// <param name="fileName">文件路徑</param>
        /// <returns></returns>
        public static byte[] ReadFile(string fileName)
        {
            FileStream pFileStream = null;
            try
            {
                pFileStream = new FileStream(fileName, FileMode.Open, FileAccess.Read);
                var r = new BinaryReader(pFileStream);
                //將文件指針設置到文件開
                r.BaseStream.Seek(0, SeekOrigin.Begin);
                var pReadByte = r.ReadBytes((int)r.BaseStream.Length);
                return pReadByte;
            }
            catch (Exception ex)
            {
                throw new Exception(ex.Message);

            }
            finally
            {
                if (pFileStream != null) pFileStream.Close();
            }
        }


        /// <summary>
        /// 將byte寫入文件
        /// </summary>
        /// <param name="pReadByte">字節流</param>
        /// <param name="fileName">文件路徑</param>
        /// <returns></returns>
        public static bool WriteFile(byte[] pReadByte, string fileName)
        {
            FileStream pFileStream = null;
            try
            {
                pFileStream = new FileStream(fileName, FileMode.OpenOrCreate);
                pFileStream.Write(pReadByte, 0, pReadByte.Length);
            }
            catch (Exception ex)
            {
                throw new Exception(ex.Message);
            }
            finally
            {
                if (pFileStream != null) pFileStream.Close();
            }
            return true;

        }
        
        
        
        
---------------------------------------




        /// <summary>
        /// 刪除文件
        /// </summary>
        /// <param name="fileName">文件的完整路徑</param>
        /// <returns></returns>
        public static bool DeleteFile(string fileName)
        {
            try
            {
                if (!Exists(fileName)) return false;
                File.Delete(fileName);
            }
            catch (IOException ioe)
            {
                throw new ArgumentNullException(ioe.Message);
            }

            return true;
        }


        public static void DeleteDir(DirectoryInfo dir)
        {
            if (dir == null)
            {
                throw new NullReferenceException("目錄不存在");
            }

            foreach (var d in dir.GetDirectories())
            {
                DeleteDir(d);
            }

            foreach (var f in dir.GetFiles())
            {
                DeleteFile(f.FullName);
            }

            dir.Delete();

        }


        /// <summary>
        /// 刪除目錄
        /// </summary>
        /// <param name="dir">指定目錄</param>
        /// <param name="onlyDir">是否只刪除目錄</param>
        /// <returns></returns>
        public static bool DeleteDir(string dir, bool onlyDir)
        {
            if (dir == null || dir.Trim() == "")
            {
                throw new NullReferenceException("目錄dir=" + dir + "不存在");
            }

            if (!Directory.Exists(dir))
            {
                return false;
            }

            var dirInfo = new DirectoryInfo(dir);
            if (dirInfo.GetFiles().Length == 0 && dirInfo.GetDirectories().Length == 0)
            {
                Directory.Delete(dir);
                return true;
            }


            if (!onlyDir)
            {
                return false;
            }
            DeleteDir(dirInfo);
            return true;
        }


        /// <summary>
        /// 在指定的目錄中查找文件
        /// </summary>
        /// <param name="dir">目錄</param>
        /// <param name="fileName">文件名</param>
        /// <returns></returns>
        public static bool FindFile(string dir, string fileName)
        {
            if (dir == null || dir.Trim() == "" || fileName == null || fileName.Trim() == "" || !Directory.Exists(dir))
            {
                return false;
            }

            //傳入文件路徑，獲取當前文件對象
            var dirInfo = new DirectoryInfo(dir);
            return FindFile(dirInfo, fileName);

        }


        /// <summary>
        /// 返回文件是否存在
        /// </summary>
        /// <param name="dir"></param>
        /// <param name="fileName"></param>
        /// <returns></returns>
        public static bool FindFile(DirectoryInfo dir, string fileName)
        {
            foreach (var d in dir.GetDirectories())
            {
                if (File.Exists(d.FullName + "\\" + fileName))
                {
                    return true;
                }
                FindFile(d, fileName);
            }

            return false;
        }


        /// <summary>
        /// 獲取指定文件夾中的所有文件夾名稱
        /// </summary>
        /// <param name="folderPath">路徑</param>
        /// <returns></returns>
        public static List<string> FolderName(string folderPath)
        {
            var listFolderName = new List<string>();
            try
            {
                var info = new DirectoryInfo(folderPath);

                listFolderName.AddRange(info.GetDirectories().Select(nextFolder => nextFolder.Name));
            }
            catch (Exception er)
            {
                throw new Exception(er.Message);
            }

            return listFolderName;

        }


        /// <summary>
        /// 獲取指定文件夾中的文件名稱
        /// </summary>
        /// <param name="folderPath">路徑</param>
        /// <returns></returns>
        public static List<string> FileName(string folderPath)
        {
            var listFileName = new List<string>();
            try
            {
                var info = new DirectoryInfo(folderPath);

                listFileName.AddRange(info.GetFiles().Select(nextFile => nextFile.Name));
            }
            catch (Exception er)
            {
                throw new Exception(er.Message);
            }

            return listFileName;
        }
    }

 


