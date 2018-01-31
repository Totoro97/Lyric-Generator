import pickle
import os
import json
import urllib.error
import urllib.parse
import urllib.request
import re

def get_url(url) :
    response = urllib.request.urlopen(url, timeout=10)
    return response.read().decode('utf-8')

f = open('playlists.txt', 'r')
plists = f.read().strip().split('\n')
f.close()
pat = '[^\u4e00-\u9fa5] 　\n\r]'

cnt = 0
steps = 0

for pid in plists :
    if not os.path.exists('lyrics.pkl') :
        data = dict()
    else :
        f = open('lyrics.pkl', 'rb')
        data = pickle.load(f)
        f.close()
    url = 'http://music.163.com/api/playlist/detail?id=' + pid
    ret_text = get_url(url)
    songs = json.loads(str(ret_text))['result']['tracks']
    for song in songs :
        if (str(song['id']) in data) :
            cnt += len(data[str(song['id'])])
            print('pass:', cnt)
            continue
        surl = 'http://music.163.com/api/song/lyric?id=' + str(song['id']) + '&lv=1&kv=1&tv=-1'
        ret_text = get_url(surl)
        dt = json.loads(ret_text)
        if (str(dt['code']) == '200') :
            try :
                lrc = dt['lrc']['lyric']
            except BaseException :
                lrc = ''
        else :
            print('fuck')
            exit(0)
        lrc = re.sub('[^\u4e00-\u9fa5 　\n\r]', '', lrc)
        lrc = re.sub('[ 　\n\r]+', '\n', lrc)
        data[str(song['id'])] = lrc
        cnt += len(lrc)
        print(lrc)
        print(cnt)
        
        if (steps % 10 == 0) :
            f = open('lyrics.pkl', 'wb')
            pickle.dump(data, f)
            f.close()
        steps += 1
        
    f = open('lyrics.pkl', 'wb')
    pickle.dump(data, f)
    f.close()
