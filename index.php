<?php
$a = $_GET['a'];
$b = $_GET['b'];
$c = $_GET['c'];

$output = shell_exec("python3 /var/www/html/calculate.py a=$a b=$b c=$c");
echo $output;
?>