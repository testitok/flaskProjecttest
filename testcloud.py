import jieba
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
from PIL import Image
from  wordcloud import  WordCloud
text=""
sql='select info from movie250'
conn=sqlite3.connect('movie.db')
cur=conn.cursor()
res=cur.execute(sql)
for item in res:
    text=text+item[0]
cur.close()
conn.close()

cut=jieba.cut(text)
st=' '.join(cut)
print(st)
img=Image.open(r'./static/3.jpg')
img_array=np.array(img)

wc=WordCloud(background_color='white',
    mask=img_array,
    font_path='STCAIYUN.TTF')
wc.generate_from_text(st)
fig=plt.figure(1)
plt.imshow(wc)
plt.axis('off')
# plt.show()
plt.savefig(r'./static/4.jpg',dpi=500)