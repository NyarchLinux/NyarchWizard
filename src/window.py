# window.py
#
# Copyright 2023 Francesco Caracciolo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later


from gi.repository import Adw
from gi.repository import Gtk
from .pages import PAGES
import subprocess
@Gtk.Template(resource_path='/moe/nyarchlinux/wizard/window.ui')
class NyarchwizardWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'NyarchwizardWindow'

    carousel = Gtk.Template.Child("carousel")
    previous = Gtk.Template.Child("previous")
    nextbutton = Gtk.Template.Child("next")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.commands = {}
        for page in PAGES:
            p = self.generate_page(page)
            self.carousel.append(p)
        self.carousel.connect("page-changed", self.page_changes)
        self.nextbutton.connect("clicked", self.next_page)
        self.previous.connect("clicked", self.previous_page)


    def page_changes(self, carousel, page):
        if page > 0:
            self.previous.set_opacity(1)
        else:
            self.previous.set_opacity(0)
        if page >= self.carousel.get_n_pages()-1:
            self.nextbutton.set_opacity(0)
        else:
           self.nextbutton.set_opacity(1)
    def next_page(self, button):
        self.carousel.get_position()
        if self.carousel.get_position() < self.carousel.get_n_pages()-1:
            self.carousel.scroll_to(self.carousel.get_nth_page(self.carousel.get_position()+1), True)

    def previous_page(self, button):
        self.carousel.get_position()
        if self.carousel.get_position() > 0:
            self.carousel.scroll_to(self.carousel.get_nth_page(self.carousel.get_position()-1), True)

    def generate_page(self, page):
        builder = Gtk.Builder.new_from_resource("/moe/nyarchlinux/wizard/carousel_page.ui")
        p = builder.get_object("page")
        statuspage = builder.get_object("statuspage")
        buttonsBox = builder.get_object("buttonsBox")
        appcontainer = builder.get_object("appcontainer")
        for app in page['apps']:
        	row = Adw.ActionRow()
        	picture = Gtk.Picture()
        	button = Gtk.Button()
        	button.set_css_classes(["suggested-action"])
        	button.set_label("Install")
        	self.commands[button] = app["command"]
        	button.connect("clicked", self.button_clicked)
        	button.set_margin_top(10)
        	button.set_margin_bottom(10)
        	row.set_title(app["title"])
        	row.set_subtitle(app["subtitle"])
        	picture.set_resource("/moe/nyarchlinux/wizard/pictures/" + app["icon"] + ".png")
        	row.add_prefix(picture)
        	row.add_suffix(button)
        	appcontainer.add(row)

        statuspage.set_icon_name(page["icon"])
        statuspage.set_title(page["title"])
        statuspage.set_description(page["body"])
        return statuspage

    def button_clicked(self, button):
        	self.background_process(self.commands[button])

    def background_process(self, command):
    	subprocess.Popen(["flatpak-spawn",  "--host"] + command.split())
