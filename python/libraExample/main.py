
from suzdal_finc.click_buscar_file import click_buscar
from suzdal_finc.click_image_file import click_por_imagen
from suzdal_finc.delay_file import delay
from suzdal_finc.input_user_file import cerrar_notificaciones, input_login
from suzdal_finc.kill_process_file import kill_process
from suzdal_finc.scroll_bottom_file import scroll_tabla_linea_a_linea
from suzdal_finc.start_process_file import libra_start


# Cerrar libra
kill_process('Libra')
delay(7)

libra_start()
delay(9)

input_login()
delay(9)

cerrar_notificaciones()
delay(9)

click_buscar()
delay(9)

click_por_imagen('menu_clasificacion_articulos.png')
delay(9)

click_por_imagen('top_lupa.png')
delay(9)

click_por_imagen('top_rallo.png')
delay(9)

scroll_tabla_linea_a_linea()
delay(9)