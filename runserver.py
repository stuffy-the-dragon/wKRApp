from wKRApp import app
app.secret_key = "my precious" # 2 security flaws, need to sort out
app.run(debug=True)
