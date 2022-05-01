<?php
// Бросаем кодировку utf-8
header('Content-type: text/html; charset=utf-8');

function post_content ($url,$postdata) {
	$uagent = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)";

	$ch = curl_init( $url );
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_HEADER, 0);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt($ch, CURLOPT_ENCODING, "");
	curl_setopt($ch, CURLOPT_USERAGENT, $uagent);  // useragent
	curl_setopt($ch, CURLOPT_TIMEOUT, 120);
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $postdata);
	curl_setopt($ch, CURLOPT_COOKIEJAR, "c://coo.txt");
	curl_setopt($ch, CURLOPT_COOKIEFILE,"c://coo.txt");

	$content = curl_exec( $ch );
	$err     = curl_errno( $ch );
	$errmsg  = curl_error( $ch );
	$header  = curl_getinfo( $ch );
	curl_close( $ch );

	$header['errno']   = $err;
	$header['errmsg']  = $errmsg;
	$header['content'] = $content;
	return $header;
}
$ch = curl_init();
$url = "http://127.0.0.1:8000/sendsms/info/?format=json";

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$resp = curl_exec($ch);

$info = json_decode($resp);

curl_close($ch);

// Логин для доступа к платформе smspro.nikita.kg
$login = "login";

// Пароль для доступа к платформе smspro.nikita.kg
$password = "passwd";

// Текст СМС-сообщения - текст на русском или латинице любой длины (до 800 знаков). В случае необходимости платформа smspro.nikita.kg автоматически порубит текст на несколько сообщений.
$sms_text = "Содержимое SMS-сообщения! Код: "+ (echo $info->smscode);

// Уникальный идентификатор транзакции. Для каждой новой отправки он должен быть новым! 
// В данном примере он прошит жестко. Используя этот ID можно получить отчет о доставке сообщения.
$transactionId = echo $info->id;

// Имя отправителя.                 ДОЛЖНО БЫТЬ СОГЛАСОВАНО С Админом smspro.nikita.kg!
// может быть либо текстом на литинице либо цифрами или номером телефона (по согласованию с smspro.nikita.kg)
$sender_id = "nikita.kg";

// номер телефона получателя СМС в формате 996ххххххххх.
// В одной транзакции отправки может быть указано и более 1го телефона.
$phone = echo $info->number;

// Сама строка - XML-запрос к плафторме smspro.nikita.kg
$xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>".
	"<message>".
		"<login>" . $login . "</login>".
		"<pwd>" . $password . "</pwd>".
		"<id>" . $transactionId . "</id>".
		"<sender>" . $sender_id . "</sender>".
		"<text>" . $sms_text . "</text>".
		// "<time>20101118214600</time>".		// Можно указать время отправки этого сообщения
		"<phones>".
		"<phone>" . $phone . "</phone>".
		// "<phone>996772947637</phone>".		// Можно указать дополнительные номера телефонов
		"</phones>".
		//"<test>1</test>".					// Если раскомментировать эту строку, то СМС не будет отправлено фактически и не будет протарифицированно 
	"</message>";	
	
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Страничка отправки SMS используя шлюз smspro.nikita.kg</title>
</head>
<body>
<h1>Страничка отправки SMS используя шлюз smspro.nikita.kg</h1>
<hr>
<h4>Отправляемый XML-запрос:</h4>
<code>
	<?=htmlspecialchars($xml) ?>
</code>

<h4>Результат:</h4>
<?
// Процесс отправки СМС

try {
	$url = "http://smspro.nikita.kg/api/message";

	$result = post_content( $url, $xml );
	$html = $result['content'];

	// Ответ сервера smspro.nikita.kg
	$responceXML = htmlspecialchars($html);
	?>
	
	HTTP-соединение с сервером smspro.nikita.kg состоялось.<br>
	Ответ сервера:<br>
	<code><?=$responceXML ?></code>
	
	<?    	
} catch(Exception $e) {
	echo 'Caught exception: ',  $e->getMessage(), "\n";
	var_dump($e->getTrace());
}
?>

</body>
</html>