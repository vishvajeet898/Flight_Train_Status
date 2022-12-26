import tkinter
from tkintermapview import TkinterMapView

root_tk = tkinter.Tk()
root_tk.geometry(f"{1000}x{800}")
root_tk.title("map_view_example.py")

# create map widget
map_widget = TkinterMapView(root_tk, width=600, height=1000, corner_radius=0)
map_widget.pack(fill="both", expand=True)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

root_tk.mainloop()
