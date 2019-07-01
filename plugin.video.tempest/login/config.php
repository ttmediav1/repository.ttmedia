<?php
/* Database credentials. Assuming you are running MySQL
server with default setting (user 'root' with no password) */
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'ttmedial_eng64tw');
define('DB_PASSWORD', 'Tony1964');
define('DB_NAME', 'ttmedial_logintest');
 
/* Attempt to connect to MySQL database */
$link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
 
// Check connection
if($link === false){
    die("ERROR: Could not connect to database. " . mysqli_connect_error());
}
?>