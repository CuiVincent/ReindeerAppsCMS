__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

import tornado.web
import reindeer.sys.base_handler
from reindeer.sys.model.sys_action import SysAction
from reindeer.sys import strings


class IndexHandler(reindeer.sys.base_handler.BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user_name = self.get_current_user().NAME
        self.render('sys/index.html', user_name=user_name, main_menu=self.get_user_main_menu(),
                    main_page='sys/main.html', logout_url='logout')

    def get_user_main_menu(self):
        user_id = self.get_current_user().ID
        parent_id = strings.action_root_main_parent
        menu = SysAction.get_action_tree_by_user_and_parent(user_id, parent_id, strings.action_type_menu_menu)
        return menu


class ContentHandler(reindeer.sys.base_handler.BaseHandler):
    @reindeer.sys.base_handler.authenticated
    def get(self, url):
        if url and url.lower().endswith('.html'):
            try:
                self.render(url)
                return
            except IOError:
                pass
        if not url.startswith('/'):
            url = '/' + url
        self.redirect(url)