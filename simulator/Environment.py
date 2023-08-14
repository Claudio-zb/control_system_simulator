from typing import Dict, List, Any

from .Blocks import Block, OBlock, IOBlock, Connection
import numpy as np


class Environment:
    def __init__(self, blocks: list[Block], connections: list[Connection], ts: float = 1):
        self.blocks = blocks
        self.connections = connections
        self.ts = ts

        graph: dict[str, list[str]] = {}
        for connection in self.connections:
            source_id = connection.source.name
            target_id = connection.target.name
            if source_id not in graph:
                graph[source_id] = []
            graph[source_id].append(target_id)

        self.graph = graph
        blocks_dict = {}
        for block in blocks:
            blocks_dict.update({block.name: block})
        self.blocks_dict: dict[str, Block] = blocks_dict

    def simulation(self, end_time):

        # method to do DFS
        outputs = {}
        for block in self.blocks:
            name = block.name
            if name not in outputs:
                outputs[name] = []

        def dfs(root_name: str, node_name: str, visited: dict, isOver: bool = True):

            visited[node_name] = True

            if node_name in self.graph:
                current_block = self.blocks_dict[node_name]
                x0 = current_block.get_initial_condition()
                outputs[node_name].append(x0)
                neighbors = self.graph[node_name]
                for neighbor in neighbors:

                    if not visited[neighbor] or root_name==neighbor:
                        next_block = self.blocks_dict[neighbor]
                        next_block.set_u_k(x0)
                        #for block_name in self.graph[node_name]:
                            #next_block = self.blocks_dict[block_name]
                            #next_block.set_u_k(x0)
                        if root_name != neighbor:
                            dfs(root_name, neighbor, visited)
            return

        def update():
            for item in self.blocks:
                item.initial_state = item.get_next_state()

        n_steps = int(np.ceil(end_time / self.ts))
        sim_time = 0

        for i in range(n_steps):
            start_node = self.blocks[0].name
            visited_nodes = {node.name: False for node in self.blocks}

            dfs(start_node, start_node, visited_nodes)

            update()
            sim_time += self.ts

        return outputs
