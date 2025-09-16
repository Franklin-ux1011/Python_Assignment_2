#!/usr/bin/env python3
import cgi, math, datetime

form = cgi.FieldStorage()

def fail(msg):
    print("Content-type: text/html\n")
    print(f"<!doctype html><meta charset='utf-8'><p style='font-family:system-ui;color:#b91c1c'><strong>Error:</strong> {msg}</p>")
    raise SystemExit

# read inputs
try:
    a = float(form.getfirst("a"))
    b = float(form.getfirst("b"))
    c = float(form.getfirst("c"))
except Exception:
    fail("Provide numeric a, b, c (e.g. /calculate?a=2&b=3&c=4)")

if a == 0:
    fail("'a' must not be 0 (division by zero).")

# math
c_cubed   = c ** 3
sqrt_val  = math.sqrt(c_cubed)
division  = sqrt_val / a
multiplied= division * 10
result    = b + multiplied
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# styled HTML similar to your example
print("Content-type: text/html\n")
print(f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Assignment #2</title>
<style>
  :root {{ --paper:#f7efe6; --card:#f9eadf; --ink:#111827; --muted:#6b7280; --sep:#e5d5c9; --ok:#16a34a; --okbar:#22c55e; --panel:#2f3337; }}
  body {{ background:var(--paper); color:var(--ink); font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif; }}
  .wrap {{ max-width:860px; margin:24px auto; padding:0 16px; }}
  .card {{ background:var(--card); border:1px solid var(--sep); border-radius:6px; padding:22px; }}
  .rule {{ font-family:ui-monospace,Menlo,Consolas,monospace; color:var(--muted); margin:0 0 12px; }}
  h1 {{ color:var(--ok); margin:8px 0 2px; }}
  h3 {{ margin:0 0 16px; color:#9ca3af; font-weight:600; }}
  .result {{ font-size:1.1rem; }}
  .steps {{ display:flex; background:var(--panel); color:#e5e7eb; border-radius:6px; margin:14px 0 18px; }}
  .steps .bar {{ width:10px; background:var(--okbar); border-radius:6px 0 0 6px; }}
  .steps pre {{ margin:0; padding:12px 16px; font-family:ui-monospace,Menlo,Consolas,monospace; }}
  footer {{ font-style:italic; color:#374151; margin-top:6px; }}
</style>
</head>
<body>
  <div class="wrap"><div class="card">
    <pre class="rule">{"="*62}</pre>

    <h1>Assignment #2</h1>
    <h3>Your_Lastname</h3>

    <p><strong class="result">Final Result: {result:.1f}</strong></p>

    <div class="steps">
      <div class="bar"></div>
      <pre>Step 1: c = {c:.1f} , c³ = {c_cubed:.1f}

Step 2: √(c³) = {sqrt_val:.1f}

Step 3: {sqrt_val:.1f} / {a:.1f} = {division:.1f}

Step 4: {division:.1f} * 10 = {multiplied:.1f}

Step 5: {multiplied:.1f} + {b:.1f} = {result:.1f}</pre>
    </div>

    <footer>Calculation completed at {timestamp}</footer>
    <pre class="rule">{"="*62}</pre>
  </div></div>
</body></html>
""")
