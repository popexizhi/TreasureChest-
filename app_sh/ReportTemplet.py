# -*- coding:utf8
html_str = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>

	<head>
		<meta http-equiv="content-type" content="text/html;charset=UTF-8">
		<title></title>
		<link href="css_js/Properties.css" rel="stylesheet" media="screen">
        <script type="text/javascript" src="css_js/dygraph-combined-dev.js"></script>
			<script type="text/javascript"><!--
function CSClickReturn () {
	var bAgent = window.navigator.userAgent;
	var bAppName = window.navigator.appName;
	if ((bAppName.indexOf("Explorer") >= 0) && (bAgent.indexOf("Mozilla/3") >= 0) && (bAgent.indexOf("Mac") >= 0))
		return true; // dont follow link
	else return false; // dont follow link
}
CSStopExecution=false;
function CSAction(array) {return CSAction2(CSAct, array);}
function CSAction2(fct, array) {
	var result;
	for (var i=0;i<array.length;i++) {
		if(CSStopExecution) return false;
		var aa = fct[array[i]];
		if (aa == null) return false;
		var ta = new Array;
		for(var j=1;j<aa.length;j++) {
			if((aa[j]!=null)&&(typeof(aa[j])=="object")&&(aa[j].length==2)){
				if(aa[j][0]=="VAR"){ta[j]=CSStateArray[aa[j][1]];}
				else{if(aa[j][0]=="ACT"){ta[j]=CSAction(new Array(new String(aa[j][1])));}
				else ta[j]=aa[j];}
			} else ta[j]=aa[j];
		}
		result=aa[0](ta);
	}
	return result;
}
CSAct = new Object;
function CSGotoLink(action) {
	if (action[2].length) {
		var hasFrame=false;
		for(i=0;i<parent.frames.length;i++) { if (parent.frames[i].name==action[2]) { hasFrame=true; break;}}
		if (hasFrame==true)
			parent.frames[action[2]].location = action[1];
		else
			window.open (action[1],action[2],"");
	}
	else location = action[1];
}

// --></script>
		</csscriptdict>
		<csactiondict>
			<script type="text/javascript"><!--
CSAct[/*CMP*/ 'BC43C8C88'] = new Array(CSGotoLink,/*URL*/ 'Report0.xls','');

// --></script>
		</csactiondict>
	</head> 
	<body class="main">
		<table width="100%%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td class="sp_10px_row"></td>
			</tr>
			<tr>
				<td>
					<table cols="2" width="100%%" height="20" border="0" cellpadding="0" cellspacing="0">
						<tr>
<td class="header_page">%s</td>
						</tr>
					</table>
				</td>
			</tr>
			<tr>
				<td class="sp_10px_row"></td>
			</tr>
			<tr>
				<td>
					<table width="100%%" border="0" cellspacing="0" cellpadding="0">
						<tr>
							<td>
								<table class="TableSummary" summary="Graph Summary Table">
									<tr>
									<td class="text_em" id="LraTitle" width="120"><font class="SummaryHeader">Title:</font></td>
									<td headers="LraTitle"><font class="Verbl8">%s</font></td>
									</tr>
		<tr>
									<tr>
									<td class="text_em" id="LraCurrent Results" width="120"><font class="SummaryHeader">Current Results:</font></td>
									<td headers="LraCurrent Results"><font class="Verbl8">%s</font></td>
									</tr>
		<tr>
									<tr>
									<td class="text_em" id="LraGranularity" width="120"><font class="SummaryHeader">Duration:</font></td>
									<td headers="LraGranularity"><font class="Verbl8">%s</font></td>
									</tr>
								</table>
							</td>
							<td align="right" valign="top" width="180">
								<table border="0" cellspacing="0" cellpadding="0">
									<tr>
										<td>Graph data in Excel format</td>
										<td>&nbsp;&nbsp;</td>
										<td><button class="bu_toexcel" onclick="CSAction(new Array(/*CMP*/'BC43C8C88'));" name="buttonName" type="button" csclick="BC43C8C88">&nbsp;</button></td>
									</tr>
								</table>
							</td>
						</tr>
					</table>
				</td>
			</tr>
			<tr>
				<td class="sp_10px_row"></td>
			</tr>
			<tr>
				<td>
					<div class="pane_full">
<div id="graphdiv2"
  style="width:1500px; height:500px;"></div>
<script type="text/javascript">
  g2 = new Dygraph(
    document.getElementById("graphdiv2"),
    "%s", // path to CSV file
    {
      rollPeriod: 1,
      avoidMinZero: true,//y轴的最小值不为0，相当于y=0那条线上升了
      axisLabelWidth:100,//X Y轴的标题的宽度
    }          // options
  );
</script>
                                    </div>
				</td>
			</tr>
			<tr>
				<td class="sp_10px_row"></td>
			</tr>
			<tr>
				<td>
					<div class="pane_full">
<table width="100%%" border="1" frame="box" rules="all" cellpadding="1" cellspacing="0" class="legendTable">
<tr class="legendHeader">
<td>
Scale
</td>
<td>
Measurement
</td>
<td>
Graph Minimum
</td>
<td>
Graph Average
</td>
<td>
Graph Maximum
</td>
<td>
Graph Median
</td>
<td>
Graph Std. Deviation
</td>
</tr>
<tr class="legendRow">
<td>
1
</td>
<td>
%s
</td>
<td>
%s
</td>
<td>
%s
</td>
<td>
%s
</td>
<td>
%s
</td>
<td>
%s
</td>
</tr>
</table>

					</div>
				</td>
			</tr>
			<tr>
				<td class="sp_10px_row"></td>
			</tr>
			<tr>
				<td class="sp_5px_row"></td>
			</tr>
			<tr>
				<td class="sp_h_line"><img src="dot_trans.gif" alt="" height="1" width="1" border="0"></td>
			</tr>
			<tr>
				<td class="sp_5px_row"></td>
			</tr>
			<tr>
				<td>
					<div class="pane_full">
						<table width="100%%" border="0" cellspacing="0" cellpadding="0">
							<tr>
								<td valign="top"><font class="VerBl8"><b>Description: </b></font><font class="VerBl8">
                                %s
                                <br>
									</font></td>
							</tr>
			<tr>
				<td class="sp_5px_row"></td>
			</tr>
						</table>
					</div>
				</td>
			</tr>
			<tr>
				<td></td>
			</tr>
			<tr>
				<td></td>
			</tr>
		</table>
	</body>
</html>
"""

def templet_data( title, csvfp, testtime_str, da_min, da_avg, da_max, da_med, da_std, des, fp="x.html"):
    res = html_str % ( title, title, csvfp, testtime_str, csvfp, title, da_min, da_avg, da_max, da_med, da_std, des)
    f = open(fp,"w")
    f.write(res)
    f.close()
    return fp

if __name__=="__main__":
   print templet_data(title="Test Gw Count", csvfp="jenkins_fgw_online.csv" , testtime_str="2016-11-29 10:20 ~ 2016-11-29 13:00", \
   da_min="6.0", da_avg="5253.87573447887", da_max="124503.0", da_med="1245", da_std="13466.531697681452", des="最大 L2 数据收发速率") 
