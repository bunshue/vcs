
本文整理匯總了C#中HtmlAgilityPack.HtmlDocument.LoadHtml方法的典型用法代碼示例。如果您正苦於以下問題：C# HtmlDocument.LoadHtml方法的具體用法？C# HtmlDocument.LoadHtml怎麽用？C# HtmlDocument.LoadHtml使用的例子？那麽恭喜您, 這裏精選的方法代碼示例或許可以為您提供幫助。您也可以進一步了解該方法所在類HtmlAgilityPack.HtmlDocument的用法示例。

在下文中一共展示了HtmlDocument.LoadHtml方法的20個代碼示例，這些例子默認根據受歡迎程度排序。您可以為喜歡或者感覺有用的代碼點讚，您的評價將有助於我們的係統推薦出更棒的C#代碼示例。
示例1: GetVideoLink

        private static async Task<string> GetVideoLink(string link)
        {
            var httpClient = new HttpClient();

            var response = await httpClient.GetStringAsync(link);

            var doc = new HtmlDocument();
            doc.LoadHtml(response);

            var iframeLink = doc.DocumentNode.Descendants("body").
                First().
                Descendants("iframe").
                First().
                Attributes["src"].
                Value;

            response = await httpClient.GetStringAsync(iframeLink);

            doc.LoadHtml(response);

            var videoLink = response.Split('\"').
                Where(part =>
                part.Contains(".mp4") && part.StartsWith(@"http://")).
                FirstOrDefault();

            return videoLink;
        }

開發者ID:SamirHafez，項目名稱:Fresh，代碼行數:27，代碼來源:FreeTVCrawlerService.cs


示例2: ParseHtmlAsync

        public async Task<string> ParseHtmlAsync(string tenant, string html)
        {
            var doc = new HtmlDocument();
            doc.LoadHtml(html);

            var nodes = doc.DocumentNode.SelectNodes("//include[@article-alias and @category-alias]");
            if (nodes == null)
            {
                return html;
            }

            foreach (var node in nodes)
            {
                string alias = node.Attributes["article-alias"].Value;
                string categoryAlias = node.Attributes["category-alias"].Value;

                var model =  await ContentModel.GetContentAsync(tenant, categoryAlias, alias).ConfigureAwait(false);
                if (model != null)
                {
                    string contents = model.Contents;

                    var newNode = HtmlNode.CreateNode(contents);
                    node.ParentNode.ReplaceChild(newNode, node);
                }
            }

            return doc.DocumentNode.OuterHtml;
        }

開發者ID:frapid，項目名稱:frapid，代碼行數:28，代碼來源:ArticleExtension.cs


示例3: HtmlDocument

        /// <summary>
        /// New html document instance
        /// </summary>
        /// <param name="html"></param>
        /// <returns></returns>
        public HtmlDocument HtmlDocument(string html)
        {
            var d = new HtmlDocument();
            d.LoadHtml(html);

            return d;
        }

開發者ID:Alchemy86，項目名稱:DAS-Desktop，代碼行數:12，代碼來源:HttpBase.cs


示例4: ParseTopPerson

 public static void ParseTopPerson(string html, Action<List<Person>> finished)
 {
     BackgroundWorker bw = new BackgroundWorker();
     bw.DoWork += new DoWorkEventHandler((sender, e) =>
     {
         List<Person> TopPerson = new List<Person>();
         HtmlDocument hDoc = new HtmlDocument();
         hDoc.LoadHtml(html);
         var tableRows = hDoc.DocumentNode.SelectNodes(Constants.Instance.XPATH_GAME_TOP_RESULT);
         foreach (var node in tableRows)
         {
             var results = ChildElementsInTableRow(node);
             if (results.Count == Constants.Instance.COUNT_GAME_TOP_RESULT_COLUMNS)
             {
                 var person = TopPersonFromStrings(results);
                 if (person.Total != 0)
                 {
                     TopPerson.Add(person);
                 }
             }
         }
         finished(TopPerson);
     });
     bw.RunWorkerAsync();
 }

