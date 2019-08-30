<?php
$current="";
$answer="";
if(! empty($_POST)){
    $current= $_POST['code'];
    $file="yogi.cpp";
    file_put_contents($file,$current);
    putenv("PATH=C:\Program Files (x86)\Dev-Cpp\MinGW64\bin");
    shell_exec("g++ yogi.cpp -o yogi.exe");//compile
    $answer=shell_exec("yogi.exe");//run

}

?>

<form method="POST">
        <textarea name="code" style="width: 500px;height:500px" placeholder="Write your code here"><?php echo $current ;?></textarea>
        <input type="submit" value="Run">
        <textarea name="output" style="width: 500px;height:500px" placeholder="Output" disabled ><?php echo $answer ;?></textarea>
</form>