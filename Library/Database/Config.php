<?php


class Config
{
    public $host;
    public $user;
    public $pass;
    public $dbname;

    /**
     * Config constructor.
     */
    public function __construct()
    {
        $this->host = $_ENV['DB_HOST'];
        $this->user = $_ENV['DB_USERNAME'];
        $this->pass = $_ENV['DB_PASSWORD'];
        $this->dbname = $_ENV['DB_DATABASE'];
    }

    /**
     * @param $host
     * @param $user
     * @param $pass
     * @param $dbname
     */
    public function setConfig($host, $user, $pass, $dbname)
    {
        $this->host = $host;
        $this->user = $user;
        $this->pass = $pass;
        $this->dbname = $dbname;
    }
}