開發者ID:nkwsqyyzx，項目名稱:BetStrategy，代碼行數:25，代碼來源:HtmlParser.cs


示例5: ParsePage

        public static SteamApp ParsePage(int appId, string html)
        {
            if (string.IsNullOrWhiteSpace(html)) throw new ArgumentNullException(nameof(html));

            try
            {
                var app = SteamApp.NewSteamApp(appId, html);

                var htmlDocument = new HtmlDocument();

                var htmlCleaned = html.Replace("\"", "'");

                htmlDocument.LoadHtml(htmlCleaned);

                var documentNode = htmlDocument.DocumentNode;

                var titleNode = documentNode.SelectSingleNode($"//div[@class='{AppTitleClass}']");

                app.Title = titleNode.InnerHtml.Trim();

                var packageNodes = documentNode.SelectNodes($"//div[@class='{PackageClass}']").ToArray();

                foreach (var packageNode in packageNodes)
                {
                    AddPackage(app, packageNode);
                }

                return app;
            }
            catch (Exception)
            {
                throw new InvalidAppException(appId);
            }
        }

開發者ID:tstepanski，項目名稱:SteamScraper，代碼行數:34，代碼來源:Parser.cs


示例6: ParseRecommends

 public static void ParseRecommends(string html, Action<List<Recommend>> finished)
 {
     BackgroundWorker bw = new BackgroundWorker();
     bw.DoWork += new DoWorkEventHandler((sender, e) =>
     {
         List<Recommend> allRecommends = new List<Recommend>();
         HtmlDocument hDoc = new HtmlDocument();
         hDoc.LoadHtml(html);
         var tableRows = hDoc.DocumentNode.SelectNodes(Constants.Instance.XPATH_GAME_SHOW_RESULT);
         foreach (var node in tableRows)
         {
             var results = ChildElementsInTableRow(node);
             if (results.Count == Constants.Instance.COUNT_GAME_SHOW_RESULT_COLUMNS)
             {
                 var rec = RecommendFromStrings(results);
                 if (IsValidRecommend(rec))
                 {
                     allRecommends.Add(rec);
                 }
             }
         }
         finished(allRecommends);
     });
     bw.RunWorkerAsync();
 }

開發者ID:nkwsqyyzx，項目名稱:BetStrategy，代碼行數:25，代碼來源:HtmlParser.cs


示例7: ConvertHtml

        private void ConvertHtml(ExCSS.Stylesheet sheet, string html, Section section)
        {
            _sheet = sheet;
            if (string.IsNullOrEmpty(html))
            {
                throw new ArgumentNullException("html");
            }

            if (section == null)
            {
                throw new ArgumentNullException("section");
            }

            //section.PageSetup.HeaderDistance = "0.001cm";
            section.PageSetup.FooterDistance = Unit.FromCentimeter(0.01);

 // Create a paragraph with centered page number. See definition of style "Footer".
            var footer = section.Footers.Primary.AddParagraph();
            //section.Footers.Primary.
            footer.Format.Alignment = ParagraphAlignment.Right;
            footer.AddPageField();
            footer.AddText(" of ");
            footer.AddNumPagesField();
            
            var doc = new HtmlDocument();
            doc.LoadHtml(html);
            ConvertHtmlNodes(doc.DocumentNode.ChildNodes, sheet, section);
        }

開發者ID:jgshumate1，項目名稱:MigraDoc.Extensions，代碼行數:28，代碼來源:HtmlConverter.cs


示例8: CreateRequest

        public static HtmlDocument CreateRequest(string url)
        {
            using (var client = new HttpClient())
            {
                try
                {
                    var response = client.GetAsync(url).Result;

                    if (response.StatusCode == HttpStatusCode.OK)
                    {
                        var responseContent = response.Content.ReadAsStringAsync().Result;

                        var doc = new HtmlDocument();
                        doc.LoadHtml(responseContent);
                        return doc;
                    }
                    else
                    {
                        throw new Exception(response.StatusCode.ToString());
                    }
                }
                catch (Exception e)
                {
                    throw new Exception("Error executing query " + url + ". " + e.Message + " " + e.InnerException);
                }
            }
        }

