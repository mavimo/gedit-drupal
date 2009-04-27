import gedit
import os
import re
import gtk
import gtkmozembed
import types

class DrupalApi(gedit.Plugin):

  # A list of (handler_id, view) tuples
  handler_ids = []

  def __init__(self):
    # Create Drupal API browser
    self._panel = gtkmozembed.MozEmbed()
    gedit.Plugin.__init__(self)

  def activate(self, window):
    # Load image icon
    image = gtk.image_new_from_file(os.path.join(os.path.dirname(__file__), 'drupalapi.png'))
    
    # Find bottm panel obj
    bottom = window.get_bottom_panel()
    
    # Add new item
    bottom.add_item(self._panel, _("Drupal API"), image)
    
    # Start auto completion for the active view
    view = window.get_active_view()
    self.setup_dapi_autocompletion(view)

  def deactivate(self, window):
    # Remove browser into bottom Panel
    bottom = window.get_bottom_panel()
    bottom.remove_item(self._panel)
    # Disconnect all handlers which have been connected by this plugin
    for (handler_id, view) in self.handler_ids:
      view.disconnect(handler_id)

  def update_ui(self, window):
    # Start auto completion for the active view
    view = window.get_active_view()
    self.setup_dapi_autocompletion(view)

  # Starts auto completion for a given view
  def setup_dapi_autocompletion(self, view):
    if type(view) != types.NoneType:
      if getattr(view, 'completion_instance', False) == False:
        setattr(view, 'completion_instance', DApiCompletion(self._panel))
        handler_id = view.connect(
          'key-press-event',
          view.completion_instance.complete_word)
        view.completion_instance.handler_id = handler_id
        self.handler_ids.append((handler_id, view))

class DApiCompletion():
  def __init__(self, panel):
    self._dapi_panel = panel
    return

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
    
    return False

  def complete_word(self, view, event):
    # Use multiple mouse click on function to open API Doc 
    # (change 'key-press-event' to 'button-press-event')
    #    if (event.type == gtk.gdk._3BUTTON_PRESS):
    # Used to find Keycode to use
    #    print event.keyval
    # Set CTRL + KEYCODE to open API Doc
    if(event.state & gtk.gdk.CONTROL_MASK and event.keyval == 62):
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
      self._dapi_panel.load_url('http://api.drupal.org/api/function/' + function + '/6')
      return False
    else:
      return False
