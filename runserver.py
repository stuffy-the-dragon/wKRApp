from wKRApp import app
 # 2 security flaws, need to sort out
 # 		1. the key should be randomy generated
 # 		2. the key should be set in a config file that is then imported in.
app.secret_key = "my precious"
app.run(debug=True)
