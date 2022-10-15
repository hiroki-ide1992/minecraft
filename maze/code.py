# mcipからMineCraftを操作するモジュールをインポートしている
from mcpi import minecraft, block
import generate


def main():

  mc = minecraft.Minecraft.create()
  """
  現在起動しているMineCraftワールドのオブジェクト生成して変数mcに格納している
  上記のimportで呼び出した「minecraft」ライブラリから「Minecraft」クラスにアクセスし「create()」メソッドを使用している
  """

  mc.player.setPos(0,1,0)
  """
  setPos関数:プレイヤーの位置を移動させる関数

  Parameters
  ----------
  X : int
    X座標、minecraftでは東西を表す
  Y : int
    Y座標、minecraftでは高さを表す
  Z : int
    Z座標、minecraftでは南北を表す
  """

  mc.setBlocks(
    -3, 0, -3,  # ブロックを置く"開始位置"、左からX,Y,Z座標
    50, 50, 50, # ブロックを置く"終了位置"、左からX,Y,Z座標
    block.AIR   # 配置するブロックの種類
  )
  mc.setBlocks(
    -3, 0, -3,  # ブロックを置く"開始位置"、左からX,Y,Z座標
    50, 0, 50, # ブロックを置く"終了位置"、左からX,Y,Z座標
    block.GRASS   # 配置するブロックの種類
  )

  HEIGHT  = 5
  # 以下の数字は必ず"奇数"にすること、でないと迷路が途切れる
  X_COORD = 11
  Z_COORD = 11


  maze = generate.GenerateMaze(X_COORD, Z_COORD)
  maze.preset_start_goal()
  # maze.print_maze()


  def put_maze_block(mc, mark, x_pos, z_pos):
    # マークが#の座標にブロックを置く
    if mark == '#':
        mc.setBlocks(
            x_pos, 0, z_pos,
            x_pos, HEIGHT, z_pos,
            block.STONE
        )


  for z, column in enumerate(maze.maze):
    for x, symbol in enumerate(column):
      put_maze_block(mc,symbol,x,z)


if __name__ == "__main__":
    main()

