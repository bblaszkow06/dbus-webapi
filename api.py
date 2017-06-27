from jsonrpc.backend.flask import api
from pydbus import SessionBus

blueprint = api.as_blueprint()
bus = SessionBus()

@api.dispatcher.add_method
def ping():
    return "pong"

@api.dispatcher.add_method
def dbus_call_p(name, path, method, *args):
    proxy = bus.get(name, path)
    fun = getattr(proxy, method)
    return fun(*args)

@api.dispatcher.add_method
def dbus_call(name, method, *args):
    return dbus_call_p(name, None, method, *args)

@api.dispatcher.add_method
def dbus_list_names():
    return dbus_call(".DBus", "ListNames")

@api.dispatcher.add_method
def dbus_introspect(name, path):
    return dbus_call_p(name, path, "Introspect")

pm = ".PowerManagement"
pm_kde_path = "/org/kde/Solid/PowerManagement"
@api.dispatcher.add_method
def kde_brightness():
    return dbus_call_p(pm, pm_kde_path + "/Actions/BrightnessControl", "brightness")

@api.dispatcher.add_method
def kde_set_brightness(value):
    return dbus_call_p(pm, pm_kde_path + "/Actions/BrightnessControl", "setBrightness", value)