開發者ID:maxMakaronok，項目名稱:Assistent，代碼行數:27，代碼來源:CommonWebWorker.cs


示例9: Parse

        protected override void Parse(String page)
        {
            var doc = new HtmlDocument();
            doc.LoadHtml(page);

            var nodes = doc.DocumentNode.SelectNodes("//ul[@class='list']//li");
            if (nodes != null)
            {
                foreach (var node in nodes)
                {
                    var sale = false; //из списка нельзя получить инфу о скидке, поэтому всегда false

                    var title = node.SelectSingleNode(".//div[@class='title']").FirstChild.InnerText.Replace("\r\n", " ");
                    var searchString = DelBadChar(ref title);

                    var gameUrl = StoreUrl + node.SelectSingleNode(".//a").GetAttributeValue("href", String.Empty);
                    var cost = node.SelectSingleNode(".//div[@class='price']//span[@class='new']").InnerText;

                    _entries.Add(new GameEntry()
                    {
                        SearchString = searchString,
                        StoreUrl = StoreUrl,
                        Title = title,
                        GameUrl = gameUrl,
                        Cost = cost,
                        Sale = sale
                    });
                }
            }
        }

開發者ID:soramusoka，項目名稱:gbn-parser，代碼行數:30，代碼來源:Shop1cParser.cs


示例10: btnTestCode_Click

        private void btnTestCode_Click(object sender, RoutedEventArgs e)
        {
            var mainPage = GetHtml("http://htmlagilitypack.codeplex.com");
            var homepage = new HtmlDocument();
            homepage.LoadHtml(mainPage);

            var nodes =
                homepage.DocumentNode.Descendants("a").Where(x => x.Id.ToLower().Contains("releasestab")).FirstOrDefault
                    ();
            var link = nodes.Attributes["href"].Value;

            var dc = new HtmlDocument();
            try
            {
                Cursor = Cursors.Wait;
                var req = (HttpWebRequest) WebRequest.Create(link);
                using (var resp = req.GetResponse().GetResponseStream())
                using (var read = new StreamReader(resp))
                {
                    dc.LoadHtml(read.ReadToEnd());
                    var span =
                        dc.DocumentNode.Descendants("span").Where(
                            x => x.Id.ToLower().Contains("releasedownloadsliteral")).FirstOrDefault();
                    MessageBox.Show(
                        int.Parse(span.InnerHtml.ToLower().Replace("downloads", string.Empty).Trim()).ToString());
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error loading file: " + ex.Message, "Error", MessageBoxButton.OK, MessageBoxImage.Error,
                                MessageBoxResult.OK);
            }
        }

開發者ID:Clancey，項目名稱:HtmlAgilityPack，代碼行數:33，代碼來源:Window1.xaml.cs


示例11: GetForms

 public IEnumerable<HtmlForm> GetForms()
 {
     var doc = new HtmlDocument();
     doc.LoadHtml(Content);
     var forms = doc.DocumentNode.SelectNodes("//form");
     return forms.Select(HtmlForm.FromNode);
 }

開發者ID:Sjord，項目名稱:ScoutsOffline，代碼行數:7，代碼來源:Response.cs


示例12: GetFundamentals

        static IDictionary<string, string> GetFundamentals(Uri url)
        {
            string html;
            using (var webClient = new WebClient())
                html = webClient.DownloadString(url);

            var doc = new HtmlDocument
                          {
                              OptionFixNestedTags = true
                          };

            doc.LoadHtml(html);

            var fundamentals = new Dictionary<string, string>();
            var trs = doc.DocumentNode.SelectNodes("//div[@data-ajax-name='EquitySummaryTable']//table[contains(@class, 'horizontalTable')]//tr");

            if (trs == null)
                return fundamentals;

            foreach (var tr in trs)
            {
                var name = tr.Elements("th").Single().InnerText;
                var value = tr.Elements("td").Single().InnerText;

                if (value == "--")
                {
                    Log.DebugFormat("Missing: {0} = {1}", name, value);
                    continue;
                }

                Log.DebugFormat("Found: {0} = {1}", name, value);
                fundamentals.Add(name, value);
            }
            return fundamentals;
        }

