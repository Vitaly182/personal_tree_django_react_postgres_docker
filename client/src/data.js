import { useEffect, useState } from "react";
import axios from 'axios';
import Tree from './Tree'


function TreeData() {

  const [data, setData] = useState([]);

  const fetchData = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/employee/",
      );
      setData(response.data);
    } catch (err) {
        console.log(err);
    } 
  };

  useEffect(() => {
    fetchData();
  }, []);

  const tree = array => array
    .reduce ((a, c) => {
      c.children = array.filter (i => i.parent_id === c.child_id)
      a.push (c)
      return a
    }, [])
    .filter (i => i.parent_id === 1)

  const  treeData =  (tree(data))

  return (
    <div className="App">
      <h1>React Tree View</h1>
      <Tree treeData={treeData} />
    </div>
  );
}

export default TreeData



