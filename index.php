<?php
// Minimal PHP → CGI Python (same-page)
$py     = '/usr/bin/python3';            // run: which python3
$script = '/var/www/html/calculate.py';

$qs = $_SERVER['QUERY_STRING'] ?? '';
if ($qs !== '') {
  $cmd = 'REQUEST_METHOD=GET QUERY_STRING=' . escapeshellarg($qs) . ' '
       . escapeshellcmd($py) . ' ' . escapeshellarg($script) . ' 2>&1';
  $out = shell_exec($cmd);
  echo preg_replace('/^Content-type:.*\R+/i', '', (string)$out);
  exit;
}
?>
<!doctype html><meta charset="utf-8"><title>Assignment #2</title>
<form method="get" action="" style="font-family:system-ui;margin:2rem;max-width:800px">
  <label>A <input type="number" step="any" name="a" required></label>
  <label>B <input type="number" step="any" name="b" required></label>
  <label>C <input type="number" step="any" name="c" required></label>
  <button type="submit">Calculate</button>
</form>
<p style="font-family:system-ui;margin:0 2rem">Example: <code>?a=2&b=3&c=4</code></p>