開發者ID:rdingwall，項目名稱:fundamentals-aggregator，代碼行數:35，代碼來源:FtDotComSummary.cs


示例13: ReplaceTags

        private string ReplaceTags(string html)
        {
            var doc = new HtmlDocument();
            doc.LoadHtml(html);

            var divs = doc.DocumentNode.Descendants("div").Where(d =>
                d.Attributes.Contains("class")).ToList(); //&& d.Attributes["class"].Value.Contains("editable-wrapper"));


            var editableDivs = new List<HtmlNode>();

            foreach (var div in divs)
            {
                if(div.Attributes["class"].Value.Contains("editable-wrapper"))
                {
                    editableDivs.Add(div);
                }
            }


            foreach (var editableDiv in editableDivs)
            {
                editableDiv.AppendChild(GetEditButtonElement());
                editableDiv.AppendChild(GetSaveButtonElement());
            }

            return doc.DocumentNode.OuterHtml;
        }

開發者ID:Excepti0n，項目名稱:misechko.com.ua，代碼行數:28，代碼來源:ReplaceTagsFilter.cs


示例14: ItemCrawler

 public ItemCrawler(Uri url)
 {
     _htmlDocument = new HtmlDocument();
     var html = new WebClient().DownloadString(url.OriginalString);
     _htmlDocument.LoadHtml(html);
     _document = _htmlDocument.DocumentNode;
 }

開發者ID:stiano，項目名稱:ShopperDopper，代碼行數:7，代碼來源:ItemCrawler.cs


示例15: RefreshAsync

        /// <summary>
        /// 非同步刷新最新資訊
        /// </summary>
        /// <returns></returns>
        public async Task RefreshAsync() {
            HttpClient client = new HttpClient();
            HtmlDocument HTMLDoc = new HtmlDocument();
            HTMLDoc.LoadHtml(await client.GetStringAsync(DataSource));

            var script = HTMLDoc.DocumentNode.Descendants("script")
                .Where(x => x.InnerHtml?.Length > 0).Select(x => x.InnerHtml).ToArray();

            var tempAry = script.First()
                .Split(new char[] { ';' }, StringSplitOptions.RemoveEmptyEntries)
                .Select((x, i) => new { index = i, item = x })
                .GroupBy(x => Math.Floor(x.index / 4.0));

            this.LastPassed = null;
            this.Delay = new TimeSpan();

            foreach (var item in tempAry) {
                string[] temp = item.Select(x=>x.item).ToArray();
                if(temp[3] == "TRSearchResult.push('x')") {
                    this.LastPassed = await Station.GetStationByNameAsync(
                        innerString(temp[0],"'","'")
                        );
                }                
            }

            var time = new TimeSpan(0, int.Parse(innerString(script.Last(), "=", ";")),0);
            this.Delay= time;
        }

開發者ID:XuPeiYao，項目名稱:TwOpenData.Railways，代碼行數:32，代碼來源:RealTimeTrainInfo.cs


