<?php
	header('Access-Control-Allow-Origin: *');

	if (isset($_GET['phone'])) {
	    $phone = $_GET['phone'];
	} else {
	    return;
	}
	
	$type = 'content';
	if (isset($_GET['type'])) {
	    $type = 'count';
	} 
	
	//$txtUrl = "http://localhost/+1".$phone."/batches_accepted.txt";
	$txtPath = "+1".$phone."/batches_accepted.txt";
	if(file_exists($txtPath)){
      $content = file_get_contents($txtPath);
      $arr = explode("\n", $content);           
      $cnt = count($arr);
      if($type == 'count')
      {
      	  //%d/%m/%y
      	$rcnt = 0;
      	for($i=0;$i<$cnt;$i++) {
      	   $curdate = date('Y-m-d');
           $datetime1 = new DateTime($curdate);            
           $a = explode(" ", $arr[$i]);
           $aa = explode("/", $a[0]);
           $started_date = date($aa[2].'-'.$aa[1].'-'.$aa[0]);
           $datetime2 = new DateTime($started_date);
           $interval = $datetime1->diff($datetime2);
           $days = $interval->format('%a');
           if($days==0) $rcnt++;
        }
      	echo $rcnt;
      	return;
      }
      if($cnt>4) {
      	  $start = $cnt-4;
      } else {
      	  $start = 0;
      }
      
      for ($i = $start; $i < $cnt; $i++) {     	  
    	echo $arr[$i]."<br/>";
	  }
    }
	
?>