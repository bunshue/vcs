using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Net;
using System.Net.Mail;

namespace vcs_SendMail
{
    /// <summary>
    /// 功能：實現郵件發送,分裝發送郵件的調用方法
    /// </summary>
    /// <auther>
    ///     <name>Kencery</name>
    ///     <date>2015-8-18</date>
    /// </auther>
    public class Email
    {
        #region  --------------------字段--------------------

        private string _serviceType = "SMTP";
        private string _host;

        #endregion

        #region  --------------------屬性--------------------

        /// <summary>
        /// 發送者郵箱
        /// </summary>
        public string From { get; set; }

        /// <summary>
        /// 接收者郵箱列表
        /// </summary>
        public string[] To { get; set; }

        /// <summary>
        /// 抄送者郵箱列表
        /// </summary>
        public string[] Cc { get; set; }

        /// <summary>
        /// 秘抄者郵箱列表
        /// </summary>
        public string[] Bcc { get; set; }

        /// <summary>
        /// 郵件主題
        /// </summary>
        public string Subject { get; set; }

        /// <summary>
        /// 郵件內容
        /// </summary>
        public string Body { get; set; }

        /// <summary>
        /// 是否是HTML格式
        /// </summary>
        public bool IsBodyHtml { get; set; }

        /// <summary>
        /// 附件列表
        /// </summary>
        public string[] Attachments { get; set; }

        /// <summary>
        /// 郵箱服務類型(Pop3,SMTP,IMAP,MAIL等)，默認為SMTP
        /// </summary>
        public string ServiceType
        {
            get { return _serviceType; }
            set { _serviceType = value; }
        }

        /// <summary>
        /// 郵箱服務器，如果沒有定義郵箱服務器，則根據serviceType和Sender組成郵箱服務器
        /// </summary>
        public string Host
        {
            get
            {
                /*
                return string.IsNullOrEmpty(_host)
                    ? (this.ServiceType + "." +
                       Sender.Split("@".ToCharArray(), StringSplitOptions.RemoveEmptyEntries)[1])
                    : _host;
               */
                return "smtp.gmail.com";
                //return null;
            }
            set { _host = value; }
        }

        /// <summary>
        /// 郵箱賬號(默認為發送者郵箱的賬號)
        /// </summary>
        public string UserName { get; set; }

        /// <summary>
        /// 郵箱密碼(默認為發送者郵箱的密碼)，默認格式GB2312
        /// </summary>
        public string Password { get; set; }

        /// <summary>
        /// 郵箱優先級
        /// </summary>
        public MailPriority MailPriority { get; set; }

        /// <summary>
        ///  郵件正文編碼格式
        /// </summary>
        public Encoding Encoding { get; set; }

        #endregion

        #region  ------------------調用方法------------------

        /// <summary>
        /// 構造參數，發送郵件，使用方法備注：公開方法中調用
        /// </summary>
        public void Send()
        {
            var mail = new MailMessage();

            //讀取To  接收者郵箱列表
            if (this.To != null && this.To.Length > 0)
            {
                foreach (string to in this.To)
                {
                    if (string.IsNullOrEmpty(to)) continue;
                    try
                    {
                        mail.To.Add(new MailAddress(to.Trim()));
                    }
                    catch (Exception ex)
                    {
                        throw new Exception(ex.Message);
                    }
                }
            }
            //讀取Cc  抄送者郵件地址
            if (this.Cc != null && this.Cc.Length > 0)
            {
                foreach (var cc in this.Cc)
                {
                    if (string.IsNullOrEmpty(cc)) continue;
                    try
                    {
                        mail.CC.Add(new MailAddress(cc.Trim()));
                    }
                    catch (Exception ex)
                    {
                        throw new Exception(ex.Message);
                    }
                }
            }
            //讀取Attachments 郵件附件
            if (this.Attachments != null && this.Attachments.Length > 0)
            {
                foreach (var attachment in this.Attachments)
                {
                    if (string.IsNullOrEmpty(attachment)) continue;
                    try
                    {
                        mail.Attachments.Add(new Attachment(attachment));
                    }
                    catch (Exception ex)
                    {
                        throw new Exception(ex.Message);
                    }
                }
            }
            //讀取Bcc 秘抄人地址
            if (this.Bcc != null && this.Bcc.Length > 0)
            {
                foreach (var bcc in this.Bcc)
                {
                    if (string.IsNullOrEmpty(bcc)) continue;
                    try
                    {
                        mail.Bcc.Add(new MailAddress(bcc.Trim()));
                    }
                    catch (Exception ex)
                    {
                        throw new Exception(ex.Message);
                    }
                }
            }
            //讀取From 發送人地址
            try
            {
                mail.From = new MailAddress(this.From);
            }
            catch (Exception ex)
            {
                throw new Exception(ex.Message);
            }

            Console.WriteLine("");
            Console.WriteLine("from = " + this.From);
            Console.WriteLine("to = " + this.To);
            Console.WriteLine("Host = " + this.Host);
            Console.WriteLine("UserName = " + this.UserName);
            Console.WriteLine("Password = " + this.Password);
            Console.WriteLine("");

            //郵件標題
            Encoding encoding = Encoding.GetEncoding("GB2312");
            mail.Subject = this.Subject;
            //郵件正文是否為HTML格式
            mail.IsBodyHtml = this.IsBodyHtml;
            //郵件正文
            mail.Body = this.Body;
            mail.BodyEncoding = this.Encoding;
            //郵件優先級
            mail.Priority = this.MailPriority;

            //SMTP 外寄郵件伺服器設定
            SmtpClient smtp = new SmtpClient(this.Host, 25);   //實例一個SmtpClient類
            //smtp.Host = smtp_server;
            //smtp.Port = smtp_server_port;
            smtp.Timeout = 9999;
            smtp.EnableSsl = true; //gmail預設開啟驗證, 指定 SmtpClient 使用安全套接字層 (SSL) 加密連接
            smtp.UseDefaultCredentials = false; //不使用默認憑證，注意此句必須放在smtp.Credentials() 的上面
            smtp.Credentials = new NetworkCredential(this.From, this.Password); //這裡要填正確的帳號跟密碼, 驗證寄件者
            //smtp.Credentials = CredentialCache.DefaultNetworkCredentials;   //不可, 需要驗證寄件者
            smtp.DeliveryMethod = SmtpDeliveryMethod.Network;   //通過網絡發送到SMTP服務器
            try
            {
                smtp.Send(mail);
            }
            catch (Exception ex)
            {
                throw new Exception(ex.Message);
            }
            smtp.Dispose();
        }

