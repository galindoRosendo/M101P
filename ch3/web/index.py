import bottle

@bottle.route('/')
def home_page():
    mythings = ['OSX', 'W10', 'Ubuntu']
    # return bottle.template()
    return bottle.template('Students', {'username':"Rosendo", 'things':mythings})

#Later
@bottle.post('/favorite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if (fruit == None or fruit == ""):
        fruit="No fruit selected"

    bottle.response.set_cookie("fruit", fruit)
    bottle.redirect("/show_fruit")

@bottle.route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie("fruit")

    return bottle.template('fruit_selection.tpl', {'fruit':fruit})

bottle.debug(True)
bottle.run(host='localhost', port=7777)
