_curlen = len(t_arr)
_newlen = len(t_arr)+len(_spikes)
t_arr.resize(_newlen)
i_arr.resize(_newlen)
t_arr[_curlen:_newlen] = t
i_arr[_curlen:_newlen] = _spikes
