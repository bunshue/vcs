
如果要聲明派生自另一個類的一個類,就可以使用下面的語法:

    class LearningClass : BasicClass
    {
    }

如果類(或結構)也派生自接口,則用逗號分隔列表中的基類和接口:

　　class LearningClass : BasicClass, BasicInterface, BasicInterface2
    {
    }


2.虛方法virtual： 

有時候我們繼承一個基類的某些方法希望能重新定義這個方法，我們可以把一個基類函數聲明virtual，就可以在任何派生類中重寫這個函數:

public class BasicClass
    {
        public virtual string GetMessage()
        {
            return "Basic class message";
        }
    }

C#中虛函數的概念與標准00P的概念相同:可以在派生類中重寫虛函數。在調用方法時,會調用該類對象的合適方法。在C#中,函數在默認情況下不是虛擬的,但(除了構造函數以外)可以顯 式地聲明為virtual。這遵循C++的方式,即從性能的角度來看,除非顯式指定,否則函數就不是虛 擬的。而在Java中,所有的函數都是虛擬的。但C#的語法與C++的語法不同,因為C#要求在派生 類的函數重寫另一個函數時,要使用override關鍵字顯式聲明:

    class LearningClass : BasicClass
    {
        public override string GetMessage()
        {
            return "Learning class message";
        }
    }

重寫方法的語法避免了C++中很容易發生的潛在運行錯誤:當派生類的方法簽名無意中與基類 版本略有差別時,該方法就不能重寫基類的方法:在C#中,這會出現一個編譯錯誤,因為編譯器會 認為函數已標記為override,但沒有重寫其基類的方法。

成員字段和靜態函數都不能聲明為virtual,因為這個概念只對類中的實例函數成員有意義。
3.隱藏方法： 

如果簽名相同的方法在基類和派生類中都進行了聲明,但該方法沒有分別聲明為virtual和 override,派生類方法就會隱藏基類方法。

在大多數清況下,是要重寫方法,而不是隱藏方法,因為隱藏方法會造成對於給定類的實例調用 錯誤方法的危險。但是,如下面的例子所示,C#語法可以確保開發人員在編譯時收到這個潛在錯誤的 警告,從而使隱藏方弦【如果這確實是用戶的本匐更加安全。這也是類庫開發人員得到的版本方面的 · 好處

　　public class LearningClass : BasicClass { public new string GetMessage() { return "Learning class message"; } }
4.調用函數的基類版本： 

C#有一種特殊的語法用於從派生類中調用方法的基類版本:base.()。例如,假定 派生類中的一個方法要返回基類的方法20%的返回值,就可以使用下面的語法:

    public class BasicClass
    {
        public virtual float GetPrice()
        {
            return 1.5f;
        }
    }
    public class LearningClass : BasicClass
    {
        public float GetPrice()
        {
            return base.GetPrice() * 0.2f;
        }
    }

ps：可以使用base.()語法調用基類中的任何方法,不必從同一個方法的重載 中調用它。
5.抽象類和抽象函數： 

C#允許把類和函數聲明為abstract。抽象類不能實例化,而抽象函數不能直接實現,必須在非抽 象的派生類中重寫。顯然,抽象函數本身也是虛擬的(盡管也不需要提供virtual關鍵字,實際上,如 果提供了該關鍵字,就會產生一個語法錯誤。如果類包含抽象函數,則該類也是抽象的,也必須聲 明為抽象的:

    public abstract class BasicClass
    {
        public abstract float GetPrice();
    }
    public class LearningClass : BasicClass
    {
        public override float GetPrice()
        {
            return 0.2f;
        }
    }

6.密封類和密封方法： 

C#允許把類和方法聲明為sealed。對於類,這表示不能繼承該類；對於方法，這表示不能重寫該方法。
C# 繼承

在把類或方法標記為sealed時,最可能的情形是:如果要對庫、類或自己編寫的其他類作用域 之外的類或方法進行操作,則重寫某些功能會導致代碼混亂。也可以因商業原因把類或方法標記為 sealed,以防第三方以違反授權協議的方式擴展該類。但一般情況下,在把類或成員標記為sealed 時要小心,因為這麼做會嚴重限制它的使用方式。即使認為它不能對繼承自一個類或重寫類的某個 成員發揮作用,仍有可能在將來的某個時刻,有人會遇到我們沒有預料到的情形,此時這麼做就很 有用。.NET基類庫大量使用了密封類,使希望從這些類中派生出自己的類的第三方開發人員無法訪 問這些類。例如,string就是一個密封類。

把方法聲明為sealed也可以實現類似的目的,但很少這麼做。
7.修飾符： 

C#共有五種訪問修飾符：public、private、protected、internal、protected internal。作用范圍如下表：
訪問修飾符 說明 public 公有訪問。不受任何限制。 private 私有訪問。只限於本類成員訪問，子類，實例都不能訪問。 protected 保護訪問。只限於本類和子類訪問，實例不能訪問。 internal 內部訪問。只限於本項目內訪問，其他不能訪問。 protected internal 內部保護訪問。只限於本項目或是子類訪問，其他不能訪問

C#成員類型的可修飾及默認修飾符如下表：
成員類型 默認修飾符 可被修飾符 enum public none class private public、protected、internal、private、
protected internal interface public none struct private public、internal、private

修飾符可以應用於類型的成員，而且有不同的用途：
修飾符 應用於 說明 new 函數成員 成員用相同的簽名隱藏繼承的成員 static 所有成員 成員不作用於類的具體實例 virtual 僅函數成員 成員可以由派生類重寫 abstract 僅函數成員 虛擬成員定義了成員的簽名，但沒有提供實例代碼 override 僅函數成員 成員重寫了繼承的虛擬或抽象成員 sealed 類,方法和屬性 對於類，不能繼承自密封類。對於屬性和方法，成員重寫已繼承的虛擬成員，但任何派生類中的任何成員都不能重寫該成員。該修飾符必須與override一起使用 extern 僅靜態[DllImport]方法 成員在外部用另一種語言實現




作　　者：請叫我頭頭哥
出　　處：http://www.cnblogs.com/toutou/
關於作者：專注於微軟平台的項目開發。如有問題或建議，請多多賜教！
版權聲明：本文版權歸作者和博客園共有，歡迎轉載，但未經作者同意必須保留此段聲明，且在文章頁面明顯位置給出原文鏈接。
特此聲明：所有評論和私信都會在第一時間回復。也歡迎園子的大大們指正錯誤，共同進步。或者直接私信我
聲援博主：如果您覺得文章對您有幫助，可以點擊文章右下角【推薦】一下。您的鼓勵是作者堅持原創和持續寫作的最大動力！



