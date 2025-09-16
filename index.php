<?php
function h($s){ return htmlspecialchars($s ?? '', ENT_QUOTES, 'UTF-8'); }

$py     = '/usr/bin/python3';                 // adjust if: run `which python3`
$script = '/var/www/html/calculate.py';       // your Python script path

$a = $_GET['a'] ?? '';
$b = $_GET['b'] ?? '';
$c = $_GET['c'] ?? '';

$errors = [];
$result = null;

if ($a !== '' || $b !== '' || $c !== '') {
    // Basic validation
    if ($a === '' || $b === '' || $c === '') $errors[] = "Please provide a, b, and c.";
    if (!is_numeric($a) || !is_numeric($b) || !is_numeric($c)) $errors[] = "a, b, and c must be numbers.";
    if ((float)$a == 0.0) $errors[] = "a must not be 0 (division by zero).";

    if (!$errors) {
        // Build safe command: python3 /var/www/html/calculate.py a b c
        $cmd = escapeshellcmd($py) . ' ' .
               escapeshellarg($script) . ' ' .
               escapeshellarg($a) . ' ' .
               escapeshellarg($b) . ' ' .
               escapeshellarg($c) . ' 2>&1';

        $raw = shell_exec($cmd);

        if ($raw === null) {
            $errors[] = "No output from Python. Check /var/log/httpd/error_log";
        } else {
            // Your script prints a "Content-type:" line; remove it and trim
            $clean = preg_replace('/^Content-type:.*\R+/i', '', $raw);
            $result = trim($clean);
        }
    }
}
?>
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Assignment #2</title>
  <style>
    body{font-family:system-ui,Segoe UI,Arial;margin:2rem;max-width:720px}
    form{display:flex;gap:.75rem;flex-wrap:wrap;align-items:flex-end;margin:1rem 0 1.25rem}
    label{display:flex;flex-direction:column;font-weight:600}
    input{padding:.5rem;border:1px solid #ddd;border-radius:.5rem;min-width:8rem}
    button{padding:.55rem .9rem;border:0;border-radius:.5rem;cursor:pointer}
    .error{color:#b91c1c;margin:.25rem 0}
    .result{padding:.75rem 1rem;border:1px solid #e5e7eb;border-radius:.5rem;background:#fafafa}
  </style>
</head>
<body>
  <h1>Assignment #2</h1>

  <form method="get">
    <label>A <input type="number" step="any" name="a" value="<?=h($a)?>" required></label>
    <label>B <input type="number" step="any" name="b" value="<?=h($b)?>" required></label>
    <label>C <input type="number" step="any" name="c" value="<?=h($c)?>" required></label>
    <button type="submit">Calculate</button>
  </form>

  <?php foreach ($errors as $e): ?>
    <div class="error">⚠️ <?=h($e)?></div>
  <?php endforeach; ?>

  <?php if ($result !== null && !$errors): ?>
    <div class="result"><strong>Result:</strong> <?=h($result)?></div>
  <?php elseif (!$errors): ?>
    <p>Try: <code>?a=2&b=3&c=4</code></p>
  <?php endif; ?>
</body>
</html>