示例16: aSyncSearchForModel

        private static IEnumerator aSyncSearchForModel(string filename, string searchterm)
        {
            WebClient w = new WebClient();
            string htmlstring = w.DownloadString("http://sketchup.google.com/3dwarehouse/doadvsearch?title=" + searchterm.Replace(" ","+")
                                        + "&scoring=d&btnG=Search+3D+Warehouse&dscr=&tags=&styp=m&complexity=any_value&file="
                                        + "zip" + "&stars=any_value&nickname=&createtime=any_value&modtime=any_value&isgeo=any_value&addr=&clid=");
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.LoadHtml(htmlstring);

            //Grab a result from the search page
            HtmlAgilityPack.HtmlNodeCollection results = doc.DocumentNode.SelectNodes("//div[@class='searchresult']");
            string model_page_url = "http://sketchup.google.com" + results[0].SelectSingleNode(".//a").Attributes["href"].Value;
            htmlstring = w.DownloadString(model_page_url);
            doc.LoadHtml(htmlstring);

            //Find the downloadable zip file
            results = doc.DocumentNode.SelectNodes("//a[contains(@href,'rtyp=zip')]");
            foreach (HtmlNode r in results)
            {
                HtmlAttribute src = r.Attributes["href"];
                string url = "http://sketchup.google.com" + src.Value;
                url = url.Replace("&amp;", "&");
                string location = @"path to downloads folder" + filename + ".zip";
                System.Diagnostics.Debug.WriteLine(url+"\n"+location);
                w.DownloadFile(new Uri(url),location);
            }
            return null;
        }

開發者ID:jrafferty3，項目名稱:SketchupImporter，代碼行數:28，代碼來源:Program.cs


示例17: GetFilmsInfo

        public void GetFilmsInfo()
        {
            Console.WriteLine("Start getting info...\n");
            var filmList = new List<Film>();

            foreach (var filmName in filmNames)
            {
                var film = new Film() { Name = filmName };

                // Get html page from kinoppoisk.
                String searchString = String.Format(SearchLinkTemplate, filmName, FilmYear);
                var html = ExtendedHtmlHelpers.GetResponseHtml(searchString, Host);
                if (String.IsNullOrEmpty(html))
                {
                    Console.WriteLine("Can't find info for " + filmName);
                    continue;
                }

                // Get film URL.
                var htmlDocument = new HtmlDocument();
                htmlDocument.LoadHtml(html);
                var filmUrl = htmlDocument.DocumentNode
                                          .SelectNodes("//div[@class='info']/p[@class='name']/a[@href]")
                                          .First()
                                          .Attributes["href"].Value;

                // Get film ID.
                var result = Regex.Match(filmUrl, @"film\/(\d)+").Value.Substring(5);
                int id;
                Int32.TryParse(result, out id);
                film.Id = id;

                // Get film properties.
                html = ExtendedHtmlHelpers.GetResponseHtml(String.Format(FilmLinkTemplate, id), Host);
                htmlDocument.LoadHtml(html);

                try
                {
                    film.NameEng = HttpUtility.HtmlDecode(GetInnerText(htmlDocument, "//div[@id='headerFilm']/span[@itemprop='alternativeHeadline']"));
                    film.Year = HttpUtility.HtmlDecode(GetInnerText(htmlDocument, "//table[@class='info']//a[@title='']"));
                    film.DatePremierWorld = Convert.ToDateTime(
                        HttpUtility.HtmlDecode(
                            GetInnerText(htmlDocument, "//td[@id='div_world_prem_td2']//a[@href]")));
                    film.DateDVD = Convert.ToDateTime(
                        HttpUtility.HtmlDecode(
                            GetInnerText(htmlDocument, "//td[@class='calendar dvd']//a[@href]")));
                    Console.WriteLine(film.ToString());
                }
                catch (Exception)
                {
                    Console.WriteLine("\tDidn't get a full info for film " + filmName);
                }
                filmList.Add(film);
            }
            // Save result.
            var films = filmList.OrderBy(x => x.DatePremierWorld);
            ExtendedIOHelpers.SaveAsJsonToFile(OutputFileName, films);
            ExtendedIOHelpers.SaveToFile("films.csv", Encoding.Default, ToUsualView(films));
        }

開發者ID:KlimZavadski，項目名稱:FilmInfoFromKinopoisk，代碼行數:59，代碼來源:Program.cs


