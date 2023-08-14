from typing import Dict, List, Any

from .Blocks import Block, OBlock, IOBlock, Connection
import numpy as np


class Environment:
    """
    Environment that stores the blocks, handles its connections and run the simulation
    """

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
            if target_id is not None:
                graph[source_id].append(target_id)

        self.graph = graph
        blocks_dict = {}
        for block in blocks:
            blocks_dict.update({block.name: block})
        self.blocks_dict: dict[str, Block] = blocks_dict

    def simulation(self, end_time) -> dict[str, list]:

        # method to do DFS
        outputs = {}
        for block in self.blocks:
            name = block.name
            if name not in outputs and block.saveStates:
                outputs[name] = []

        def dfs(root_name: str, node_name: str, visited: dict[str, bool]):

            visited[node_name] = True

            if node_name in self.graph:
                current_block = self.blocks_dict[node_name]
                if current_block.saveStates:
                    x0 = current_block.get_initial_condition()
                    outputs[node_name][:, i] = x0[:, 0]
                neighbors = self.graph[node_name]
                for neighbor in neighbors:

                    if not visited[neighbor] or root_name == neighbor:
                        next_block = self.blocks_dict[neighbor]
                        try:
                            next_block.set_u_k(x0)
                        except:
                            pass
                        if root_name != neighbor:
                            dfs(root_name, neighbor, visited)
            return

        def update():
            for item in self.blocks:
                item.initial_state = item.get_next_state()

        n_steps = int(np.ceil(end_time / self.ts))
        sim_time = 0
        for name in outputs:
            dim_output = self.blocks_dict[name].dim_output
            outputs[name] = np.empty((dim_output, n_steps + 1))

        for i in range(n_steps+1):
            start_node = self.blocks[0].name
            visited_nodes = {node.name: False for node in self.blocks}

            dfs(start_node, start_node, visited_nodes)

            update()
            sim_time += self.ts

        return outputs
