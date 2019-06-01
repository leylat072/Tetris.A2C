  board =[[0,0,0,0,0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0, 1],
 [0,0,0,0,0,0,0,0,0,0,0,0,
  0,0,0,0,0, 1,  1,  1],
 [0,0,0,0,0,0,0,0,0,0,0,0,
  0, 1 , 1,  1,  1, 0,0, 1],
 [0,0,0,0,0,0,0,0,0,0,0,0,
   1 , 1, 0,0, 1  ,1,  1,  1],
 [0,0,0,0,0,0,0,0,0,0,0,0,
  0,0,0,0,0,0, 1, 0],
 [0,0,0,0,0,0,0,0,0,0,0,0,
  0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,
  0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,
  0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,
  0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,
  0,0,0,0,0,0,0,0]]
            _height = 0
            height =20
            _has = 0
            score  =0 
            for i in range (0, len(board)):
                for j in range (0, len(board[i])):
                     if engine.board[i][j] == True :
                         #print(engine.board)
                         _has = _has +1

                if _height < _has :
                    _height = _has
            print('_height')
            print(_height)
            #print(engine.board)
           # print(engine)
            if(_height > height/2):
                score += -100
            if(_height< height/2 and _height > height/4):
                score += -50
            if(_height< height/4 and _height > height/8):
                score += -10
            else:
                score += -1
            #print(score)
            ##################################################