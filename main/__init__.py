from main.multi_thread import multi_thread

class Main:

  def __init__(self):
    return

  def Run(self):
    # 切东京范围
    tile_file = open('./tokyo_tile')
    tile_list = []
    for line in tile_file.readlines():
      tile_list.append(line)

    for x in range(29086, 29120 + 1):
        obj_thread = multi_thread(x, tile_list)
        obj_thread.start()
    return

  def RunDrain(self):
    obj_thread = multi_thread(0, [])
    obj_thread.RunDrain()
    return
