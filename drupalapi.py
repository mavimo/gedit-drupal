import gedit
import os
import re
import gtk
import webkit
import types

class DrupalApi(gedit.Plugin):

  def update_ui(self, window):
    # Start auto completion for the active view
    view = window.get_active_view()
    self.setup_dapi_autocompletion(view)

  # Starts auto completion for a given view
  def setup_dapi_autocompletion(self, view):
    if type(view) != types.NoneType:
      if getattr(view, 'completion_instance', False) == False:
        setattr(view, 'completion_instance', DApiCompletion())
        handler_id = view.connect(
          'key-press-event',
          view.completion_instance.complete_word)

class DApiCompletion():
  def _current_module_name(self):
    window = gedit.app_get_default().get_active_window()
    doc = window.get_active_document()
    uri = doc.get_uri().split('/')
    uri = uri[len(uri) - 1].split('.')[0].lower()
    return uri

  def _split_function(var, char, limit):
    if(char == ' '):
      return True
    if(char == '('):
      return True
    if(char == '='):
      return True
    if(char == '>'):
      return True
    if(char == ','):
      return True
    if(char == '.'):
      return True
    
    return False

  def complete_word(self, view, event):
    # Use multiple mouse click on function to open API Doc 
    # (change 'key-press-event' to 'button-press-event')
    #
    #    if (event.type == gtk.gdk._3BUTTON_PRESS):
    #
    # Set CTRL + CHAR to open API Doc
    if(event.state & gtk.gdk.CONTROL_MASK and gtk.gdk.keyval_name(event.keyval) == 'l'):
      buffer      = view.get_buffer()
      iter_cursor = buffer.get_iter_at_mark(buffer.get_insert())
      iter_start  = iter_cursor.copy()
      iter_stop   = iter_cursor.copy()
      
      iter_el     = iter_cursor.copy()
      iter_sl     = iter_cursor.copy()
      iter_el.forward_to_line_end()
      iter_sl.set_line_offset(0)
      
      iter_start.backward_find_char(self._split_function, True, iter_sl)
      iter_stop.forward_find_char(  self._split_function, True, iter_el)
      
      word        = buffer.get_text(iter_start, iter_stop)
      
      function = re.sub("\s", "", word)
      
      name = self._current_module_name()
      
      # if start with same file name is a hook
      if(function.startswith(name + '_')):
        function = function.replace(name + '_', 'hook_', 1)

      # Load info page
      # Window elements
      main_window     = gtk.Window ()
      scrolled_window = gtk.ScrolledWindow ()
      web_view        = webkit.WebView ()
      # Add elements into window
      gtk.Container.add (scrolled_window, web_view)
      gtk.Container.add (main_window, scrolled_window)
      # Set URL to open
      webkit.WebView.load_uri (web_view, "http://api.drupal.org/api/function/" + function + '/6')
      # Set window size
      gtk.Window.set_default_size (main_window, 1024, 600)
      # Set window position (center)
      main_window.set_position(gtk.WIN_POS_CENTER)
      # Set window title
      main_window.set_title ("Drupal 6 API: " + function)
      # Show window
      gtk.Widget.show_all (main_window)
      return False
    else:
      return False
