# package require Tk
# button .b
# pack .b
grid [::tclmacbag::dbutton .b -pathname .e \
  -gridopts {-column 2 -row 1}] -column 1 -row 1
# Set up the disclosed/hidden frame.
ttk::frame .e
grid [ttk::label .e.l1 -text "Hello world."]
