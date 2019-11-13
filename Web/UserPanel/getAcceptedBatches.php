<?php
	if (isset($_GET['phone'])) {
	    $phone = $_GET['phone'];
	} else {
	    return;
	}
	
	//$txtUrl = "http://localhost/+1".$phone."/batches_accepted.txt";
	$txtPath = "+1".$phone."/batches_accepted.txt";
	if(file_exists($txtPath)){
      $content = file_get_contents($txtPath);
      $arr = explode("\n", $content);           
      $cnt = count($arr);
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