from django.template import Context, Template
raw_template = """{% extends "base.html" %}


<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"> </script>
	<script>
		function setupPage()
		{
			$.get("/events/homepage_events/", function (data,status) {
				setupTable(data);
			});
			//$.get("/companies/donations/all/", function (data,status) {
			//	var tit = 0;
			//	for(cat in data){
			//		tit = tit + parseInt(data[cat].company_donations);
			//	}
			//	tit = addCommas(tit);
			//	document.getElementById("cashRaised").innerHTML = "$" + tit + " Raised";
			//});
		}
		function setupTable(data)
		{
			var sponsor_title = '#sponsor_title';
			var sponsor_paragraph = '#sponsor_paragraph';
			var sponsor_image = '#sponsor_image';
			var sponsor_candles = '#sponsor_candles';
			var sponsor_date = '#sponsor_date';

			var sponsor_number = 1;
			for(item in data)
			{
				var current_title = sponsor_title + sponsor_number;
				var current_paragraph = sponsor_paragraph + sponsor_number;
				var current_image = sponsor_image + sponsor_number;
				var current_candles = sponsor_candles + sponsor_number;
				var date = sponsor_date + sponsor_number;
				sponsor_number = sponsor_number+1;
				record = data[item];
				$(current_title).append(record.fields.name);
				$(current_paragraph).append(record.fields.description);
				$(current_image).attr("src", record.fields.image);
				$(current_candles).append(record.fields.candles_rewarded+' candles');

				//var d1=new Date(record.fields.date);
				//d1.toString('dddd, MMMM ,yyyy')  //returns "Monday, June 29,2009"

				//$(date).append(d1);



				var m_names = new Array("January", "February", "March",
"April", "May", "June", "July", "August", "September",
"October", "November", "December");

var d = new Date(record.fields.date);
var curr_date = d.getDate();
curr_date++;
var sup = "";
if (curr_date == 1 || curr_date == 21 || curr_date ==31)
   {
   sup = "st";
   }
else if (curr_date == 2 || curr_date == 22)
   {
   sup = "nd";
   }
else if (curr_date == 3 || curr_date == 23)
   {
   sup = "rd";
   }
else
   {
   sup = "th";
   }

var curr_month = d.getMonth();
var curr_year = d.getFullYear();

$(date).append(m_names[curr_month] + " " + curr_date + "<SUP>" + sup + "</SUP>");
			}
		}
</script>
        {% block content %}
        	<div class="textRaised">
				<div style="float:left;">
					 <!--<h1 id="cashRaised" class="textRaised">$$$$$$ Raised</h1>
					<img src="img/underline.png"  class="textRaised"></img>-->
				</div>
				<div style="float:right;">
					<!--<h1 class="textRaised" >521 Candles</h1>
					<img src="img/underline.png" id="candles" class="textRaised"></img>-->
				</div>
			</div><!-- end textRaised -->
			<div id="teamBoxes">
				<div class="teamBox">
					<a href="corpsList.html" id="cadets">Cadets For Cure</a>
				</div>
				<div class="teamBox">
					<a href="greekList.html" id="greeks">Greeks For Life</a>
				</div>
				<div class="teamBox">
					<a href="teamList.html" id="general">General Teams</a>
				</div><!-- end teamBox -->
			</div><!-- end teamBoxes -->
            <div id="idk">
			<div class="sponsor" id="sponsor1">
				<div class="sponsorHeader">
                	<h3 id="sponsor_title1" class="sponsor_title"></h3>
                </div>
                <img src="" id="sponsor_image1" class="sponsor_image"></img>
                <div id="sponsor_candles1" class="sponsor_candles"></div>
				<div id="sponsor_date1" class="sponsor_candles"></div>
				<p></p>
                <div class="forScroll">
                	<p id="sponsor_paragraph1" class="sponsor_paragraph"></p>
                </div>
			</div>
			<div class="sponsor" id="sponsor2">
				<div class="sponsorHeader">
                	<h3 id="sponsor_title2" class="sponsor_title"></h3>
                </div>
                <img src="" id="sponsor_image2" class="sponsor_image"></img>
                <div id="sponsor_candles2" class="sponsor_candles"></div>
				<div id="sponsor_date2" class="sponsor_candles"></div>
				<p></p>
                <div class="forScroll">
                	<p id="sponsor_paragraph2" class="sponsor_paragraph"></p>
                </div>
			</div>
			<div class="sponsor" id="sponsor3">
				<div class="sponsorHeader">
                	<h3 id="sponsor_title3" class="sponsor_title"></h3>
                </div>
                <img src="" id="sponsor_image3" class="sponsor_image"></img>
                <div id="sponsor_candles3" class="sponsor_candles"></div>
				<div id="sponsor_date3" class="sponsor_candles"></div>
				<p></p>
                <div class="forScroll">
                	<p id="sponsor_paragraph3" class="sponsor_paragraph"></p>
                </div>
			</div>
			<div class="sponsor" id="sponsor4">
				<div class="sponsorHeader">
                	<h3 id="sponsor_title4" class="sponsor_title"></h3>
                </div>
                <img src="" id="sponsor_image4" class="sponsor_image"></img>
                <div id="sponsor_candles4" class="sponsor_candles"></div>
				<div id="sponsor_date4" class="sponsor_candles"></div>
				<p></p>
                <div class="forScroll" >
                	<p id="sponsor_paragraph4" class="sponsor_paragraph"></p>
                </div>
			</div><!-- end sponsor -->
            <div id="actualSponsors">
        	<ul>
            	<li>
                    <a href="http://www.campuscookie.com/"><img id="campusCookies" src="../img/77765836.jpg"></img></a>
                    <a href="http://www.sageenvironmental.com/"><img id="sageEnvironmentalConsulting" src="../img/Sage.jpg"></img></a>
                    <!--<a id="" href=""><img src=""></img></a>-->
                    <a href="http://www.dominos.com/"><img id="dominosPizza" src="../img/Dominos_pizza_logo.png"></img></a>
                    <a href="http://www.blockandbridle.org.vt.edu/"><img id="blockAndBridle" src="../img/B and B.gif"></img></a>
                    <a href="http://www.redbullusa.com/cs/Satellite/en_US/Red-Bull-Home/001242746208542"><img id="redBull" src="../img/Red-Bull-3.jpg"></img></a>
                </li>
				<li>
                    <a href="http://www.prism.org.vt.edu/"><img id="PRISM" src="../img/prism logo.png"></img></a>
                    <a href="http://www.moes.com/"><img id="moes" src="../img/MoesSouthwestGrill.jpg"></img></a>
                    <a href="http://www.rhf.vt.edu/"><img id="rhf" src="../img/RHF.jpg"></img></a>
                    <a href="http://www.sga.vt.edu/"><img id="sga" src="../img/sgalogo.jpg"></img></a>
                    <a href="http://www.bookstore.vt.edu/"><img id="universityBookstore" src="../img/TechServicesInc.jpg"></img></a>
                    <a href=""><img id="aJMiniStorage" src="../img/Route114 Black.jpg"></img></a>
                </li>
            </ul>
        </div>
		</div><!-- end idk -->
        {% endblock content %}"""


t = Template(raw_template)

c = Context({"my_name": "Adrian"})
t.render(c)
#"My name is Adrian."

c = Context({"my_name": "Dolores"})
t.render(c)
#"My name is Dolores."