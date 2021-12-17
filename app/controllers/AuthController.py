class AuthController():
    def __init__(self):
        pass

    def index(self):  
        return render_template('index.html')
    

    def signup(self):
        if request.method == 'POST':
            name = request.form['name']
            useranme = request.form['useranme']
            direccion = request.form['direccion']
            email = request.form['email']           
            password = bycrypt.generate_password_hash(request.form['password'])
            phone = request.form['phone']
            #picture_profile = 'user.png'
            #user = User(name=name,username=username,direccion=direccion, email=email, password=password, picture_profile=picture_profile)
            user = User(name=name,useranme=useranme,direccion=direccion, email=email, password=password, phone=phone,rol_user='cliente')
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado exitosamente')
            return render_template('auth/login.html')
        return render_template('auth/signup.html')
    def signupadmin(self):
        if request.method == 'POST':
            name = request.form['name']
            useranme = request.form['useranme']
            direccion = request.form['direccion']
            email = request.form['email']           
            password = bycrypt.generate_password_hash(request.form['password'])
            phone = request.form['phone']
            #picture_profile = 'user.png'
            #user = User(name=name,username=username,direccion=direccion, email=email, password=password, picture_profile=picture_profile)
            user = User(name=name,useranme=useranme,direccion=direccion, email=email, password=password, phone=phone,rol_user='administrador')
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado exitosamente')
            return render_template('admin.html')
        return render_template('auth/signup.html')

    def login(self):
        if request.method == 'POST':
            #user = User.query.filter_by(name=request.form['name']).first()
            user = User.query.filter_by(name=request.form['name']).first()
            if user: 
                if bycrypt.check_password_hash(user.password, request.form['password']):
                    login_user(user)
                    if user.rol_user == 'cliente':
                        return redirect(url_for('main_router.main'))
                    if user.rol_user == 'administrador':
                        return redirect(url_for('main_router.client'))
            flash('Usuario no existe, o los creadenciales no son válidos')
            return redirect(url_for('auth_router.login'))
        return render_template('auth/login.html')

    def logout(self):
        session.clear()
        logout_user()
        return redirect(url_for('auth_router.login'))

authcontroller = AuthController()
