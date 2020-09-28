<?php
ini_set('max_execution_time', 900);
require_once 'phpQuery/phpQuery/phpQuery.php';
$linkDB = mysqli_connect('localhost','root' , '','reviews');
$html=file_get_contents("https://www.e-katalog.ru");
$document=phpQuery::newDocument($html);
foreach($document->find(".touchcarousel-item") as $key => $value){
    $pq = pq($value);
    $link=$pq->attr("href");
    $link="https://www.e-katalog.ru"."$link";
    $htmlCurrProducts = file_get_contents($link);
    $documentCurrProducts = phpQuery::newDocument($htmlCurrProducts);
    $name = $documentCurrProducts->find(".t2")->text();
    $category = $documentCurrProducts->find(".path_lnk")->text();
    $desc = $documentCurrProducts->find(".desc-ai-title")->text();
    $query ="INSERT INTO `reviews` (`id`, `adres_r`, `category_r`, `name_r`, `descrip_r`) 
                VALUES (NULL, '$link', '$category', '$name', '$desc');";
    $result=  mysqli_query($linkDB, $query) or die("Ошибка " . mysqli_error($linkDB));
}
echo "Готово!";
phpQuery::unloadDocuments();
?>
