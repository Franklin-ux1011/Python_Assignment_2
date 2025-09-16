import cgi
import datetime

form = cgi.FieldStorage()

try:
    a = float(form.getvalue("a"))
    b = float(form.getvalue("b"))
    c = float(form.getvalue("c"))

    steps = []

    c_cubed = c ** 3
    steps.append(f"Step 1: c^3 = {c}^3 = {c_cubed}")

    sqrt_val = c_cubed ** 0.5
    steps.append(f"Step 2: sqrt(c^3) = sqrt({c_cubed}) = {sqrt_val}")

    div_result = sqrt_val / a
    steps.append(f"Step 3: {sqrt_val} / {a} = {div_result}")

    mult_result = div_result * 10
    steps.append(f"Step 4: {div_result} * 10 = {mult_result}")

    result = b + mult_result
    steps.append(f"Step 5: {b} + {mult_result} = {result}")

    print("Content-type: text/html\n")
    print("<html><body>")
    print("<pre>")
    print("====================================")
    print("Assignment #2")
    print("Your_Lastname")
    print()
    print(f"Final Result: {result}")
    print()
    for s in steps:
        print(s)
    print()
    print(f"Calculation completed at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("====================================")
    print("</pre>")
    print("</body></html>")

except Exception as e:
    print("Content-type: text/html\n")
    print(f"<h1>Error: {e}</h1>")


