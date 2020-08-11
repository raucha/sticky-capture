from pynput import keyboard

def on_activate_h():
    print('<shift>+<cmd>+7')

def on_activate_i():
    print('<cmd>+l')

with keyboard.GlobalHotKeys({
        '<shift>+<cmd>+7': on_activate_h,
        '<cmd>+l': on_activate_i}) as h:
    h.join()



# from pynput import keyboard

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))

# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()




# from pynput import keyboard

# def on_activate():
#     print('Global hotkey activated!')

# def for_canonical(f):
#     return lambda k: f(l.canonical(k))

# hotkey = keyboard.HotKey(
#     keyboard.HotKey.parse('<ctrl>+l'),
#     on_activate)
# with keyboard.Listener(
#         on_press=for_canonical(hotkey.press),
#         on_release=for_canonical(hotkey.release)) as l:
#     l.join()


