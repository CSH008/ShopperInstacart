<?php
	header('Access-Control-Allow-Origin: *');
	if (isset($_GET['phonenumber'])) {
	    $phonenumber = $_GET['phonenumber'];
	    if(isset($_GET['extension']))
	    {
	    	$ext = $_GET['extension'];
	    	exec("START  ".$phonenumber.".".$ext);
	    } else
	    	exec("START  ".$phonenumber);
	    echo 'success';
	} else {
		echo 'failed';
	}	
?>