from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt
from application import app
from application.forms import RegistrationForm, LoginForm, createcharacter, inventoryform
from application.models import Users, Characters, Inventory
from flask import render_template, redirect, url_for, request, flash
from flask import Flask, render_template


@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/signup.html', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(username=form.username.data,last_name=form.last_name.data,first_name=form.first_name.data,email=form.email.data, password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('mycharacters'))
    return render_template('signup.html', title='Register', form=form)


@app.route("/login.html", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home')) #If user is authenticated it sends them to the landing page
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/mycharacters.html', methods=['GET', 'POST'])
def mycharacters():
    characters = Characters.query.all()
    if current_user.is_anonymous:
        return redirect(url_for('home'))
    return render_template('mycharacters.html',characters = characters, title='MyCharacters')

@app.route('/charactersheet.html', methods=['GET', 'POST'])
def charactersheet():
    form = createcharacter()
    if form.validate_on_submit():
        character = Characters(Characte_name=form.Characte_name.data,
                               first_name=form.first_name.data,
                               char_class=form.char_class.data,
                               background=form.background.data, 
                               race=form.race.data,
                               alignment=form.alignment.data, 
                               experience_points=form.experience_points.data, 
                               strength=form.strength.data, 
                               dexterity=form.dexterity.data, 
                               constitution=form.constitution.data, 
                               intelligence=form.intelligence.data, 
                               wisdom=form.wisdom.data, 
                               charisma=form.charisma.data)

        db.session.add(character)
        db.session.commit()

        return redirect(url_for('mycharacters'))
    return render_template('charactersheet.html', title='Create Character', form=form)

@app.route('/inventory.html', methods=['GET', 'POST'])
def inventories():
    form = inventoryform()
    inventories = Inventory.query.all()
    if current_user.is_anonymous:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        character = Characters.query.filter_by(Characte_name=form.character_name.data).first()
        inv = Inventory(health_potions=form.health_potions.data,
                        scrolls=form.scrolls.data,
                        keys=form.keys.data,
                        arrows=form.arrows.data, 
                        shortsword=form.shortsword.data,
                        longsword=form.longsword.data,
                        characters=character)

        db.session.add(inv)
        db.session.commit()
        
        return redirect(url_for('inventory'))
    return render_template('inventory.html', inventory = inventories, title='inventory', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    character = Characters.query.get_or_404(id)

    try:
        db.session.delete(character)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting data."

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    character = Characters.query.get_or_404(id)

    if request.method == 'POST':
        character.Characte_name = request.form['name']
        character.strength = request.form['strength']
        character.dexterity = request.form['dexterity']
        character.constitution = request.form['constitution']
        character.intelligence = request.form['intelligence']
        character.wisdom = request.form['wisdom']
        character.charisma = request.form['charisma']

        try:
            db.session.commit()
            return redirect(url_for('mycharacters'))
        except:
            return "There was a problem updating data."

    else:
        title = "Update Data"
        return render_template('update.html', title=title, character=character)

@app.route('/updateinv/<int:id>', methods=['GET', 'POST'])
def updateinv(id):
    inventory = Inventory.query.get_or_404(id)

    if request.method == 'POST':
        inventory.health_potions = request.form['health_potions']
        inventory.scrolls = request.form['scrolls']
        inventory.keys = request.form['keys']
        inventory.arrows = request.form['arrows']
        inventory.shortsword = request.form['shortsword']
        inventory.longsword = request.form['longsword']

        try:
            db.session.commit()
            return redirect(url_for('inventories'))
        except:
            return redirect(url_for('inventory'))

    else:
        title = "Update Data"
        return render_template('updateinv.html', title=title, inventory=inventory)
