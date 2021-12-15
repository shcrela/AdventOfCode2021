dead_ends = []
for node in G.nodes():
    n_list = list(G.neighbors(node))
    if (len(n_list)==1) and n_list[0].islower(): # if a cave is connected only to 1 small cave
           dead_ends.append(node)

init_pos = nx.get_node_attributes(G, "pos")
initial_pos = nx.spring_layout(G, pos=init_pos, fixed=["start", "end"], seed=34)

pos = deepcopy(initial_pos)
# if you want to adjust the positions manually:
pos['start'] += np.array([0, 0])
pos['end'] += np.array([0, 0])
pos['MY'] += np.array([0, 0])
pos['xc'] += np.array([0, 0])
pos['ho'] += np.array([0, 0])
pos['NF'] += np.array([0.7, -0.5])
pos['yf'] += np.array([0.7, 0])
pos['TP'] += np.array([0, 0])
pos['qo'] += np.array([0.5, 0])
pos['dc'] += np.array([-1.6, 0])
pos['EM'] += np.array([-1, 2])
pos['uh'] += np.array([0, 0])
ns = nx.get_node_attributes(G, 'size')
dead_end_sizes = itemgetter(*dead_ends)(ns)
ns = list(ns.values())

plt.close()
fig, ax = plt.subplots()
nx.draw_networkx(G, pos=pos, node_size=ns, alpha=.9, font_weight='bold', width=2)
nx.draw_networkx_nodes(G, pos=pos, nodelist=['start', 'end'], node_color='g', node_shape='s', node_size=900);
nx.draw_networkx_nodes(G, pos=pos, nodelist=dead_ends, node_color='r', node_size=dead_end_sizes);
plt.show();