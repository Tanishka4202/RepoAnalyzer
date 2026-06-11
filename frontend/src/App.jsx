import { useEffect, useState } from "react";
import axios from "axios";

import ReactFlow, {
  Background,
  Controls,
  MiniMap,
} from "reactflow";

import "reactflow/dist/style.css";

function App() {
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/scan")
      .then((res) => {
        const graph = res.data;

        const flowNodes = graph.nodes.map((node, index) => ({
          id: node.id,
          data: {
            label: (
              <div>
                <strong>{node.label}</strong>
                <br />
                LOC: {node.loc}
                <br />
                CC: {node.complexity || 0}
              </div>
            ),
          },
          position: {
            x: index * 200,
            y: 100,
          },
        }));

        const flowEdges = graph.edges.map((edge, index) => ({
          id: String(index),
          source: edge.source,
          target: edge.target,
        }));

        setNodes(flowNodes);
        setEdges(flowEdges);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <ReactFlow nodes={nodes} edges={edges}>
        <MiniMap />
        <Controls />
        <Background />
      </ReactFlow>
    </div>
  );
}

export default App;