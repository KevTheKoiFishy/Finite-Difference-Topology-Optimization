import numpy as np
from   typing import Union

class bitmap:
    def __init__(self, dims):
        self.canvas_dim = dims
        self.map = np.zeros(dims, dtype=np.float32)

    def rect(self, pos: tuple, dim: tuple, center: bool=True, value: float = 1.0, operation = "set", proportion:bool = False):
        
        if proportion:
            pos = tuple([int(p * d) for p, d in zip(pos, self.canvas_dim)])
            dim = tuple([int(s * d) for s, d in zip(dim, self.canvas_dim)])

        X0 = [np.clip(p - (d >> 1), 0, w) for p, d, w in zip(pos, dim, self.canvas_dim)] if center else [np.clip(p    , 0, w) for p, d, w in zip(pos, dim, self.canvas_dim)]
        XF = [np.clip(p + (d >> 1), 0, w) for p, d, w in zip(pos, dim, self.canvas_dim)] if center else [np.clip(p + d, 0, w) for p, d, w in zip(pos, dim, self.canvas_dim)]
        
        indexer = tuple([slice(x0, xf) for x0, xf in zip(X0, XF)])
        
        match operation:
            case "random":
                self.map[indexer] = np.random.random(size=self.map[indexer].shape)
                self.map[indexer] *= value
            case "set":
                self.map[indexer] = value
            case "add":
                self.map[indexer] += value
            case _:
                self.map[indexer] = value

        return X0, XF
    
    def flatten_hoz(self):
        return self.map.reshape(1, -1)
    
    def flatten_ver(self):
        return self.map.reshape(-1, 1)

# b = bitmap((10, 10))
# print(b.map)
# b.rect((5, 5), (2, 2))
# print(b.map)
# print(b.flatten_ver())