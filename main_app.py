import gtk
import webkit



class main_app:
  def __init__(self):
    self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window.set_size_request(1024,800)
    self.window.connect("delete_event", lambda w,e: gtk.main_quit())
    
    self.go_button = gtk.Button("GO!")
    self.go_button.set_size_request(65,10)
    self.go_button.show()
    self.text_box = gtk.Entry()
    self.text_box.set_text("http://www.google.com")
    self.text_box.connect("activate",self.goto_link)
    self.text_box.show()
    
    self.go_button.connect("clicked", self.goto_link )
    
    self.box = gtk.HBox()
    self.box.add(self.text_box)
    self.box.pack_end(self.go_button,False)
    self.box.show()
    self.rows = gtk.VBox()
    self.rows.pack_start(self.box,False)
    self.rows.show()
    self.web_init()
    self.window.add(self.rows)
    
    self.window.show()
  
  def web_init(self):
    self.brow_space = webkit.WebView()
    self.brow_space.show()
    self.brow_space.connect("title-changed",self.change_title)
    self.brow_space.connect("load-progress-changed",self.set_progress)
    self.brow_space.connect("load-started", lambda w,f: self.prog_bar.set_visible(True))
    self.brow_space.connect("load-finished", lambda w,f: self.prog_bar.set_visible(False))

    
    self.brow_space.open('http://www.google.com')
    
    self.brow_area=gtk.ScrolledWindow()
    self.brow_area.add(self.brow_space)
    self.brow_area.show()
    self.rows.add(self.brow_area)
    
    self.prog_bar = gtk.ProgressBar()
    self.rows.pack_end(self.prog_bar,False)


  def goto_link(self, blah):
    self.brow_space.open(self.text_box.get_text())

  def change_title(self,w,f,title):
    self.window.set_title(title)

  def set_progress(self, w, val):
    self.prog_bar.set_fraction(val/100.00)
  
  

