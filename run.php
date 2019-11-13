<?php
	if (isset($_GET['phonenumber'])) {
	    $phonenumber = $_GET['phonenumber'];
	    echo 'success';
	    exec("START  ".$phonenumber.".exe");	    
	} else {
		echo 'failed';
	}	
?>