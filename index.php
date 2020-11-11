<?php
require __DIR__ . '/vendor/autoload.php';
//require_once 'Library/Database/Config.php';

use Dotenv\Dotenv;

$dotEnv = Dotenv::createImmutable(__DIR__);
$dotEnv->load();

echo 'testing database connection class...';

$config = new Config();
try {
    $db = new Connection($config);
} catch (ConnectionException $e) {
}

echo "Prob success...";