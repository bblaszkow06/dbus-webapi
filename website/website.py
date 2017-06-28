from flask import Flask, render_template, url_for, g, flash, request, redirect
from dbusapi import blueprint, api

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    SECRET_KEY='development key',
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

app.register_blueprint(blueprint, url_prefix='/api')

@app.route("/")
def index():
    set_navbar()
    return render_template('main.html')

@app.route("/calls")
def calls_list():
    set_navbar()
    brightness = api.kde_brightness()
    calls = [
        ('Brightness UP', url_for('call_fun', fun_name='kde_set_brightness', value=brightness + 15)),
        ('Brightness DOWN', url_for('call_fun', fun_name='kde_set_brightness', value=brightness - 15)),
        ('Get brightness', url_for('call_fun', fun_name='kde_brightness'))
    ]
    return render_template('calls_list.html', calls=calls)

@app.route("/calls/<fun_name>")
def call_fun(fun_name):
    foo = getattr(api, fun_name)
    res = foo(**(request.args.to_dict()))
    flash("Function invoked" + (", result: {}.".format(res) if res is not None else "."))
    return redirect(url_for("calls_list"))

@app.route('/names')
def names_list():
    set_navbar()
    names = sorted([ name for name in api.dbus_list_names() if name[0] != ':'])
    urls = [ url_for('name_introspection', dbus_name=name) for name in names ]
    return render_template('list_names.html', entries=zip(urls, names))

@app.route("/names/<dbus_name>/", defaults={'dbus_path': ''})
@app.route("/names/<dbus_name>/<path:dbus_path>")
def name_introspection(dbus_name, dbus_path):
    set_navbar()
    try:
        xml_info = api.dbus_introspect_p(dbus_name, '/'+dbus_path)
    except KeyError:
        xml_info = api.dbus_introspect(dbus_name)
    return render_template('name_introspection.html', data=xml_info)

def set_navbar():
    labels = ["Nazwy", "Wywołania", "API map"]
    urls   = [ url_for('names_list'), url_for('index'), url_for('index') + "api/map"]
    g.nav_items = zip(urls, labels)
