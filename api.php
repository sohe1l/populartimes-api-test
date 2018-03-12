<?php 

define("API_KEY", "AIzaSyCTmst6SvsOAQanZKNt-2pt6nuLoFf2kSA");

$type = "bar";

// $x1 = "48.132986";
// $y1 = "11.566126";

// $x2 = "48.142199";
// $y2 = "11.580047";



$x1 = "37.79076156430289";
$y1 = "-122.40101544189451";

$x2 = "37.76594178232798";
$y2 = "-122.43363745117188";




$command = escapeshellcmd('python3 /home/forge/default/public/populartimes-api-test/test.py ' . API_KEY . " $type $x1 $y1 $x2 $y2");

echo($command);

$output = shell_exec($command);

echo $output;

/*
AIzaSyCTmst6SvsOAQanZKNt-2pt6nuLoFf2kSA", ["bar"],(48.132986, 11.566126), (48.142199, 11.580047
*/
?>