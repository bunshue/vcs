default_status=""
	num_drops=9
	first_drop_offset_from_centre=371 //gives reference point for resizing
	agt=navigator.userAgent.toLowerCase();

	ie=(document.all) ? 1:0
	if(ie){
		ie4=(agt.indexOf('msie 4.01')!=-1) ? 1:0
		ie5=(agt.indexOf('msie 5.01')!=-1) ? 1:0
		}
	else { ie4=0;ie5=0 }

	ns=(document.layers) ? 1:0
	ns6=(document.getElementByID) ? 1:0

	win=( (agt.indexOf("win")!=-1) || (agt.indexOf("16bit")!=-1) )
	mac=(agt.indexOf("mac")!=-1);

	imgs=(document.images) ? 1:0

//quickfinder dropdown
	offset=first_drop_offset_from_centre
	dropsloaded=0
	timerID=null

	function showdrop(num,theimg,newsrc){
		if(dropsloaded){
			clearTimeout(timerID)
			hideall()
			if(ie) { theblah="drop"+num+".style.visibility='visible'" }
			if(ns) { theblah="document.drop"+num+".visibility='show'" }
			eval(theblah); swpimg(theimg,newsrc)
			}
		}

	function akshowdrop(theimg,newsrc){
		if(dropsloaded){
			clearTimeout(timerID)
			hideall()
			eval(theblah); swpimg(theimg,newsrc)
			}
		}

	function hidedrop(){
		if(dropsloaded){
			timerID=window.setTimeout('hideall()',300); return
			}
		}

	function hideall(){
		if(dropsloaded){
			swpback()
			for(i=1;i<=num_drops;i++){
				if(ie) { theblah="drop"+i+".style.visibility='hidden'" }
				if(ns) { theblah="document.drop"+i+".visibility='hide'" }
				eval(theblah)
				}
			}
		}

	function keepdrop(){
		if(dropsloaded){
			clearTimeout(timerID)
			}
		}

	layerpos=new Array()
	function registerlayer(num){
		if(ie) { layerpos[num]=eval("drop"+num+".style.pixelLeft") }
		if(ns) { layerpos[num]=eval("document.drop"+num+".left") }
		}

	function reposition(num){
		if(ie) { thewindowwidth=document.body.clientWidth }
		if(ns) { thewindowwidth=window.innerWidth-14 }  //ns weirdness
		layeroffset=layerpos[num]
		temp_newpos=(thewindowwidth/2)-offset
		if(temp_newpos<0) { temp_newpos=0 }
		newpos=temp_newpos+layeroffset //this for irregularly spaced drops
		if(num==num_drops && thewindowwidth<(offset*2)+25){ newpos=newpos-10 } //kinda fixes if the last drop if off the edge of the page
		//		newpos=newposA+((num-1)*drop_width) //if they're spaced evenly
		if(ie) { theblah="drop"+num+".style.left=newpos" }
		if(ns) { theblah="document.drop"+num+".left=newpos" }
		eval(theblah);
		if(ie4) { eval("drop"+num+".style.width=160") } //fix silly width bug in IE4
		if(ie && mac) { eval("drop"+num+".style.width=160") }
		}

		clickedimg=""; overimg=""; downimg=""

	function swpimg(theimg,newsrc){
		if(imgs){
			oldsrc=document.images[theimg].src; overimg=theimg
			document.images[theimg].src=newsrc
			}
		}

	function swpback(){
		if(overimg!="" && overimg!=clickedimg &&overimg!=downimg){
			if(imgs){ document.images[overimg].src=oldsrc }
			}
		}

	function clickit(){
		if(clickedimg!=""){
			document.images['clickedimg'].src=clickedimgoldsrc
			}
		clickedimg=overimg; clickedgimgoldsrc=oldsrc
		}

	function set_down_img(){
		if(page_sect && page_sect!=""){
			downimg=page_sect
			if(document.images[page_sect]){
				document.images[page_sect].src="/_artwork/topnav/square_"+page_sect+".gif"
				}
			}
		else{ downimg=0 }
		}

	function MM_reloadPage(init) {  //reloads the window if Nav4 resized
		if (init==true) with (navigator) {if ((appName=="Netscape")&&(parseInt(appVersion)==4)) {
		    document.MM_pgW=innerWidth; document.MM_pgH=innerHeight; onresize=MM_reloadPage; }}
		else if (innerWidth!=document.MM_pgW || innerHeight!=document.MM_pgH) location.reload();
		}
	MM_reloadPage(true);

	if(ns || ns6){ offscreenBuffering=true }

	function ezine(){
		theform=document.forms['ezine']
		theurl=theform.action+"?"
		for(k=0;k<theform.length;k++){
			theurl=theurl+theform.elements[k].name+"="+theform.elements[k].value+"&"
			}
		top.location.href=theurl
		}


	function global_init(){
		window.status=default_status
		set_down_img()
		}

function MM_openBrWindow(theURL,winName,features) { //v2.0
  window.open(theURL,winName,features);
}