<?php 


echo (getenv("MAPS_API"));

die;



$command = escapeshellcmd('/usr/custom/test.py');
$output = shell_exec($command);
echo $output;

?>