示例18: Extract

        private static void Extract(string home, string subSite)
        {
            HtmlDocument doc = new HtmlDocument();
            doc.LoadHtml(home);
            List<string> hrefTags = new List<string>();
            hrefTags = ExtractAllAHrefTags(doc);

            string lastItem = string.Empty;
            foreach (string item in hrefTags)
            {
                if (item != lastItem)
                {
                    lastItem = item;
                    try
                    {
                        if (item.Contains(subSite) && item.Length > 12)
                        {
                            Console.Write(".");
                            WebClient adClient = new WebClient();
                            string ad = string.Empty;
                            try
                            {
                                if (item.Contains("http://"))
                                {
                                    ad = adClient.DownloadString(item);
                                }
                                else
                                {
                                    ad = adClient.DownloadString(rootUrl + item);
                                }

                                HtmlDocument adDoc = new HtmlDocument();
                                doc.LoadHtml(ad);
                                string text = GetPostingBody(doc);
                                if (!string.IsNullOrEmpty(text))
                                {
                                    text = text.Replace("#", "sharp");
                                    text = text.Replace("++", "plusplus");

                                    FindPhrases(text);
                                    FindWords(text);
                                }
                            }
                            catch (Exception xx)
                            {
                                Console.WriteLine("adClient.DownloadString, rootUrl = " + rootUrl + ", item = " + item + " - " + xx.Message);
                                continue;
                            }
                        }
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Extract: " + ex.Message);
                        break;
                    }
                }
            }
        }

開發者ID:atoi2008，項目名稱:CraigslistStudy，代碼行數:58，代碼來源:Program.cs


示例19: HSD

        //HTMLSTEALDATA
        public string HSD(string link)
        {
            //variables and object
            WebClient wC = new WebClient();
            string data = "";
            string text = "You set bad link!!! => ";
            string newdata = "";
            var htmlDoc = new HtmlAgilityPack.HtmlDocument();

            //checking link started with http://
            if (link.StartsWith("http://"))
            {
                //try take data from code of website
                try
                {
                    data = wC.DownloadString(link);
                    htmlDoc.LoadHtml(data);

                    newdata += part1(htmlDoc, newdata);
                    newdata += part2(htmlDoc, newdata);
                    newdata += part3(htmlDoc, newdata);
                    newdata += part4(htmlDoc, newdata);
                }
                catch(WebException e)
                {
                    text += e.ToString();
                    MessageBox.Show(text, "Bad link!!!", MessageBoxButtons.OKCancel, MessageBoxIcon.Error);
                }
            }
            else
            {
                try
                {
                    data = wC.DownloadString(link.Insert(0, "http://"));
                    htmlDoc.LoadHtml(data);

                    newdata += part1(htmlDoc, newdata);
                    newdata += part2(htmlDoc, newdata);
                    newdata += part3(htmlDoc, newdata);
                    newdata += part4(htmlDoc, newdata);
                }
                catch(WebException e)
                {
                    text += e.ToString();
                    MessageBox.Show(text, "Bad link!!!", MessageBoxButtons.OKCancel, MessageBoxIcon.Error);
                }
            }

            return newdata;
        }

開發者ID:WolfMan12333，項目名稱:PM4P，代碼行數:51，代碼來源:DataFromWeb.cs


示例20: LoadBox

        private async void LoadBox ()
        {
            listBoxTopics.IsEnabled = false;
            ProgressIndicatorSwitch ( true );
            url = "";
            if ( currentPage == 1 )
                url = "https://vozforums.com/forumdisplay.php?f=" + boxId;
            else
                url = "https://vozforums.com/forumdisplay.php?f=" + boxId + "&order=desc&page=" + currentPage;
            client = new HttpClient ();
            doc = new HtmlDocument ();

            //neu chua dang nhap
            if ( Model.UserData.isLoggedIn == false )
            {
                try
                {
                    doc.LoadHtml ( await client.GetStringAsync ( url ) );
                }
                catch ( Exception ex )
                {
                    MessageBox.Show ( "Lỗi server Voz: " + ex.Message );
                    Application.Current.Terminate ();
                }
            }
            //neu da dang nhap
            else
            {
                string responseresult = await Model.Login.GetResponseURL ( url );
                if ( responseresult == "Error" )
                {
                    MessageBox.Show ( "Server Voz đang bị lỗi, thử lại sau" );
                }
                else
                {
                    doc.LoadHtml ( responseresult );
                }
            }
            
            Helper.HAP.RemoveComment ( doc );

            GetBoxTitle ();
            GetMaxPage ();
            GetListThreads ();

            listBoxTopics.ItemsSource = listThreads;
            listBoxTopics.IsEnabled = true;
            ProgressIndicatorSwitch ( false );
        }

