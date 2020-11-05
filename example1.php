<!DOCTYPE html>

<html>
<body>

<?php
// get the input variables and their values
$cgi_line = $_POST['f_line'];
$cgi_line2 = $_POST['f_line2'];
$cgi_select = $_POST['f_select'];
$cgi_radio = $_POST['f_radio'];

echo "You have entered the following projects: <br>";
echo "Project Name:".$cgi_line. " <br>";
echo "Project Number: ".$cgi_line2. " <br>";
echo "Project Location: ".$cgi_select. " <br>";
echo "Controlling Dept: ".$cgi_radio. " <br>";
echo "<br>";

?>

</body>
</html>
