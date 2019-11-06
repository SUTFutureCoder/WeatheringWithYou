from main.multi_thread import multi_thread

class Main:

  def __init__(self):
    return

  def Run(self):
    # 切东京范围
    for x in range(29086, 29120 + 1):
      obj_thread = multi_thread(x)
      obj_thread.start()
    return