開發者ID:tranchikhang，項目名稱:Voz，代碼行數:49，代碼來源:Box.xaml.cs



注：本文中的HtmlAgilityPack.HtmlDocument.LoadHtml方法示例整理自Github/MSDocs等源碼及文檔管理平台，相關代碼片段篩選自各路編程大神貢獻的開源項目，源碼版權歸原作者所有，傳播和使用請參考對應項目的License；未經允許，請勿轉載。
相關方法

    HtmlDocument.Load
    HtmlDocument.GetElementbyId
    HtmlDocument.CreateElement
    HtmlDocument.LoadHtml
    HtmlDocument.Save
    HtmlDocument.LoadHtml2
    HtmlDocument.CreateAttribute
    HtmlDocument.CreateNavigator
    HtmlDocument.AssertMatch
    HtmlDocument.TryMerge
    HtmlDocument.FirstOfDescendantsWithClass
    HtmlDocument.DetectEncodingAndLoad
    HtmlDocument.TabularData
    HtmlDocument.QuerySelector
    HtmlDocument.CreateTextNode
    HtmlDocument.GetNodes
    HtmlDocument.SelectNodes
    HtmlDocument.DetectEncoding
    HtmlDocument.CreateComment
    HtmlDocument.WhereOfDescendantsWithClass
    HtmlDocument.GetElementById
    HtmlDocument.GetInnerText
    HtmlDocument.LoadUri
    HtmlDocument.GetAttribute
    HtmlDocument.DetectEncodingHtml
    HtmlDocument.GetText
    HtmlDocument.get_DocumentNode
    HtmlDocument.QuerySelectorAll
    HtmlDocument.GetLinks
    HtmlDocument.GetElementsByTagName
    HtmlDocument.Load2
    HtmlDocument.LoadUrl
    HtmlDocument.GetNode
    HtmlDocument.GetInlineStyles
    HtmlDocument.GetResourcesUrls
    HtmlDocument.GetType
    HtmlDocument.IsAttribute
    HtmlDocument.SelectSingleNode
    HtmlDocument.ExtractText
    HtmlDocument.GetInternalLinks
    HtmlDocument.ExtractLastArticleId
    HtmlDocument.ExtractContent
    HtmlDocument.ToString
    HtmlDocument.ToLinkInfos
    HtmlDocument.ToPlainText
    HtmlDocument.ExtractAutor
    HtmlDocument.WalkTemplate
    HtmlDocument.Body
    HtmlDocument.SearchPropertiesSmart
    HtmlDocument.FirstOfDescendantsWithId
    HtmlDocument.ExtractTitle
    HtmlDocument.ExtractWrittenTime
    HtmlDocument.NotNull
    HtmlDocument.GetLanguageTables
    HtmlDocument.LoadRaw
    HtmlDocument.GetDataFromHtml
    HtmlDocument.GetDataFromXPath
    HtmlDocument.Links
    HtmlDocument.IsSelectorInUse
    HtmlDocument.IsDeletedArticle
    HtmlDocument.GetExternalCssUrls
    HtmlDocument.AsDocument
    HtmlDocument.Anchors

©2008-2022 | 純淨天空  |  簡體  |  繁體  |  聯係我們  |  京ICP備15018527號-1  |  讚助商  | 
