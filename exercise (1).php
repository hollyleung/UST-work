<!DOCTYPE html>

<html>
<body>

<!--This is the structure for the exercise-->
<!--please add necessary codes by yourself-->

You have entered the following projects: 



<form action="example1.php" method="POST" >
    <table border="1">

    <!--one line text input-->
    <tr>
        <td>
            Project Name: <input name=f_line type=text size=25>
        </td>
    </tr>

    <tr>
        <td>
            Project Number: <input name=f_line2 type=integer size=25>
        </td>
    </tr>

    <tr>
        <td>
        	<select name=f_select>
	          <?php
			      $link= fopen("project_locations.txt", "r");
			      while (!feof($link)) {
				      $location = fgets($link);
				      echo "<option value = $location> $location";
				  }      
			      fclose($link);
	   	 	  ?>
	   	 	  </select>
        </td>
    </tr>
	<tr>
        <td>
		    <?php
		        $link2= fopen("dept_info.txt", "r");
		        while (!feof($link2)) {
		            $dep = fgets($link2);
		            $dept_info = split(" ", $dep);
		            echo "<input type = radio name= f_radio value= $dept_info[0]> $dept_info[1]";
		        } 
		        fclose($link2);     
		    ?>
    	</td>
    </tr>
    <tr>
        <td>
            <input type=submit value="Click Here to submit">
        </td>
    </tr>

    <tr>
        <td>
            <input type=reset value="Reset All Choices">
        </td>
    </tr>

</body>
</html>