        #endregion
    }

    /// <summary>
    ///郵件發送接口調用：bool isTrue=EmailInfo.SendEmail(參數,........);   參數解釋參考方法
    /// <auther>
    ///     <name>Kencery</name>
    ///     <date>2015-8-18</date>
    /// </auther>
    /// </summary>
    public static class EmailInfo
    {
        /// <summary>
        /// 郵件發送方法，傳遞參數(使用中如出現問題，請調試)
        /// </summary>
        /// <param name="from">發送者郵箱名稱(從配置文件中讀取，比如：934532778@qq.com)(必填項)</param>
        /// <param name="to">接收者郵箱列表，可以傳遞多個，使用string[]表示(從配置文件中讀取)(必填項)</param>
        /// <param name="cc">抄送者郵箱列表，可以傳遞多個，使用string[]表示(從配置文件中讀取)</param>
        /// <param name="bcc">秘抄者郵箱列表，可以傳遞多個，使用string[]表示(從配置文件中讀取)</param>
        /// <param name="subject">郵件主題，構造(必填項)</param>
        /// <param name="body">郵件內容，構造發送的郵件內容，可以發送網頁(必填項)</param>
        /// <param name="isBodyHtml">是否是HTML格式，true為是，false為否</param>
        /// <param name="attachments">郵箱附件，可以傳遞多個，使用string[]表示(從配置文件中讀取)，可空</param>
        /// <param name="host">郵箱服務器(從配置文件中讀取，如：smtp@qq.com)(必填項)</param>
        /// <param name="password">郵箱密碼(從配置文件中讀取，from郵箱的密碼)(必填項)</param>
        /// <returns>郵件發送成功，返回true,否則返回false</returns>
        public static bool SendEmail(string from, string[] to, string[] cc, string[] bcc, string subject, string body,
            bool isBodyHtml, string[] attachments, string host, string password)
        {
            //郵箱發送不滿足，限制這些參數必須傳遞
            Console.WriteLine("from = " + from);
            Console.WriteLine("to.len = " + to.Length.ToString());
            Console.WriteLine("subject = " + subject);
            Console.WriteLine("host = " + host);
            Console.WriteLine("password = " + password);

            if (from == "" || to.Length <= 0 || subject == "" || body == "" || host == "" || password == "")
            {
                Console.WriteLine("FFFFFFFF 1");

                return false;
            }

            var email = new Email
            {
                From = @from,
                To = to,
                Cc = cc,
                Bcc = bcc,
                Subject = subject,
                Body = body,
                IsBodyHtml = isBodyHtml,
                Attachments = attachments,
                Host = host,
                Password = password
            };
            try
            {
                email.Send();
                Console.WriteLine("OKOKOK");
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine("FFFFFFFF 2");
                throw new Exception(ex.Message);
            }
        }
    }
}
