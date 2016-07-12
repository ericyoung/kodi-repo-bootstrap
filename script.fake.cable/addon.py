import xbmcaddon
import xbmcgui

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

line1 = "Fake Cable!"
line2 = "This is Fake Cable!"
line3 = "Fake Cable, I tell you!"

xbmcgui.Dialog().ok(addonname, line1, line2, line3)
