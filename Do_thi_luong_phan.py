import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
import ast

print('Bệnh và các triệu chứng của nó.')
file = open("TrieuChungCuaBenh.txt", "r", encoding="utf-8")
noiDUng = file.read()
tuDien = ast.literal_eval(noiDUng)
file.close()

print('Các triệu chứng riêng biệt.')
file = open("TrieuChung.txt","r",encoding="utf-8")
trieuChung = file.read().split("\n")
file.close()

trieuChung=trieuChung[0:-2]
G=nx.Graph()
G.add_nodes_from(tuDien.keys(), bipartite = 0)
G.add_nodes_from(trieuChung, bipartite=1)
for tuKhoa in tuDien.keys():
    u = tuKhoa
    val = tuDien[tuKhoa]
    val = val.split(",")

    for v in val:
        G.add_edge(u,v)

print('Vẽ dồ thị và các cạnh được tạo.')
X, Y = bipartite.sets(G)

pos=dict()
pos.update( (n, (1, i)) for i, n in enumerate(X) )
pos.update( (n, (2, i)) for i, n in enumerate(Y) )

color_map=[]

for node in X:
    color_map.append('blue')

for node in Y:
    color_map.append('red')

print(X)
print(Y)
plt.title("Cơ sở kiến thức lưỡng phân(đồ thị hai phía)")
nx.draw(G,node_color=color_map, with_labels = True,pos=pos)
# plt.savefig("dothiluongphan.pdf")
plt.show()

